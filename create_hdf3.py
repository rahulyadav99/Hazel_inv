import numpy as np
import matplotlib.pyplot as pl
#import hazel
import h5py
import scipy.io as io
from ipdb import set_trace as stop
from scipy.io import readsav as readsav

	
f=readsav('observations/rebinned_2pix.sav')
stokes = f['rebinned']
stokes[:] = stokes[:]/1.0065
nx,ny,nl,stk = stokes.shape


stokes_3d = np.reshape(stokes,[nx*ny,nl,stk])
cc,nl,stk = stokes_3d.shape

sigma_3d = np.zeros((cc,nl,4), dtype=np.float64)
sigma_3d[:]= np.std(stokes[0:100,0:15,1])
los_3d = np.zeros((cc,3), dtype=np.float64)
los_3d[:]=[60,0,73]
boundary_3d = np.zeros((cc,nl,4), dtype=np.float64)
boundary_3d[:] = [1,0,0,0]

fname='observations/spatially_binned_2pix.h5'
f = h5py.File(fname, 'w')

db_stokes = f.create_dataset('stokes', stokes_3d.shape, dtype=np.float64)
db_sigma = f.create_dataset('sigma', sigma_3d.shape, dtype=np.float64)
db_los = f.create_dataset('LOS', los_3d.shape, dtype=np.float64)
db_boundary = f.create_dataset('boundary', boundary_3d.shape, dtype=np.float64)
db_stokes[:] = stokes_3d
db_sigma[:] = sigma_3d
db_los[:] = los_3d
db_boundary[:] = boundary_3d

print('Stokes file created -->',fname)
print(stokes_3d.shape)
f.close()

