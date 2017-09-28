import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os, errno
import random
from spacepy import pycdf
from urllib import error
from matplotlib.pyplot import cm
import glob
import calendar
import shutil


def bartels( start_date, end_date ):
	ref_bart_rot = 2286
	ref_bart_date = datetime.date(2001, 1, 7) # datetime.date.strptime('20010107', "%Y%m%d")
	bart_start_day = int( abs(start_date - ref_bart_date).days / 27 )
	bart_end_day = int( abs(end_date - ref_bart_date).days / 27 )
	bart_start = ref_bart_rot + bart_start_day
	bart_end = ref_bart_rot + bart_end_day

	print(f"Bartels Rotation ({start_date}): ", bart_start)
	print(f"Bartels Rotation ({end_date}): ", bart_end)


print(f'\n{"="*40}\n{"=" + f"Bartels Rotation Number".center(38," ") + "="}\n{"="*40}')


start_date = input("Input Start Date (yyyymmdd): ")
end_date = input("Input End Date (yyyymmdd): ")

start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )

bartels(start, end)


'''
day = '20120307'
b_day = '20100114'
ref_b = 2408

f_day = datetime.datetime.strptime(day, "%Y%m%d")
l_day = datetime.datetime.strptime(b_day, "%Y%m%d")

del_day = abs(f_day - l_day).days
b_ind = int(del_day / 27)

b_rot = ref_b + b_ind

print(b_rot)
'''









