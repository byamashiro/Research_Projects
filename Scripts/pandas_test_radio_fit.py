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
from matplotlib.pyplot import cm

import shutil

plt.close("all")
# ======= Parameters to set

data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # saves the data files
save_plot_option = 'no' # saves the plots



event_option = 'no' # use event list to plot
# ========== Event list (Still being implemented, do not uncomment)
'''
event_list_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/event_lists'
event_list_name = 'xflare_list.txt'


event_columns = ['event_date_st', 'event_date_ed', 'flare_int', 'event_st_hr', 'event_ed_hr', 'opt_1', 'opt_2', 'opt_3', 'opt_4', 'prot_sat', 'xray_sat', 'prot_opt']


if event_option == 'yes':
	event_list = pd.read_csv(f'{event_list_directory}/{event_list_name}', sep = '\t', names=event_columns, comment='#')

'''
# ========== Definitions

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

#==============Choosing Dataset

print(f'{"="*40}\n{"=" + "Radio Burst Fit Program".center(38," ") + "="}\n{"="*40}')

'''
1 - GOES Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
5 - GOES-15 Xray Flux
'''


option_bin_set = set()

'''
while True: # energy_bin != 'done':
	if event_option == 'yes':
		# option_bin_set = {'1', '2', '4', '5'}
		option_bin_set = {'2'}

		break

	if event_option != 'yes':
		option_bin = input('Enter Dataset Option then "done" or "all": ').lower()

		if option_bin != 'done':
			if option_bin == 'all':
				option_bin_set.add('1')
				option_bin_set.add('2')
				option_bin_set.add('3')
				option_bin_set.add('4')
				option_bin_set.add('5')
				break
			
			elif int(option_bin) < 6:
				option_bin_set.add(option_bin)
	
				if len(option_bin_set) > 4:
					print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
					sys.exit(0)
	
		elif option_bin == 'done':
			break
'''
option_bin_set = {'2'}

#===============Time frame
if event_option == 'yes':
	start_date = str(event_list['event_date_st'][0])
	end_date = str(event_list['event_date_ed'][0])

if event_option != 'yes':
	start_date = input('Enter a start date (yyyymmdd): ')
	end_date = input('Enter a end date (yyyymmdd): ')


if end_date == '':
	end_date = start_date

start_day = start_date[6:8]
start_month = start_date[4:6]
start_year = start_date[:4]

end_day = end_date[6:8]
end_month = end_date[4:6]
end_year = end_date[:4]
'''
if int(start_year) < 2010: # testing old 2003 data, uncomment laterß
	print('\nDATE ERROR: Date must start after September 1, 2010')
	sys.exit(0)
'''
if len(start_date) != 8 or len(end_date) != 8:
	print('\nDATE ERROR: Dates must have 8 digits.')
	sys.exit(0)


if event_option == 'yes':
	start_hour = str(event_list['event_st_hr'][0])
	end_hour = str(event_list['event_ed_hr'][0])

if event_option != 'yes':
	start_hour = input('Enter a start hour or "full": ').zfill(2)

	if start_hour.isdigit() == True:
		end_hour = input('Enter a end hour: ').zfill(2)
		if start_date == end_date:
			if (int(end_hour) - int(start_hour)) < 0:
				print('\nTIME ERROR: Difference between two hours must be greater than zero.')
				sys.exit(0)
		elif int(end_hour) > 24 or int(start_hour) > 23:
			print('\nTIME ERROR: Hours must be between 0 and 23.')
			sys.exit(0)

	if start_hour.isdigit() == False:
		if start_hour == 'full':
			start_hour = '00'.zfill(2)
			end_hour = '23'.zfill(2)
		else:
			print('\nTIME ERROR: Not a valid alternative hour.')
			sys.exit(0)


start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )

#=========Defining event strings

event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H')

event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H')


#=========== 2: Wind Type III Radio Burst
if '2' in option_bin_set:
	print(f'\n{"="*40}\n{"=" + "Wind Type III Radio Bursts".center(38," ") + "="}\n{"="*40}')
	rb_data = pd.DataFrame([])
	
	for date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')

			#print(event_date[0:6])
			radio_name = f'wi_h1_wav_{event_date}_v01.cdf'
			radio_check = os.path.isfile(f'{data_directory}/WIND/RAD1/{radio_name}')

			if radio_check == True:
				cdf = pycdf.CDF(f'{data_directory}/WIND/RAD1/{radio_name}')

			elif radio_check == False:
				radio_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_name}'
				radio_in = wget.download(radio_url)	
				cdf = pycdf.CDF(radio_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
				if save_option == 'yes':
					shutil.move(f'{radio_name}', f'{data_directory}/WIND/RAD1/')
				elif save_option == 'no':
					os.remove(radio_name)

			# radio_in = wget.download(url)
			
			# os.remove(radio_name)
			# print(f'\nParsing Type III Data for {date}')
			time_rb = []
			for i in cdf['Epoch']:
				time_rb.append(i)
			freq_rb = []
			for i in cdf['Frequency_RAD1']:
				freq_rb.append(i)
			rad1_rb = []
			for i in cdf['E_VOLTAGE_RAD1']:
				rad1_rb.append(i)

			data_time = pd.DataFrame(time_rb)
			data_time.columns = ['date_time']

			data_freq = pd.DataFrame(freq_rb)
			data_freq.columns = ['freq']

			data_rad1 = pd.DataFrame(rad1_rb)
			data_rad1.columns = data_freq['freq']
			# data_rad1[data_rad1 <= 0.0] = np.nan

			rb_concat = pd.concat([data_time, data_rad1], axis=1)
			rb_concat.set_index(['date_time'], inplace=True)
			rb_data = rb_data.append(rb_concat)

		except:
			print(f'\nMISSING DATA FOR: {date}\n')
			continue
	
	# 256 columns (frequencies) + 1 column (average)

	# rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)
	rb_data[rb_data.values == 0.0] = np.nan # replaces 0.0 with np.nan values
	# rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True) # making values zero is not a good idea since arange is scaled appropriately 

	# ===== preliminary method to deal with nans
	'''
	for zero_ind in rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].columns:
		# print('===========freq', zero_ind)
		zero_index = rb_data.index[rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].values == 0.0]
		for zero_val in zero_index:
			# print('======================================================================== zero val', zero_val)
			idx = np.searchsorted(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index, zero_val)
			# loc_ind = rb_data.index.get_loc(zero_val)
			for prev_idx in range(1, 10):
				prev_ind = rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index[max(0, idx-prev_idx)]
				# print('prev ind', prev_ind)
				if rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].loc[prev_ind] != 0.0:
					# print('prev val',rb_data[zero_ind].loc[prev_ind])
					top_val = rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].loc[prev_ind]
					# print('top val', top_val)
					break

			for next_idx in range(1,10):
				next_ind = rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index[min(idx + next_idx, len(rb_data) - next_idx)]
				# print('next ind', next_ind)
				if rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].loc[next_ind] != 0.0:
					# print('next val',rb_data[zero_ind].loc[next_ind])
					bottom_val = rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].loc[next_ind]
					# print('bottom val', bottom_val)
					break

			if bottom_val > top_val:
				large_val = bottom_val
				small_val = top_val
			elif bottom_val < top_val:
				large_val = top_val
				small_val = bottom_val

			rb_data[zero_ind].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].loc[zero_val] = (large_val + small_val)/2
		# break # only runs for one frequency
	#sys.exit(0)
	'''

	# ===== preliminary method end






	fit_option = 'yes'
	if fit_option == 'yes':
		length_data = int(len(option_bin_set))
		length_data_list = []
		for i in range(length_data):
			length_data_list.append(i)
		
		
		j = -1
		def next_global():
			global j
			if (j < length_data+2):
				j += 1


		def applyPlotStyle():
			axes[length_data_list[j]].grid(True)
			axes[length_data_list[j]].minorticks_on()
			axes[length_data_list[j]].legend(loc='upper right', ncol=1,fontsize=8)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)
			axes[length_data_list[j]].tick_params(axis='y', which='both', direction='in')
			if '1' in option_bin_set:
				high_bin_proton = sorted(energy_bin_list)[-1][0]
				low_bin_proton = sorted(energy_bin_list)[0][0]
		
				high_bin_proton_str = sorted(energy_bin_list)[-1][1]
				low_bin_proton_str = sorted(energy_bin_list)[0][1]
				axes[length_data_list[j]].axvline(proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), zorder=1) # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified


		if length_data > 1:
			f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6))

		if length_data == 1:
			length_data_list[0] = 0,0
			f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=False, figsize=(10, 6), squeeze=False)



		# ======= fit process
		

		ymax_ind = rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()
		ymax_val = rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max()
		tvals = rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index
		# xvals = np.arange(len(tvals))

		panda_ind = pd.DataFrame([])
		panda_ind['time'] = tvals
		xvals = panda_ind.index.values
		yvals =rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].values

		ymax_center = panda_ind.index[panda_ind['time'] == ymax_ind].values

		# =========== Skewed Gaussian limfit Model (BEGIN)
		
		from lmfit.models import SkewedGaussianModel
		model_skg = SkewedGaussianModel(missing='drop') # when using np.nan instead of .drop # missing='drop'
		params_skg = model_skg.make_params(amplitude=ymax_val, center=ymax_center, sigma=1, gamma=0)
		
		skewed_gaussian = model_skg.fit(yvals, params_skg, x = xvals)
		print("Skewed Gaussian Model\n", skewed_gaussian.fit_report())
		
		# =========== Skewed Gaussian limfit Model (END)

		# =========== Exponential Gaussian limfit Model (BEGIN)
		
		from lmfit.models import ExponentialGaussianModel
		model_exg = ExponentialGaussianModel(missing='drop') # when using np.nan instead of .drop # missing='drop'
		params_exg = model_exg.make_params(amplitude=ymax_val, center=ymax_center, sigma=1, gamma=0)
		
		exponential_gaussian = model_exg.fit(yvals, params_exg, x = xvals)
		print("Exponential Gaussian Model\n", exponential_gaussian.fit_report())
		
		# =========== Exponential Gaussian limfit Model (END)

		# =========== Donaich limfit Model (BEGIN)
		
		from lmfit.models import DonaichModel
		model_donaich = DonaichModel(missing='drop') # when using np.nan instead of .drop # missing='drop'
		params_donaich = model_donaich.make_params(amplitude=ymax_val, center=ymax_center, sigma=1, gamma=0)
		
		donaich = model_donaich.fit(yvals, params_donaich, x = xvals)
		print("Doniach Model\n", donaich.fit_report())
		
		# =========== Donaich limfit Model (END)


		# =========== Lognormal limfit Model (BEGIN) =========== DOES NOT WORK, nans
		'''
		from lmfit.models import LognormalModel
		model_lognorm = LognormalModel(missing='drop') # when using np.nan instead of .drop # missing='drop'
		params_lognorm = model_lognorm.make_params(amplitude=ymax_val, center=ymax_center, sigma=1)
		
		log_normal = model_lognorm.fit(yvals, params_lognorm, x = xvals)
		print("Log Normal Model\n", log_normal.fit_report())
		'''
		# =========== Lognormal limfit Model (END)

		# =========== Gaussian SCIPY (BEGIN)

		gaussian = lambda x: 3*np.exp(-(30-x)**2/20.)
		
		# data = gaussian(np.arange(100))
		# plt.plot(data, '.')
		
		X = xvals #np.arange(data.size)
		x = np.sum(X * yvals)/np.sum(yvals) # np.sum(X*data)/np.sum(data)
		width = np.sqrt(np.abs(np.sum((X-x)**2*yvals)/np.sum(yvals)))
		
		# max = data.max()
		
		fit = lambda t : ymax_val * np.exp(-(t-x)**2/(2*width**2)) # max
		

		# ======= load fits into pandas df

		# panda_ind['scipy_gaussian'] = fit(X)
		rb_data.drop(rb_data[rb_data.isnull().values].index, inplace=True)

		panda_ind_2 = pd.DataFrame([])
		panda_ind_2['time'] = rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index


		panda_ind_2['lmfit_skewedgaussian'] = skewed_gaussian.best_fit
		panda_ind_2['lmfit_exponentialgaussian'] = exponential_gaussian.best_fit
		panda_ind_2['lmfit_donaich'] = donaich.best_fit
		# panda_ind_2['lmfit_lognorm'] = log_normal.best_fit
		panda_ind_2.set_index('time', inplace=True)


		# panda_ind['lmfit_skewedgaussian'] = result.best_fit
		# panda_ind.set_index('time', inplace=True)



		# ===========Gaussian SCIPY (END)




		next_global()
		'''
		color_cm=iter(cm.viridis(np.linspace(0,1, 5 )))
		freq_list = [100, 300, 500, 700, 900]
		
		for frequency in freq_list:
			color_choice = next(color_cm)
	
			axes[length_data_list[j]].plot(rb_data[frequency].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=color_choice, label= f'{frequency} kHz', zorder=5)
		'''
		# axes[length_data_list[j]].plot(rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label= '300 kHz', zorder=5)
		axes[length_data_list[j]].plot(rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],'o', markerfacecolor='none', markeredgecolor='blue', color='blue', label= '300 kHz', zorder=5)
		
		# axes[length_data_list[j]].plot(x=rb_data[300].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index, y = result.best_fit, color='red', label= 'Best Fit', zorder=5) # x=xvals,
		# axes[length_data_list[j]].plot(panda_ind['scipy_gaussian'], color='red', label= 'Scipy Gaussian', zorder=5) # x=xvals,
		axes[length_data_list[j]].plot(panda_ind_2['lmfit_skewedgaussian'], color='red', label= 'LMFIT Skewed Gaussian', zorder=5, linestyle ='--', linewidth=3) # x=xvals,
		axes[length_data_list[j]].plot(panda_ind_2['lmfit_exponentialgaussian'], color='green', label= 'LMFIT Exponential Gaussian', zorder=5, linewidth=3) # x=xvals,
		axes[length_data_list[j]].plot(panda_ind_2['lmfit_donaich'], color='purple', label= 'LMFIT Donaich', zorder=5, linestyle='-.', linewidth=3) # x=xvals,
		# axes[length_data_list[j]].plot(panda_ind_2['lmfit_lognorm'], color='purple', label= 'LMFIT Log-normal', zorder=5, linestyle='-.') # x=xvals,


		# axes[length_data_list[j]].set_ylim(0, 500)
		axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)


	applyPlotStyle()
	plt.xlabel('Time (UT)', fontname="Arial", fontsize = 12)

	myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
	ax = plt.gca()
	ax.xaxis.set_major_formatter(myFmt)
	
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center') # returning ordinal error
	plt.suptitle(f'Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14) #, y=1.04,
	#plt.tight_layout()
	
	plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
	#plt.savefig('omni_test_legacy.png', format='png', dpi=900)
	
	if event_option == 'yes':
		plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)
	
	if save_plot_option == 'yes':
		plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)
	
	elif save_plot_option != 'yes':
		plt.show()

	plt.show()
	sys.exit(0)



# ======================================== END CURRENT CODE



''' Templates for new data
#===========
print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')

#===========
print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')
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
	#print(length_data_list[j])

#high_bin_proton = sorted(energy_bin_list[-1])[1]
#low_bin_proton = sorted(energy_bin_list[0])[1]

#high_bin_proton_str = sorted(energy_bin_list[-1])[0]
#low_bin_proton_str = sorted(energy_bin_list[0])[0]





def applyPlotStyle():
	axes[length_data_list[j]].grid(True)
	axes[length_data_list[j]].minorticks_on()
	axes[length_data_list[j]].legend(loc='lower right', ncol=1,fontsize=8)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)
	axes[length_data_list[j]].tick_params(axis='y', which='both', direction='in')
	if '1' in option_bin_set:
		high_bin_proton = sorted(energy_bin_list)[-1][0]
		low_bin_proton = sorted(energy_bin_list)[0][0]

		high_bin_proton_str = sorted(energy_bin_list)[-1][1]
		low_bin_proton_str = sorted(energy_bin_list)[0][1]
		axes[length_data_list[j]].axvline(proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), zorder=1) # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified
	# axes[length_data_list[j]].axvline(proton_df.idxmax().P6W_UNCOR_FLUX) # (proton_df.P6W_UNCOR_FLUX.max())


if length_data > 1:
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10, 6))

if length_data == 1:
	length_data_list[0] = 0,0
	f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=False, figsize=(10, 6), squeeze=False)


#======dataset plotting


if '1' in option_bin_set:
	next_global()
	for i in sorted(energy_bin_list):
		axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
	axes[length_data_list[j]].set_yscale('log')
	# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))

	axes[length_data_list[j]].set_yticks([10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3])
	axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
	applyPlotStyle()



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
	freq_list = [100, 300, 500, 700, 900]
	
	for frequency in freq_list:
		color_choice = next(color_cm)
	
		axes[length_data_list[j]].plot(rb_data[frequency].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=color_choice, label= f'{frequency} kHz', zorder=5)
	axes[length_data_list[j]].set_ylim(0, 500)
	axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 12)
	# axes[length_data_list[j]].set_ylabel('Type III Radio\nBurst Int. [sfu]', fontname="Arial", fontsize = 12)
	

	#================= Working code (uncommented) ---- end ----
	# axes[length_data_list[j]].plot(rb_data[int('1020')].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label= '1020')
	# wind_range = range(20,1041, 2)
	# axes[length_data_list[j]].plot(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']) # [wind_range] , color='red', label= '1020')

	# rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(cmap='viridis') # using viridis

	''' This is the next step of the program, uncomment when using
	axes[length_data_list[j]].plot(rb_data[20].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label= '20 kHz')
	axes[length_data_list[j]].plot(rb_data[1040].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='green', label= '1040 kHz')
	'''

	'''
	for i in rb_data.columns:
		if i != 'avg':
			axes[length_data_list[j]].plot(rb_data[i].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], label= f'i')
	'''



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


plt.xlabel('Time (UT)', fontname="Arial", fontsize = 12)

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax.xaxis.set_major_formatter(myFmt)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
plt.suptitle(f'Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()

plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
#plt.savefig('omni_test_legacy.png', format='png', dpi=900)

if event_option == 'yes':
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

if save_plot_option == 'yes':
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option != 'yes':
	plt.show()
