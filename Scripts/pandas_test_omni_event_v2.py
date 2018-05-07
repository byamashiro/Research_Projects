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
from dateutil.relativedelta import relativedelta

from scipy import signal
from matplotlib.pyplot import cm 


import shutil


plt.close("all")
# plt.ion()

# ======= Parameters to set

data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # either 'yes' or 'no'

event_option = 'yes' # either 'yes' or 'no'
goes_corrected_option = 'yes'

save_plot_option = 'yes'
event_option_show = 'no'

# ========== Event list (Still being implemented, do not uncomment)

script_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts'
event_list_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Scripts/event_lists'

event_plot_folder = 'a_events'
event_list_name = 'a_events_list.txt'


event_columns = ['event_date_st', 'event_date_ed', 'flare_int', 'event_st_hr', 'event_ed_hr', 'opt_1', 'opt_2', 'opt_3', 'prot_sat', 'xray_sat', 'prot_opt'] # , 'opt_4'


if event_option == 'yes':
	event_list_file = pd.read_csv(f'{event_list_directory}/{event_list_name}', sep = '\t', names=event_columns, comment='#')


# ========== Definitions

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

#==============Choosing Dataset
print(f'\n{"="*40}\n{"=" + "OMNI Event Script".center(38," ") + "="}\n{"="*40}')


# radio_check = os.path.isfile(f'{data_directory}/WIND/RAD1/{radio_name}')
for event_no in range(len(event_list_file)):

	event_list = event_list_file.loc[event_no]


	if os.path.isfile(f"{script_directory}/{event_plot_folder}/omni_test_{event_list['event_date_st']}.png") == True:
		print(f"The plot for {event_list['event_date_st']} already exists.")

	elif os.path.isfile(f"{script_directory}/{event_plot_folder}/omni_test_{event_list['event_date_st']}.png") == False:
		print(f"== {event_list['event_date_st']} ==")
		# event_list = event_list_file.loc[event_no]
	
		# print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-13/15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts (Requires Internet Connection)\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-13/15 Xray Flux\n{"="*40}')
		# \n{"="*40}\n1 - GOES-13/15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts (Requires Internet Connection)\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-13/15 Xray Flux\n{"="*40}')
	
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
				option_bin_set = {'1', '4', '5'}
		
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
		
		
		#===============Time frame
		if event_option == 'yes':
			start_date = str(event_list['event_date_st'])
			end_date = str(event_list['event_date_ed'])
		
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
			start_hour = str(event_list['event_st_hr'])
			end_hour = str(event_list['event_ed_hr'])
		
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
				satellite_no = str(event_list['prot_sat'])
		
			if event_option != 'yes':
				satellite_no = input('Specify which GOES Satellite for Proton Flux (13 or 15): ')
				if satellite_no != '13':
					if satellite_no != '15':
						print('SATELLITE ERROR: Must specify either 13 or 15.')
						sys.exit(0)
		
			# print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Proton Flux".center(38," ") + "="}\n{"="*40}')
			print(f'\rProcessing GOES-{satellite_no} Proton Flux...', end='\r')
			# print(f'{"Energy Channels".center(7, " ")}\n{"-"*20}\n1: 6.5 MeV\n2: 11.6 MeV\n3: 30.6 MeV\n4: 63.1 MeV\n5: 165 MeV\n6: 433 MeV')
	
			if goes_corrected_option == 'yes':
				print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Proton Flux".center(38," ") + "="}\n{"="*40}')
		
				energy_bin_list = []
		
				if start_date[4:6] != end_date[4:6]: # if the month of the start day is NOT the same as the month of the end date
					proton_df = pd.DataFrame([])
		
					cur_date =  start
					date_in_year = [cur_date]
		
					while cur_date < end:
						# print(cur_date)
						cur_date += relativedelta(months=1)
						date_in_year.append(cur_date)
		
		
					if start.year >= 2011:
						cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']
		
						energy_bin_list.append(['ZPGT10W','>10 MeV', 'red'])
						energy_bin_list.append(['ZPGT50W','>50 MeV', 'blue'])
						energy_bin_list.append(['ZPGT100W','>100 MeV', 'lime'])
		
						for date_event in date_in_year:
							try:
								f_l_day = calendar.monthrange(int(date_event.year), int(date_event.month)) #	f_l_day = calendar.monthrange(int(detection_year), int(month_event))
								event_f_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
								event_l_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
				
				
								dir_check = os.path.isdir(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
								if dir_check == False:
									try:
									    os.makedirs(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
									except OSError as e:
									    if e.errno != errno.EEXIST:
									        raise
								
								proton_name = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
								proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}/{proton_name}')
					
								if proton_check == True:
									dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
									proton_df_ind = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
									proton_df = proton_df.append(proton_df_ind)
			
					
								elif proton_check == False:
									proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{date_event.year}/{str(date_event.month).zfill(2)}/goes{satellite_no}/csv/{proton_name}'
									# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
									proton_in = wget.download(proton_url)
									dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
									proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0) # ZPGT100W
									proton_df = proton_df.append(proton_df_ind)
			
									if save_option == 'yes':
										shutil.move(f'{proton_name}', f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
									elif save_option == 'no':
										os.remove(proton_name)
					
								continue
					
							except Exception as e:
								print(e)
								print(f'{date_event.month} does not have data.')
		
						proton_df.drop(proton_df[proton_df['ZPGT10W'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['ZPGT50W'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['ZPGT100W'] <= 0.0].index, inplace=True)
		
		
		
					# ====== Legacy GOES data protons (GOES-10)
		
					elif start.year < 2011:
						cpflux_names_legacy = ['time_tag','e1_flux_ic','e2_flux_ic','e3_flux_ic','p1_flux','p2_flux','p3_flux','p4_flux','p5_flux','p6_flux','p7_flux','a1_flux','a2_flux','a3_flux','a4_flux','a5_flux','a6_flux','p1_flux_c','p2_flux_c','p3_flux_c','p4_flux_c','p5_flux_c','p6_flux_c','p7_flux_c','p1_flux_ic','p2_flux_ic','p3_flux_ic','p4_flux_ic','p5_flux_ic','p6_flux_ic','p7_flux_ic']
		
						energy_bin_list.append(['p3_flux_ic','>10 MeV', 'red'])
						energy_bin_list.append(['p5_flux_ic','>50 MeV', 'blue'])
						energy_bin_list.append(['p7_flux_ic','>100 MeV', 'lime'])
		
						for date_event in date_in_year:
							try:
								f_l_day = calendar.monthrange(int(date_event.year), int(date_event.month)) #	f_l_day = calendar.monthrange(int(detection_year), int(month_event))
								event_f_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
								event_l_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
				
				
								dir_check = os.path.isdir(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
								if dir_check == False:
									try:
									    os.makedirs(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
									except OSError as e:
									    if e.errno != errno.EEXIST:
									        raise
								
								proton_name = f'g{satellite_no}_eps_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
								proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}/{proton_name}')
					
								if proton_check == True:
									dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
									proton_df_ind = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}/{proton_name}', skiprows=452, date_parser=dateparse, names=cpflux_names_legacy,index_col='time_tag', header=0)
									proton_df = proton_df.append(proton_df_ind)
			
					
								elif proton_check == False:
									proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{date_event.year}/{date_event.month}/goes{satellite_no}/csv/{proton_name}'
									# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
									proton_in = wget.download(proton_url)
									dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
									proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=452, date_parser=dateparse, names=cpflux_names_legacy,index_col='time_tag', header=0) # ZPGT100W
									proton_df = proton_df.append(proton_df_ind)
			
									if save_option == 'yes':
										shutil.move(f'{proton_name}', f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{date_event.year}')
									elif save_option == 'no':
										os.remove(proton_name)
					
								continue
					
							except Exception as e:
								print(e)
								print(f'{date_event.month} does not have data.')
			
						proton_df.drop(proton_df[proton_df['p3_flux_ic'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['p5_flux_ic'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['p7_flux_ic'] <= 0.0].index, inplace=True)
		
		
		
				elif start_date[4:6] == end_date[4:6]: # if the month of the start day is the same as the month of the end date
					if start.year >= 2011:
						cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']
						energy_bin_list.append(['ZPGT10W','>10 MeV', 'red'])
						energy_bin_list.append(['ZPGT50W','>50 MeV', 'blue'])
						energy_bin_list.append(['ZPGT100W','>100 MeV', 'lime'])
		
						f_l_day = calendar.monthrange(int(f'{start_year}'), int(f'{start_month}'))
						event_f_day = str(f'{start_year}{str(start_month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
						event_l_day = str(f'{start_year}{str(start_month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
						dir_check = os.path.isdir(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}')
						if dir_check == False:
							try:
							    os.makedirs(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}')
							except OSError as e:
							    if e.errno != errno.EEXIST:
							        raise
		
						proton_name = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
						proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}/{proton_name}')
				
						if proton_check == True:
							dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
							proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
				
				
						elif proton_check == False:
							proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{start_year}/{start_month}/goes{satellite_no}/csv/{proton_name}'
							# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
							proton_in = wget.download(proton_url)
							dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
							proton_df = pd.read_csv(f'{proton_in}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0) # ZPGT100W
				
							if save_option == 'yes':
								shutil.move(f'{proton_name}', f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}')
							elif save_option == 'no':
								os.remove(proton_name)
				
						proton_df.drop(proton_df[proton_df['ZPGT10W'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['ZPGT50W'] <= 0.0].index, inplace=True)
						proton_df.drop(proton_df[proton_df['ZPGT100W'] <= 0.0].index, inplace=True)

			# ======= proton event detection
			# ======= added for event options
			proton_channel = 'ZPGT100W' # t3_freq = 120
			proton_event_option = 'smooth' # 'standard' or 'smooth'
		
			if proton_event_option == 'standard':
				proton_threshold = pow(10,-1.3)# pow(10,-1.25)
				proton_data_event = pd.DataFrame([])
				proton_concat_event = proton_df[[proton_channel]]
				proton_data_event = proton_data_event.append(proton_concat_event)
			
				proton_event_df = pd.DataFrame([])
				proton_list_temp = []
				proton_list_event = []
				proton_counter = 0
		
		
			# ======== (BEGIN) Interpolating and smoothing data
			elif proton_event_option == 'smooth':
				proton_threshold = pow(10,-1.26) # pow(10,-1.45) when Butterworth filter was at (1 or 2, 0.08)
				butter_order = 1
				butter_filter = f'butter{butter_order}'
				proton_smooth_df = pd.DataFrame(proton_df[f'{proton_channel}']) # pd.DataFrame(proton_df[f'{proton_channel}'].loc[event_obj_start:event_obj_end])
		
				proton_smooth_df_rs_1m = proton_smooth_df.resample('min')
				proton_smooth_df_rs_1s = proton_smooth_df.resample('S')
			
				proton_smooth_df_interp_1m = proton_smooth_df_rs_1m.interpolate(method='cubic')
				proton_smooth_df_interp_1s = proton_smooth_df_rs_1s.interpolate(method='cubic')
			
				order_list = [1,2,3,4,5,6,7,8,9,10]
			
				for order in order_list:
					b, a = signal.butter(order, 0.4) # order of the filter (increases in integer values), cut off frequency # 0.08
				
					y1 = signal.filtfilt(b, a, proton_smooth_df[f'{proton_channel}'])
					proton_smooth_df[f'butter{order}'] = y1
		
				proton_smooth_df[proton_smooth_df[f'{butter_filter}'] <= 0.024] = 0.024
		
				proton_data_event = pd.DataFrame([])
				proton_concat_event = proton_smooth_df[[f'{butter_filter}']] # [[proton_channel]]
				proton_data_event = proton_data_event.append(proton_concat_event)
					
				proton_event_df = pd.DataFrame([])
				proton_list_temp = []
				proton_list_event = []
				proton_counter = 0
		
			# ======== (END) Interpolating and smoothing data
		
			min_length_event = 500 # changed thresholds (03/06/2018): 1000 # 60
			min_t_between_pts = 60 # changed thresholds (03/06/2018): 60 # 40
		
			for i in proton_data_event[proton_data_event.values > proton_threshold].index: # for i in rb_data[rb_data.values > 300].index: # one level is 1 minute
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
		
			print("\n")
			proton_event_df = pd.DataFrame(columns=('start_time', 'end_time', 'proton_duration', 'proton_max_int'))
		
		
		
			# =========  Outlier list
			if len( proton_list_event ) == 1:
				proton_event_df.loc[0] = [proton_list_event[0][0], proton_list_event[0][-1], ((proton_list_event[0][-1] - proton_list_event[0][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[0][0]:proton_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		
			elif len( proton_list_event ) > 1:
				for i in range(len(proton_list_event)):
					proton_event_df.loc[i] = [proton_list_event[i][0], proton_list_event[i][-1], ((proton_list_event[i][-1] - proton_list_event[i][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[i][0]:proton_list_event[i][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		
			print('='*40)
			print(f"Number of Proton Events ({start} - {end}): ", len(proton_list_event))
			print(proton_event_df)
			print('='*40)

		
		#=========== 2: Wind Type III Radio Burst
		if '2' in option_bin_set:
			print(f'\r                                                                                                    ', end='\r')
			print('\rProcessing Wind Type III Radio Bursts...', end='\r')
			# sys.stdout.write('/r Processing Wind Type III Radio Bursts')
			# sys.stdout.flush()
			# print(f'\n{"="*40}\n{"=" + "Wind Type III Radio Bursts".center(38," ") + "="}\n{"="*40}')
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
			
			rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)




			
		
		
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
			print(f'\r                                                                                                    ', end='\r')
			print(f'\rProcessing ACE/Wind Solar Wind Speed...', end='\r')
			# print(f'\n{"="*40}\n{"=" + "ACE/Wind Solar Wind Speed".center(38," ") + "="}\n{"="*40}')
			
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
			
			
			
			ace_data.loc[ace_data['ace_bulk_vel'] <= 0.0] = np.nan #6.5 MeV
			wind_data.loc[wind_data['wind_bulk_vel'] <= 0.0] = np.nan #6.5 MeV
		
		
		#=========== 5: GOES-15 Xray Flux
	
		if '5' in option_bin_set:
			if event_option == 'yes':
				satellite_no_xray = str(event_list['xray_sat'])
			if event_option != 'yes':
				satellite_no_xray = input('Specify which GOES Satellite for Xray Flux (13 or 15): ')
				if satellite_no_xray != '13':
					if satellite_no_xray != '15':
						print('SATELLITE ERROR: Must specify either 13 or 15.')
						sys.exit(0)
			print(f'\r                                                                                                    ', end='\r')
			print(f'\rProcessing GOES-{satellite_no_xray} Xray Flux...', end='\r')
			
			xray_df = pd.DataFrame([])
			
			for date in daterange( start, end ):

				try:
					event_date = str(date).replace('-','')
		
					xray_name = f'g{satellite_no_xray}_xrs_2s_{event_date}_{event_date}.csv' #g15_xrs_2s_20120307_20120307.csv
					xray_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no_xray}/XRflux/{xray_name}')
					xray_name_list = ['time_tag','A_QUAL_FLAG','A_COUNT','A_FLUX','B_QUAL_FLAG','B_COUNT','B_FLUX']		
		
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
		
			
			# xray_df.loc[xray_df['A_FLUX'] <= 0.0] = np.nan #6.5 MeV
			# xray_df.loc[xray_df['B_FLUX'] <= 0.0] = np.nan #11.6 MeV
			
			xray_df.drop(xray_df[xray_df['A_FLUX'] <= 0.0].index, inplace=True)
			xray_df.drop(xray_df[xray_df['B_FLUX'] <= 0.0].index, inplace=True)
		
		
		
		''' Templates for new data
		#===========
		print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')
		
		#===========
		print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')
		'''
		
		#=========== Plotting Data
		sys.stdout.flush()
		print(f'\r                                                                                                    ', end='\r')
		print(f'\rGenerating plot for {event_date}...')
		sys.stdout.flush()
	
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
			axes[length_data_list[j]].grid(True, linestyle='dotted')
			axes[length_data_list[j]].tick_params(axis='both', which='both', direction='in')


			axes[length_data_list[j]].minorticks_on()
			axes[length_data_list[j]].legend(loc='upper right', ncol=1,fontsize=10)# borderaxespad=0)# bbox_to_anchor=(1, 0.5)) # bbox_to_anchor=(1.02,1.0)
			if '1' in option_bin_set:
				high_bin_proton = sorted(energy_bin_list)[-1][0]
				low_bin_proton = sorted(energy_bin_list)[0][0]
		
				high_bin_proton_str = sorted(energy_bin_list)[-1][1]
				low_bin_proton_str = sorted(energy_bin_list)[0][1]
				# axes[length_data_list[j]].set_zorder(0)
				# axes[length_data_list[j]].axvline(proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), zorder=1) # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified
			# axes[length_data_list[j]].axvline(proton_df.idxmax().P6W_UNCOR_FLUX) # (proton_df.P6W_UNCOR_FLUX.max())
		
		
		if length_data > 1:
			f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=True, figsize=(10,12)) # figsize=(10, 6))
		
		if length_data == 1:
			length_data_list[0] = 0,0
			f, axes = plt.subplots(nrows=length_data, ncols=1, sharex=False, figsize=(10, 6), squeeze=False)
		
		
		#======dataset plotting
		
		'''
		if '1' in option_bin_set:
			next_global()
			for i in sorted(energy_bin_list):
				axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
			axes[length_data_list[j]].set_yscale('log')
			axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)
			applyPlotStyle()
		'''

		if '1' in option_bin_set:
			next_global()
			if goes_corrected_option == 'yes':
				for i in energy_bin_list: # for i in sorted(energy_bin_list): # changed to unsorted because the sort queued off of 10 -> 100 -> 50 rather than 10 -> 50 -> 100
					axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], '.', mfc='none', color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
				
				# axes[length_data_list[j]].plot(proton_smooth_df['ZPGT100W'].ewm(span=20).mean(), color='red', linewidth=1, label= 'EWM', zorder=5) # butter filter
		
		
				color_tree = iter(cm.rainbow(np.linspace(0,1,10)))
				'''
				for order in range(10):
					axes[length_data_list[j]].plot(proton_smooth_df[f'butter{order+1}'], color=next(color_tree), linewidth=1, label= f'Butter-{order}', zorder=5) # butter filter
				'''
				if proton_event_option == 'smooth':
					axes[length_data_list[j]].plot(proton_smooth_df[f'{butter_filter}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='purple', linewidth=2, label=f'Butter-{butter_order}', zorder=5)
				# axes[length_data_list[j]].plot(proton_smooth_df_interp_1m, color='red', linestyle='-.', label= '1m Interp.', zorder=5) # interpolated (no time reshape)
				# axes[length_data_list[j]].plot(proton_smooth_df_interp_1s, color='purple', linestyle=':', label= '1s Interp.', zorder=5) # interpolated (1 second)
		
				axes[length_data_list[j]].set_yscale('log')
				# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
		
		
				
				'''
				axes[length_data_list[j]].set_yticks([10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3]) # 10**-3, 
				'''
				axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Epead Proton\nFlux [pfu]', fontname="Arial", fontsize = 16)
		
			elif goes_corrected_option == 'no':
				for i in sorted(energy_bin_list):
					axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
				axes[length_data_list[j]].set_yscale('log')
				# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
			
				axes[length_data_list[j]].set_yticks([10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3])
				axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Epead Proton\nFlux [pfu]', fontname="Arial", fontsize = 16)
		
		
		
			s_time = datetime.datetime.strptime(start_hour, '%H').time()
			e_time = datetime.datetime.strptime(end_hour, '%H').time()
		
			s_dtime = datetime.datetime.combine(start, s_time)
			e_dtime = datetime.datetime.combine(end, e_time)
		
			for i in range(len(proton_event_df)):
				if s_dtime <= (proton_event_df['start_time'][i] and proton_event_df['end_time'][i]) <= e_dtime:
					axes[length_data_list[j]].axvspan(proton_event_df['start_time'][i], proton_event_df['end_time'][i], color='palegreen', alpha=0.5)
					axes[length_data_list[j]].axvline(proton_event_df['start_time'][i], linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1
					axes[length_data_list[j]].axvline(proton_event_df['end_time'][i], linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1
		
			axes[length_data_list[j]].axhline(proton_threshold, linewidth=1, zorder=2, color='red', linestyle='-.', label=f'{round(proton_threshold, 3)} pfu') #  xmin=0, xmax=1 # threshold
		
			# axes[length_data_list[j]].axvline(s_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1
			# axes[length_data_list[j]].axvline(e_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1
		
		
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
			
			color_cm=iter(cm.viridis(np.linspace(0,1, 5 )))
			freq_list = [100, 300, 500, 700, 900]
	
			for frequency in freq_list:
				color_choice = next(color_cm)
				axes[length_data_list[j]].plot(rb_data[frequency].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=color_choice, label= f'{frequency} kHz', zorder=5)
				
			axes[length_data_list[j]].set_ylabel('Wind Type III\nRadio Burst [sfu]', fontname="Arial", fontsize = 16)
			axes[length_data_list[j]].set_ylabel('Type III Radio\nBurst Int. [sfu]', fontname="Arial", fontsize = 16)
			
		
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
			axes[length_data_list[j]].set_ylabel('Neu. Monitor\n[counts/s]', fontname="Arial", fontsize = 16)
			applyPlotStyle()
		
		if '4' in option_bin_set:
			next_global()
			axes[length_data_list[j]].plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE', zorder=5)
			axes[length_data_list[j]].plot(ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='ACE: H Bulk Speed', zorder=5)
			axes[length_data_list[j]].set_ylabel('Solar Wind\nSpeed [km/s]', fontname="Arial", fontsize = 16)
			applyPlotStyle()
		

		if '5' in option_bin_set:
			def flare_class(X):
				if X == 10**-4:
					return "X"
		
			next_global()
			axes[length_data_list[j]].plot(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm', zorder=5)
			axes[length_data_list[j]].plot(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.4 nm', zorder=5)
			axes[length_data_list[j]].set_yscale('log')
		
			flare_classes = ['', 'A', 'B', 'C', 'M', 'X']
			ax2 = axes[length_data_list[j]].twinx()
			ax2.set_yscale('log')
			ax2.set_ylim(axes[length_data_list[j]].get_ylim())
			ax2.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
			ax2.set_yticklabels(labels=flare_classes)
			ax2.tick_params(axis='y', which='both', direction='in')
		
			axes[length_data_list[j]].set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
		
			axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no_xray} Xray\nFlux [Wm$^2$]', fontname="Arial", fontsize = 16)
			applyPlotStyle()
		
		# plt.xlabel('Time [UT]', fontname="Arial", fontsize = 16)
		axes[length_data_list[j]].set_xlabel('Time [UT]', fontname="Arial", fontsize = 16)

		
		myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
		ax = plt.gca()
		ax.xaxis.set_major_formatter(myFmt)
		
		plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
		plt.suptitle(f"Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]  (Flare Class: {event_list['flare_int']})", fontname="Arial", fontsize = 16) #, y=1.04,
		#plt.tight_layout() ({event_list['flare_int']})
		
		plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)

		#plt.savefig('omni_test_legacy.png', format='png', dpi=900)
		if save_plot_option == 'yes':
			plt.savefig(f'a_events/omni_{event_obj_start_str_date[:8]}.png', format='png', dpi=500)
			print(f'\nPlot successfully generated for: {event_obj_start_str_date[:8]}', end='\n')
		
		if event_option_show == 'no':
			continue

		if event_option_show == 'yes':
			plt.show()
		


sys.exit(0)

	