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
from scipy import signal

import calendar

import shutil


# ======= Parameters to set
data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # either 'yes' or 'no'
plot_option = 'yes'
unique_inclusion_option = 'yes'
proton_event_option = 'smooth'

proton_event_full_df_13 = pd.DataFrame() # columns=('start_time', 'end_time', 'proton_duration', 'proton_max_int'))
proton_event_full_df_15 = pd.DataFrame()

proton_smooth_full_df_13 = pd.DataFrame()
proton_smooth_full_df_15 = pd.DataFrame()


# ==== Must change for different energies
energy_parse = int(input("Enter the energy channel (10/50/100): ")) # MeV
if energy_parse != 10:
	if energy_parse != 50:
		if energy_parse != 100:
			print("Please enter a valid energy channel: 10, 50, or 100.")
			sys.exit(0)


if energy_parse == 100:
	detection_threshold = pow(10, -0.8) # 0.25 # detection threshold changed from 0.25 to pow(10, -0.8) (02/02/2018)
	detection_threshold_str = 'new' # 0.50 # changed from '0d25' to pow(10, -0.8)
	energy_channel = 100
	energy_header = 'ZPGT100W' # just change the integer
	
elif energy_parse == 50:
	detection_threshold = 0.6 # 0.25
	detection_threshold_str = '0d60' # 0.50
	energy_channel = 50
	energy_header = 'ZPGT50W' # just change the integer
	
elif energy_parse == 10:
	detection_threshold = 1.5 # 0.25
	detection_threshold_str = '1d50' # 0.50
	energy_channel = 10
	energy_header = 'ZPGT10W' # just change the integer



# ================ 


detection_year = input("Enter year to parse (yyyy) or 'all': ").lower() #yyyypurge or yyyypurgeall
if detection_year == 'all':
	year_list = []
	year_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

elif 'purge' in detection_year: # detection_year == 'purge'
	year_list = []
	year_list.append(f'{detection_year[:4]}')

	if 'all' in detection_year:
		delete_all_warning = input(f"Confirm data deletion for - {detection_year[:4]} (yes/no): ")
		if delete_all_warning == 'yes':
			for satellite_no in ['13', '15']:
				file_del_list = glob.glob(f"{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year[:4]}/*.csv")
				print(file_del_list)
				for file in file_del_list:
					os.remove(file)
	sys.exit(0)



	print(f'\n{"="*40}\n{"=" + "GOES-13/15 Proton Event File Purger".center(38," ") + "="}\n{"="*40}')

	for detection_year in year_list:
		print(f'{"="*40}\n{"=" + f"{detection_year}".center(38," ") + "="}\n{"="*40}')
	
		event_set_13 = set()
		event_set_15 = set()

		months_in_year_purge = []
		months_in_year_purge.append(input("Enter month to be purged (mm): ").zfill(2))
	
		for satellite_no in ['13', '15']:
			print(f'GOES-{satellite_no} Proton Event Purge\n{"-" * 25}')
			for month_event in months_in_year_purge:
				try:
					# print(f'\r                                                                                                    ', end="\r")
					print(f'Purging month - {month_event}', end="\r")
	
					f_l_day = calendar.monthrange(int(detection_year), int(month_event))
					event_f_day = str(f'{detection_year}{str(month_event).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
					event_l_day = str(f'{detection_year}{str(month_event).zfill(2)}{str(f_l_day[1]).zfill(2)}')
	
					dir_check = os.path.isdir(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}')
					if dir_check == False:
						try:
						    os.makedirs(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}')
						except OSError as e:
						    if e.errno != errno.EEXIST:
						        raise
					
					proton_name = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
					proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}/{proton_name}')
		
					if proton_check == True:
						os.remove(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}/{proton_name}')
						print(f"Removed {proton_name}")

					elif proton_check == False:
						print(f'File does not exist for month: {month_event}')


				except Exception as e:
					print(e)
					print(f'{month_event} does not have data.')
	sys.exit(0)

elif detection_year != 'all':
	year_list = []
	year_list.append(f'{detection_year}')



print(f'\n{"="*40}\n{"=" + "GOES-13/15 Proton Event Detector".center(38," ") + "="}\n{"="*40}')
# print(f'Parsing events for GOES-{satellite_no} for year {detection_year}')

proton_df = pd.DataFrame([])
proton_df_15 = pd.DataFrame([])
proton_df = pd.DataFrame([])

cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']

year_set_13 = set()
year_set_15 = set()




months_in_year = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

for detection_year in year_list:
	print(f'{"="*40}\n{"=" + f"{detection_year}".center(38," ") + "="}\n{"="*40}')

	event_set_13 = set()
	event_set_15 = set()

	for satellite_no in ['13', '15']:
		print(f'GOES-{satellite_no} Proton Events\n{"-" * 25}')
		for month_event in months_in_year:
			try:
				# print(f'\r                                                                                                    ', end="\r")
				print(f'Parsing month - {month_event}', end="\r")

				f_l_day = calendar.monthrange(int(detection_year), int(month_event))
				event_f_day = str(f'{detection_year}{str(month_event).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day = str(f'{detection_year}{str(month_event).zfill(2)}{str(f_l_day[1]).zfill(2)}')


				dir_check = os.path.isdir(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}')
				if dir_check == False:
					try:
					    os.makedirs(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}')
					except OSError as e:
					    if e.errno != errno.EEXIST:
					        raise
				
				proton_name = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}/{proton_name}')
	
				if proton_check == True:
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
	
	
				elif proton_check == False:
					proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{detection_year}/{str(month_event).zfill(2)}/goes{satellite_no}/csv/{proton_name}'
					# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
					proton_in = wget.download(proton_url)
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					proton_df = pd.read_csv(f'{proton_in}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0) # ZPGT100W
	
					if save_option == 'yes':
						shutil.move(f'{proton_name}', f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{detection_year}')
					elif save_option == 'no':
						os.remove(proton_name)

				proton_df.drop(proton_df[proton_df['ZPGT10W'] <= 0.0].index, inplace=True)
				proton_df.drop(proton_df[proton_df['ZPGT50W'] <= 0.0].index, inplace=True)
				proton_df.drop(proton_df[proton_df['ZPGT100W'] <= 0.0].index, inplace=True)
				
				# ========== Adding smoothed (begin)
				if proton_event_option == 'smooth':
					detection_threshold = pow(10,-1.26)
					butter_order = 1
					butter_filter = f'butter{butter_order}'
					proton_smooth_df = pd.DataFrame(proton_df[f'{energy_header}'])
					detection_threshold_str = str(round(detection_threshold,3))

					b, a = signal.butter(butter_order, 0.4)
					y1 = signal.filtfilt(b, a, proton_smooth_df[f'{energy_header}'])
					proton_smooth_df[f'{butter_filter}'] = y1

					proton_smooth_df[proton_smooth_df[f'{butter_filter}'] <= 0.024] = 0.024
					# proton_df = proton_smooth_df

					if satellite_no == '13':
						proton_smooth_full_df_13 = proton_smooth_full_df_13.append(proton_smooth_df)
					elif satellite_no == '15':
						proton_smooth_full_df_15 = proton_smooth_full_df_15.append(proton_smooth_df)


					proton_data_event = pd.DataFrame([])
					proton_concat_event = proton_smooth_df[[f'{butter_filter}']] # [[proton_channel]]
					proton_data_event = proton_data_event.append(proton_concat_event)
					# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0
						
					proton_event_df = pd.DataFrame([])
					proton_list_temp = []
					proton_list_event = []
					proton_counter = 0


					min_length_event = 1000 # 60
					min_t_between_pts = 60 # 40

					for i in proton_data_event[proton_data_event.values > detection_threshold].index: # for i in rb_data[rb_data.values > 300].index: # one level is 1 minute
						if len(proton_list_temp) == 0:
							proton_list_temp.append(i)
					
						elif len(proton_list_temp) >= 1:
							# time between points
							if (i - proton_list_temp[-1]) <= datetime.timedelta(minutes=min_t_between_pts): # originally 5 minutes # also had at 30 minutes, but increasing to 40
								proton_list_temp.append(i)
					
							elif (i - proton_list_temp[-1]) > datetime.timedelta(minutes=min_t_between_pts): # originally 5 minutes # time between first interval of time event to the second
								if (proton_list_temp[-1] - proton_list_temp[0]) >= datetime.timedelta(minutes=min_length_event): # length of event
									proton_list_event.append(proton_list_temp)
									proton_list_temp = []
									proton_list_temp.append(i)
					
								elif (proton_list_temp[-1] - proton_list_temp[0]) < datetime.timedelta(minutes=min_length_event): # if the time difference is less than 30 minutes, then create a new event
									proton_list_temp = []
									proton_list_temp.append(i)
						
					if len(proton_list_temp) > 0:
						if (proton_list_temp[-1] - proton_list_temp[0]) >= datetime.timedelta(minutes=min_length_event):
							proton_list_event.append(proton_list_temp)
							proton_list_temp = []
							proton_list_temp.append(i)
						elif (proton_list_temp[-1] - proton_list_temp[0]) < datetime.timedelta(minutes=min_length_event):
							proton_list_temp = []
							proton_list_temp.append(i)
						proton_list_temp = []
					
					# print("\n")
					proton_event_df = pd.DataFrame(columns=('start_time', 'end_time', 'proton_duration', 'proton_max_int'))
					
					if len( proton_list_event ) == 1:
						proton_event_df.loc[0] = [proton_list_event[0][0], proton_list_event[0][-1], ((proton_list_event[0][-1] - proton_list_event[0][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[0][0]:proton_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
				
					elif len( proton_list_event ) > 1:
						for i in range(len(proton_list_event)):
							proton_event_df.loc[i] = [proton_list_event[i][0], proton_list_event[i][-1], ((proton_list_event[i][-1] - proton_list_event[i][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[i][0]:proton_list_event[i][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
					
					# print(proton_event_df)
					if len(proton_event_df) > 0 and satellite_no == '13':
						# print(proton_event_df)
						proton_event_full_df_13 = proton_event_full_df_13.append(proton_event_df, ignore_index=True)

					elif len(proton_event_df) > 0 and satellite_no == '15':
						# print(proton_event_df)
						proton_event_full_df_15 = proton_event_full_df_15.append(proton_event_df, ignore_index=True)




					'''
					print('='*40)
					print(f"Number of Proton Events (): ", len(proton_list_event))
					print(proton_event_df)
					print('='*40)
					'''

					'''
					for i in proton_df[proton_df[f'{butter_filter}'] > detection_threshold].index:
						# print(str(i)[:10].replace('-',''))
						if satellite_no == '13':
							event_set_13.add(str(i)[:10].replace('-',''))
							year_set_13.add(str(i)[:10].replace('-',''))
						elif satellite_no == '15':
							event_set_15.add(str(i)[:10].replace('-',''))
							year_set_15.add(str(i)[:10].replace('-',''))
					'''



					
				# ========== Adding smooth (end)

				elif proton_event_option != 'smooth':
					for i in proton_df[proton_df[f'{energy_header}'] > detection_threshold].index:
						# print(str(i)[:10].replace('-',''))
						if satellite_no == '13':
							event_set_13.add(str(i)[:10].replace('-',''))
							year_set_13.add(str(i)[:10].replace('-',''))
						elif satellite_no == '15':
							event_set_15.add(str(i)[:10].replace('-',''))
							year_set_15.add(str(i)[:10].replace('-',''))				
	
				
	
				continue
	
			except Exception as e:
				print(e)
				print(f'{month_event} does not have data.')

	if proton_event_option == 'smooth':
		print(f'\n{"=" * 60}')
		print(f'GOES-13 Events ({detection_year}):')
		print(proton_event_full_df_13[proton_event_full_df_13['start_time'].dt.year == int(detection_year)])
		

		print(f'GOES-15 Events ({detection_year}):')
		print(proton_event_full_df_15[proton_event_full_df_15['start_time'].dt.year == int(detection_year)])
		print('=' * 60)

	elif proton_event_option != 'smooth':
		print(f'\n{"=" * 60}')
		print(f'GOES-13 Events ({detection_year}): {sorted(list(event_set_13))}')
		print(f'--GOES-13 Unique Events ({detection_year}): {sorted(list(event_set_13.difference(event_set_15)))}')
		
		print(f'\nGOES-15 Events ({detection_year}): {sorted(list(event_set_15))}')
		print(f'--GOES-15 Unique Events ({detection_year}): {sorted(list(event_set_15.difference(event_set_13)))}')
		print('=' * 60)
		
		print(f'\nShared Events ({detection_year}): {sorted(list(event_set_13.intersection(event_set_15)))}')
	
if len(year_list) > 1:
	
	if proton_event_option != 'smooth':
		print(f'{"="*40}\n{"=" + f"Full Event List".center(38," ") + "="}\n{"="*40}')
	
		print(f'\n{"=" * 60}')
		print(f'GOES-13 Events: {sorted(list(year_set_13))}')
		print(f'--GOES-13 Unique Events: {sorted(list(year_set_13.difference(year_set_15)))}')
		
		print(f'\nGOES-15 Events: {sorted(list(year_set_15))}')
		print(f'--GOES-15 Unique Events: {sorted(list(year_set_15.difference(year_set_13)))}')
		print('=' * 60)
		
		print(f'\nShared Events: {sorted(list(year_set_13.intersection(year_set_15)))}')
		year_df = pd.DataFrame([])
		year_df['g_events'] = sorted(list(year_set_13.intersection(year_set_15)))
	
		# year_df.to_csv('hep_events.txt', sep='\t', index=False)
	
		if unique_inclusion_option == 'yes':
			list_of_intersection = list(year_set_13.intersection(year_set_15).union(year_set_13.difference(year_set_15), year_set_15.difference(year_set_13)))
		elif unique_inclusion_option == 'no':
			list_of_intersection = list(year_set_13.intersection(year_set_15))
	
		full_event = []
		full_year = []
		for i in sorted(list_of_intersection):
			if len(full_event) == 0:
				full_event.append(i)
	
			elif len(full_event) >= 1:
	
					# full_event.append(i)
				
				if datetime.datetime.strptime(f'{i}', '%Y%m%d') == datetime.datetime.strptime(f'{full_event[-1]}', '%Y%m%d') + datetime.timedelta(days=1): # if int(i) == int(full_event[-1]) + 1:
					full_event.append(i)
	
				elif datetime.datetime.strptime(f'{i}', '%Y%m%d') != datetime.datetime.strptime(f'{full_event[-1]}', '%Y%m%d') + datetime.timedelta(days=1): # int(i) != int(full_event[-1]) + 1:
					# print(i , " ", int(full_event[-1]), " ", int(full_event[-1]) + 1)
					full_year.append(full_event)
					full_event = []
					full_event.append(i)
	
		if len(full_event) != 0:
			full_year.append(full_event)
			full_year_df = pd.DataFrame(full_year)
			full_year_df.fillna(value='none', inplace=True)
	
			full_year_df.to_csv(f'{data_directory}/detected_events/event_dates/{detection_threshold_str}pfu_{energy_channel}mev_{year_list[0]}_{year_list[-1]}.txt', sep=',', index=False)


proton_event_full_df_13.to_csv(f'{data_directory}/detected_events/event_dates/g13_{detection_threshold_str}pfu_{energy_channel}mev_{year_list[0]}_{year_list[-1]}.txt', sep=',', index=True)
proton_event_full_df_15.to_csv(f'{data_directory}/detected_events/event_dates/g15_{detection_threshold_str}pfu_{energy_channel}mev_{year_list[0]}_{year_list[-1]}.txt', sep=',', index=True)


if plot_option == 'yes':
	# ===== GOES-13 Plotting
	print(f'{"="*40}\n{"=" + f"Plotting GOES-13 Events".center(38," ") + "="}\n{"="*40}')
	for event_day in range(len(proton_event_full_df_13)):
		event_name_str = str(    (proton_event_full_df_13['start_time'].iloc[event_day] ).date()   ).replace('-','')

		event_start_str = str(    (proton_event_full_df_13['start_time'].iloc[event_day] - datetime.timedelta(days=1)).date()   ).replace('-','')
		event_end_str = str(    (proton_event_full_df_13['end_time'].iloc[event_day] + datetime.timedelta(days=1)).date() ).replace('-','')

		plot_check = os.path.isfile(f'{data_directory}/detected_events/{energy_channel}mev/GOES-13/{event_name_str}_g13_{energy_channel}mev_{detection_threshold_str}pfu.png')

		if plot_check == True:
			print(f"Plot exists for {event_name_str}")

		elif plot_check == False:
			print(f'\rGenerating GOES-13 plot for {event_name_str}')
			plt.close("all")
			plt.figure(figsize=(10,6))
		
			if event_start_str[4:6] == event_end_str[4:6]:
				f_l_day = calendar.monthrange(int(f'{event_start_str[:4]}'), int(f'{event_start_str[4:6]}'))
			
				event_f_day = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}{str(f_l_day[1]).zfill(2)}')
	
				proton_name = f'g13_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			
				proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_13/{event_start_str[:4]}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				proton_df.loc[proton_df[f'{energy_header}'] <= 0.0] = np.nan
			

			elif event_start_str[4:6] != event_end_str[4:6]:

				print("Event requires additional month parsing")

				f_l_day_1 = calendar.monthrange(int(f'{event_start_str[:4]}'), int(f'{event_start_str[4:6]}'))
				f_l_day_2 = calendar.monthrange(int(f'{event_end_str[:4]}'), int(f'{event_end_str[4:6]}'))
			
				event_f_day_1 = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day_1 = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}{str(f_l_day_1[1]).zfill(2)}')

				event_f_day_2 = str(f'{event_end_str[:4]}{str(event_end_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day_2 = str(f'{event_end_str[:4]}{str(event_end_str[4:6]).zfill(2)}{str(f_l_day_2[1]).zfill(2)}')
	
				proton_name_1 = f'g13_epead_cpflux_5m_{event_f_day_1}_{event_l_day_1}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				proton_name_2 = f'g13_epead_cpflux_5m_{event_f_day_2}_{event_l_day_2}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			
				proton_df_1 = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_13/{event_start_str[:4]}/{proton_name_1}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				proton_df_2 = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_13/{event_end_str[:4]}/{proton_name_2}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)

				proton_df_1.loc[proton_df_1[f'{energy_header}'] <= 0.0] = np.nan
				proton_df_2.loc[proton_df_2[f'{energy_header}'] <= 0.0] = np.nan

				proton_df = proton_df.append(proton_df_1)
				proton_df = proton_df.append(proton_df_2)

			plt.axvspan(proton_event_full_df_13["start_time"][event_day], proton_event_full_df_13["end_time"][event_day], color='lightgreen', alpha=0.5, zorder=1)
			plt.axvline(proton_event_full_df_13["start_time"][event_day], color='green', linestyle='-',linewidth=1 , zorder = 1)
			plt.axvline(proton_event_full_df_13["end_time"][event_day], color='green', linestyle='-',linewidth=1 , zorder = 1)

			plt.plot(proton_df['ZPGT10W'].loc[f'{proton_event_full_df_13["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_13["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-13 >10 MeV', color='red')
			plt.plot(proton_df['ZPGT50W'].loc[f'{proton_event_full_df_13["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_13["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-13 >50 MeV', color='blue')
			plt.plot(proton_df['ZPGT100W'].loc[f'{proton_event_full_df_13["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_13["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-13 >100 MeV', color='lime')
			
			if proton_event_option == 'smooth':
				plt.plot(proton_smooth_full_df_13[f'{butter_filter}'].loc[f'{proton_event_full_df_13["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_13["end_time"][event_day] + datetime.timedelta(days=1) }'], label = f'Butter-{butter_order}', color='purple')


			myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
			ax = plt.gca()
			ax.xaxis.set_major_formatter(myFmt)
			ax.set_ylim([10**-2,10**4])

			plt.axhline(detection_threshold, color='yellow', linestyle='-',linewidth=4 , zorder = 1)
			plt.axhline(detection_threshold, color='red', linestyle='--', label='Threshold', zorder = 1) # 0.25

			plt.yscale('log')
			plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
			plt.minorticks_on()
			plt.grid(True)
			plt.legend(loc='upper right', ncol=2,fontsize=8)
			
			plt.title(f'Proton Event Detector [GOES-13]\n[{proton_event_full_df_13["start_time"][event_day]} -- {proton_event_full_df_13["end_time"][event_day]}] (Threshold : {round(detection_threshold,3)} pfu -- {energy_channel} MeV)', fontname="Arial", fontsize = 14) #, y=1.04,
			
			plt.ylabel('Proton Flux [pfu]', fontname="Arial", fontsize = 12)
			plt.xlabel('Time [UT]', fontname="Arial", fontsize = 12)

			plt.savefig(f'{data_directory}/detected_events/{energy_channel}mev/GOES-13/{event_name_str}_g13_{energy_channel}mev_{detection_threshold_str}pfu.png', format='png', dpi=900)


	# ======= GOES-15 plotting
	print(f'{"="*40}\n{"=" + f"Plotting GOES-15 Events".center(38," ") + "="}\n{"="*40}')
	for event_day in range(len(proton_event_full_df_15)):
		event_name_str = str(    (proton_event_full_df_15['start_time'].iloc[event_day] ).date()   ).replace('-','')

		event_start_str = str(    (proton_event_full_df_15['start_time'].iloc[event_day] - datetime.timedelta(days=1)).date()   ).replace('-','')
		event_end_str = str(    (proton_event_full_df_15['end_time'].iloc[event_day] + datetime.timedelta(days=1)).date() ).replace('-','')

		plot_check = os.path.isfile(f'{data_directory}/detected_events/{energy_channel}mev/GOES-15/{event_name_str}_g15_{energy_channel}mev_{detection_threshold_str}pfu.png')

		if plot_check == True:
			print(f"Plot exists for {event_name_str}")

		elif plot_check == False:
			print(f'\rGenerating GOES-15 plot for {event_name_str}')
			plt.close("all")
			plt.figure(figsize=(10,6))
		
			if event_start_str[4:6] == event_end_str[4:6]:
				f_l_day = calendar.monthrange(int(f'{event_start_str[:4]}'), int(f'{event_start_str[4:6]}'))
			
				event_f_day = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}{str(f_l_day[1]).zfill(2)}')
	
				proton_name = f'g15_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			
				proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_15/{event_start_str[:4]}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				proton_df.loc[proton_df[f'{energy_header}'] <= 0.0] = np.nan
			

			elif event_start_str[4:6] != event_end_str[4:6]:

				print("Event requires additional month parsing")

				f_l_day_1 = calendar.monthrange(int(f'{event_start_str[:4]}'), int(f'{event_start_str[4:6]}'))
				f_l_day_2 = calendar.monthrange(int(f'{event_end_str[:4]}'), int(f'{event_end_str[4:6]}'))
			
				event_f_day_1 = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day_1 = str(f'{event_start_str[:4]}{str(event_start_str[4:6]).zfill(2)}{str(f_l_day_1[1]).zfill(2)}')

				event_f_day_2 = str(f'{event_end_str[:4]}{str(event_end_str[4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day_2 = str(f'{event_end_str[:4]}{str(event_end_str[4:6]).zfill(2)}{str(f_l_day_2[1]).zfill(2)}')
	
				proton_name_1 = f'g15_epead_cpflux_5m_{event_f_day_1}_{event_l_day_1}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				proton_name_2 = f'g15_epead_cpflux_5m_{event_f_day_2}_{event_l_day_2}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			
				proton_df_1 = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_15/{event_start_str[:4]}/{proton_name_1}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				proton_df_2 = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_15/{event_end_str[:4]}/{proton_name_2}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)

				proton_df_1.loc[proton_df_1[f'{energy_header}'] <= 0.0] = np.nan
				proton_df_2.loc[proton_df_2[f'{energy_header}'] <= 0.0] = np.nan

				proton_df = proton_df.append(proton_df_1)
				proton_df = proton_df.append(proton_df_2)

			plt.axvspan(proton_event_full_df_15["start_time"][event_day], proton_event_full_df_15["end_time"][event_day], color='lightgreen', alpha=0.5, zorder=1)
			plt.axvline(proton_event_full_df_15["start_time"][event_day], color='green', linestyle='-',linewidth=1 , zorder = 1)
			plt.axvline(proton_event_full_df_15["end_time"][event_day], color='green', linestyle='-',linewidth=1 , zorder = 1)

			plt.plot(proton_df['ZPGT10W'].loc[f'{proton_event_full_df_15["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_15["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-15 >10 MeV', color='red')
			plt.plot(proton_df['ZPGT50W'].loc[f'{proton_event_full_df_15["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_15["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-15 >50 MeV', color='blue')
			plt.plot(proton_df['ZPGT100W'].loc[f'{proton_event_full_df_15["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_15["end_time"][event_day] + datetime.timedelta(days=1)}'], label = f'GOES-15 >100 MeV', color='lime')
			
			if proton_event_option == 'smooth':
				plt.plot(proton_smooth_full_df_15[f'{butter_filter}'].loc[f'{proton_event_full_df_15["start_time"][event_day] - datetime.timedelta(days=1) }':f'{proton_event_full_df_15["end_time"][event_day] + datetime.timedelta(days=1) }'], label = f'Butter-{butter_order}', color='purple')


			myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
			ax = plt.gca()
			ax.xaxis.set_major_formatter(myFmt)
			ax.set_ylim([10**-2,10**4])


			plt.axhline(detection_threshold, color='yellow', linestyle='-',linewidth=4 , zorder = 1)
			plt.axhline(detection_threshold, color='red', linestyle='--', label='Threshold', zorder = 1) # 0.25

			plt.yscale('log')
			plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
			plt.minorticks_on()
			plt.grid(True)
			plt.legend(loc='upper right', ncol=2,fontsize=8)
			
			plt.title(f'Proton Event Detector [GOES-15]\n[{proton_event_full_df_15["start_time"][event_day]} -- {proton_event_full_df_15["end_time"][event_day]}] (Threshold : {round(detection_threshold,3)} pfu -- {energy_channel} MeV)', fontname="Arial", fontsize = 14) #, y=1.04,
			
			plt.ylabel('Proton Flux [pfu]', fontname="Arial", fontsize = 12)
			plt.xlabel('Time [UT]', fontname="Arial", fontsize = 12)

			plt.savefig(f'{data_directory}/detected_events/{energy_channel}mev/GOES-15/{event_name_str}_g15_{energy_channel}mev_{detection_threshold_str}pfu.png', format='png', dpi=900)




''' # old plotting technique
if plot_option == 'yes':
	print(f'{"="*40}\n{"=" + f"Plotting Events".center(38," ") + "="}\n{"="*40}')
	# if os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{sat}/{detection_year}/{proton_name}')
	for event_day in (full_year):
		plot_check = os.path.isfile(f'{data_directory}/detected_events/{energy_channel}mev/{detection_threshold_str}pfu_{energy_channel}mev_{event_day[0]}.png')

		if plot_check == True:
			print(f"Plot exists for {event_day}")

		elif plot_check == False:
			print(f'\rGenerating plot for {event_day}')
			plt.close("all")
			plt.figure(figsize=(10,6))
		
			for sat in ['13','15']:
		
				f_l_day = calendar.monthrange(int(f'{event_day[0][:4]}'), int(f'{event_day[0][4:6]}'))
		
				event_f_day = str(f'{event_day[0][:4]}{str(event_day[0][4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day = str(f'{event_day[0][:4]}{str(event_day[0][4:6]).zfill(2)}{str(f_l_day[1]).zfill(2)}')
		
				proton_name = f'g{sat}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				# proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{sat}/{detection_year}/{proton_name}')
		
				proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{sat}/{event_day[0][:4]}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				proton_df.loc[proton_df[f'{energy_header}'] <= 0.0] = np.nan
				if sat == '13':
					marker_sat = 'x'
				elif sat == '15':
					marker_sat = 'o'
			

				plt.plot(proton_df['ZPGT10W'].loc[f'{event_day[0]}':f'{event_day[-1]}'], label = f'GOES-{sat} >10 MeV', marker=marker_sat, color='red')
				plt.plot(proton_df['ZPGT50W'].loc[f'{event_day[0]}':f'{event_day[-1]}'], label = f'GOES-{sat} >50 MeV', marker=marker_sat, color='blue')
				plt.plot(proton_df['ZPGT100W'].loc[f'{event_day[0]}':f'{event_day[-1]}'], label = f'GOES-{sat} >100 MeV', marker=marker_sat, color='lime')

			myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
			ax = plt.gca()
			ax.xaxis.set_major_formatter(myFmt)
			ax.set_ylim([10**-2,10**4])
		


			plt.axhline(detection_threshold, color='yellow', linestyle='-',linewidth=4 , zorder = 1)
			plt.axhline(pow(10, -0.8), color='green', linestyle='--', label='100 MeV', zorder = 1) # 0.25
			plt.axhline(0.60, color='navy', linestyle='--', label='50 MeV', zorder = 1)
			plt.axhline(1.5, color='crimson', linestyle='--', label='10 MeV', zorder = 1)

			plt.yscale('log')
			plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
			plt.minorticks_on()
			plt.grid(True)
			plt.legend(loc='upper right', ncol=2,fontsize=8)
			
			if ''.join(event_day[0]) in list(year_set_13.difference(year_set_15)):
				plt.title(f'Proton Event Detector [GOES-13 UNIQUE]\n[{event_day[0]} -- {event_day[-1]}] (Threshold : {detection_threshold} pfu -- {energy_channel} MeV)', fontname="Arial", fontsize = 14) #, y=1.04,
			elif ''.join(event_day[0]) in list(year_set_15.difference(year_set_13)):
				plt.title(f'Proton Event Detector [GOES-15 UNIQUE]\n[{event_day[0]} -- {event_day[-1]}] (Threshold : {detection_threshold} pfu -- {energy_channel} MeV)', fontname="Arial", fontsize = 14) #, y=1.04,
			elif ''.join(event_day[0]) in list_of_intersection:
				plt.title(f'Proton Event Detector [GOES-13/15 CONFIRMED]\n[{event_day[0]} -- {event_day[-1]}] (Threshold : {detection_threshold} pfu -- {energy_channel} MeV)', fontname="Arial", fontsize = 14) #, y=1.04,
	
	
			plt.ylabel('Proton Flux [pfu]', fontname="Arial", fontsize = 12)
			plt.xlabel('Time [UT]', fontname="Arial", fontsize = 12)
		
			# plt.show()
			# sys.exit(0)
			

			plt.savefig(f'{data_directory}/detected_events/{energy_channel}mev/{detection_threshold_str}pfu_{energy_channel}mev_{event_day[0]}.png', format='png', dpi=900)
			#sys.exit(0)
'''
