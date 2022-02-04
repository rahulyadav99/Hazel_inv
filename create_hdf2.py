import numpy as np
import matplotlib.pyplot as pl
#import hazel
import h5py
import scipy.io as io
from ipdb import set_trace as stop

outdir = '/home/raya0718/hazel2/examples/grisinv/dataset/new/'

ff = h5py.File('2bingris_stokes_g.h5','r')
stokes=ff.get('stokes')

tpix,nl,stk = stokes.shape

px=37
py=109
npix = 10000
for i in range(0,10):
	
	stokes_3d = np.squeeze(stokes[5000*i:5000*i+5000,:,:])
	if i == 9:stokes_3d = np.squeeze(stokes[5000*i:,:,:])
	cc,nl,stk = stokes_3d.shape

	sigma_3d = np.zeros((cc,nl,4), dtype=np.float64)
	sigma_3d[:]= np.std(stokes[0:100,0:15,1])
	los_3d = np.zeros((cc,3), dtype=np.float64)
	los_3d[:]=[60,0,73]
	boundary_3d = np.zeros((cc,nl,4), dtype=np.float64)
	boundary_3d[:] = [1,0,0,0]

	fname='set'+'{:02d}'.format(i)
	f = h5py.File(outdir+fname+'.h5', 'w')

	db_stokes = f.create_dataset('stokes', stokes_3d.shape, dtype=np.float64)
	db_sigma = f.create_dataset('sigma', sigma_3d.shape, dtype=np.float64)
	db_los = f.create_dataset('LOS', los_3d.shape, dtype=np.float64)
	db_boundary = f.create_dataset('boundary', boundary_3d.shape, dtype=np.float64)
	db_stokes[:] = stokes_3d
	db_sigma[:] = sigma_3d
	db_los[:] = los_3d
	db_boundary[:] = boundary_3d

	print('Stokes file created -->',i,fname)
	print(stokes_3d.shape)
	f.close()
stop()
	#_____________________________________
	# create model atmosphere, photosphere
	n_pixel = cc
	tau = np.loadtxt('../photospheres/model_photosphere.1d',skiprows=4)
	nz,par = tau.shape

	model_3d = np.zeros((n_pixel,nz,8), dtype=np.float64)

	model_3d[:] = tau

	ff_3d = np.zeros((n_pixel,), dtype=np.float64)
	ff_3d[:] = 1.0

	f = h5py.File(outdir+str(i+5)+'_2binphotosphere.h5', 'w')
	db_model = f.create_dataset('model', model_3d.shape, dtype=np.float64)
	db_ff = f.create_dataset('ff', ff_3d.shape, dtype=np.float64)
	db_model[:] = model_3d
	db_ff[:] = ff_3d
	print('Photospheric model file created:')
	print(model_3d.shape)
	f.close()

	#_____________________________________
	# create model atmosphere, photosphere
	model_3d = np.zeros((n_pixel,8), dtype=np.float64)
	ff_3d = np.zeros((n_pixel,), dtype=np.float64)
	for j in range(n_pixel):
		mod = [50.0,10.0,100.0,0.2,0.0,8.0,1.0,0.0]
		model_3d[j,:]=mod

	ff_3d[:] =1.0
	 
	f = h5py.File(outdir+str(i+5)+'_2binchromosphere.h5', 'w')
	db_model = f.create_dataset('model', model_3d.shape, dtype=np.float64)
	db_ff = f.create_dataset('ff', ff_3d.shape, dtype=np.float64)
	db_model[:] = model_3d
	db_ff[:] = ff_3d
	print('Chromospheric model file created:')
	print(model_3d.shape)
	f.close()
stop()
#________________________________________________________________
# create Mask file, 1 (inverted pixels) & 0 (not inverted pixels)
'''mask_3d = np.zeros((n_pixel,8), dtype=np.int8)

for j in range(n_pixel):
	mod = [50.0,10.0,100.0,0.2,0.0,8.0,1.0,0.0]
	model_3d[j,:]=mod

ff_3d[:] =1.0
 
f = h5py.File('grisdata/m2chromosphere.h5', 'w')
db_model = f.create_dataset('model', model_3d.shape, dtype=np.float64)
db_ff = f.create_dataset('ff', ff_3d.shape, dtype=np.float64)
db_model[:] = model_3d
db_ff[:] = ff_3d
print('Chromospheric model file created:')
print(model_3d.shape)
f.close()'''
