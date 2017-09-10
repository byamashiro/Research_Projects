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
save_option = 'yes' # either 'yes' or 'no'



event_option = 'no' # either 'yes' or 'no'
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

''' // uncomment for final
detection_year = input('Enter year to parse for proton events: ')
detection_start = f'{detection_year}0101'
detection_end = f'{int(detection_year)+1}0101'
'''
detection_year = '2012'
detection_start = 20120301
detection_end = 20120331

detection_threshold = 0.5


# l_day = calendar.monthrange(2002,1)


# print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-13/15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts (Requires Internet Connection)\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-13/15 Xray Flux\n{"="*40}')

'''
1 - GOES Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
5 - GOES-15 Xray Flux
'''

'''
option_bin_set = set()
while True: # energy_bin != 'done':
	if event_option == 'yes':
		option_bin_set = {'1', '2', '4', '5'}

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

#===============Time frame

start_date = str(detection_start)
end_date = str(detection_end)


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



start_hour = '00' # input('Enter a start hour or "full": '), zfill(2)

if start_hour.isdigit() == True:
	end_hour = '23' # input('Enter a end hour: '), zfill(2)
	if start_date == end_date:
		if (int(end_hour) - int(start_hour)) < 0:
			print('\nTIME ERROR: Difference between two hours must be greater than, zero.')
			sys.exit(0)
	elif int(end_hour) > 24 or int(start_hour) > 23:
		print('\nTIME ERROR: Hours must be between 0 and 23.')
		sys.exit(0)

if start_hour.isdigit() == False:
	if start_hour == 'full':
		start_hour = '00', zfill(2)
		end_hour = '23', zfill(2)
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
option_bin_set = {'1'}

if '1' in option_bin_set:
	if event_option == 'yes':
		satellite_no = str(event_list['prot_sat'][0])

	if event_option != 'yes':
		satellite_no = input('Specify which GOES Satellite for Proton Flux (13 or 15): ')
		if satellite_no != '13':
			if satellite_no != '15':
				print('SATELLITE ERROR: Must specify either 13 or 15.')
				sys.exit(0)

	print(f'\n{"="*40}\n{"=" + "GOES Proton Event Detector".center(38," ") + "="}\n{"="*40}')
	print(f'Parsing events for GOES-{satellite_no} for year {detection_year}')
	energy_bin_set = set()
	'''
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
	'''
	
	proton_df_13 = pd.DataFrame([])
	proton_df = pd.DataFrame([])

	cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']
	

	event_set = set()

	months_in_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	for month_event in months_in_year:
		try:
			print(f'\rParsing month - {month_event}', end="\r")
			f_l_day = calendar.monthrange(int(detection_year), int(month_event))
			event_f_day = str(f'{detection_year}{str(month_event).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
			event_l_day = str(f'{detection_year}{str(month_event).zfill(2)}{str(f_l_day[1]).zfill(2)}')
			
			proton_name_13 = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/{proton_name_13}')


			if proton_check == True:
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_13 = pd.read_csv(f'{data_directory}/GOES_Detection/{proton_name_13}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)


			elif proton_check == False:
				proton_url_13 = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{detection_year}/{str(month_event).zfill(2)}/goes{satellite_no}/csv/{proton_name_13}'
				# proton_url_13 = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name_13}'
				proton_in_13 = wget.download(proton_url_13)
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_13 = pd.read_csv(f'{proton_in_13}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0) # ZPGT100W
	
			for i in proton_df_13[proton_df_13['ZPGT100W'] > detection_threshold].index:
				# print(str(i)[:10].replace('-',''))
				event_set.add(str(i)[:10].replace('-',''))

			if save_option == 'yes':
				shutil.move(f'{proton_name_13}', f'{data_directory}/GOES_Detection/')
			if save_option == 'no':
				os.remove(proton_name_13)

			continue
			
		except:
			print(f'{month_event} does not have data.')


	print(sorted(list(event_set)))

	sys.exit(0)



'''
	date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')
			f_l_day = calendar.monthrange(int(detection_year), int(i))
	
			event_f_day = str(f'{date.year}{str(date.month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
			event_l_day = str(f'{date.year}{str(date.month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
	
	
			#print(event_date[0:6])
			# proton_name = f'g{satellite_no}_epead_p27w_32s_{event_date}_{event_date}.csv'
			proton_name_13 = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name_13}')
	
			if proton_check == True:
				dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
				proton_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				proton_df = proton_df.append(proton_df_ind)
	
			elif proton_check == False:
				# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
				# proton_in = wget.download(proton_url)
	
				
				# [i for i in range(len(proton_df_13.columns)) if i]
	
				for i in proton_df_13.columns:
					if i != 'ZPGT100W':
						proton_df_13.drop(f'{i}', inplace=True, axis=1)
	
				proton_df_13.loc[proton_df_13['ZPGT100W'] < 0.0] = np.nan
	
				print(proton_df_13.loc[proton_df_13['ZPGT100W'] > 1.0] )
	
				for i in proton_df_13[proton_df_13['ZPGT100W'] > 1.0].index:
					# print(str(i)[:10].replace('-',''))
					event_set.add(str(i)[:10].replace('-',''))
						
	
				# print(proton_df_13.loc[proton_df_13['ZPGT100W'] > 1.0]) #check if value is over 1
	
				
				# for i in proton_df_13.values:
				#	if i >= 1.0:
				#		print()
				
	
	
	
				
				# for i in range(len(proton_df_13)):
				#	if proton_df_13['ZPGT100W'][i] < 0.0:
				#		print(proton_df_13.iloc[i])
				
				# proton_13 = proton_df_13['ZPGT100W']
				# proton_df_13 = pd.DataFrame([])
				# del proton_df_13
	
				# proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
				# proton_df_13 = proton_df_13.append(proton_df_ind_13) # appends for all dates, keep if want a year long memory file
				if save_option == 'yes':
					shutil.move(f'{proton_name_13}', f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/')
				elif save_option == 'no':
					os.remove(proton_name_13)
		
			# os.remove(proton_name)
		except:
			print(f'\nMissing data for {date}')
			continue
		
		# proton_df.loc[proton_df['P2W_UNCOR_FLUX'] < 0.0] = np.nan #6.5 MeV
	# proton_df.loc[proton_df['P3W_UNCOR_FLUX'] < 0.0] = np.nan #11.6 MeV
	# proton_df.loc[proton_df['P4W_UNCOR_FLUX'] < 0.0] = np.nan #30.6 MeV
	# proton_df.loc[proton_df['P5W_UNCOR_FLUX'] < 0.0] = np.nan #63.1 MeV
	# proton_df.loc[proton_df['P6W_UNCOR_FLUX'] < 0.0] = np.nan #165 MeV
	# proton_df.loc[proton_df['P7W_UNCOR_FLUX'] < 0.0] = np.nan #433 MeV
'''