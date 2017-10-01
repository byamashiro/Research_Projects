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
import calendar

import shutil

plt.close("all")
# ======= Parameters to set

data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # saves the data files
save_plot_option = 'yes' # saves the plots
data_collection_option = 'no'
event_option = 'no' # use event list to plot

# long_plot_option = 'yes'

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

print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-13/15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts (Requires Internet Connection)\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-13/15 Xray Flux\n6 - STEREO-A Proton Flux\n7 - STEREO-B Proton Flux\n{"="*40}')

'''
1 - GOES Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
5 - GOES-15 Xray Flux
'''


option_bin_set = set()
while True: # energy_bin != 'done':
	if event_option == 'yes':
		option_bin_set = {'1', '2', '4', '5', '6', '7'}

		break

	if event_option != 'yes':
		option_bin = input('Enter Dataset Option then "done" or "all": ').lower()

		if option_bin != 'done':
			if option_bin == 'all':
				option_bin_set.add('1')	# 1 - GOES-13/15 Proton Flux
				option_bin_set.add('2')	# 2 - Wind Type III Radio Bursts
				option_bin_set.add('3')	# 3 - Neutron Monitor Counts (Requires Internet Connection)
				option_bin_set.add('4')	# 4 - ACE/Wind Solar Wind Speed
				option_bin_set.add('5')	# 5 - GOES-13/15 Xray Flux
				option_bin_set.add('6')	# 6 - STEREO-A Proton Flux
				option_bin_set.add('7')	# 7 - STEREO-B Proton Flux
				break
			
			elif int(option_bin) < 8:
				option_bin_set.add(option_bin)
				'''
				if len(option_bin_set) > 4 and long_plot_option == 'no':
					print('SELECTION ERROR: Only 4 datasets are allowed per canvas.')
					sys.exit(0)
				'''
	
		elif option_bin == 'done':
			break


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


#=========== 1: GOES Proton Flux
if '1' in option_bin_set:
	if event_option == 'yes':
		satellite_no = str(event_list['prot_sat'][0])

	if event_option != 'yes':
		satellite_no = input('Specify which GOES Satellite for Proton Flux (13 or 15): ')
		if satellite_no != '13':
			if satellite_no != '15':
				print('SATELLITE ERROR: Must specify either 13 or 15.')
				sys.exit(0)

	print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Proton Flux".center(38," ") + "="}\n{"="*40}')
	print(f'{"Energy Channels".center(7, " ")}\n{"-"*20}\n1: 6.5 MeV\n2: 11.6 MeV\n3: 30.6 MeV\n4: 63.1 MeV\n5: 165 MeV\n6: 433 MeV')
	energy_bin_set = set()
	
	while True: # energy_bin != 'done':

		if event_option == 'yes':
			energy_bin = 'full'

		elif event_option != 'yes':
			energy_bin = input('Enter Energy Channel(s) or "full": ')

		if energy_bin != 'done':
			if energy_bin == 'full':
				energy_bin_set.add('1')
				energy_bin_set.add('2')
				energy_bin_set.add('3')
				energy_bin_set.add('4')
				energy_bin_set.add('5')
				energy_bin_set.add('6')
				break
			if int(energy_bin) < 7:
				energy_bin_set.add(energy_bin)
				#print(len(energy_bin_set))
	
				if len(energy_bin_set) >= 6:
					#print('len very long')
					break
		elif energy_bin == 'done':
			break
	
	energy_bin_list = []
	for i in energy_bin_set:
		if '1' in i:
			energy_bin_list.append(['P2W_UNCOR_FLUX','6.5 MeV', 'red'])
		elif '2' in i:
			energy_bin_list.append(['P3W_UNCOR_FLUX','11.6 MeV','orange'])
		elif '3' in i:
			energy_bin_list.append(['P4W_UNCOR_FLUX','30.6 MeV','green'])
		elif '4' in i:
			energy_bin_list.append(['P5W_UNCOR_FLUX','63.1 MeV','blue'])
		elif '5' in i:
			energy_bin_list.append(['P6W_UNCOR_FLUX','165 MeV','purple'])
		elif '6' in i:
			energy_bin_list.append(['P7W_UNCOR_FLUX','433 MeV','violet'])
	
	
	proton_df = pd.DataFrame([])
	
	for date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')

			#print(event_date[0:6])
			proton_name = f'g{satellite_no}_epead_p27w_32s_{event_date}_{event_date}.csv'
			proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}')
			if proton_check == True:
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)

			elif proton_check == False:
				proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
				proton_in = wget.download(proton_url)	
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)
				if save_option == 'yes':
					shutil.move(f'{proton_name}', f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/')
				elif save_option == 'no':
					os.remove(proton_name)
	
			# os.remove(proton_name)
		except:
			print(f'\nMissing data for {date}')
			continue
	
	proton_df.drop(proton_df[proton_df['P2W_UNCOR_FLUX'] <= 0.0].index, inplace=True)
	proton_df.drop(proton_df[proton_df['P3W_UNCOR_FLUX'] <= 0.0].index, inplace=True)
	proton_df.drop(proton_df[proton_df['P4W_UNCOR_FLUX'] <= 0.0].index, inplace=True)
	proton_df.drop(proton_df[proton_df['P5W_UNCOR_FLUX'] <= 0.0].index, inplace=True)
	proton_df.drop(proton_df[proton_df['P6W_UNCOR_FLUX'] <= 0.0].index, inplace=True)
	proton_df.drop(proton_df[proton_df['P7W_UNCOR_FLUX'] <= 0.0].index, inplace=True)

	'''
	proton_df.loc[proton_df['P2W_UNCOR_FLUX'] <= 0.0] = np.nan #6.5 MeV
	proton_df.loc[proton_df['P3W_UNCOR_FLUX'] <= 0.0] = np.nan #11.6 MeV
	proton_df.loc[proton_df['P4W_UNCOR_FLUX'] <= 0.0] = np.nan #30.6 MeV
	proton_df.loc[proton_df['P5W_UNCOR_FLUX'] <= 0.0] = np.nan #63.1 MeV
	proton_df.loc[proton_df['P6W_UNCOR_FLUX'] <= 0.0] = np.nan #165 MeV
	proton_df.loc[proton_df['P7W_UNCOR_FLUX'] <= 0.0] = np.nan #433 MeV
	'''



#proton flux 2003
'''
	if int(start_year) == 2003:
		print(f'\n{"="*40}\n{"=" + "GOES-10 Time Averaged Proton Flux".center(38," ") + "="}\n{"="*40}')
		print(f'{"Energy Channels".center(7, " ")}\n{"-"*20}\n1: 0.6 - 4.0 MeV\n2: 4.0 - 9.0 MeV\n3: 9.0 - 15.0 MeV\n4: 15.0 - 44.0 MeV\n5: 40.0 - 80.0 MeV\n6: 80.0 - 165.0 MeV\n7: 165.0 - 500.0 MeV')
		energy_bin_set = set()
		while True: # energy_bin != 'done':
			energy_bin = input('Enter Energy Channel(s) or "full": ')
			if energy_bin != 'done':
				if energy_bin == 'full':
					energy_bin_set.add('1')
					energy_bin_set.add('2')
					energy_bin_set.add('3')
					energy_bin_set.add('4')
					energy_bin_set.add('5')
					energy_bin_set.add('6')
					energy_bin_set.add('7')
					break
				if int(energy_bin) < 8:
					energy_bin_set.add(energy_bin)
					#print(len(energy_bin_set))
					if len(energy_bin_set) >= 7:
						#print('len very long')
						break
			elif energy_bin == 'done':
				break
		energy_bin_list = []
		for i in energy_bin_set:
			if '1' in i:
				energy_bin_list.append(['p1_flux','0.6 - 4.0 MeV', 'red'])
			elif '2' in i:
				energy_bin_list.append(['p2_flux','4.0 - 9.0 MeV','orange'])
			elif '3' in i:
				energy_bin_list.append(['p3_flux','9.0 - 15.0 MeV','green'])
			elif '4' in i:
				energy_bin_list.append(['p4_flux','15.0 - 44.0 MeV','blue'])
			elif '5' in i:
				energy_bin_list.append(['p5_flux','40.0 - 80.0 MeV','purple'])
			elif '6' in i:
				energy_bin_list.append(['p6_flux','80.0 - 165.0 MeV','violet'])
			elif '7' in i:
				energy_bin_list.append(['p7_flux','165.0 - 500.0 MeV','limegreen'])
		proton_df = pd.DataFrame([])
		for date in daterange( start, end ):
			try:
				event_date = str(date).replace('-','')
				#print(event_date[0:6])
				proton_name = f'g10_eps_1m_20031001_20031031.csv' # need to change the final date {event_date}
				#g10_eps_1m_{event_date}_20031031.csv
				proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes10/csv/{proton_name}'

				#https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes10/csv/
				proton_in = wget.download(proton_url)
				#name_list = ['datetime'] + [ str(i) for i in sorted_nm_list]
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=214, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)
				os.remove(proton_name)
			except:
				print(f'\nMissing data for {date}')
				continue
		proton_df.loc[proton_df['p1_flux'] < 0.0] = np.nan #6.5 MeV
		proton_df.loc[proton_df['p2_flux'] < 0.0] = np.nan #11.6 MeV
		proton_df.loc[proton_df['p3_flux'] < 0.0] = np.nan #30.6 MeV
		proton_df.loc[proton_df['p4_flux'] < 0.0] = np.nan #63.1 MeV
		proton_df.loc[proton_df['p5_flux'] < 0.0] = np.nan #165 MeV
		proton_df.loc[proton_df['p6_flux'] < 0.0] = np.nan #433 MeV
		proton_df.loc[proton_df['p7_flux'] < 0.0] = np.nan #433 MeV
'''
'''
GOES-8 1995-01 to 2003-06
GOES-9 1996-04 to 1998-07
GOES-10 1998-07 to 2009-12
GOES-11 2000-07 to 2011-02
GOES-12 2003-01 to 2010-08
GOES-13 2010-04 to present, (2006-07 to present for EUVS data)
GOES-14 2009-12 to present, (2009-07 to 2012-11 for EUVS data)
GOES-15 2010-09 to present, (2010-04 to present for EUVS data)
'''


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




			'''
			radio_name = f'wi_h1_wav_{event_date}_v01.cdf'
			url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_name}'
			radio_in = wget.download(url)
			
			cdf = pycdf.CDF(radio_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
			os.remove(radio_name)
		
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
			
			rb_concat = pd.concat([data_time, data_rad1], axis=1)
			rb_concat.set_index(['date_time'], inplace=True)
		
			rb_data = rb_data.append(rb_concat)
			'''
		except:
			print(f'\nMISSING DATA FOR: {date}\n')
			continue
	
	 # 256 columns (frequencies) + 1 column (average)
	rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)
	'''
	for radio_line in rb_data.values:
		# print("rad line", radio_line)
		print(radio_line.index)
		radio_null = 0
		for radio_freq in radio_line:
			if radio_freq == 0.0:
				radio_null += 1
		print("radionull", radio_null)

		if radio_null > 200:
			rb_data.drop(radio_line, inplace=True)
	'''
	# rb_data[rb_data.values == 0.0].index.values

	rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True)


	# if radio_null > 200:
	#	rb_data = rb_data[rb_data['avg'] != 0.0]


	# ============ EXPERIMENTAL FITTING (DO NOT USE)
	'''
	fit_choice = input('\nType "1 - 3" if you would like to fit: (currently in work)')


	if fit_choice == '1': # curve fitting
		rb_data['d_int'] = mdates.date2num(rb_data.index.to_pydatetime())

		z4 = np.polyfit(rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], 3)
		p4 = np.poly1d(z4)

		xx = np.linspace(rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].min(), rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max(), 20)
		dd = mdates.num2date(xx)

		plt.plot(dd, p4(xx), 'o')
		plt.show()



	if fit_choice == '2': # gaussian fitting
		from astropy.modeling import models, fitting

		rb_data['d_int'] = mdates.date2num(rb_data.index.to_pydatetime())
		rs_time = rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']


		n_obs = len(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index)
		data = rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']
		# X = np.arange(n_obs)
		X = rs_time


		x = np.sum(X * data)/np.sum(data)
		width = np.sqrt(np.abs(np.sum((X-x)**2*data)/np.sum(data)))

		max_data = data.max()

		gauss_fit = lambda t : max_data*np.exp(-(t-x)**2/(2*width**2))

		plt.plot(gauss_fit(X), '-', color='blue')
		plt.plot(rs_time, data, 'o', color='red')
		


		plt.show()

	if fit_choice == '3': # skewed gaussian fitting
		from lmfit.models import SkewedGaussianModel
	
		from astropy.modeling import models, fitting
	
		rb_data['d_int'] = mdates.date2num(rb_data.index.to_pydatetime())
		rs_time = rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']
		n_obs = len(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index)
		data = rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']

		data_max_index = mdates.date2num(rb_data['avg'].idxmax().to_pydatetime())
		# X = np.arange(n_obs)
		X = rs_time
		x = np.sum(X * data)/np.sum(data)

		width = np.sqrt(np.abs(np.sum((X-x)**2*data)/np.sum(data)))
		max_data = data.max()
		gauss_fit = lambda t : max_data*np.exp(-(t-x)**2/(2*width**2))
	
		skg_model = SkewedGaussianModel()
		skg_params = skg_model.make_params(amplitude = 147, center = 734569.0245138889, sigma = 1, gamma = 0) # sigma, gamma = 1, 0
		# skg_params = skg_model.make_params(amplitude = data.max(), center = data_max_index, sigma = 1, gamma = 0) # sigma, gamma = 1, 0
		

		skg_result = skg_model.fit(data, skg_params, x=rs_time)
		print(skg_result.fit_report())

		plt.axvline(734569.0245138889)
		plt.plot(gauss_fit(X), '-', color='blue')
		plt.plot(rs_time, data, 'o', color='red')
		plt.plot(rs_time, skg_result.best_fit)
		
		plt.show()

	if fit_choice == '4': # inverse gaussian fit
		from scipy.stats import invgauss

		rb_data['d_int'] = mdates.date2num(rb_data.index.to_pydatetime())
		rs_time = rb_data['d_int'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']
		n_obs = len(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index)
		data = rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}']
		data_max_index = mdates.date2num(rb_data['avg'].idxmax().to_pydatetime())
		# X = np.arange(n_obs)
		X = rs_time
		x = np.sum(X * data)/np.sum(data)
		width = np.sqrt(np.abs(np.sum((X-x)**2*data)/np.sum(data)))
		max_data = data.max()
		gauss_fit = lambda t : max_data*np.exp(-(t-x)**2/(2*width**2))
		skg_model = SkewedGaussianModel()
		skg_params = skg_model.make_params(amplitude = 147, center = 734569.0245138889, sigma = 1, gamma = 0) # sigma, gamma = 1, 0
		# skg_params = skg_model.make_params(amplitude = data.max(), center = data_max_index, sigma = 1, gamma = 0) # sigma, gamma = 1, 0
		skg_result = skg_model.fit(data, skg_params, x=rs_time)
		print(skg_result.fit_report())

		plt.axvline(734569.0245138889)

		inv_gauss = invgauss.fit(data)

		plt.plot(gauss_fit(X), '-', color='blue')
		plt.plot(rs_time, data, 'o', color='red')
		plt.plot(rs_time, skg_result.best_fit)
		plt.plot(rs_time, inv_gauss, color = 'green')

		plt.show()


''' # end experimental fitting





#=========== 3: Neutron Monitors
if '3' in option_bin_set:
	print(f'\n{"="*40}\n{"=" + "Neutron Monitors".center(38," ") + "="}\n{"="*40}')
	
	list_nm = ['AATB','APTY','ARNM','ATHN','BKSN','CALG','CALM','DOMB',
				'DOMC','DRBS','ESOI','FSMT','HRMS','INVK','IRK2','IRK3',
				'IRKT','JBGO','JUNG','JUNG1','KERG','KIEL','KIEL2','LMKS',
				'MCRL','MGDN','MOSC','MRNY','MWSN','MXCO','NAIN','NANM','NEU3',
				'NEWK','NRLK','NVBK','OULU','PSNM','PTFM','PWNK','ROME','SANB','SNAE'
				,'SOPB','SOPO','TERA','THUL','TIBT','TXBY','YKTK']
	
	num_station = int(input('How many stations to parse: '))
	print(f'You are parsing {num_station} station(s)')
	
	station_multi = []
	for i in range(num_station):
		station = input('Enter station names: ').upper()
		if station == '':
			station = 'OULU'
			station_multi.append(station)
		elif station == 'RANDOM':
			station = random.choice(list_nm)
			station_multi.append(station)
		else:
			station_multi.append(station)
	
	print(f'Parsing the {station_multi} stations')
	
	
	#sorter_list = ['PSNM', 'TIBT', 'ESOI', 'ATHN', 'MXCO', 'ARNM', 'NANM', 'PTFM', 'CALM', 'AATB', 'ROME', 'BKSN', 'HRMS', 'JUNG', 'JUNG1', 'LMKS', 'IRK2', 'IRK3', 'IRKT', 'DRBS', 'NVBK', 'MCRL', 'MOSC', 'NEWK', 'KIEL', 'KIEL2', 'MGDN', 'YKTK', 'KERG', 'CALG', 'OULU', 'SANB', 'SNAE', 'APTY', 'NRLK', 'TXBY', 'FSMT', 'INVK', 'JBGO', 'NAIN', 'PWNK', 'THUL', 'MWSN', 'NEU3', 'SOPB', 'SOPO', 'MRNY', 'DOMB', 'DOMC', 'TERA']
	sorter = {'PSNM':0, 'TIBT':1, 'ESOI':2, 'ATHN':3, 'MXCO':4, 'ARNM':5, 'NANM':6, 'PTFM':7, 'CALM':8, 'AATB':9, 'ROME':10, 'BKSN':11, 'HRMS':12, 'JUNG':13, 'JUNG1':14, 'LMKS':15, 'IRK2':16, 'IRK3':17, 'IRKT':18, 'DRBS':19, 'NVBK':20, 'MCRL':21, 'MOSC':22, 'NEWK':23, 'KIEL':24, 'KIEL2':25, 'MGDN':26, 'YKTK':27, 'KERG':28, 'CALG':29, 'OULU':30, 'SANB':31, 'SNAE':32, 'APTY':33, 'NRLK':34, 'TXBY':35, 'FSMT':36, 'INVK':37, 'JBGO':38, 'NAIN':39, 'PWNK':40, 'THUL':41, 'MWSN':42, 'NEU3':43, 'SOPB':44, 'SOPO':45, 'MRNY':46, 'DOMB':47, 'DOMC':48, 'TERA':49}
	sorted_lambda = sorted(sorter.items(), key=lambda x: x[1])
	
	
	sorted_nm_list = []
	for i in [i[0] for i in sorted_lambda]:
		if i in station_multi:
			sorted_nm_list.append(i)
	
	
	station_str = ''
	for i in sorted_nm_list:
		station_str += f'&stations[]={i}'
	
	
	url = f'http://www.nmdb.eu/nest/draw_graph.php?formchk=1{station_str}&tabchoice=revori&dtype=corr_for_efficiency&tresolution=0&yunits=0&date_choice=bydate&start_day={start_day}&start_month={start_month}&start_year={start_year}&start_hour={start_hour}&start_min=00&end_day={end_day}&end_month={end_month}&end_year={end_year}&end_hour={end_hour}&end_min=00&output=ascii'
	# start minute set to '00', fix this eventually using {start_minute} and {end_minute}
	nm_data = pd.DataFrame([])
	
	name_list = ['datetime'] + [ str(i) for i in sorted_nm_list]
	
	dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
	nm_data = pd.read_csv(url,sep=';|\n|\b', skiprows=133, skipfooter=3, engine='python', index_col='datetime', date_parser=dateparse, names=name_list, na_values=['   null']) #, , parse_dates=['datetime'], date_parser=dateparse
	
	nm_counter = []
	for item in sorted_nm_list:
		if nm_data[f'{item}'].isnull().values.any() == True:
			nm_counter.append(1)
		else:
			nm_counter.append(0)




#=========== 4: Solar Wind (ACE, Wind)
if '4' in option_bin_set:
	print(f'\n{"="*40}\n{"=" + "ACE/Wind Solar Wind Speed".center(38," ") + "="}\n{"="*40}')
	
	ace_data = pd.DataFrame([])
	wind_data = pd.DataFrame([])
	
	
	for date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')
	
			#====ACE
			swind_ace_name = f'ac_h0_swe_{event_date}_v10.cdf'
			swind_ace_check = os.path.isfile(f'{data_directory}/ACE/SWE_H0/{swind_ace_name}')

			if swind_ace_check == True:
				swind_ace_cdf = pycdf.CDF(f'{data_directory}/ACE/SWE_H0/{swind_ace_name}')

			elif swind_ace_check == False:
				swind_ace_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/{event_date[:4]}/{swind_ace_name}'
				swind_ace_in = wget.download(swind_ace_url)
				swind_ace_cdf = pycdf.CDF(swind_ace_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
				if save_option == 'yes':
					shutil.move(f'{swind_ace_name}', f'{data_directory}/ACE/SWE_H0/')
				elif save_option == 'no':
					os.remove(swind_ace_name)

			# os.remove(swind_ace_name)
				
			time_ace_swind = []
			for i in swind_ace_cdf['Epoch']:
				time_ace_swind.append(i)
			
			bulk_ace_vel = []
			for i in swind_ace_cdf['Vp']:
				bulk_ace_vel.append(i)
	
			data_ace_time = pd.DataFrame(time_ace_swind)
			data_ace_time.columns = ['date_time']
			
			ace_vel = pd.DataFrame(bulk_ace_vel)
			ace_vel.columns = ['ace_bulk_vel']
			
			ace_concat = pd.concat([data_ace_time, ace_vel], axis=1)
			ace_concat.set_index(['date_time'], inplace=True)
		
			ace_data = ace_data.append(ace_concat)
	
			#====WIND
			for i in range(10):
				try:
					swind_wind_name = f'wi_k0_swe_{event_date}_v0{i}.cdf'
					swind_wind_check = os.path.isfile(f'{data_directory}/WIND/K0/{swind_wind_name}')

					if swind_wind_check == True:
						swind_wind_cdf = pycdf.CDF(f'{data_directory}/WIND/K0/{swind_wind_name}')

					elif swind_wind_check == False:
						swind_wind_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_k0/{event_date[:4]}/{swind_wind_name}'
						swind_wind_in = wget.download(swind_wind_url)
						swind_wind_cdf = pycdf.CDF(swind_wind_in)
						if save_option == 'yes':
							shutil.move(f'{swind_wind_name}', f'{data_directory}/WIND/K0/')
						elif save_option == 'no':
							os.remove(swind_wind_name)

				except error.HTTPError as err:
					#print(f'\nVERSION ERROR: The version v0{i} for WIND data does not exist, attempting v0{i+1}')
					continue
				else:
					break
	
	
			# swind_wind_cdf = pycdf.CDF(swind_wind_name) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
			# os.remove(swind_wind_name)
				
			time_wind_swind = []
			for i in swind_wind_cdf['Epoch']:
				time_wind_swind.append(i)
			
			bulk_wind_vel = []
			for i in swind_wind_cdf['V_GSE_p']:
				bulk_wind_vel.append(i)
	
			data_wind_time = pd.DataFrame(time_wind_swind)
			data_wind_time.columns = ['date_time']
			
			wind_vel = pd.DataFrame(bulk_wind_vel)
			wind_vel.columns = ['wind_bulk_vel', 'longitude', 'latitude']
			
			wind_concat = pd.concat([data_wind_time, wind_vel], axis=1)
			wind_concat.set_index(['date_time'], inplace=True)
		
			wind_data = wind_data.append(wind_concat)
	
		except:
			print(f'\nMissing data for {date}')
			continue
	
	
	'''
	ace_data.loc[ace_data['ace_bulk_vel'] <= 0.0] = np.nan #6.5 MeV
	wind_data.loc[wind_data['wind_bulk_vel'] <= 0.0] = np.nan #6.5 MeV
	'''

	ace_data.drop(ace_data[ace_data['ace_bulk_vel'] <= 0.0].index, inplace=True)
	wind_data.drop(wind_data[wind_data['wind_bulk_vel'] <= 0.0].index, inplace=True)


#=========== 5: GOES-15 Xray Flux
if '5' in option_bin_set:
	if event_option == 'yes':
		satellite_no_xray = str(event_list['xray_sat'][0])
	if event_option != 'yes':
		satellite_no_xray = input('\nSpecify which GOES Satellite for Xray Flux (13 or 15): ')
		if satellite_no_xray != '13':
			if satellite_no_xray != '15':
				print('SATELLITE ERROR: Must specify either 13 or 15.')
				sys.exit(0)

	print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no_xray} Xray Flux".center(38," ") + "="}\n{"="*40}')

	xray_df = pd.DataFrame([])
	
	for date in daterange( start, end ):
		'''
		try:
			event_date = str(date).replace('-','')

			#print(event_date[0:6])
			proton_name = f'g{satellite_no}_epead_p27w_32s_{event_date}_{event_date}.csv'
			proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}')
			if proton_check == True:
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)

			elif proton_check == False:
				proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
				proton_in = wget.download(proton_url)	
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)
				if save_option == 'yes':
					shutil.move(f'{proton_name}', f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/')
				elif save_option == 'no':
					os.remove(proton_name)
		'''



		try:
			event_date = str(date).replace('-','')

			xray_name = f'g{satellite_no_xray}_xrs_2s_{event_date}_{event_date}.csv' #g15_xrs_2s_20120307_20120307.csv
			xray_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no_xray}/XRflux/{xray_name}')
			xray_name_list = ['time_tag','A_QUAL_FLAG','A_COUNT','A_FLUX','B_QUAL_FLAG','B_COUNT','B_FLUX']
			#xray_name_list = ['time_tag','A_QUAL_FLAG','A_COUNT','A_FLUX','B_QUAL_FLAG','B_COUNT','B_FLUX']


			if xray_check == True:
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				xray_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no_xray}/XRflux/{xray_name}', skiprows=140, names=xray_name_list, date_parser=dateparse,index_col='time_tag', header=0)
				xray_df = xray_df.append(xray_df_ind)


			elif xray_check == False:
				xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no_xray}/csv/{xray_name}'
				xray_in = wget.download(xray_url)
	
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				xray_df_ind = pd.read_csv(f'{xray_in}', skiprows=140, names=xray_name_list, date_parser=dateparse,index_col='time_tag', header=0) # 138 for 20120307
				xray_df = xray_df.append(xray_df_ind)

				if save_option == 'yes':
					shutil.move(f'{xray_name}', f'{data_directory}/GOES/GOES_{satellite_no_xray}/XRflux/')
				elif save_option == 'no':
					os.remove(xray_name)


		
		except error.HTTPError as err:
			
			# print("working except error")
			# print(f'\nVERSION ERROR: The version v0{i} for WIND data does not exist, attempting v0{i+1}')

			satellite_no_xray_error = ['13', '15']

			for i in satellite_no_xray_error:
				if i == satellite_no_xray:
					satellite_no_xray_error.remove(f'{i}')
					satellite_no_xray = satellite_no_xray_error[0]
					print(f'GOES-{i} data does not exist for this date ({event_date}), using data from GOES-{satellite_no_xray}.')

					xray_name_error = f'g{satellite_no_xray_error[0]}_xrs_2s_{event_date}_{event_date}.csv' #g15_xrs_2s_20120307_20120307.csv
					xray_error_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no_xray_error[0]}/XRflux/{xray_name_error}')
					
					if xray_error_check == True:
						dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
						xray_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no_xray_error[0]}/XRflux/{xray_name_error}', skiprows=140, names=xray_name_list, date_parser=dateparse,index_col='time_tag', header=0)
						xray_df = xray_df.append(xray_df_ind)

					elif xray_error_check == False:
						xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no_xray_error[0]}/csv/{xray_name_error}'
						xray_in = wget.download(xray_url)
				
						dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
						xray_df_ind = pd.read_csv(f'{xray_in}', skiprows=140, names=xray_name_list, date_parser=dateparse,index_col='time_tag', header=0) # 138 for 20120307
						xray_df = xray_df.append(xray_df_ind)
		
						if save_option == 'yes':
							shutil.move(f'{xray_name_error}', f'{data_directory}/GOES/GOES_{satellite_no_xray_error[0]}/XRflux/')
						elif save_option == 'no':
							os.remove(xray_name)

		except:
			print(f'\nMissing data for {date}')
			continue

		else:
			continue	

	'''
	xray_df.loc[xray_df['A_FLUX'] <= 0.0] = np.nan #6.5 MeV
	xray_df.loc[xray_df['B_FLUX'] <= 0.0] = np.nan #11.6 MeV
	'''

	xray_df.drop(xray_df[xray_df['A_FLUX'] <= 0.0].index, inplace=True)
	xray_df.drop(xray_df[xray_df['B_FLUX'] <= 0.0].index, inplace=True)


#=========== 6: STEREO-A Proton Flux
if '6' in option_bin_set:
	if event_option == 'yes':
		satellite_no_st = str(event_list['xray_sat'][0])
	if event_option != 'yes':
		satellite_no_st = 'A' # input('\nSpecify which STEREO Satellite for Proton Flux (A or B): ').upper()
		if satellite_no_st != 'A':
			if satellite_no_st != 'B':
				print('SATELLITE ERROR: Must specify either A or B.')
				sys.exit(0)

	print(f'\n{"="*40}\n{"=" + f"STEREO-{satellite_no_st} Proton Flux".center(38," ") + "="}\n{"="*40}')

	sta_df = pd.DataFrame([])
	curr_month = 'none'
	
	for date in daterange( start, end ):

		try:
			event_date = str(date).replace('-','')

			sta_name = f'{satellite_no_st}eH{event_date[2:4]}{calendar.month_name[int(event_date[4:6])][:3]}.1m' #g15_xrs_2s_20120307_20120307.csv
			sta_check = os.path.isfile(f'{data_directory}/STEREO/STEREO_{satellite_no_st}/{sta_name}')
			# sta_name_list = ['time_tag','A_QUAL_FLAG','A_COUNT','A_FLUX','B_QUAL_FLAG','B_COUNT','B_FLUX']
			sta_name_list = list(np.arange(33))



			if sta_check == True:
				if curr_month != event_date[4:6]:
					curr_month = event_date[4:6]
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					sta_df_ind = pd.read_csv(f'{data_directory}/STEREO/STEREO_{satellite_no_st}/{sta_name}', skiprows=22, delim_whitespace=True, names=sta_name_list, parse_dates=[[1,2,3,4]], index_col='1_2_3_4')
					sta_df = sta_df.append(sta_df_ind)


			elif sta_check == False:
				if curr_month != event_date[4:6]:
					# xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no_xray}/csv/{xray_name}'
					sta_url = f'http://www.srl.caltech.edu/STEREO/DATA/HET/Ahead/1minute/{sta_name}'
					sta_in = wget.download(sta_url)
		
					# dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					sta_df_ind = pd.read_csv(f'{sta_in}', skiprows=22, delim_whitespace=True, names=sta_name_list, parse_dates=[[1,2,3,4]], index_col='1_2_3_4') # 138 for 20120307, parse_dates=[[1,2,3,4]], index_col='1_2_3_4'
					# sta_df_ind = pd.read_csv('AeH07Jan.1m.txt', skiprows=22, delim_whitespace=True, names=sta_name_list, parse_dates=[[1,2,3,4]], header = False, index_col='1_2_3_4')
					sta_df = sta_df.append(sta_df_ind)
	
					if save_option == 'yes':
						shutil.move(f'{sta_name}', f'{data_directory}/STEREO/STEREO_{satellite_no_st}/')
					elif save_option == 'no':
						os.remove(sta_name)

		


		
		except error.HTTPError as err:
			print(f'\nHTTP ERROR: Missing data for {date}')

		except:
			print(f'\nMissing data for {date}')
			continue

		else:
			continue	

	sta_df.drop(sta_df[sta_df[31] <= 0.0].index, inplace=True)
	sta_df.drop(sta_df[sta_df[29] <= 0.0].index, inplace=True)
	sta_df.drop(sta_df[sta_df[27] <= 0.0].index, inplace=True)


#=========== 7: STEREO-B Proton Flux
if '7' in option_bin_set:
	if event_option == 'yes':
		satellite_no_st = str(event_list['xray_sat'][0])
	if event_option != 'yes':
		satellite_no_st = 'B' # input('\nSpecify which STEREO Satellite for Proton Flux (A or B): ').upper()
		if satellite_no_st != 'B':
			if satellite_no_st != 'A':
				print('SATELLITE ERROR: Must specify either A or B.')
				sys.exit(0)

	print(f'\n{"="*40}\n{"=" + f"STEREO-{satellite_no_st} Proton Flux".center(38," ") + "="}\n{"="*40}')

	stb_df = pd.DataFrame([])
	curr_month = 'none'
	
	for date in daterange( start, end ):

		try:
			event_date = str(date).replace('-','')

			stb_name = f'{satellite_no_st}eH{event_date[2:4]}{calendar.month_name[int(event_date[4:6])][:3]}.1m' #g15_xrs_2s_20120307_20120307.csv
			stb_check = os.path.isfile(f'{data_directory}/STEREO/STEREO_{satellite_no_st}/{stb_name}')
			# sta_name_list = ['time_tag','A_QUAL_FLAG','A_COUNT','A_FLUX','B_QUAL_FLAG','B_COUNT','B_FLUX']
			stb_name_list = list(np.arange(33))



			if stb_check == True:
				if curr_month != event_date[4:6]:
					curr_month = event_date[4:6]
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					stb_df_ind = pd.read_csv(f'{data_directory}/STEREO/STEREO_{satellite_no_st}/{stb_name}', skiprows=22, delim_whitespace=True, names=stb_name_list, parse_dates=[[1,2,3,4]], index_col='1_2_3_4')
					stb_df = stb_df.append(stb_df_ind)


			elif stb_check == False:
				if curr_month != event_date[4:6]:
					# xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no_xray}/csv/{xray_name}'
					stb_url = f'http://www.srl.caltech.edu/STEREO/DATA/HET/Behind/1minute/{stb_name}'
					stb_in = wget.download(stb_url)
		
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					stb_df_ind = pd.read_csv(f'{stb_in}', skiprows=22, delim_whitespace=True, names=stb_name_list, parse_dates=[[1,2,3,4]], index_col='1_2_3_4') # 138 for 20120307
					# sta_df_ind = pd.read_csv('AeH07Jan.1m.txt', skiprows=22, delim_whitespace=True, names=sta_name_list, parse_dates=[[1,2,3,4]], header = False, index_col='1_2_3_4')
					stb_df = stb_df.append(stb_df_ind)
	
					if save_option == 'yes':
						shutil.move(f'{stb_name}', f'{data_directory}/STEREO/STEREO_{satellite_no_st}/')
					elif save_option == 'no':
						os.remove(stb_name)

		


		
		except error.HTTPError as err:
			print(f'\nHTTP ERROR: Missing data for {date}')

		except:
			print(f'\nMissing data for {date}')
			continue

		else:
			continue	

	stb_df.drop(stb_df[stb_df[31] <= 0.0].index, inplace=True)
	stb_df.drop(stb_df[stb_df[29] <= 0.0].index, inplace=True)
	stb_df.drop(stb_df[stb_df[27] <= 0.0].index, inplace=True)

'''
# Templates for new data

#===========
print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')
'''






#=========== Data prints
# 1 - GOES-13/15 Proton Flux
# 2 - Wind Type III Radio Bursts
# 3 - Neutron Monitor Counts (Requires Internet Connection)
# 4 - ACE/Wind Solar Wind Speed
# 5 - GOES-13/15 Xray Flux
# 6 - STEREO-A Proton Flux
# 7 - STEREO-B Proton Flux


if data_collection_option == 'yes':
# Xray

	if '1' in option_bin_set:
		for i in sorted(energy_bin_list):
			pmaxflux = proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max()
			pmaxflux_exp = "%0.3E" % pmaxflux
			print(f"GOES-{satellite_no} Peak Proton Flux ({i[1]}): {pmaxflux_exp} [pfu]")


	if '5' in option_bin_set:
		xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()
		fint = xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max()
		fint_exp = "%0.2E" % fint
		if int(str(fint_exp[-3:])) >= -4:
			print(f"GOES-{satellite_no_xray} Peak Xray Flux (0.1-0.8 nm): X{fint_exp[:3]} ({fint_exp} Wm^2)")
		elif int(str(fint_exp[-3:])) >= -5 and int(str(fint_exp[-3:])) < -4:
			print(f"GOES-{satellite_no_xray} Peak Xray Flux (0.1-0.8 nm): M{fint_exp[:3]} ({fint_exp} Wm^2)")
		elif int(str(fint_exp[-3:])) >= -6 and int(str(fint_exp[-3:])) < -5:
			print(f"GOES-{satellite_no_xray} Peak Xray Flux (0.1-0.8 nm): C{fint_exp[:3]} ({fint_exp} Wm^2)")
		elif int(str(fint_exp[-3:])) >= -7 and int(str(fint_exp[-3:])) < -6:
			print(f"GOES-{satellite_no_xray} Peak Xray Flux (0.1-0.8 nm): B{fint_exp[:3]} ({fint_exp} Wm^2)")
		elif int(str(fint_exp[-3:])) < -7:
			print(f"GOES-{satellite_no_xray} Peak Xray Flux (0.1-0.8 nm): A{fint_exp[:3]} ({fint_exp} Wm^2)")
		
		xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()

	sys.exit(0)

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
axes[length_data_list[j]].set_xlabel('Time [UT]', fontname="Arial", fontsize = 12)

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

if save_plot_option == 'yes' and len(option_bin_set) <= 4:
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option == 'yes' and len(option_bin_set) > 4:
	plt.savefig(f'full_omni_plots/omni_full_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option != 'yes':
	plt.show()
