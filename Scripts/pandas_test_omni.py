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

#==============Choosing Dataset
print(f'{"="*40}\n{"=" + "DATASETS".center(38," ") + "="}\n{"="*40}\n1 - GOES-15 Proton Flux\n2 - Wind Type III Radio Bursts\n3 - Neutron Monitor Counts\n4 - ACE/Wind Solar Wind Speed\n{"="*40}')

'''
1 - GOES-15 Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
'''

#print('Choose Dataset(s) to Plot')

option_bin_set = set()
while True: # energy_bin != 'done':
	option_bin = input('Enter Dataset Option or "all": ')
	if option_bin != 'done':
		if option_bin == 'all':
			option_bin_set.add('1')
			option_bin_set.add('2')
			option_bin_set.add('3')
			option_bin_set.add('4')
			break
		
		elif int(option_bin) < 5:
			option_bin_set.add(option_bin)

			if len(option_bin_set) >= 4:
				break
	elif option_bin == 'done':
		break
'''
   		elif option_bin == '1':
   			option_bin_set.add('1')
   			continue
   		elif option_bin == '2':
   			option_bin_set.add('2')
   			continue
   		elif option_bin == '3':
   			option_bin_set.add('3')
   			continue
   		elif option_bin == '4':
   			option_bin_set.add('4')
   			continue
'''	

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

if int(start_year) < 2010:
	print('\nDATE ERROR: Date must start after September 1, 2010')
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


#=========== 1: GOES-15 Proton Flux
if '1' in option_bin_set:
	print(f'{"="*40}\n{"=" + "GOES-15 Proton Flux".center(38," ") + "="}\n{"="*40}')
	print(f'{"Energy Channels".center(7, " ")}\n{"-"*20}\n1: 6.5 MeV\n2: 11.6 MeV\n3: 30.6 MeV\n4: 63.1 MeV\n5: 165 MeV\n6: 433 MeV')
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
			proton_name = f'g15_epead_p27w_32s_{event_date}_{event_date}.csv'
			proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes15/csv/{proton_name}'
			proton_in = wget.download(proton_url)
	
			#name_list = ['datetime'] + [ str(i) for i in sorted_nm_list]
	
			dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
			proton_df_ind = pd.read_csv(f'{proton_in}', skiprows=282, date_parser=dateparse,index_col='time_tag', header=0)
			proton_df = proton_df.append(proton_df_ind)
	
			os.remove(proton_name)
		except:
			print(f'\nMissing data for {date}')
			continue
	
	proton_df.loc[proton_df['P2W_UNCOR_FLUX'] <= 0.0] = np.nan #6.5 MeV
	proton_df.loc[proton_df['P3W_UNCOR_FLUX'] <= 0.0] = np.nan #11.6 MeV
	proton_df.loc[proton_df['P4W_UNCOR_FLUX'] <= 0.0] = np.nan #30.6 MeV
	proton_df.loc[proton_df['P5W_UNCOR_FLUX'] <= 0.0] = np.nan #63.1 MeV
	proton_df.loc[proton_df['P6W_UNCOR_FLUX'] <= 0.0] = np.nan #165 MeV
	proton_df.loc[proton_df['P7W_UNCOR_FLUX'] <= 0.0] = np.nan #433 MeV



#=========== 2: Wind Type III Radio Burst
if '2' in option_bin_set:
	print(f'{"="*40}\n{"=" + "Wind Type III Radio Bursts".center(38," ") + "="}\n{"="*40}')
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
	print(f'{"="*40}\n{"=" + "Neutron Monitors".center(38," ") + "="}\n{"="*40}')
	
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
	#sorted_sorter = sorted(sorter.items(), key=operator.itemgetter(1))
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
	print(f'{"="*40}\n{"=" + "ACE/Wind Solar Wind Speed".center(38," ") + "="}\n{"="*40}')
	
	ace_data = pd.DataFrame([])
	wind_data = pd.DataFrame([])
	
	
	for date in daterange( start, end ):
		try:
			event_date = str(date).replace('-','')
	
			#====ACE
			swind_ace_name = f'ac_h0_swe_{event_date}_v10.cdf'
			swind_ace_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/{event_date[:4]}/{swind_ace_name}'
			swind_ace_in = wget.download(swind_ace_url)
	
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
					print(f'\nVERSION ERROR: The version v0{i} for WIND data does not exist, attempting v0{i+1}')
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



'''
#===========
print(f'{"="*40}\nGOES-15 Proton Flux\n{"="*40}')

#===========
print(f'{"="*40}\nGOES-15 Proton Flux\n{"="*40}')

#===========
print(f'{"="*40}\nGOES-15 Proton Flux\n{"="*40}')

'''


#===========Plotting (VERY BROKEN, DO NOT ATTEMPT TO RUN FROM HERE)
'''
1 - GOES-15 Proton Flux
2 - Wind Type III Radio Bursts
3 - Neutron Monitor Counts
4 - ACE/Wind Solar Wind Speed'
'''
'''
list_subplot = []
for i in sorted(option_bin_set):
	list_subplot.append(f'ax{i}')

# '1'
fig = plt.figure()
ax = fig.add_subplot(111)
rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax, color='navy', label= '20 kHz - 1040 kHz')


fig = plt.figure()
ax = fig.add_subplot(n+1, 1, n+1)
rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax, color='navy', label= '20 kHz - 1040 kHz')

n = len(fig.axes)
for i in range(n):
	fig.axes[i].change_geometry(n+1, 1, i+1)

ax = fig.add_subplot(n+1, 1, n+1)
for i in sorted(energy_bin_list):
	proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax, color=f'{i[2]}', label= f'{i[1]}', logy=True)

plt.show()
'''


#=====sol 2
'''
number_of_subplots=len(option_bin_set)

for i,v in enumerate(range(number_of_subplots)):
	v = v+1
	ax1 = plt.subplot(number_of_subplots,1,v)
	if '1' in option_bin_set and v == 1:
		rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax1, color='navy', label= '20 kHz - 1040 kHz')
	if '2' in option_bin_set and v == 2:
		for i in sorted(energy_bin_list):
			proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax1, color=f'{i[2]}', label= f'{i[1]}', logy=True)
	if '3' in option_bin_set and v == 3:
		color_count = []
		for i in sorted_nm_list:

			color_list = ['red','orange','green','blue','indigo','violet','purple'] #,'yellow'
			color_list = list(set(color_list) - set(color_count))

			rand_color = random.choice(color_list)
			color_count.append(rand_color)

			plt.plot(nm_data.index, nm_data[f'{i}'], color=rand_color, label=f'{i}')
	if '4' in option_bin_set and v == 4:
		plt.plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE')
		plt.plot(ace_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='ACE: H Bulk Speed')


plt.title(f'Solar Wind Bulk Flow Speed\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)

plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Speed [km/s]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='lower right')
plt.tight_layout()

ax = plt.gca()
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

ax.xaxis.set_major_formatter(myFmt)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
#ax.xaxis.set_major_formatter(myFmt)
plt.show()

'''
#======sol 3
f, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True, sharey=False) #plt.subplots(4, sharex=True, sharey=False)




rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax1, color='navy', label= '20 kHz - 1040 kHz')

for i in sorted(energy_bin_list):
	proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(ax=ax2, color=f'{i[2]}', label= f'{i[1]}', logy=True)

color_count = []
for i in sorted_nm_list:

	color_list = ['red','orange','green','blue','indigo','violet','purple'] #,'yellow'
	color_list = list(set(color_list) - set(color_count))

	rand_color = random.choice(color_list)
	color_count.append(rand_color)

	ax3.plot(nm_data.index, nm_data[f'{i}'], color=rand_color, label=f'{i}')

ax4.plot(wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='red', label='Wind: Ion Bulk Flow Speed GSE')
ax4.plot(ace_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'], color='blue', label='ACE: H Bulk Speed')


ax1.set_title(f'Solar Wind Bulk Flow Speed\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
ax4.grid(True)

plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Speed [km/s]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
#plt.grid(True)
#plt.yscale('log')
plt.legend(loc='lower right')
plt.tight_layout()

#ax = plt.gca()
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

ax4.xaxis.set_major_formatter(myFmt)
f.subplots_adjust(hspace=.15)

plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
#ax.xaxis.set_major_formatter(myFmt)
plt.show()



'''

#proton plotting



plt.title(f'GOES-15W Proton Flux\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)

#radio burst plotting




plt.title(f'WIND Type III Radio Bursts: RAD 1\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Intensity [sfu]', fontname="Arial", fontsize = 14)


#Neutron monitor plotting


#nm_data['RCORR_E'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='limegreen', label= 'Corrected for Efficiency')

plt.title(f'Neutron Monitor Data Corrected for Efficiency\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Counts/s', fontname="Arial", fontsize = 14)



#=========Solar Wind Plotting
print(f'\nPlotting Solar Wind Data: [{event_obj_start_str} -- {event_obj_end_str}]')


#ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='blue', label= 'ACE')
#wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='red', label= 'WIND')




plt.title(f'Solar Wind Bulk Flow Speed\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Speed [km/s]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='lower right')
plt.tight_layout()

ax = plt.gca()
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

ax.xaxis.set_major_formatter(myFmt)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
#ax.xaxis.set_major_formatter(myFmt)

plt.savefig('solarwind_test.png', format='png', dpi=900)
plt.show()
#plt.clf()
'''