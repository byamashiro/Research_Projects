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

# ===== WAVES code
from io import StringIO
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
from matplotlib import colors, ticker, cm
# ====== End WAVES code

plt.close("all")
plt.ion()
# ======= Parameters to set

data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # saves the data files
save_plot_option = 'no' # saves the plots
data_collection_option = 'no'
event_option = 'no' # use event list to plot
HEPAD_save_option = 'no'
rad2_include = 'yes'

goes_corrected_option = 'yes'


# ========== Definitions

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

#==============Choosing Dataset

print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-13/15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts (Requires Internet Connection)\n4 - ACE/Wind Solar Wind Speed\n5 - GOES-13/15 Xray Flux\n6 - STEREO-A Proton Flux\n7 - STEREO-B Proton Flux\n8 - GOES-13/15 HEPAD Proton Flux\n9 - GOES-13/15 SEPEM Proton Flux\n{"="*40}')

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
		option_bin_set = {'1', '2', '4', '5', '6', '7', '8','9'}

		break

	if event_option != 'yes':
		option_bin = input('Enter Dataset Option then "done" or "all": ').lower()

		if option_bin != 'done':
			if option_bin == 'all':
				option_bin_set.add('1')	# 1 - GOES-13/15 Epead Proton Flux
				option_bin_set.add('2')	# 2 - Wind Type III Radio Bursts
				option_bin_set.add('3')	# 3 - Neutron Monitor Counts (Requires Internet Connection)
				option_bin_set.add('4')	# 4 - ACE/Wind Solar Wind Speed
				option_bin_set.add('5')	# 5 - GOES-13/15 Xray Flux
				option_bin_set.add('6')	# 6 - STEREO-A Proton Flux
				option_bin_set.add('7')	# 7 - STEREO-B Proton Flux
				option_bin_set.add('8')	# 8 - GOES-13/15 HEPAD Proton Flux
				option_bin_set.add('9') # 9 - SEPEM Proton Flux

				break
			
			elif int(option_bin) < 10:
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
				if satellite_no != '10':
					print('SATELLITE ERROR: Must specify either 13 or 15.')
					sys.exit(0)



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

			'''
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
				proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{start_year}/{str({start_month}).zfill(2)}/goes{satellite_no}/csv/{proton_name}'
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
			'''


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
		

			# ====== legacy start
			elif start.year < 2011:
				cpflux_names_legacy = ['time_tag','e1_flux_ic','e2_flux_ic','e3_flux_ic','p1_flux','p2_flux','p3_flux','p4_flux','p5_flux','p6_flux','p7_flux','a1_flux','a2_flux','a3_flux','a4_flux','a5_flux','a6_flux','p1_flux_c','p2_flux_c','p3_flux_c','p4_flux_c','p5_flux_c','p6_flux_c','p7_flux_c','p1_flux_ic','p2_flux_ic','p3_flux_ic','p4_flux_ic','p5_flux_ic','p6_flux_ic','p7_flux_ic']

				energy_bin_list.append(['p3_flux_ic','>10 MeV', 'red'])
				energy_bin_list.append(['p5_flux_ic','>50 MeV', 'blue'])
				energy_bin_list.append(['p7_flux_ic','>100 MeV', 'lime'])


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
				
		
				proton_name = f'g{satellite_no}_eps_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}/{proton_name}')
		
				if proton_check == True:
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}/{proton_name}', skiprows=455, date_parser=dateparse, names=cpflux_names_legacy,index_col='time_tag', header=0)
		
		
				elif proton_check == False:
					proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{start_year}/{start_month}/goes{satellite_no}/csv/{proton_name}'
					# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
					proton_in = wget.download(proton_url)
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					proton_df = pd.read_csv(f'{proton_in}', skiprows=455, date_parser=dateparse, names=cpflux_names_legacy,index_col='time_tag', header=0) # ZPGT100W
		
					if save_option == 'yes':
						shutil.move(f'{proton_name}', f'{data_directory}/GOES_Detection/GOES_{satellite_no}/{start_year}')
					elif save_option == 'no':
						os.remove(proton_name)
		
				proton_df.drop(proton_df[proton_df['p3_flux_ic'] <= 0.0].index, inplace=True)
				proton_df.drop(proton_df[proton_df['p5_flux_ic'] <= 0.0].index, inplace=True)
				proton_df.drop(proton_df[proton_df['p7_flux_ic'] <= 0.0].index, inplace=True)		
	# ==== legacy end


	elif goes_corrected_option == 'no':
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


	# ======= proton event detection
	# ======= added for event options
	 # t3_threshold = 5 # 5 # pow(10, -0.9) # pow(10, -0.8)
	proton_channel = 'ZPGT100W' # t3_freq = 120
	proton_event_option = 'smooth' # 'standard' or 'smooth'

	if proton_event_option == 'standard':
		proton_threshold = pow(10,-1.3)# pow(10,-1.25)
		proton_data_event = pd.DataFrame([])
		proton_concat_event = proton_df[[proton_channel]]
		proton_data_event = proton_data_event.append(proton_concat_event)
		# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0
	
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
		# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0
			
		proton_event_df = pd.DataFrame([])
		proton_list_temp = []
		proton_list_event = []
		proton_counter = 0

	# ======== (END) Interpolating and smoothing data
	'''
	proton_data_event = pd.DataFrame([])
	proton_concat_event = proton_df[[proton_channel]]
	proton_data_event = proton_data_event.append(proton_concat_event)
	# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0

	proton_event_df = pd.DataFrame([])
	proton_list_temp = []
	proton_list_event = []
	proton_counter = 0
	'''

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

	# add the lists here
	# p_10mev_list = pd.read_csv(f'{data_directory}/detected_events/event_dates/1d50pfu_10mev_2011_2017.txt', delim_whitespace=True, header=1)



	# =========  Outlier list
	if len( proton_list_event ) == 1:
		''' # block commented when adding smoothing since the proton channel is no longer used
		proton_var_list = []
		proton_outlier_list = []

		proton_mean = proton_df[proton_channel].loc[proton_list_event[0][1]:proton_list_event[0][-1]].mean(axis=0) # stopped here
		proton_len = len(proton_list_event[0])

		for i in proton_list_event[0]:
			proton_var = np.sqrt(  pow((proton_data_event[proton_channel].loc[i]  -  proton_mean), 2) / (proton_len - 1)  )
			if proton_var > 10.0:
				proton_outlier_list.append(i)
			proton_var_list.append(proton_var)

		if len(proton_outlier_list) != 0:
			for i in proton_outlier_list:
				proton_df.drop(i, inplace=True)
				proton_data_event.drop(i, inplace=True)
			# rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True)
		'''
		proton_event_df.loc[0] = [proton_list_event[0][0], proton_list_event[0][-1], ((proton_list_event[0][-1] - proton_list_event[0][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[0][0]:proton_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])

	elif len( proton_list_event ) > 1:
		''' # block commented when adding smoothing since the proton channel is no longer used
		#====== may not work for multiple events
		proton_var_list = []
		proton_outlier_list = []

		proton_mean = proton_df[proton_channel].loc[proton_list_event[0][1]:proton_list_event[0][-1]].mean(axis=0)
		proton_len = len(proton_list_event[0])

		for i in proton_list_event[0]:
			proton_var = np.sqrt(  pow((proton_data_event[proton_channel].loc[i]  -  proton_mean), 2) / (proton_len - 1)  )
			if proton_var > 10.0:
				proton_outlier_list.append(i)
			proton_var_list.append(proton_var)

		if len(proton_outlier_list) != 0:
			for i in proton_outlier_list:
				proton_df.drop(i, inplace=True)
				proton_data_event.drop(i, inplace=True)
		# ======= end might not work
		'''
		for i in range(len(proton_list_event)):
			proton_event_df.loc[i] = [proton_list_event[i][0], proton_list_event[i][-1], ((proton_list_event[i][-1] - proton_list_event[i][0]).total_seconds()/60), float(proton_data_event.loc[proton_list_event[i][0]:proton_list_event[i][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		# print(f"{rb_list_event[i][0]} -- {rb_list_event[i][-1]}", " Total Time: ", days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0]), " minutes")

	print('='*40)
	print(f"Number of Proton Events ({start} - {end}): ", len(proton_list_event))
	print(proton_event_df)
	print('='*40)

	# ============== end proton detection





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

			if rad2_include == 'yes':
				freq_rb2 = []
				for i in cdf['Frequency_RAD2']:
					freq_rb2.append(i)

				rad2_rb = []
				for i in cdf['E_VOLTAGE_RAD2']:
					rad2_rb.append(i)
	
				# data_time = pd.DataFrame(time_rb)
				# data_time.columns = ['date_time']
	
				data_freq2 = pd.DataFrame(freq_rb2)
				data_freq2.columns = ['freq']
	
				data_rad1 = pd.DataFrame(rad1_rb)
				data_rad1.columns = data_freq['freq']

				data_rad2 = pd.DataFrame(rad2_rb)
				data_rad2.columns = data_freq2['freq']



			if rad2_include != 'yes':
				rb_concat = pd.concat([data_time, data_rad1], axis=1)
				rb_concat.set_index(['date_time'], inplace=True)
				rb_data = rb_data.append(rb_concat)
			elif rad2_include == 'yes':
				rb_concat = pd.concat([data_time, data_rad1, data_rad2], axis=1)
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
	freq_rad1 = []
	full_freq = []
	freq_rad2 = []

	for rad1 in data_freq['freq']:
		freq_rad1.append(rad1)
		full_freq.append(rad1)

	for rad2 in data_freq2['freq']:
		full_freq.append(rad2)
		freq_rad2.append(rad2)

	rb_true_index = list(rb_data.index)
	rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True) # drop indices that contain values of values <= 0


	# RAD1 and RAD2
	rb_data['avg'] = rb_data[full_freq].mean(axis=1, numeric_only=True)

	# RAD 1 only
	# rb_data['avg'] = rb_data[freq_rad1].mean(axis=1, numeric_only=True)
	rb_data['rad1_avg'] = rb_data[freq_rad1].mean(axis=1, numeric_only=True)
	# sys.exit(0)


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



	# ======= TIII radio burst event detection
	# ======= added for event options
	t3_threshold = 2.0 # 5
	t3_freq = 'avg' # 120

	rb_data_event = pd.DataFrame([])
	rb_concat_event = rb_data[[t3_freq]]
	rb_data_event = rb_data_event.append(rb_concat_event)
	rb_data_event.drop(rb_data[rb_data.values == 0.0].index, inplace=True)

	rb_event_df = pd.DataFrame([])
	rb_list_temp = []
	rb_list_event = []
	rb_counter = 0

	min_length_event = 30 # 10
	min_t_between_pts = 10 # 10

	for i in rb_data_event[rb_data_event.values > t3_threshold].index: # for i in rb_data[rb_data.values > 300].index: # one level is 1 minute
		if len(rb_list_temp) == 0:
			rb_list_temp.append(i)

		elif len(rb_list_temp) >= 1:
			if (i - rb_list_temp[-1]) <= datetime.timedelta(minutes=min_t_between_pts): # originally 5 minutes
				rb_list_temp.append(i)

			elif (i - rb_list_temp[-1]) > datetime.timedelta(minutes=min_t_between_pts): # originally 5 minutes
				if (rb_list_temp[-1] - rb_list_temp[0]) >= datetime.timedelta(minutes=min_length_event):
					rb_list_event.append(rb_list_temp)
					rb_list_temp = []
					rb_list_temp.append(i)

				elif (rb_list_temp[-1] - rb_list_temp[0]) < datetime.timedelta(minutes=min_length_event):
					rb_list_temp = []
					rb_list_temp.append(i)

	if len(rb_list_temp) > 0:
		if (rb_list_temp[-1] - rb_list_temp[0]) >= datetime.timedelta(minutes=min_length_event):
			rb_list_event.append(rb_list_temp)
			rb_list_temp = []
			rb_list_temp.append(i)
		elif (rb_list_temp[-1] - rb_list_temp[0]) < datetime.timedelta(minutes=min_length_event):
			rb_list_temp = []
			rb_list_temp.append(i)
		rb_list_temp = []

	print("\n")
	rb_event_df = pd.DataFrame(columns=('start_time', 'end_time', 't3_duration', 't3_max_time', 't3_max_int', 'points_no'))

	# add the lists here
	# p_10mev_list = pd.read_csv(f'{data_directory}/detected_events/event_dates/1d50pfu_10mev_2011_2017.txt', delim_whitespace=True, header=1)



	# =========  Outlier list
	t3_freq_outlier = 120
	if len( rb_list_event ) == 1:
		rb_var_list = []
		rb_outlier_list = []
		test_var_list = []

		rb_mean = rb_data[t3_freq_outlier].loc[rb_list_event[0][1]:rb_list_event[0][-1]].mean(axis=0) # had 120 instead of t3_freq
		rb_len = len(rb_list_event[0])

		for i in rb_list_event[0]:
			rb_var = np.sqrt(  pow((rb_data[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # changed rb_data_event to rb_data due to outlier only showing well in 120 kHz channel # had 120 instead of t3_freq 
			# rb_var = np.sqrt(  pow((rb_data_event[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq (20180308) removed for new algorithm
			if rb_var > 20.0: # was set at 10.0 20120205
				print("Outliers: ", i, " :  ",rb_var)
				rb_outlier_list.append(i)
			rb_var_list.append(rb_var)
			test_var_list.append(str(f"{i} {rb_var} {rb_data[120].loc[i]}"))

		if len(rb_outlier_list) != 0:
			for i in rb_outlier_list:
				rb_data.drop(i, inplace=True)
				rb_data_event.drop(i, inplace=True)
			# rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True)

		rb_event_df.loc[0] = [rb_list_event[0][0], rb_list_event[0][-1], ((rb_list_event[0][-1] - rb_list_event[0][0]).total_seconds()/60), rb_data_event[f'{t3_freq}'].loc[rb_list_event[0][0]:rb_list_event[0][-1]].idxmax(), float(rb_data_event.loc[rb_list_event[0][0]:rb_list_event[0][-1]].max().values), len(rb_list_event[0]), ] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		# elif t3_freq != 'avg':
		#	rb_event_df.loc[0] = [rb_list_event[0][0], rb_list_event[0][-1], ((rb_list_event[0][-1] - rb_list_event[0][0]).total_seconds()/60), rb_data_event[int(f'{t3_freq}')].loc[rb_list_event[0][0]:rb_list_event[0][-1]].idxmax(), float(rb_data_event.loc[rb_list_event[0][0]:rb_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])

	elif len( rb_list_event ) > 1:

		#====== may not work for multiple events (more data points with added events lower threshold for variance)
		rb_var_list = []
		rb_outlier_list = []

		rb_mean = rb_data[t3_freq_outlier].loc[rb_list_event[0][1]:rb_list_event[0][-1]].mean(axis=0) # had 120 instead of t3_freq
		rb_len = len(rb_list_event[0])

		for i in rb_list_event[0]:
			print(i)
			rb_var = np.sqrt(  pow((rb_data[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq
			# rb_var = np.sqrt(  pow((rb_data_event[t3_freq].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq

			if rb_var > 20.0: # 10.0
				print("Outliers: ", i, " :  ",rb_var)
				rb_outlier_list.append(i)
			rb_var_list.append(rb_var)

		if len(rb_outlier_list) != 0:
			for i in rb_outlier_list:
				rb_data.drop(i, inplace=True)
				rb_data_event.drop(i, inplace=True)
		# ======= end might not work

		for i in range(len(rb_list_event)):
			rb_event_df.loc[i] = [rb_list_event[i][0], rb_list_event[i][-1], ((rb_list_event[i][-1] - rb_list_event[i][0]).total_seconds()/60), rb_data_event[t3_freq].loc[rb_list_event[i][0]:rb_list_event[i][-1]].idxmax(), float(rb_data_event.loc[rb_list_event[i][0]:rb_list_event[i][-1]].max().values),len(rb_list_event[i]), ] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		# print(f"{rb_list_event[i][0]} -- {rb_list_event[i][-1]}", " Total Time: ", days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0]), " minutes")

	print('='*40)
	print(f"Number of Radio Events ({start} - {end}) [{t3_freq} kHz]: ", len(rb_list_event))
	print(rb_event_df)
	print('='*40)



	# ======== (BEGIN) Interpolating and smoothing data for T3 data
	rb_data_df_interp = rb_data.reindex(rb_true_index).interpolate(method='linear').ffill()

	# ======= Event parameters for interpolated t3 data
	t3_threshold_interp = 2.0 # 5
	t3_freq_interp = 'avg' # 120

	rb_data_event_interp = pd.DataFrame([])
	rb_concat_event_interp = rb_data_df_interp[[t3_freq_interp]]
	rb_data_event_interp = rb_data_event_interp.append(rb_concat_event_interp)
	# rb_data_event.drop(rb_data[rb_data.values == 0.0].index, inplace=True)

	rb_event_df_interp = pd.DataFrame([])
	rb_list_temp_interp = []
	rb_list_event_interp = []
	rb_counter_interp = 0

	min_length_event_interp = 30 # 10
	min_t_between_pts_interp = 10 # 10

	for i in rb_data_event_interp[rb_data_event_interp.values > t3_threshold_interp].index: # for i in rb_data[rb_data.values > 300].index: # one level is 1 minute
		if len(rb_list_temp_interp) == 0:
			rb_list_temp_interp.append(i)

		elif len(rb_list_temp_interp) >= 1:
			if (i - rb_list_temp_interp[-1]) <= datetime.timedelta(minutes=min_t_between_pts_interp): # originally 5 minutes
				rb_list_temp_interp.append(i)

			elif (i - rb_list_temp_interp[-1]) > datetime.timedelta(minutes=min_t_between_pts_interp): # originally 5 minutes
				if (rb_list_temp_interp[-1] - rb_list_temp_interp[0]) >= datetime.timedelta(minutes=min_length_event_interp):
					rb_list_event_interp.append(rb_list_temp_interp)
					rb_list_temp_interp = []
					rb_list_temp_interp.append(i)

				elif (rb_list_temp_interp[-1] - rb_list_temp_interp[0]) < datetime.timedelta(minutes=min_length_event_interp):
					rb_list_temp_interp = []
					rb_list_temp_interp.append(i)

	if len(rb_list_temp_interp) > 0:
		if (rb_list_temp_interp[-1] - rb_list_temp_interp[0]) >= datetime.timedelta(minutes=min_length_event_interp):
			rb_list_event_interp.append(rb_list_temp_interp)
			rb_list_temp_interp = []
			rb_list_temp_interp.append(i)
		elif (rb_list_temp_interp[-1] - rb_list_temp_interp[0]) < datetime.timedelta(minutes=min_length_event_interp):
			rb_list_temp_interp = []
			rb_list_temp_interp.append(i)
		rb_list_temp_interp = []

	print("\n")
	rb_event_df_interp = pd.DataFrame(columns=('start_time', 'end_time', 't3_duration', 't3_max_time', 't3_max_int', 'points_no', 'intgl_int_dur'))

	# =========  Outlier list
	# t3_freq_outlier = 120
	if len( rb_list_event_interp ) == 1:
		'''
		rb_var_list = []
		rb_outlier_list = []

		rb_mean = rb_data[t3_freq_outlier].loc[rb_list_event[0][1]:rb_list_event[0][-1]].mean(axis=0) # had 120 instead of t3_freq
		rb_len = len(rb_list_event[0])

		for i in rb_list_event[0]:
			rb_var = np.sqrt(  pow((rb_data[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # changed rb_data_event to rb_data due to outlier only showing well in 120 kHz channel # had 120 instead of t3_freq 
			# rb_var = np.sqrt(  pow((rb_data_event[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq (20180308) removed for new algorithm
			if rb_var > 10.0: # was set at 10.0 20120205
				rb_outlier_list.append(i)
			rb_var_list.append(rb_var)

		if len(rb_outlier_list) != 0:
			for i in rb_outlier_list:
				rb_data.drop(i, inplace=True)
				rb_data_event.drop(i, inplace=True)
			# rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True)
		'''
		rb_event_df_interp.loc[0] = [rb_list_event_interp[0][0], rb_list_event_interp[0][-1], ((rb_list_event_interp[0][-1] - rb_list_event_interp[0][0]).total_seconds()/60), rb_data_event_interp[f'{t3_freq_interp}'].loc[rb_list_event_interp[0][0]:rb_list_event_interp[0][-1]].idxmax(), float(rb_data_event_interp.loc[rb_list_event_interp[0][0]:rb_list_event_interp[0][-1]].max().values), len(rb_list_event_interp[0]), round(rb_data_df_interp['avg'][rb_list_event_interp[0]].sum(),3), ] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		# elif t3_freq != 'avg':
		# rb_event_df.loc[0] = [rb_list_event[0][0], rb_list_event[0][-1], ((rb_list_event[0][-1] - rb_list_event[0][0]).total_seconds()/60), rb_data_event[int(f'{t3_freq}')].loc[rb_list_event[0][0]:rb_list_event[0][-1]].idxmax(), float(rb_data_event.loc[rb_list_event[0][0]:rb_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])

	elif len( rb_list_event_interp ) > 1:

		#====== may not work for multiple events (more data points with added events lower threshold for variance)
		'''
		rb_var_list = []
		rb_outlier_list = []

		rb_mean = rb_data[t3_freq_outlier].loc[rb_list_event[0][1]:rb_list_event[0][-1]].mean(axis=0) # had 120 instead of t3_freq
		rb_len = len(rb_list_event[0])

		for i in rb_list_event[0]:
			rb_var = np.sqrt(  pow((rb_data[t3_freq_outlier].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq
			# rb_var = np.sqrt(  pow((rb_data_event[t3_freq].loc[i]  -  rb_mean), 2) / (rb_len - 1)  ) # had 120 instead of t3_freq

			if rb_var > 10.0: # 10.0
				rb_outlier_list.append(i)
			rb_var_list.append(rb_var)

		if len(rb_outlier_list) != 0:
			for i in rb_outlier_list:
				rb_data.drop(i, inplace=True)
				rb_data_event.drop(i, inplace=True)
		# ======= end might not work
		'''
		for i in range(len(rb_list_event_interp)):
			rb_event_df_interp.loc[i] = [rb_list_event_interp[i][0], rb_list_event_interp[i][-1], ((rb_list_event_interp[i][-1] - rb_list_event_interp[i][0]).total_seconds()/60), rb_data_event_interp[t3_freq_interp].loc[rb_list_event_interp[i][0]:rb_list_event_interp[i][-1]].idxmax(), float(rb_data_event_interp.loc[rb_list_event_interp[i][0]:rb_list_event_interp[i][-1]].max().values), len(rb_list_event_interp[i]), round(rb_data_df_interp['avg'][rb_list_event_interp[i]].sum(),3),  ] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])



		# print(f"{rb_list_event[i][0]} -- {rb_list_event[i][-1]}", " Total Time: ", days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0]), " minutes")		


	print('='*40)
	print(f"Number of Radio Events by Interpolation ({start} - {end}) [{t3_freq_interp} kHz]: ", len(rb_list_event_interp))
	print(rb_event_df_interp)
	print('='*40)





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





#=========== 8: GOES Proton Flux HEPAD
if '8' in option_bin_set:
	if event_option == 'yes':
		satellite_no = str(event_list['prot_sat'][0])

	if event_option != 'yes':
		satellite_no = input('Specify which GOES Satellite for Proton Flux (13 or 15): ')
		if satellite_no != '13':
			if satellite_no != '15':
				if satellite_no != '10':
					print('SATELLITE ERROR: Must specify either 13 or 15.')
					sys.exit(0)



	if goes_corrected_option == 'yes':
		print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Proton Flux HEPAD".center(38," ") + "="}\n{"="*40}')

		HEP_energy_bin_list = []

		if start_date[4:6] != end_date[4:6]: # if the month of the start day is NOT the same as the month of the end date
			HEP_proton_df = pd.DataFrame([])

			cur_date =  start
			date_in_year = [cur_date]

			while cur_date < end:
				# print(cur_date)
				cur_date += relativedelta(months=1)
				date_in_year.append(cur_date)


			if start.year >= 2011:
				# cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']
				HEP_cpflux_names = ['time_tag','A7_QUAL_FLAG','A7_NUM_PTS','A7_FLUX','A8_QUAL_FLAG','A8_NUM_PTS','A8_FLUX','P8_QUAL_FLAG','P8_NUM_PTS','P8_FLUX','P9_QUAL_FLAG','P9_NUM_PTS','P9_FLUX','P10_QUAL_FLAG','P10_NUM_PTS','P10_FLUX','P11_QUAL_FLAG','P11_NUM_PTS','P11_FLUX']

				# energy_bin_list.append(['ZPGT10W','>10 MeV', 'red'])
				# energy_bin_list.append(['ZPGT50W','>50 MeV', 'blue'])
				# energy_bin_list.append(['ZPGT100W','>100 MeV', 'lime'])

				HEP_energy_bin_list.append(['P8_FLUX','375 MeV', 'red'])
				HEP_energy_bin_list.append(['P9_FLUX','465 MeV', 'orange'])
				HEP_energy_bin_list.append(['P10_FLUX','605 MeV', 'green'])
				HEP_energy_bin_list.append(['P11_FLUX','>700 MeV', 'blue'])


				for date_event in date_in_year:
					try:
						f_l_day = calendar.monthrange(int(date_event.year), int(date_event.month)) #	f_l_day = calendar.monthrange(int(detection_year), int(month_event))
						event_f_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
						event_l_day = str(f'{date_event.year}{str(date_event.month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
		
		
						dir_check = os.path.isdir(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{date_event.year}')
						if dir_check == False:
							try:
							    os.makedirs(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{date_event.year}')
							except OSError as e:
							    if e.errno != errno.EEXIST:
							        raise
						
						HEP_proton_name = f'g{satellite_no}_hepad_ap_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
						proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{date_event.year}/{HEP_proton_name}')
			
						if proton_check == True:
							dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
							HEP_proton_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{date_event.year}/{HEP_proton_name}', skiprows=310, date_parser=dateparse, names=HEP_cpflux_names,index_col='time_tag', header=0)
							HEP_proton_df = HEP_proton_df.append(HEP_proton_df_ind)
	
			
						elif proton_check == False:
							HEP_proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{date_event.year}/{str(date_event.month).zfill(2)}/goes{satellite_no}/csv/{HEP_proton_name}'
							# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
							proton_in = wget.download(HEP_proton_url)
							dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
							HEP_proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=310, date_parser=dateparse, names=HEP_cpflux_names,index_col='time_tag', header=0) # ZPGT100W
							HEP_proton_df = HEP_proton_df.append(HEP_proton_df_ind)
	
							if save_option == 'yes':
								shutil.move(f'{HEP_proton_name}', f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{date_event.year}')
							elif save_option == 'no':
								os.remove(HEP_proton_name)
			
						continue
			
					except Exception as e:
						print(e)
						print(f'{date_event.month} does not have data.')

				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P8_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P9_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P10_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P11_FLUX'] <= 0.0].index, inplace=True)



		elif start_date[4:6] == end_date[4:6]: # if the month of the start day is the same as the month of the end date

			if start.year >= 2011:
				HEP_cpflux_names = ['time_tag','A7_QUAL_FLAG','A7_NUM_PTS','A7_FLUX','A8_QUAL_FLAG','A8_NUM_PTS','A8_FLUX','P8_QUAL_FLAG','P8_NUM_PTS','P8_FLUX','P9_QUAL_FLAG','P9_NUM_PTS','P9_FLUX','P10_QUAL_FLAG','P10_NUM_PTS','P10_FLUX','P11_QUAL_FLAG','P11_NUM_PTS','P11_FLUX']

				HEP_energy_bin_list.append(['P8_FLUX','375 MeV', 'red'])
				HEP_energy_bin_list.append(['P9_FLUX','465 MeV', 'orange'])
				HEP_energy_bin_list.append(['P10_FLUX','605 MeV', 'green'])
				HEP_energy_bin_list.append(['P11_FLUX','>700 MeV', 'blue'])

				f_l_day = calendar.monthrange(int(f'{start_year}'), int(f'{start_month}'))
				event_f_day = str(f'{start_year}{str(start_month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
				event_l_day = str(f'{start_year}{str(start_month).zfill(2)}{str(f_l_day[1]).zfill(2)}')
				dir_check = os.path.isdir(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{start_year}')
				if dir_check == False:
					try:
					    os.makedirs(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{start_year}')
					except OSError as e:
					    if e.errno != errno.EEXIST:
					        raise
				
		
				HEP_proton_name = f'g{satellite_no}_hepad_ap_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
				proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{start_year}/{HEP_proton_name}')
		
				if proton_check == True:
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					HEP_proton_df = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{start_year}/{HEP_proton_name}', skiprows=310, date_parser=dateparse, names=HEP_cpflux_names,index_col='time_tag', header=0)
		
		
				elif proton_check == False:
					HEP_proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{start_year}/{start_month}/goes{satellite_no}/csv/{HEP_proton_name}'
					# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
					proton_in = wget.download(HEP_proton_url)
					dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
					HEP_proton_df = pd.read_csv(f'{proton_in}', skiprows=310, date_parser=dateparse, names=HEP_cpflux_names,index_col='time_tag', header=0) # ZPGT100W
		
					if save_option == 'yes':
						shutil.move(f'{HEP_proton_name}', f'{data_directory}/GOES/GOES_{satellite_no}/HEPflux/{start_year}')
					elif save_option == 'no':
						os.remove(HEP_proton_name)
		
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P8_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P9_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P10_FLUX'] <= 0.0].index, inplace=True)
				HEP_proton_df.drop(HEP_proton_df[HEP_proton_df['P11_FLUX'] <= 0.0].index, inplace=True)
		


	# ======= proton event detection
	''' # for reference, corrected Epead flux algorithm
	proton_threshold = pow(10,-1.25) # t3_threshold = 5 # 5 # pow(10, -0.9) # pow(10, -0.8)
	proton_channel = 'ZPGT100W' # t3_freq = 120

	proton_data_event = pd.DataFrame([])
	proton_concat_event = proton_df[[proton_channel]]
	proton_data_event = proton_data_event.append(proton_concat_event)
	# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0

	proton_event_df = pd.DataFrame([])
	proton_list_temp = []
	proton_list_event = []
	proton_counter = 0

	min_length_event = 1000 # 60
	min_t_between_pts = 40

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
	'''



	# ======= added for event options
	HEP_proton_smooth_df = pd.DataFrame(HEP_proton_df['P8_FLUX']) # .loc[event_obj_start:event_obj_end]) # this removes the limitation on the data range of smoothing

	HEP_proton_smooth_df_rs_1m = HEP_proton_smooth_df.resample('min')
	HEP_proton_smooth_df_rs_1s = HEP_proton_smooth_df.resample('S')

	HEP_proton_smooth_df_interp_1m = HEP_proton_smooth_df_rs_1m.interpolate(method='cubic')
	HEP_proton_smooth_df_interp_1s = HEP_proton_smooth_df_rs_1s.interpolate(method='cubic')


		
	HEP_order_list = [1,2,3,4,5,6,7,8,9,10]

	for order in HEP_order_list:

		b, a = signal.butter(order, 0.08) # order of the filter (increases in integer values), cut off frequency

		HEP_y1 = signal.filtfilt(b, a, HEP_proton_smooth_df['P8_FLUX'])
		HEP_proton_smooth_df[f'butter{order}'] = HEP_y1


	# =========== Smoothing end

	# ============ Background choice (start)
	'''
	bkg_start = f'2012-03-06 22'
	bkg_end = '2012-03-06 23'

	HEP_proton_threshold = HEP_proton_smooth_df['butter1'].loc[bkg_start:bkg_end].mean() + 0.0002
	print(HEP_proton_threshold)
	'''
	# ============ Background choice (end)


	
	# HEP_proton_threshold =  pow(10, -2.6) # t3_threshold = 5 # 5 # pow(10, -0.9) # pow(10,-2.7)
	HEP_proton_threshold = 0.002
	HEP_proton_channel = 'P8_FLUX' # t3_freq = 120

	HEP_proton_data_event = pd.DataFrame([])
	HEP_proton_concat_event = HEP_proton_smooth_df[['butter7']]
	# HEP_proton_concat_event = HEP_proton_df[[HEP_proton_channel]] # old algorithm

	HEP_proton_data_event = HEP_proton_data_event.append(HEP_proton_concat_event)
	# proton_data_event.drop(proton_df[proton_df.values == 0.0].index, inplace=True) # proton_data.values == 0.0

	HEP_proton_event_df = pd.DataFrame([])
	HEP_proton_list_temp = []
	HEP_proton_list_event = []
	proton_counter = 0

	HEP_min_length_event = 100 # 100 # 60
	HEP_min_t_between_pts = 70

	for i in HEP_proton_data_event[HEP_proton_data_event.values > HEP_proton_threshold].index: # for i in rb_data[rb_data.values > 300].index: # one level is 1 minute
		if len(HEP_proton_list_temp) == 0:
			HEP_proton_list_temp.append(i)

		elif len(HEP_proton_list_temp) >= 1:
			if (i - HEP_proton_list_temp[-1]) <= datetime.timedelta(minutes=HEP_min_t_between_pts): # originally 5 minutes # also had at 30 minutes, but increasing to 40 
				HEP_proton_list_temp.append(i)

			elif (i - HEP_proton_list_temp[-1]) > datetime.timedelta(minutes=HEP_min_t_between_pts): # originally 5 minutes # time between first interval of time event to the second
				if (HEP_proton_list_temp[-1] - HEP_proton_list_temp[0]) >= datetime.timedelta(minutes=HEP_min_length_event):
					HEP_proton_list_event.append(HEP_proton_list_temp)
					HEP_proton_list_temp = []
					HEP_proton_list_temp.append(i)

				elif (HEP_proton_list_temp[-1] - HEP_proton_list_temp[0]) < datetime.timedelta(minutes=HEP_min_length_event): # if the time difference is less than 30 minutes, then create a new event
					HEP_proton_list_temp = []
					HEP_proton_list_temp.append(i)

	if len(HEP_proton_list_temp) > 0:
		if (HEP_proton_list_temp[-1] - HEP_proton_list_temp[0]) >= datetime.timedelta(minutes=HEP_min_length_event):
			HEP_proton_list_event.append(HEP_proton_list_temp)
			HEP_proton_list_temp = []
			HEP_proton_list_temp.append(i)
		elif (HEP_proton_list_temp[-1] - HEP_proton_list_temp[0]) < datetime.timedelta(minutes=HEP_min_length_event):
			HEP_proton_list_temp = []
			HEP_proton_list_temp.append(i)
		HEP_proton_list_temp = []

	print("\n")
	HEP_proton_event_df = pd.DataFrame(columns=('start_time', 'end_time', 'proton_duration', 'proton_max_int'))

	# add the lists here
	# p_10mev_list = pd.read_csv(f'{data_directory}/detected_events/event_dates/1d50pfu_10mev_2011_2017.txt', delim_whitespace=True, header=1)


	# =========  Outlier list
	if len( HEP_proton_list_event ) == 1:
		'''
		
		HEP_proton_var_list = []
		HEP_proton_outlier_list = []

		HEP_proton_mean = HEP_proton_df[HEP_proton_channel].loc[HEP_proton_list_event[0][1]:HEP_proton_list_event[0][-1]].mean(axis=0) # stopped here
		HEP_proton_len = len(HEP_proton_list_event[0])

		for i in HEP_proton_list_event[0]:
			proton_var = np.sqrt(  pow((HEP_proton_data_event[HEP_proton_channel].loc[i]  -  HEP_proton_mean), 2) / (HEP_proton_len - 1)  )
			if proton_var > 10.0:
				HEP_proton_outlier_list.append(i)
			HEP_proton_var_list.append(proton_var)

		if len(HEP_proton_outlier_list) != 0:
			for i in HEP_proton_outlier_list:
				HEP_proton_df.drop(i, inplace=True)
				HEP_proton_data_event.drop(i, inplace=True)
			# rb_data.drop(rb_data[rb_data.values == 0.0].index, inplace=True)
		'''
		HEP_proton_event_df.loc[0] = [HEP_proton_list_event[0][0], HEP_proton_list_event[0][-1], ((HEP_proton_list_event[0][-1] - HEP_proton_list_event[0][0]).total_seconds()/60), float(HEP_proton_data_event.loc[HEP_proton_list_event[0][0]:HEP_proton_list_event[0][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])

	elif len( HEP_proton_list_event ) > 1:
		'''
		#====== may not work for multiple events
		HEP_proton_var_list = []
		HEP_proton_outlier_list = []

		HEP_proton_mean = HEP_proton_df[HEP_proton_channel].loc[HEP_proton_list_event[0][1]:HEP_proton_list_event[0][-1]].mean(axis=0)
		HEP_proton_len = len(HEP_proton_list_event[0])

		for i in HEP_proton_list_event[0]:
			proton_var = np.sqrt(  pow((HEP_proton_data_event[HEP_proton_channel].loc[i]  -  HEP_proton_mean), 2) / (HEP_proton_len - 1)  )
			if proton_var > 10.0:
				HEP_proton_outlier_list.append(i)
			HEP_proton_var_list.append(proton_var)

		if len(HEP_proton_outlier_list) != 0:
			for i in HEP_proton_outlier_list:
				HEP_proton_df.drop(i, inplace=True)
				HEP_proton_data_event.drop(i, inplace=True)
		# ======= end might not work
		'''
		for i in range(len(HEP_proton_list_event)):
			HEP_proton_event_df.loc[i] = [HEP_proton_list_event[i][0], HEP_proton_list_event[i][-1], ((HEP_proton_list_event[i][-1] - HEP_proton_list_event[i][0]).total_seconds()/60), float(HEP_proton_data_event.loc[HEP_proton_list_event[i][0]:HEP_proton_list_event[i][-1]].max().values)] # days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0])
		# print(f"{rb_list_event[i][0]} -- {rb_list_event[i][-1]}", " Total Time: ", days_hours_minutes(rb_list_event[i][-1] - rb_list_event[i][0]), " minutes")
	

	print('='*40)
	print(f"Number of Proton Events ({start} - {end}): ", len(HEP_proton_list_event))
	print(HEP_proton_event_df)
	print('='*40)

	'''
	HEP_proton_smooth_df = pd.DataFrame(HEP_proton_df['P8_FLUX'].loc[event_obj_start:event_obj_end])

	HEP_proton_smooth_df_rs_1m = HEP_proton_smooth_df.resample('min')
	HEP_proton_smooth_df_rs_1s = HEP_proton_smooth_df.resample('S')

	HEP_proton_smooth_df_interp_1m = HEP_proton_smooth_df_rs_1m.interpolate(method='cubic')
	HEP_proton_smooth_df_interp_1s = HEP_proton_smooth_df_rs_1s.interpolate(method='cubic')


	
	HEP_order_list = [1,2,3,4,5,6,7,8,9,10]

	for order in HEP_order_list:

		b, a = signal.butter(order, 0.08) # order of the filter (increases in integer values), cut off frequency

		HEP_y1 = signal.filtfilt(b, a, HEP_proton_smooth_df['P8_FLUX'])
		HEP_proton_smooth_df[f'butter{order}'] = HEP_y1
	'''


'''
# Templates for new data

#===========
print(f'\n{"="*40}\nNew Dataset Name Goes Here\n{"="*40}')
'''



# ======================== Modified Code for plotting, change things in here
import matplotlib.dates as mdate


f, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(10, 7))

'''
def string_date_to_numeric(li):
    series = pd.Series(li)
    datetime = pd.to_datetime(series)
    numeric = pd.to_numeric(datetime)
    return numeric
'''

def string_date_to_numeric(li):
    # series = pd.Series(li)
    # datetime = pd.to_datetime(series)
    # numeric = datetime.strftime('%s') # pd.to_numeric(datetime)
    # numeric = li.strftime('%s')
    datetime = li.strftime('%s')
    numeric = np.array(datetime, dtype=np.int64)
    return numeric


# ====== Convert 20110607 to epoch
xray_june = string_date_to_numeric(datetime.datetime(2011, 6, 7, 6, 16, 00))
t3_june = string_date_to_numeric(datetime.datetime(2011, 6, 7, 6, 26, 30))
proton_june = string_date_to_numeric(datetime.datetime(2011, 6, 7, 6, 45, 00))


# ====== End conversion


# x = string_date_to_numeric(rb_data.index)
x = string_date_to_numeric(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index)
# x = np.arange(0,len(rb_data.index))
y = full_freq
X, Y = np.meshgrid(x,y)
Xt = np.transpose(X)
Yt = np.transpose(Y)
# print(np.shape(Xt))
# print(X, Y)

# Z = rb_data[full_freq].values
z = rb_data[full_freq].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].values
Z = np.transpose(z)


s_time = datetime.datetime.strptime(start_hour, '%H').time()
e_time = datetime.datetime.strptime(end_hour, '%H').time()

s_dtime = datetime.datetime.combine(start, s_time)
e_dtime = datetime.datetime.combine(end, e_time)


# fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(8, 6))
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X,Y,Z, cmap=cm.viridis)


# ========= xray flux (ax1)
def flare_class(X):
	if X == 10**-4:
		return "X"
	#return ["%.3f" % z for z in V]

ax1.plot(string_date_to_numeric(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm', zorder=5)
ax1.plot(string_date_to_numeric(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.4 nm', zorder=5)
ax1.set_yscale('log')


flare_classes = ['', 'A', 'B', 'C', 'M', 'X']
ax7 = ax1.twinx()
ax7.set_yscale('log')
ax7.set_ylim(ax1.get_ylim())
# ax7.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
ax7.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3])
ax7.set_yticklabels(labels=flare_classes)
ax7.tick_params(axis='y', which='both', direction='in')

ax1.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3])
# ax1.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])


ax1.grid(linestyle=':')

# ======= radio bursts (ax2)
from mpl_toolkits.axes_grid1 import make_axes_locatable

lower_bound = -10
upper_bound = 50

cf = ax2.contourf(X,Y,Z,40, vmin=lower_bound, vmax=upper_bound, cmap=cm.jet, levels=np.linspace(lower_bound,upper_bound,100), extend='max') # ["neither", "both", "min", "max"]
cax = f.add_axes([0.91, 0.55, 0.0125, 0.15]) # ([0.9, 0.1, 0.03, 0.8])
cb = f.colorbar(cf, cax=cax)

tick_locator = ticker.MaxNLocator(nbins=5)
cb.locator = tick_locator
cb.update_ticks()

'''
cbar_ax = f.add_axes([0.85, 0.15, 0.05, 0.7])
f.colorbar(cf, cax=cbar_ax)
'''

# plt.colorbar()
'''
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0)

plt.colorbar(cf, cax=cax)
'''

ax2.set_yscale('log')

ax2.grid(linestyle=':')

ax2.axhline(1040, linestyle='-', zorder=2, linewidth=1, color='black')


t3_xlim = ax2.get_xticks()[-1]


ax2.text(t3_xlim-15000, 30, r'RAD1', fontsize=14)
ax2.text(t3_xlim-15000, 1100, r'RAD2', fontsize=14)

# ======= radio burst average (ax3)
ax3.plot(string_date_to_numeric(rb_data_df_interp.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), rb_data_df_interp['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], '.', mfc='none', color='blue', zorder=3)

for rbevent_no_interp in range(len(rb_list_event_interp)):
	for rbpoint_interp in rb_list_event_interp[rbevent_no_interp]:
		interp_x = string_date_to_numeric(rbpoint_interp)
		ax3.vlines(x=interp_x, ymin=t3_threshold_interp, ymax=rb_data_df_interp['avg'].loc[rbpoint_interp], linewidth=1, color='fuchsia', zorder=2)
	
'''
for i in range(len(rb_event_df)):
	if s_dtime <= (rb_event_df['start_time'][i] and rb_event_df['end_time'][i]) <= e_dtime:
		ax2.axvspan(rb_event_df['start_time'][i], rb_event_df['end_time'][i], color='lightblue', alpha=0.5)
	# axes[length_data_list[j]].axvspan(rb_event_df['start_time'].values, rb_event_df['end_time'].values, color='blue', alpha=0.5)
'''
'''
for i in range(len(rb_event_df)):
	ax2.axvspan(string_date_to_numeric(rb_event_df['start_time'][i]), string_date_to_numeric(rb_event_df['end_time'][i]), color='lightblue', alpha=0.5)
'''

ax3.axhline(t3_threshold, linewidth=1, zorder=1, color='red', linestyle='-', label=f'{t3_threshold} dB') #  xmin=0, xmax=1
'''
for i in range(len(rb_event_df)):
	if s_dtime <= (rb_event_df_interp['start_time'][i] and rb_event_df_interp['end_time'][i]) <= e_dtime:
		ax3.axvline(string_date_to_numeric(rb_event_df_interp['start_time'][i]).values, linewidth=1, zorder=3, color='green', linestyle=':') #  xmin=0, xmax=1
'''

ax3.grid(linestyle=':')
ax3.set_yticks([25,50,75,100])


# ======= Protons (ax4)
for i in energy_bin_list: # for i in sorted(energy_bin_list): # changed to unsorted because the sort queued off of 10 -> 100 -> 50 rather than 10 -> 50 -> 100
	ax4.plot(string_date_to_numeric(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],'.', mfc='none', color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True) , 
	# ax3.plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], '.', mfc='none', color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)

color_tree = iter(cm.rainbow(np.linspace(0,1,10)))

if proton_event_option == 'smooth':
	ax4.plot(string_date_to_numeric(proton_smooth_df[f'{butter_filter}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), proton_smooth_df[f'{butter_filter}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='purple', linewidth=1, label=f'Butter-{butter_order}', zorder=5)

ax4.set_yscale('log')



s_time = datetime.datetime.strptime(start_hour, '%H').time()
e_time = datetime.datetime.strptime(end_hour, '%H').time()

s_dtime = datetime.datetime.combine(start, s_time)
e_dtime = datetime.datetime.combine(end, e_time)

'''
for i in range(len(proton_event_df)):
	if s_dtime <= (proton_event_df['start_time'][i] and proton_event_df['end_time'][i]) <= e_dtime:
		# string_date_to_numeric(rb_event_df['start_time'][0]).values
		# ax3.axvspan(proton_event_df['start_time'][i], proton_event_df['end_time'][i], color='palegreen', alpha=0.5)
		ax4.axvline(string_date_to_numeric(proton_event_df['start_time'][i]).values, linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1
		# ax3.axvline(string_date_to_numeric(proton_event_df['end_time'][i]).values, linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1
'''

# ax3.axvline(s_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1
# ax3.axvline(e_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1


ax4.axhline(proton_threshold, linewidth=1, zorder=2, color='red', linestyle='-.', label=f'{round(proton_threshold, 3)} pfu') #  xmin=0, xmax=1 # threshold
ax4.grid(linestyle=':')



# ===== vertical lines

ax4.axvline(xray_june, linestyle=':', linewidth=2, color='red')
ax4.axvline(t3_june, linestyle=':', linewidth=2, color='blue')
# ax4.axvline(t3_june)
ax4.axvline(proton_june, linestyle=':', linewidth=2, color='green')


ax1.minorticks_on()
ax2.minorticks_on()
ax3.minorticks_on()
ax4.minorticks_on()


ax1.tick_params(axis='y', which='both', direction='in')
ax2.tick_params(axis='y', which='both', direction='in')
ax3.tick_params(axis='y', which='both', direction='in')
ax4.tick_params(axis='y', which='both', direction='in')

ax1.tick_params(axis='x', which='both', direction='in',top='on', bottom='on')
ax2.tick_params(axis='x', which='both', direction='in',top='on', bottom='on')
ax3.tick_params(axis='x', which='both', direction='in',top='on', bottom='on')
ax4.tick_params(axis='x', which='both', direction='in',top='on', bottom='on')




'''
for i in range(len(rb_event_df)):
	print(f"Radio Burst Start Time ({rb_event_df['start_time'][i]}): ", string_date_to_numeric(rb_event_df['start_time'][i]))

print("=====================")

for i in range(len(proton_event_df)):
	print(f"Proton Start Time ({proton_event_df['start_time'][i]}): ", string_date_to_numeric(proton_event_df['start_time'][i]))
'''


'''
plt.xticks(x, rb_data.index, rotation='vertical')

spacing = 100
visible = ax.xaxis.get_ticklabels()[::spacing]
for label in ax.xaxis.get_ticklabels():
    if label not in visible:
        label.set_visible(False)
'''


# ax.set_xticklabels(rb_data.index)
# ax.xaxis.set_major_formatter(mdates.ticker.FixedFormatter(rb_data.index))

'''
# Get the current axis
ax = plt.gca()

# Only label every 20th value
ticks_to_use = rb_data.index[::20]

# Set format of labels (note year not excluded as requested)
labels = [ i.strftime("%-H:%M") for i in ticks_to_use ]

# Now set the ticks and labels
ax.set_xticks(ticks_to_use)
ax.set_xticklabels(labels)
'''

# ax.xaxis_date()
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Create your ticker object with M ticks
M = 20
xticks = ticker.MaxNLocator(M)

# Set the yaxis major locator using your ticker object. You can also choose the minor
# tick positions with set_minor_locator.
# ax1.xaxis.set_major_locator(xticks)
# ax.set_xticklabels(rb_data.index[::5, :])


# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

f.autofmt_xdate()
# ax.xaxis.set_major_formatter(mdates.DateFormatter("%w %H:%M:%S"))
# ax.fmt_xdata = mdates.DateFormatter('%Y')

# ax1.yscale('log')

# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

# plt.tight_layout()

'''
axes[length_data_list[j]].set_xlabel('Time [UT]', fontname="Arial", fontsize = 12)

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax.xaxis.set_major_formatter(myFmt)

plt.suptitle(f'Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()
'''

'''
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax4.xaxis.set_major_formatter(myFmt)
'''
ax4.margins(x=0)

ax_labels_numeric = ax4.get_xticks()

ax_labels_datetime = []
for i in ax_labels_numeric:
	ax_labels_datetime.append(datetime.datetime.fromtimestamp(i)) # .strftime('%Y-%m-%d\n%H:%M'))# .strftime('%c')) # ('%Y-%m-%d %H:%M:%S')

ax_labels_datetime_formatted = []
for i in range(len(ax_labels_datetime)):
	ax_labels_datetime_formatted.append(ax_labels_datetime[i].strftime('%Y-%m-%d\n%H:%M:%S'))

ax1.set_ylabel(f'Xray Flux\n [Wm$^2$]', fontname="Arial", fontsize = 16)
ax2.set_ylabel(f'Frequency\n [kHz]', fontname="Arial", fontsize = 16)
ax3.set_ylabel(f'Averaged TIII\n Intensity [dB]', fontname="Arial", fontsize = 16)
ax4.set_ylabel(f'Proton Flux\n [pfu]', fontname="Arial", fontsize = 16)

ax4.set_xticklabels(ax_labels_datetime_formatted)
ax4.set_xlabel('Time [UT]', fontname="Arial", fontsize = 16)


# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)

# xmin, xmax = plt.xlim()  # return the current xlim
# plt.xlim((xmin, xmax))   # set the xlim to xmin, xmax
# plt.xlim(xmin, xmax)     # set the xlim to xmin, xmax

# plt.margins(x=0)


plt.axis('tight')
plt.savefig(f'presentation_plots/combined_plot.png', format='png', dpi=900)

plt.show()



# rb_data.to_csv("test_data.csv", sep=",")
# rb_data.plot.scatter(x=rb_data.index, y=data_rad1, c=rb_data.values)
sys.exit(0)








# =========================================================== END OF DATA (PLOTTING)



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


	# sys.exit(0)

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


# ======== Proton flux parameters
if goes_corrected_option == 'yes':
	if '1' in option_bin_set:
		high_bin_proton = energy_bin_list[-1][0]
		low_bin_proton = energy_bin_list[0][0]
		# print(f"\nMax Proton Flux (>100 MeV)", proton_df[f'{high_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()) #, proton_df[f'{high_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax())
		# print(f"Max Proton Flux (>10 MeV)", proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()) #, proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax())
		
		for i in energy_bin_list: # sorted(energy_bin_list): # sort listed 100W, 10W, 50W, therefore incorrectly
			pmaxflux = proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max()
			pmaxflux_exp = "%0.3E" % pmaxflux

			pmaxtime = proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()
			print(f"GOES-{satellite_no} Peak Proton Flux ({i[1]}): ({pmaxtime}) {pmaxflux_exp} [pfu]")

elif goes_corrected_option == 'no':
	if '1' in option_bin_set:
		high_bin_proton = sorted(energy_bin_list)[-1][0]
		low_bin_proton = sorted(energy_bin_list)[0][0]
		print(f"Max Proton Flux (>{low_bin_proton} MeV)", proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax())


# ======== Definition of proton flux parameters
def applyPlotStyle():
	axes[length_data_list[j]].grid(True)
	axes[length_data_list[j]].minorticks_on()
	if '1' in option_bin_set:
		# high_bin_proton_str = sorted(energy_bin_list)[-1][1]
		# low_bin_proton_str = sorted(energy_bin_list)[0][1]
		axes[length_data_list[j]].axvline(proton_df[f'{low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), linewidth=1, zorder=1, color='purple', linestyle='--', label='Max >10 MeV') # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified
		axes[length_data_list[j]].axvline(proton_df[f'{high_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), linewidth=1, zorder=1, color='green', linestyle='--', label='Max >100 MeV') # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified
	
	if '2' in option_bin_set:
		if len(rb_event_df) != 0:
			axes[length_data_list[j]].axvline(rb_event_df['t3_max_time'].loc[rb_event_df['t3_duration'].idxmax()], linewidth=1, zorder=1, color='orange', linestyle='--', label='Max T3 Intensity') # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified

	if '5' in option_bin_set:
		xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax()
		fint = xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].max()
		fint_exp = "%0.2E" % fint

		axes[length_data_list[j]].axvline(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), linewidth=1, zorder=1, color='red', linestyle=':', label=f'{fint_exp}') # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified

	if '8' in option_bin_set:
		HEP_low_bin_proton = HEP_energy_bin_list[0][0]

		axes[length_data_list[j]].axvline(HEP_proton_df[f'{HEP_low_bin_proton}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].idxmax(), linewidth=1, zorder=1, color='orange', linestyle='--', label='Max 375 MeV') # (proton_df.P6W_UNCOR_FLUX.max()) # changed maximum flux to be within time interval specified

		

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
		axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Epead Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)

	elif goes_corrected_option == 'no':
		for i in sorted(energy_bin_list):
			axes[length_data_list[j]].plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
		axes[length_data_list[j]].set_yscale('log')
		# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
	
		axes[length_data_list[j]].set_yticks([10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3])
		axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} Epead Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)



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

	axes[length_data_list[j]].axvline(s_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1
	axes[length_data_list[j]].axvline(e_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1


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
	

	s_time = datetime.datetime.strptime(start_hour, '%H').time()
	e_time = datetime.datetime.strptime(end_hour, '%H').time()

	s_dtime = datetime.datetime.combine(start, s_time)
	e_dtime = datetime.datetime.combine(end, e_time)


	color_cm=iter(cm.viridis(np.linspace(0,1, 5 )))
	if rad2_include != 'yes':
		freq_list = [120,100,'avg'] # changed (20180306) to incorporate more frequencies, originally [120] # [100, 300, 500, 700, 900]
	elif rad2_include =='yes':
		freq_list = [120,100,'rad1_avg','avg'] # changed (20180306) to incorporate more frequencies, originally [120] # [100, 300, 500, 700, 900]


	for frequency in freq_list:
		color_choice = next(color_cm)
		
		axes[length_data_list[j]].plot(rb_data[frequency].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=color_choice, label= f'{frequency} kHz', zorder=5)
	
	# axes[length_data_list[j]].axvline(rb_event_df['start_time'].values, linewidth=1, zorder=1, color='blue', linestyle='--', label='Max >10MeV')
	# axes[length_data_list[j]].axvline(rb_event_df['end_time'].values, linewidth=1, zorder=1, color='blue', linestyle='--', label='Max >10MeV')
	
	for i in range(len(rb_event_df)):
		if s_dtime <= (rb_event_df['start_time'][i] and rb_event_df['end_time'][i]) <= e_dtime:
			axes[length_data_list[j]].axvspan(rb_event_df['start_time'][i], rb_event_df['end_time'][i], color='lightblue', alpha=0.5)
		# axes[length_data_list[j]].axvspan(rb_event_df['start_time'].values, rb_event_df['end_time'].values, color='blue', alpha=0.5)


	axes[length_data_list[j]].axhline(t3_threshold, linewidth=1, zorder=2, color='red', linestyle='-', label=f'{t3_threshold} sfu') #  xmin=0, xmax=1


	# axes[length_data_list[j]].set_ylim(0, 100) # commented to allow for auto y-scaling, remove for rigid axis
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

if '8' in option_bin_set: # HEPAD
	next_global()
	if goes_corrected_option == 'yes':
		for i in HEP_energy_bin_list: # for i in sorted(energy_bin_list): # changed to unsorted because the sort queued off of 10 -> 100 -> 50 rather than 10 -> 50 -> 100
			axes[length_data_list[j]].plot(HEP_proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True) ,'o',mfc='none'
		
		color_tree = iter(cm.viridis(np.linspace(0,1,10)))

		'''
		for order in range(10):
			# axes[length_data_list[j]].plot(proton_smooth_df[f'butter{order+1}'], color=next(color_tree), linewidth=1, label= f'Butter-{order}', zorder=5) # butter filter
			axes[length_data_list[j]].plot(HEP_proton_smooth_df[f'butter{order+1}'].loc[event_obj_start:event_obj_end], color=next(color_tree), linewidth=1, label=f'Butter-{order}', zorder=5) # butter filter
		'''
		axes[length_data_list[j]].plot(HEP_proton_smooth_df['butter1'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='purple', linewidth=2, label='Butter-1', zorder=5) # butter filter

		axes[length_data_list[j]].set_yscale('log')
		# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
	
		axes[length_data_list[j]].set_yticks([10**-5, 10**-4, 10**-3, 10**-2, 10**-1, 10**0]) # 10**-3, 
		axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} HEPAD Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)


	elif goes_corrected_option == 'no':
		for i in sorted(energy_bin_list):
			axes[length_data_list[j]].plot(HEP_proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)
		axes[length_data_list[j]].set_yscale('log')
		# axes[length_data_list[j]].set_ylim((10**(-3)), (10**3))
	
		axes[length_data_list[j]].set_yticks([10**-3, 10**-2, 10**-1, 10**0, 10**1, 10**2, 10**3])
		axes[length_data_list[j]].set_ylabel(f'GOES-{satellite_no} HEPAD Proton\nFlux [pfu]', fontname="Arial", fontsize = 12)



	s_time = datetime.datetime.strptime(start_hour, '%H').time()
	e_time = datetime.datetime.strptime(end_hour, '%H').time()

	s_dtime = datetime.datetime.combine(start, s_time)
	e_dtime = datetime.datetime.combine(end, e_time)
	
	for i in range(len(HEP_proton_event_df)):
		if s_dtime <= (HEP_proton_event_df['start_time'][i] and HEP_proton_event_df['end_time'][i]) <= e_dtime:
			axes[length_data_list[j]].axvspan(HEP_proton_event_df['start_time'][i], HEP_proton_event_df['end_time'][i], color='skyblue', alpha=0.5)
			axes[length_data_list[j]].axvline(HEP_proton_event_df['start_time'][i], linewidth=1, zorder=2, color='royalblue', linestyle='-') #  xmin=0, xmax=1
			axes[length_data_list[j]].axvline(HEP_proton_event_df['end_time'][i], linewidth=1, zorder=2, color='royalblue', linestyle='-') #  xmin=0, xmax=1

	axes[length_data_list[j]].axhline(HEP_proton_threshold, linewidth=1, zorder=2, color='black', linestyle='-.', label=f'{round(HEP_proton_threshold, 3)} pfu' )# label=f'{HEP_proton_threshold} pfu') #  xmin=0, xmax=1
	


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

if HEPAD_save_option == 'yes':
	plt.savefig(f'HEPAD_events/HEPAD_event_{str(start)}_{str(end)}.png', format='png', dpi=900)

if event_option == 'yes':
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

if save_plot_option == 'yes' and len(option_bin_set) <= 4:
	# plt.savefig(f'xflare_events/bplot.png', format='png', dpi=900)
	plt.savefig(f'xflare_events/omni_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option == 'yes' and len(option_bin_set) > 4:
	plt.savefig(f'full_omni_plots/omni_full_test_{event_date}.png', format='png', dpi=900)

elif save_plot_option != 'yes':
	plt.show()







# ======= working with string_date_to_numeric
'''
# ======================== Modified Code for plotting, change things in here
import matplotlib.dates as mdate


f, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(8, 6))

def string_date_to_numeric(li):
    series = pd.Series(li)
    datetime = pd.to_datetime(series)
    numeric = pd.to_numeric(datetime)
    return numeric

x = string_date_to_numeric(rb_data.index)
# x = np.arange(0,len(rb_data.index))
y = full_freq
X, Y = np.meshgrid(x,y)
Xt = np.transpose(X)
Yt = np.transpose(Y)
# print(np.shape(Xt))
# print(X, Y)

# Z = rb_data[full_freq].values
z = rb_data[full_freq].values
Z = np.transpose(z)



s_time = datetime.datetime.strptime(start_hour, '%H').time()
e_time = datetime.datetime.strptime(end_hour, '%H').time()

s_dtime = datetime.datetime.combine(start, s_time)
e_dtime = datetime.datetime.combine(end, e_time)


# fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, figsize=(8, 6))
# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X,Y,Z, cmap=cm.viridis)


# ========= xray flux (ax1)
def flare_class(X):
	if X == 10**-4:
		return "X"
	#return ["%.3f" % z for z in V]

ax1.plot(string_date_to_numeric(xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), xray_df['B_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='0.1-0.8 nm', zorder=5)
ax1.plot(string_date_to_numeric(xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), xray_df['A_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='0.05-0.4 nm', zorder=5)
ax1.set_yscale('log')


flare_classes = ['', 'A', 'B', 'C', 'M', 'X']
ax7 = ax1.twinx()
ax7.set_yscale('log')
ax7.set_ylim(ax1.get_ylim())
ax7.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])
ax7.set_yticklabels(labels=flare_classes)
ax7.tick_params(axis='y', which='both', direction='in')

ax4.set_yticks([10**-9, 10**-8, 10**-7, 10**-6, 10**-5, 10**-4, 10**-3, 10**-2])

ax1.set_ylabel(f'Xray Flux\n [Wm$^2$]', fontname="Arial", fontsize = 12)


# ======= radio bursts (ax2)
from mpl_toolkits.axes_grid1 import make_axes_locatable

lower_bound = -10
upper_bound = 50

cf = ax2.contourf(X,Y,Z,40, vmin=lower_bound, vmax=upper_bound, cmap=cm.jet, levels=np.linspace(lower_bound,upper_bound,100), extend='max') # ["neither", "both", "min", "max"]
cax = f.add_axes([0.91, 0.55, 0.0125, 0.15]) # ([0.9, 0.1, 0.03, 0.8])
cb = f.colorbar(cf, cax=cax)

tick_locator = ticker.MaxNLocator(nbins=5)
cb.locator = tick_locator
cb.update_ticks()

'''
cbar_ax = f.add_axes([0.85, 0.15, 0.05, 0.7])
f.colorbar(cf, cax=cbar_ax)
'''

# plt.colorbar()
'''
divider = make_axes_locatable(ax2)
cax = divider.append_axes("right", size="5%", pad=0)

plt.colorbar(cf, cax=cax)
'''

ax2.set_yscale('log')
ax2.set_ylabel(f'Frequency\n [kHz]', fontname="Arial", fontsize = 12)


# ======= radio burst average (ax3)
ax3.plot(string_date_to_numeric(rb_data_df_interp.index), rb_data_df_interp['avg'], '.', mfc='none', color='blue', zorder=3)

for rbevent_no_interp in range(len(rb_list_event_interp)):
	for rbpoint_interp in rb_list_event_interp[rbevent_no_interp]:
		interp_x = string_date_to_numeric(rbpoint_interp)
		ax3.vlines(x=interp_x, ymin=t3_threshold_interp, ymax=rb_data_df_interp['avg'].loc[rbpoint_interp], linewidth=1, color='fuchsia', zorder=2)
	
'''
for i in range(len(rb_event_df)):
	if s_dtime <= (rb_event_df['start_time'][i] and rb_event_df['end_time'][i]) <= e_dtime:
		ax2.axvspan(rb_event_df['start_time'][i], rb_event_df['end_time'][i], color='lightblue', alpha=0.5)
	# axes[length_data_list[j]].axvspan(rb_event_df['start_time'].values, rb_event_df['end_time'].values, color='blue', alpha=0.5)
'''
'''
for i in range(len(rb_event_df)):
	ax2.axvspan(string_date_to_numeric(rb_event_df['start_time'][i]), string_date_to_numeric(rb_event_df['end_time'][i]), color='lightblue', alpha=0.5)
'''

ax3.axhline(t3_threshold, linewidth=1, zorder=1, color='red', linestyle='-', label=f'{t3_threshold} dB') #  xmin=0, xmax=1

for i in range(len(rb_event_df)):
	if s_dtime <= (rb_event_df_interp['start_time'][i] and rb_event_df_interp['end_time'][i]) <= e_dtime:
		ax3.axvline(string_date_to_numeric(rb_event_df_interp['start_time'][i]).values, linewidth=1, zorder=3, color='green', linestyle=':') #  xmin=0, xmax=1
ax3.set_ylabel(f'Averaged TIII\n Intensity [dB]', fontname="Arial", fontsize = 12)

# ======= Protons (ax4)
for i in energy_bin_list: # for i in sorted(energy_bin_list): # changed to unsorted because the sort queued off of 10 -> 100 -> 50 rather than 10 -> 50 -> 100
	ax4.plot_date(string_date_to_numeric(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],'.', mfc='none', color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True) , 
	# ax3.plot(proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], '.', mfc='none', color=f'{i[2]}', label= f'{i[1]}', zorder=5)#, logy=True)

color_tree = iter(cm.rainbow(np.linspace(0,1,10)))

if proton_event_option == 'smooth':
	ax4.plot(string_date_to_numeric(proton_smooth_df[f'{butter_filter}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].index), proton_smooth_df[f'{butter_filter}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='purple', linewidth=1, label=f'Butter-{butter_order}', zorder=5)

ax4.set_yscale('log')

ax4.set_ylabel(f'Proton Flux\n [pfu]', fontname="Arial", fontsize = 12)


s_time = datetime.datetime.strptime(start_hour, '%H').time()
e_time = datetime.datetime.strptime(end_hour, '%H').time()

s_dtime = datetime.datetime.combine(start, s_time)
e_dtime = datetime.datetime.combine(end, e_time)


for i in range(len(proton_event_df)):
	if s_dtime <= (proton_event_df['start_time'][i] and proton_event_df['end_time'][i]) <= e_dtime:
		# string_date_to_numeric(rb_event_df['start_time'][0]).values
		# ax3.axvspan(proton_event_df['start_time'][i], proton_event_df['end_time'][i], color='palegreen', alpha=0.5)
		ax4.axvline(string_date_to_numeric(proton_event_df['start_time'][i]).values, linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1
		# ax3.axvline(string_date_to_numeric(proton_event_df['end_time'][i]).values, linewidth=1, zorder=2, color='green', linestyle='-') #  xmin=0, xmax=1

# ax3.axvline(s_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1
# ax3.axvline(e_dtime, linewidth=1, zorder=2, color='green', linestyle=':') #  xmin=0, xmax=1


ax4.axhline(proton_threshold, linewidth=1, zorder=2, color='red', linestyle='-.', label=f'{round(proton_threshold, 3)} pfu') #  xmin=0, xmax=1 # threshold



# ===== vertical lines



'''
for i in range(len(rb_event_df)):
	print(f"Radio Burst Start Time ({rb_event_df['start_time'][i]}): ", string_date_to_numeric(rb_event_df['start_time'][i]))

print("=====================")

for i in range(len(proton_event_df)):
	print(f"Proton Start Time ({proton_event_df['start_time'][i]}): ", string_date_to_numeric(proton_event_df['start_time'][i]))
'''


'''
plt.xticks(x, rb_data.index, rotation='vertical')

spacing = 100
visible = ax.xaxis.get_ticklabels()[::spacing]
for label in ax.xaxis.get_ticklabels():
    if label not in visible:
        label.set_visible(False)
'''


# ax.set_xticklabels(rb_data.index)
# ax.xaxis.set_major_formatter(mdates.ticker.FixedFormatter(rb_data.index))

'''
# Get the current axis
ax = plt.gca()

# Only label every 20th value
ticks_to_use = rb_data.index[::20]

# Set format of labels (note year not excluded as requested)
labels = [ i.strftime("%-H:%M") for i in ticks_to_use ]

# Now set the ticks and labels
ax.set_xticks(ticks_to_use)
ax.set_xticklabels(labels)
'''

# ax.xaxis_date()
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Create your ticker object with M ticks
M = 20
xticks = ticker.MaxNLocator(M)

# Set the yaxis major locator using your ticker object. You can also choose the minor
# tick positions with set_minor_locator.
# ax1.xaxis.set_major_locator(xticks)
# ax.set_xticklabels(rb_data.index[::5, :])


# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# fig.autofmt_xdate()
# ax.xaxis.set_major_formatter(mdates.DateFormatter("%w %H:%M:%S"))
# ax.fmt_xdata = mdates.DateFormatter('%Y')

# ax1.yscale('log')

# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

# plt.tight_layout()

'''
axes[length_data_list[j]].set_xlabel('Time [UT]', fontname="Arial", fontsize = 12)

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax.xaxis.set_major_formatter(myFmt)

plt.suptitle(f'Space Weather Monitor\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14) #, y=1.04,
#plt.tight_layout()
'''

'''
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax = plt.gca()
ax4.xaxis.set_major_formatter(myFmt)
'''
ax_labels_numeric = ax4.get_xticks() * pow(10,-9)

ax_labels_datetime = []
for i in ax_labels_numeric:
	ax_labels_datetime.append(datetime.datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S'))# .strftime('%c'))

ax4.set_xticklabels(ax_labels_datetime)

plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)

plt.show()



# rb_data.to_csv("test_data.csv", sep=",")
# rb_data.plot.scatter(x=rb_data.index, y=data_rad1, c=rb_data.values)
sys.exit(0)
'''
