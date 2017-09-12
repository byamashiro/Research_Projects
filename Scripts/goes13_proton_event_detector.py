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

import calendar

import shutil


# ======= Parameters to set
data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # either 'yes' or 'no'
plot_option = 'yes'

detection_threshold = 0.25


# ================ 


detection_year = input("Enter year to parse (yyyy) or 'all': ").lower()
if detection_year == 'all':
	year_list = []
	year_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
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
			
				for i in proton_df[proton_df['ZPGT100W'] > detection_threshold].index:
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

	print(f'\n{"=" * 60}')
	print(f'GOES-13 Events ({detection_year}): {sorted(list(event_set_13))}')
	print(f'--GOES-13 Unique Events ({detection_year}): {sorted(list(event_set_13.difference(event_set_15)))}')
	
	print(f'\nGOES-15 Events ({detection_year}): {sorted(list(event_set_15))}')
	print(f'--GOES-15 Unique Events ({detection_year}): {sorted(list(event_set_15.difference(event_set_13)))}')
	print('=' * 60)
	
	print(f'\nShared Events ({detection_year}): {sorted(list(event_set_13.intersection(event_set_15)))}')
	
if len(year_list) > 1:
	

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
	full_event = []
	full_year = []
	for i in sorted(list(year_set_13.intersection(year_set_15))):
		if len(full_event) == 0:
			full_event.append(i)

		elif len(full_event) >= 1:

				# full_event.append(i)
			if int(i) == int(full_event[-1]) + 1:
				full_event.append(i)
			elif int(i) != int(full_event[-1]) + 1:
				# print(i , " ", int(full_event[-1]), " ", int(full_event[-1]) + 1)
				full_year.append(full_event)
				full_event = []
				full_event.append(i)

	if len(full_event) != 0:
		full_year.append(full_event)


if plot_option == 'yes':
	print('Plotting all proton events.')
	# if os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{sat}/{detection_year}/{proton_name}')
	for event_day in (full_year):
		plt.close("all")
		plt.figure(figsize=(10,6))
	
		for sat in ['13','15']:
	
			f_l_day = calendar.monthrange(int(f'{event_day[0][:4]}'), int(f'{event_day[0][4:6]}'))
	
			event_f_day = str(f'{event_day[0][:4]}{str(event_day[0][4:6]).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
			event_l_day = str(f'{event_day[0][:4]}{str(event_day[0][4:6]).zfill(2)}{str(f_l_day[1]).zfill(2)}')
	
			proton_name = f'g{sat}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
			# proton_check = os.path.isfile(f'{data_directory}/GOES_Detection/GOES_{sat}/{detection_year}/{proton_name}')
	
			proton_df = pd.read_csv(f'{data_directory}/GOES_Detection/GOES_{sat}/{event_day[0][:4]}/{proton_name}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
			proton_df.loc[proton_df['ZPGT100W'] < 0.0] = np.nan
			if sat == '13':
				col_def = 'blue'
			elif sat == '15':
				col_def = 'red'
	
			plt.plot(proton_df['ZPGT100W'].loc[f'{event_day[0]}':f'{event_day[-1]}'], label = f'GOES-{sat} >100 MeV', color=col_def)
	
		myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
		ax = plt.gca()
		ax.xaxis.set_major_formatter(myFmt)
	
		plt.axhline(detection_threshold, zorder = 1)
		plt.yscale('log')
		plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
		plt.minorticks_on()
		plt.grid(True)
		plt.legend(loc='upper right', ncol=1,fontsize=8)
	
		plt.suptitle(f'Proton Event Detector\n[{event_day[0]} -- {event_day[-1]}] (Threshold : {detection_threshold} pfu)', fontname="Arial", fontsize = 14) #, y=1.04,
		plt.ylabel('Proton Flux [pfu]', fontname="Arial", fontsize = 12)
		plt.xlabel('Time [UT]', fontname="Arial", fontsize = 12)
	
	
		#plt.show()
		plt.savefig(f'detected_events/detected_event_{event_day[0]}.png', format='png', dpi=900)
		#sys.exit(0)



'''
date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		f_l_day = calendar.monthrange(int(detection_year), int(i))

		event_f_day = str(f'{date.year}{str(date.month).zfill(2)}01') # {str(f_l_day[0]).zfill(2)}
		event_l_day = str(f'{date.year}{str(date.month).zfill(2)}{str(f_l_day[1]).zfill(2)}')


		#print(event_date[0:6])
		# proton_name = f'g{satellite_no}_epead_p27w_32s_{event_date}_{event_date}.csv'
		proton_name = f'g{satellite_no}_epead_cpflux_5m_{event_f_day}_{event_l_day}.csv' #g13_epead_cpflux_5m_20110101_20110131.csv
		proton_check = os.path.isfile(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}')

		if proton_check == True:
			dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
			proton_df_ind = pd.read_csv(f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/{proton_name}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
			proton_df = proton_df.append(proton_df_ind)

		elif proton_check == False:
			# proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
			# proton_in = wget.download(proton_url)

			
			# [i for i in range(len(proton_df.columns)) if i]

			for i in proton_df.columns:
				if i != 'ZPGT100W':
					proton_df.drop(f'{i}', inplace=True, axis=1)

			proton_df.loc[proton_df['ZPGT100W'] < 0.0] = np.nan

			print(proton_df.loc[proton_df['ZPGT100W'] > 1.0] )

			for i in proton_df[proton_df['ZPGT100W'] > 1.0].index:
				# print(str(i)[:10].replace('-',''))
				event_set.add(str(i)[:10].replace('-',''))
					

			# print(proton_df.loc[proton_df['ZPGT100W'] > 1.0]) #check if value is over 1

			
			# for i in proton_df.values:
			#	if i >= 1.0:
			#		print()
			



			
			# for i in range(len(proton_df)):
			#	if proton_df['ZPGT100W'][i] < 0.0:
			#		print(proton_df.iloc[i])
			
			# proton = proton_df['ZPGT100W']
			# proton_df = pd.DataFrame([])
			# del proton_df

			# proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
			# proton_df = proton_df.append(proton_df_ind) # appends for all dates, keep if want a year long memory file
			if save_option == 'yes':
				shutil.move(f'{proton_name}', f'{data_directory}/GOES/GOES_{satellite_no}/Pflux/')
			elif save_option == 'no':
				os.remove(proton_name)
	
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