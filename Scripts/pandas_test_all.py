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
import pandas_test_omni


# ================= test trial for large code loop
import subprocess

# import pandas_test_omni

script_directory_path = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/pandas_test_omni.py'
event_list_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/event_lists'
event_list_name = 'xflare_list.txt'

event_columns = ['event_date_st', 'event_date_ed', 'flare_int', 'event_st_hr', 'event_ed_hr', 'opt_1', 'opt_2', 'opt_3', 'opt_4', 'prot_sat', 'xray_sat', 'prot_opt']
# event_option = 'yes' # either 'yes' or 'no'


event_lister = pd.read_csv(f'{event_list_directory}/{event_list_name}', sep = '\t', names=event_columns, comment='#')

for i in range(len(event_lister)):
	event_list = event_lister.loc[i]
	os.system('/Users/bryanyamashiro/Documents/Research_Projects/Scripts/pandas_test_omni.py')
	# subprocess.call(f'{script_directory_path}', shell=True)
	print('this is working')



#=========== Plotting Data
'''
1 - GOES-15 Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
'''
length_data = int(len(option_bin_set))
length_data_list = []
for i in range(length_data):
	length_data_list.append(i)


j = -1
def next():
	global j
	if (j < length_data+2):
		j += 1
	#print(length_data_list[j])

def applyPlotStyle():
	axes[length_data_list[j]].grid(True)
	axes[length_data_list[j]].minorticks_on()
	axes[length_data_list[j]].legend(loc='lower right', ncol=1,fontsize=8)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)


if length_data > 1:
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6))

if length_data == 1:
	length_data_list[0] = 0,0
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6), squeeze=False)


# proton flux plotting
if '1' in option_bin_set:
	next()
	for i in sorted(energy_bin_list):
		axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}')#, logy=True)
	axes[length_data_list[j]].set_yscale('log')
	axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()



if '2' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='navy', label= '20 kHz - 1040 kHz')
	axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()


if '3' in option_bin_set:
	next()
	color_count = []

	for i in sorted_nm_list:
	
		color_list = ['red','orange','green','blue','indigo','violet','purple'] #,'yellow'
		color_list = list(set(color_list) - set(color_count))
	
		rand_color = random.choice(color_list)
		color_count.append(rand_color)
	
		axes[length_data_list[j]].plot(nm_data[f'{i}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=rand_color, label=f'{i}')
	axes[length_data_list[j]].set_ylabel('Neu. Monitor\n[counts/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '4' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE')
	axes[length_data_list[j]].plot(ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='ACE: H Bulk Speed')
	axes[length_data_list[j]].set_ylabel('Solar Wind\nSpeed [km/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '5' in option_bin_set:
	next()
	axes[length_data_list[j]].plot(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm')
	axes[length_data_list[j]].plot(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.3 nm')
	axes[length_data_list[j]].set_yscale('log')
	axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Xray\nFlux [Wm$^2$]', fontname="Arial", fontsize = 12)
	applyPlotStyle()



plt.xlabel('Time (UT)', fontname="Arial", fontsize = 12)

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax.xaxis.set_major_formatter(myFmt)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
plt.suptitle(f'Legacy Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()

plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
#plt.savefig('omni_test_legacy.png', format='png', dpi=900)

plt.show()