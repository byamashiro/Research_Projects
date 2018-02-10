import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os, errno
import random
# from spacepy import pycdf
# from urllib import error
# from matplotlib.pyplot import cm
# import glob

import calendar
import shutil
import scipy.optimize as optimization


plt.close("all")
plt.ion()

data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'

option_bin_set = '1'


def func(params, xdata, ydata):
	return (ydata - np.dot(xdata, params))

data = pd.read_csv('corr_data_20180204.csv', sep=',', comment='#')

'''
xdata = data['goes_max_proton']
ydata = data['fluence']
# Initial guess
x0 = np.array([0.0, 0.0, 0.0])

print(optimization.leastsq(func, x0, args=(xdata, ydata)))
'''

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
def next_global():
	global j
	if (j < length_data+2):
		j += 1

# ======== Definition of proton flux parameters
def applyPlotStyle():
	axes[length_data_list[j]].grid(True)
	axes[length_data_list[j]].minorticks_on()

	axes[length_data_list[j]].legend(loc='lower right', ncol=1,fontsize=8)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)
	axes[length_data_list[j]].tick_params(axis='y', which='both', direction='in')

	# axes[length_data_list[j]].axvline(proton_df.idxmax().P6W_UNCOR_FLUX) # (proton_df.P6W_UNCOR_FLUX.max())


if length_data > 1:
	if len(option_bin_set) <= 4:
		f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6))
	elif len(option_bin_set) > 4:
		f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 12))

if length_data == 1:
	length_data_list[0] = 0,0
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=False, figsize=(10, 6), squeeze=False)


#======dataset plotting


if '1' in option_bin_set:
	next_global()

	axes[length_data_list[j]].plot(data['fluence'], data['goes_max_proton'], 'o', mfc='none', color='blue', label= '120 kHz Fluence', zorder=5)#, logy=True)
	axes[length_data_list[j]].set_yscale('log')
	axes[length_data_list[j]].set_xscale('log')

	# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
	
	# axes[length_data_list[j]].set_yticks([10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3])
	axes[length_data_list[j]].set_ylabel(f'log(Max Proton Flux) [pfu]', fontname="Arial", fontsize = 12)
	axes[length_data_list[j]].set_xlabel(r'log(Corrected Type III Radio Burst Fluence) [(sfu$\cdot$min$_{TIII}$)$\cdot$ min$_{GOES}$]', fontname="Arial", fontsize = 12)


	applyPlotStyle()
	# plt.show()



if '2' in option_bin_set:
	next_global()
	#=============== Spectrogram testing (begin)
	'''
	from scipy import signal
	from matplotlib.pyplot import cm
	import seaborn as sns
	
	ax = sns.heatmap(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], cmap=cm.viridis)
	#axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)
	#axes[length_data_list[j]].set_ylabel('Type III Radio\nBurst Intensity [sfu]', fontname="Arial", fontsize = 12)

	
	'''
	#=============== Spectrogram testing (end)


	# axes[length_data_list[j]].plot(p4(xx).loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label= 'Gaussian')

	#================= Working code (uncommented) ---- begin ----
	
	#axes[length_data_list[j]].plot(rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='navy', label= '20 kHz - 1040 kHz')
	color_cm=iter(cm.viridis(np.linspace(0,1, 5 )))
	freq_list = [120] # [100, 300, 500, 700, 900]
	
	for frequency in freq_list:
		color_choice = next(color_cm)
	
		axes[length_data_list[j]].plot(rb_data[frequency].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],'.', color=color_choice, label= f'{frequency} kHz', zorder=5)
	axes[length_data_list[j]].set_ylim(0, 500)
	axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)




	applyPlotStyle()


if '3' in option_bin_set:
	next_global()
	color_count = []

	for i in sorted_nm_list:
	
		color_list = ['red','orange','green','blue','indigo','violet','purple'] #,'yellow'
		color_list = list(set(color_list) - set(color_count))
	
		rand_color = random.choice(color_list)
		color_count.append(rand_color)
	
		axes[length_data_list[j]].plot(nm_data[f'{i}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=rand_color, label=f'{i}', zorder=5)
	axes[length_data_list[j]].set_ylabel('Neu. Monitor\n[counts/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '4' in option_bin_set:
	next_global()
	axes[length_data_list[j]].plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE', zorder=5)
	axes[length_data_list[j]].plot(ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], '.',markersize=1, color='blue', label='ACE: H Bulk Speed', zorder=5)
	axes[length_data_list[j]].set_ylabel('Solar Wind\nSpeed [km/s]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '5' in option_bin_set:
	def flare_class(X):
		if X == 10**-4:
			return "X"
		#return ["%.3f" % z for z in V]


	next_global()
	axes[length_data_list[j]].plot(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm', zorder=5)
	axes[length_data_list[j]].plot(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.4 nm', zorder=5)

	axes[length_data_list[j]].set_yscale('log')



	'''
	new_tick_locations = np.array([.2, .5, .9])

	def tick_function(X):
	    V = 1/(1+X)
	    return ["%.3f" % z for z in V]

	ax2.set_xlim(ax1.get_xlim())
	ax2.set_xticks(new_tick_locations)
	ax2.set_xticklabels(tick_function(new_tick_locations))
	ax2.set_xlabel(r"Modified x-axis: $1/(1+X)$")
	'''
	flare_classes = ['', 'A', 'B', 'C', 'M', 'X']
	ax2 = axes[length_data_list[j]].twinx()
	ax2.set_yscale('log')
	ax2.set_ylim(axes[length_data_list[j]].get_ylim())
	ax2.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
	ax2.set_yticklabels(labels=flare_classes)
	ax2.tick_params(axis='y', which='both', direction='in')


	# ax2.set_yticklabels(flare_class([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2]))

	# ax2.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
	# ax2.tick_params(axis='y', which='both', direction='in')

	#axes[length_data_list[j]].set_ylim([(10**(-9)),(10**(-2))])
	# start, stop = ax.get_ylim()
	#start, stop = axes[length_data_list[j]].get_ylim()
	#ticks = np.arange(10**-9, 10**-2, 10)
	#axes[length_data_list[j]].set_yticks(ticks)
	axes[length_data_list[j]].set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])

	# axes[length_data_list[j]].tick_params(axis='y', which='both', direction='in')
	axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no_xray} Xray\nFlux [Wm$^2$]', fontname="Arial", fontsize = 12)
	applyPlotStyle()


if '6' in option_bin_set:

	next_global()
	axes[length_data_list[j]].plot(sta_df[27].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='darkred', label='35.5-40.5 MeV', zorder=5)
	axes[length_data_list[j]].plot(sta_df[29].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='40.0-60.0 MeV', zorder=5)
	axes[length_data_list[j]].plot(sta_df[31].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='orange', label='60.0-100.0 MeV', zorder=5)
	axes[length_data_list[j]].set_yscale('log')

	axes[length_data_list[j]].set_ylabel(f'ST-{satellite_no_st} Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()

if '7' in option_bin_set:

	next_global()
	axes[length_data_list[j]].plot(stb_df[27].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='green', label='35.5-40.5 MeV', zorder=5)
	axes[length_data_list[j]].plot(stb_df[29].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='40.0-60.0 MeV', zorder=5)
	axes[length_data_list[j]].plot(stb_df[31].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='darkmagenta', label='60.0-100.0 MeV', zorder=5)
	axes[length_data_list[j]].set_yscale('log')

	axes[length_data_list[j]].set_ylabel(f'ST-{satellite_no_st} Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()




# plt.xlabel('Time [UT]', fontname="Arial", fontsize = 12)

# myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
# ax.xaxis.set_major_formatter(myFmt)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
# plt.suptitle(f'Space Weather Monitor]', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()

plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
plt.savefig('corr_fluence.png', format='png', dpi=900)


#plt.savefig('omni_test_legacy.png', format='png', dpi=900)
'''
if event_option == 'yes':
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

if save_plot_option == 'yes' and len(option_bin_set) <= 4:
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option == 'yes' and len(option_bin_set) > 4:
	plt.savefig(f'full_omni_plots/omni_full_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option != 'yes':
	plt.show()


'''
plt.show()