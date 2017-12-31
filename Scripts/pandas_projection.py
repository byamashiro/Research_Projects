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


import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib.pyplot import cm

plt.close("all")


data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'

data = pd.read_csv(f'{data_directory}/Projection/location.csv', sep=',', comment='#')

proj_choice = ccrs.PlateCarree()




# ====== coordinates
west_limb_x = [90, 90]
west_limb_y = [-90, 90]

east_limb_x = [-90, -90]
east_limb_y = [-90, 90]

flare_lat_list = []
flare_long_list = []

for i in data['flare_location']:
	# print(i)
	try:
		flare_lat_temp = 0
		flare_long_temp = 0

		if i[0] == 'N':
			flare_lat_temp = int(i[1:3])
		elif i[0] == 'S':
			flare_lat_temp = -int(i[1:3])
		if i[3] == 'W':
			flare_long_temp = int(i[4:6])
		elif i[3] == 'E':
			flare_long_temp = -int(i[4:6])

		flare_lat_list.append(flare_lat_temp)
		flare_long_list.append(flare_long_temp)

	except:
		flare_lat_list.append(np.nan)
		flare_long_list.append(np.nan)
		# print("not working")

data['flare_lat'] = flare_lat_list
data['flare_long'] = flare_long_list


'''
# ==== start subplot
# ===== subplot methods
plt.figure(figsize = (8, 6))

proj_choice = ccrs.PlateCarree()


# scatter
ax1 = plt.subplot(2, 1, 1, projection=proj_choice)
ax1.set_extent((-180, 180, -90, 90)) # crs=ccrs.PlateCarree()
scatter1 = ax1.scatter(data['flare_long'], data['flare_lat'], c=data['goes_max_proton'], cmap='viridis', transform=ccrs.Geodetic(), zorder=3)
# gridlines
gl = ax1.gridlines(crs=proj_choice, draw_labels=True, zorder=2)
gl.xlabels_top = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.colorbar(scatter1)
# Limb lines
ax1.plot(west_limb_x, west_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
ax1.plot(east_limb_x, east_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
ax1.set_title('connectivity')

# scatter
ax2 = plt.subplot(2, 1, 2, projection=proj_choice)
ax2.set_extent((-180, 180, -90, 90)) # crs=ccrs.PlateCarree()
scatter2 = ax2.scatter(data['flare_long'], data['flare_lat'], c=data['fluence'], cmap='viridis', transform=ccrs.Geodetic(), zorder=3)
# gridlines
gl = ax2.gridlines(crs=proj_choice, draw_labels=True, zorder=2)
gl.xlabels_top = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.colorbar(scatter2)
# Limb lines
ax2.plot(west_limb_x, west_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
ax2.plot(east_limb_x, east_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
ax2.set_title('fluence')


# # scatter
# ax3 = plt.subplot(2, 1, 2, projection=proj_choice)
# ax3.set_extent((-180, 180, -90, 90)) # crs=ccrs.PlateCarree()
# scatter3 = ax3.scatter(data['flare_long'], data['flare_lat'], c=data['connectivity'], cmap='viridis', transform=ccrs.Geodetic(), zorder=3)
# # gridlines
# gl = ax3.gridlines(crs=proj_choice, draw_labels=True, zorder=2)
# gl.xlabels_top = False
# gl.xformatter = LONGITUDE_FORMATTER
# gl.yformatter = LATITUDE_FORMATTER
# plt.colorbar(scatter3)
# # Limb lines
# ax3.plot(west_limb_x, west_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
# ax3.plot(east_limb_x, east_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
# ax3.set_title('protons')



plt.show()

sys.exit(0)
'''

# ======== single plot, working
proj_choice = ccrs.PlateCarree() # Mollweide is the closest to aitoff
plt.figure(figsize=(12,6))
ax = plt.axes(projection=proj_choice) # PlateCarree and Mercator have functioning gridlines
# ax.stock_img()
plt.title('Plate Carree Projection')
gl = ax.gridlines(crs=proj_choice, draw_labels=True, zorder=2)
gl.xlabels_top = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
#plt.plot([ny_lon, delhi_lon], color='gray', transform=ccrs.PlateCarree())
color_cm=iter(cm.viridis(np.linspace(0,int(data['fluence'].min()), int(data['fluence'].max())  ) ) )

ax.set_extent((-180, 180, -90, 90)) # crs=ccrs.PlateCarree()
ax.plot(west_limb_x, west_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)
ax.plot(east_limb_x, east_limb_y, transform=ccrs.PlateCarree(), color='black', lw=3)


scatter = ax.scatter(data['flare_long'], data['flare_lat'], c=data['connectivity'], cmap='viridis', transform=ccrs.Geodetic(), zorder=3)
plt.colorbar(scatter)
plt.xlabel("Longitude")
# for i in range(len(data)):
	# color_choice = next(color_cm)
	#ax.plot(data['flare_long'][i], data['flare_lat'][i], 'o', transform=ccrs.Geodetic(), color=color_choice, markersize=2, zorder=3) # longitude and latitude #ccrs.PlateCarree() color=color_choice

# plt.colorbar()
# plt.savefig('/Users/bryanyamashiro/Documents/Research_Projects/Scripts/map_test/projection_test.png', format='png', dpi=900)

plt.show()

sys.exit(0)


'''
for i in range(len(data_df)):
	color_choice = next(color_cm)
	axes[length_data_list[j]].plot(list(data_df['long'])[i],list(data_df['lat'])[i], 'o', color='red', transform=ccrs.Geodetic(), markersize=2, zorder=3)
	axes[length_data_list[j]].plot([list(data_df['city_long_in'])[i],list(data_df['city_long_out'])[i]] , [list(data_df['city_lat_in'])[i],list(data_df['city_lat_out'])[i]] , color=color_choice, linewidth=1,marker='o', markersize=1, transform=ccrs.Geodetic(), zorder=4) # , marker='.'
'''



fig = plt.figure("example", figsize=(10,5))
ax = fig.add_subplot(111, projection="aitoff")
ax.plot(1.0, 1.0, 'k*', markersize = 15, color='blue')
# ax.title("Aitoff")
ax.grid(True)
plt.show()

sys.exit(0)


# ======= Parameters to set
data_directory = '/Users/bryanyamashiro/Documents/Research_Projects/Data'
save_option = 'yes' # either 'yes' or 'no'
plot_option = 'yes'
unique_inclusion_option = 'yes'


# ==== Must change for different energies
energy_parse = int(input("Enter the energy channel (10/50/100): ")) # MeV
if energy_parse != 10:
	if energy_parse != 50:
		if energy_parse != 100:
			print("Please enter a valid energy channel: 10, 50, or 100.")
			sys.exit(0)


if energy_parse == 100:
	detection_threshold = 0.25 # 0.25
	detection_threshold_str = '0d25' # 0.50
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
	year_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

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
			plt.axhline(0.25, color='green', linestyle='--', label='100 MeV', zorder = 1)
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

