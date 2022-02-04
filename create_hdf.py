import numpy as np
import matplotlib.pyplot as pl
#import hazel
import h5py
import scipy.io as io
from bin_array import binavg1D
from ipdb import set_trace as stop
import random


#_____________________________________
# create random model atmosphere-> chromosphere
n_pixel=250*452
model_3d = np.zeros((n_pixel,8), dtype=np.float64)
ff_3d = np.zeros((n_pixel,), dtype=np.float64)

for k in range(5):
	for j in range(n_pixel):
	#[Bx [G]   By [G]   Bz [G]   tau    v [km/s]     deltav [km/s]   beta    a]
		mod = [random.randint(10,200),random.randint(10,200),random.randint(50,200),random.random()+0.001,random.random()*100,random.randint(1,14),1.0,0.0001]
		model_3d[j,:]=mod

	ff_3d[:] =1.0
	fname='/scratch/rahul/grisinv/models/'+'chromo_init_model_'+str(k)+'.h5'
	f = h5py.File(fname, 'w')
	db_model = f.create_dataset('model', model_3d.shape, dtype=np.float64)
	db_ff = f.create_dataset('ff', ff_3d.shape, dtype=np.float64)
	db_model[:] = model_3d
	db_ff[:] = ff_3d
	print('Chromospheric model file created-->', fname)
	print(model_3d.shape)
	f.close()


