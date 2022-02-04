import numpy as np
import matplotlib.pyplot as pl
import hazel
import h5py
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number", type=int)
args = parser.parse_args()
i = args.number

fil ='conf/conf.mpi'+'{:02d}'.format(i)+'.ini'
print('-->',fil)

iterator = hazel.Iterator(use_mpi=True)
rank = iterator.get_rank()
mod = hazel.Model(fil, working_mode='inversion', verbose=0)

iterator.use_model(model=mod)
iterator.run_all_pixels()

print('-->',fil)
