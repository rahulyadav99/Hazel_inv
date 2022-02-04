import numpy as np
import matplotlib.pyplot as pl
import hazel
import h5py
import scipy.io as io
print(hazel.__version__)
label = ['I', 'Q', 'U', 'V']

iterator = hazel.Iterator(use_mpi=True)
rank = iterator.get_rank()
mod = hazel.Model('conf/conf.mpi00.ini', working_mode='inversion', verbose=2)

iterator.use_model(model=mod)
iterator.run_all_pixels()

