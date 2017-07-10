from spacepy import pycdf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import wget
import datetime
import os
import time


def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )


start_date = input('Enter start date (yyyymmdd): ')
start_day = start_date[6:8]
start_month = start_date[4:6]
start_year = start_date[:4]
start_minute = '00'

end_date = input('Enter a end date (yyyymmdd): ')
if end_date == '':
	end_date = start_date

end_day = end_date[6:8]
end_month = end_date[4:6]
end_year = end_date[:4]
end_minute = '00'

if start_year != end_year:
	print('\nDATE ERROR: Enter dates of the same year.')

if len(start_date) != 8 or len(end_date) != 8:
	print('\nDATE ERROR: Dates must have 8 digits.')
	sys.exit(0)

start_hour = input('Enter a start hour or "full": ').zfill(2)
if start_hour == '':
	start_hour = 'full'

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



event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H')

event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H')


start = datetime.date( year = int(f'{start_year}'), month = int(f'{start_month}') , day = int(f'{start_day}') )
end = datetime.date( year = int(f'{end_year}'), month = int(f'{end_month}') , day = int(f'{end_day}') )

start_time = time.clock()

#==========Data
radio_filename = f'wi_h1_wav_{start_date}_v01.cdf'

'''
radio_name_list = []
url_list = []
for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		radio_name_list.append(f'wi_h1_wav_{event_date}_v01.cdf')
		url_list.append(f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_filename}')
		#proton_df_ind = pd.read_csv(f'{full_proton_path}/{event_date[0:6]}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
		#proton_df = proton_df.append(proton_df_ind)
	except:
		print(f'Missing data for {date}')
		continue
'''

rb_data = pd.DataFrame([])

for date in daterange( start, end ):
	#try:
	event_date = str(date).replace('-','')
	radio_name = f'wi_h1_wav_{event_date}_v01.cdf'
	url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_name}'
	radio_in = wget.download(url)
	
	cdf = pycdf.CDF(radio_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')
	os.remove(radio_name)

	print(f'\nParsing Type III Data: [{event_obj_start_str} -- {event_obj_end_str}]')
	
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

		#proton_df_ind = pd.read_csv(f'{full_proton_path}/{event_date[0:6]}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
		#proton_df = proton_df.append(proton_df_ind)
'''
	except:
		print(f'Missing data for {date}')
		continue 
'''

#sys.exit(0)


#url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{start_year}/{radio_filename}'
#radio_in = wget.download(url)



'''
cdf = pycdf.CDF(radio_in) # cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')

os.remove(radio_filename)
print(f'\nParsing Type III Data: [{event_obj_start_str} -- {event_obj_end_str}]')

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

rb_data = pd.concat([data_time, data_rad1], axis=1)
rb_data.set_index(['date_time'], inplace=True)
'''
rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)

#=========Plotting
rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='navy', label= '20 kHz - 1040 kHz')
plt.title(f'WIND Type III Radio Bursts: RAD 1\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Intensity [sfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
#plt.yscale('log')
plt.legend(loc='upper right')
plt.tight_layout()
#ax = fig.add_subplot(111)
ax = plt.gca()
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

ax.xaxis.set_major_formatter(myFmt)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

end_time = time.clock()
print(f'Elapsed Time: {round(end_time - start_time , 2)} seconds')
plt.savefig('remastered_radio.png', format='png', dpi=900)

plt.show()

