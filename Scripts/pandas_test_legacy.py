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


def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

#==============Choosing Dataset
print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-8,10 Proton Flux (1995-Present)\n2 - Wind Type III Radio Bursts (1994-Present)\n3 - Neutron Monitor Counts\n4 - ACE/Wind Solar Wind Speed (1998-Present)/(1994-Present)\n5 - GOES-8,10 Xray Flux (1995-Present)\n{"="*40}')

'''
1 - GOES-15 Proton Flux (1995-Present)
2 - Wind Type III Radio Bursts (1994-Present)
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed' (1998-Present)/(1994-Present)
5 - GOES-15 Xray Flux
'''


option_bin_set = set()
while True: # energy_bin != 'done':
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

if int(start_year) >= 2010: # testing old 2003 data, uncomment laterß
	print('\nDATE ERROR: Date must start before 2010')
	sys.exit(0)

if int(start_year) < 1995: # testing old 2003 data, uncomment laterß
	print('\nDATE ERROR: Date must start after 1995')
	sys.exit(0)


if len(start_date) != 8 or len(end_date) != 8:
	print('\nDATE ERROR: Dates must have 8 digits.')
	sys.exit(0)

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


#=========== 1: Legacy GOES Proton Flux
if '1' in option_bin_set:
	month_final = last_day_of_month(start)
	month_final_str = datetime.datetime.strftime(month_final, '%Y%m%d')
	print(f'{"="*40}\n{"=" + "GOES Satellites".center(38," ") + "="}\n{"="*40}\n1 - GOES-8 (1995 - 1998)\n2 - GOES-10 (1999 - 2009)\n3 - GOES-13 (2010 - Present) DO NOT USE!\n{"="*40}')
	satellite_no = input('Enter GOES Satellite Option: ')
	if satellite_no == '1':
		satellite_no = '08'
	if satellite_no == '2':
		satellite_no = '10'


	print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Time Averaged Proton Flux".center(38," ") + "="}\n{"="*40}')
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
			proton_name = f'g{satellite_no}_eps_1m_{start_date[:6]}01_{month_final_str}.csv' # need to change the final date {event_date}
			#g10_eps_1m_{event_date}_20031031.csv
			proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
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
for date in daterange( start, end ):
	event_date = str(date).replace('-','')
	#print(event_date[0:6])
	proton_name = f'g{satellite_no}_eps_1m_{start_date[:6]}01_{last_day_of_month(start)}.csv' # need to change the final date {event_date}
	#g10_eps_1m_{event_date}_20031031.csv
	proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{proton_name}'
	#https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes10/csv/
	proton_in = wget.download(proton_url)
	#name_list = ['datetime'] + [ str(i) for i in sorted_nm_list]
	dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
	proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=214, date_parser=dateparse,index_col='time_tag', header=0)
	proton_df = proton_df.append(proton_df_ind)
	os.remove(proton_name)
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
			radio_name = f'wi_h1_wav_{event_date}_v01.cdf'
			url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_name}'
			radio_in = wget.download(url)
			
			cdf = pycdf.CDF(radio_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
			os.remove(radio_name)
		
			print(f'\nParsing Type III Data for {date}')
			
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
		except:
			print(f'\nMISSING DATA FOR: {date}\n')
			continue
	
	rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)


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
			for i in range(6,10):
				try:
					swind_ace_name = f'ac_h0_swe_{event_date}_v0{i}.cdf'
					swind_ace_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/{event_date[:4]}/{swind_ace_name}'
					swind_ace_in = wget.download(swind_ace_url)
				except error.HTTPError as err:
					#print(f'\nVERSION ERROR: The version v0{i} for WIND data does not exist, attempting v0{i+1}')
					continue
				else:
					break


			#swind_ace_name = f'ac_h0_swe_{event_date}_v10.cdf'
			#swind_ace_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/{event_date[:4]}/{swind_ace_name}'
			#swind_ace_in = wget.download(swind_ace_url)
	
			swind_ace_cdf = pycdf.CDF(swind_ace_name) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
			os.remove(swind_ace_name)
				
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
					swind_wind_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_k0/{event_date[:4]}/{swind_wind_name}'
					swind_wind_in = wget.download(swind_wind_url)
				except error.HTTPError as err:
					#print(f'\nVERSION ERROR: The version v0{i} for WIND data does not exist, attempting v0{i+1}')
					continue
				else:
					break
	
	
			swind_wind_cdf = pycdf.CDF(swind_wind_name) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
			os.remove(swind_wind_name)
				
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
	print(f'\n{"="*40}\n{"=" + f"GOES-{satellite_no} Time Averaged Xray Flux".center(38," ") + "="}\n{"="*40}')

	month_final = last_day_of_month(start)
	month_final_str = datetime.datetime.strftime(month_final, '%Y%m%d')
	print(f'{"="*40}\n{"=" + "GOES Satellites".center(38," ") + "="}\n{"="*40}\n1 - GOES-8 (1995 - 1998)\n2 - GOES-10 (1999 - 2009)\n3 - GOES-13 (2010 - Present) DO NOT USE!\n{"="*40}')
	satellite_no = input('Enter GOES Satellite Option: ')
	if satellite_no == '1':
		satellite_no = '08'
	if satellite_no == '2':
		satellite_no = '10'


	xray_df = pd.DataFrame([])
	
	for date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')

			#xray_name = f'g15_xrs_2s_{event_date}_{event_date}.csv'
			#xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes15/csv/{xray_name}'

			xray_name = f'g{satellite_no}_xrs_1m_{start_date[:6]}01_{month_final_str}.csv' # need to change the final date {event_date}
			xray_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/{event_date[:4]}/{event_date[4:6]}/goes{satellite_no}/csv/{xray_name}'



			xray_in = wget.download(xray_url)
	
			xray_name_list = ['time_tag','A_FLUX','B_FLUX']
	
			dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
			xray_df_ind = pd.read_csv(f'{xray_in}', skiprows=120, names=xray_name_list, date_parser=dateparse,index_col='time_tag', header=0) # 138 for 20120307
			xray_df = xray_df.append(xray_df_ind)
	
			os.remove(xray_name)
		except:
			print(f'\nMissing data for {date}')
			continue
	
	xray_df.loc[xray_df['A_FLUX'] < 0.0] = np.nan #6.5 MeV
	xray_df.loc[xray_df['B_FLUX'] < 0.0] = np.nan #11.6 MeV




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
