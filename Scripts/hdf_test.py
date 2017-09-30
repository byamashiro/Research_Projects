import h5py
import numpy as np
import pandas as pd

def keys(f):
    return [key for key in f.keys()]
'''
f = h5py.File('mag_data_16sec_2496.hdf', 'r')
print(keys(f))
f.close()
'''
with pd.HDFStore('mag_data_4min_2439.hdf',  mode='r') as newstore:
    df_restored = newstore.select('df')

