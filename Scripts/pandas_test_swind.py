import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os
import random

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )


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

#===========Data

#swind_ace_df = pd.DataFrame([])
#swind_wind_df = pd.DataFrame([])


for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')

		#====ACE
		swind_ace_name = f'ac_h0_swe_{event_date}_v10.cdf'
		swind_ace_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/2011/{swind_name}'
		swind_ace_in = wget.download(swind_ace_url)

		swind_ace_cdf = pycdf.CDF(swind_ace_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
		os.remove(swind_ace_name)
	
		#print(f'\nParsing Type III Data for {date}')
		
		time_ace_swind = []
		for i in cdf['Epoch']:
			time_ace_swind.append(i)
		
		bulk_ace_vel = []
		for i in cdf['Vp']:
			bulk_ace_vel.append(i)

		data_ace_time = pd.DataFrame(time_ace_swind)
		data_ace_time.columns = ['date_time']
		
		bulk_ace_vel = pd.DataFrame(bulk_ace_vel)
		bulk_ace_vel.columns = ['ace_bulk_vel']
		
		ace_concat = pd.concat([data_time, ace_bulk_vel], axis=1)
		#rb_concat.set_index(['date_time'], inplace=True)
	
		ace_data = ace_data.append(ace_concat)

		#====WIND
		swind_wind_name = f'wi_h1_swe_{event_date}_v01.cdf	'
		swind_wind_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/2011/{swind_name}'
		swind_wind_in = wget.download(swind_wind_url)

		swind_wind_cdf = pycdf.CDF(swind_wind_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
		os.remove(swind_wind_name)
	
		#print(f'\nParsing Type III Data for {date}')
		
		time_wind_swind = []
		for i in cdf['Epoch']:
			time_wind_swind.append(i)
		
		bulk_wind_vel = []
		for i in cdf['Vp']:
			bulk_wind_vel.append(i)

		data_wind_time = pd.DataFrame(time_wind_swind)
		data_wind_time.columns = ['date_time']
		
		bulk_wind_vel = pd.DataFrame(bulk_wind_vel)
		bulk_wind_vel.columns = ['wind_bulk_vel', 'longitude', 'latitude']
		
		wind_concat = pd.concat([data_time, wind_bulk_vel], axis=1)
		#rb_concat.set_index(['date_time'], inplace=True)
	
		wind_data = wind_data.append(wind_concat)

	except:
		print(f'\nMissing data for {date}')
		continue


ace_data.loc[wind_data['ace_bulk_vel'] <= 0.0] = np.nan #6.5 MeV
wind_data.loc[wind_data['wind_bulk_vel'] <= 0.0] = np.nan #6.5 MeV


event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H')

event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H')

#=========Proton flux
print(f'\nPlotting GOES-15W Proton Flux Data: [{event_obj_start_str} -- {event_obj_end_str}]')
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
'''
color_count = []
for i in sorted(energy_bin_list):
	color_list = ['red','orange','yellow','green','blue','purple'] #,'yellow'
	color_list = list(set(color_list) - set(color_count))

	rand_color = random.choice(color_list)
	color_count.append(rand_color)

	ace_data[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=rand_color, label= f'{i[1]}')

'''
ace_data['ace_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=blue, label= 'ACE')
wind_data['wind_bulk_vel'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=red, label= 'WIND')

plt.title(f'GOES-15W Proton Flux\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
plt.yscale('log')
plt.legend(loc='lower right')
plt.tight_layout()

ax = plt.gca()
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

ax.xaxis.set_major_formatter(myFmt)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
#ax.xaxis.set_major_formatter(myFmt)

#plt.savefig('proton_remastered.png', format='png', dpi=900)
plt.show()
#plt.clf()