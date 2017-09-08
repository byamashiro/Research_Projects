import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os
import random
from spacepy import pycdf
from urllib import error

import shutil

import subprocess

# import pandas_test_omni

script_directory_path = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/pandas_test_omni.py'
event_list_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/event_lists'
event_list_name = 'xflare_list.txt'

event_columns = ['event_date_st', 'event_date_ed', 'flare_int', 'event_st_hr', 'event_ed_hr', 'opt_1', 'opt_2', 'opt_3', 'opt_4', 'prot_sat', 'xray_sat', 'prot_opt']
event_option = 'yes' # either 'yes' or 'no'


if event_option == 'yes':
	event_lister = pd.read_csv(f'{event_list_directory}/{event_list_name}', sep = '\t', names=event_columns, comment='#')

for i in range(len(event_lister)):
	event_list = event_lister.loc[i]
	# os.system("/Users/bryanyamashiro/Documents/Research_Projects/Scripts/pandas_test_omni.py")
	subprocess.call("")
	print('this is working')

