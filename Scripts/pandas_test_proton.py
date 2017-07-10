import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import wget
import os

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



#===========Define Paths
#full_proton_path_start = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/{start_date[0:6]}'
#full_proton_path_end = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/{end_date[0:6]}'
#full_proton_path = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/'



#===========Data


#radio_name = f'g15_epead_p27w_32s_{event_date}_{event_date}.csv'
#proton_url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/{event_date[:4]}/{radio_name}'
#proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{start_year}/{start_month}/goes15/csv/'
#proton_in = wget.download(proton_url)


proton_df = pd.DataFrame([])

for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		#print(event_date[0:6])
		proton_name = f'g15_epead_p27w_32s_{event_date}_{event_date}.csv'
		proton_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes15/csv/{proton_name}'
		proton_in = wget.download(proton_url)
		print(f'\nParsing GOES-15W Data for {date}')



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
proton_df.loc[proton_df['P7W_UNCOR_FLUX'] <= 0.0] = np.nan #165 MeV


#proton_time = pd.to_datetime(proton_df['time_tag']) #xray_time = xray_df[['time_tag']]

'''
proton_2W_flux = proton_df['P2W_UNCOR_FLUX']	#6.5 MeV
proton_3W_flux = proton_df['P3W_UNCOR_FLUX']	#11.6 MeV
proton_4W_flux = proton_df['P4W_UNCOR_FLUX']	#30.6 MeV
proton_5W_flux = proton_df['P5W_UNCOR_FLUX']	#63.1 MeV
proton_6W_flux = proton_df['P6W_UNCOR_FLUX']	#165 MeV
'''

event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H')

event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H')

#=========Proton flux
print(f'\nPlotting GOES-15W Proton Flux Data: [{event_obj_start_str} -- {event_obj_end_str}]')
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

#fig = plt.figure()
#ax = fig.add_subplot(111)

#plt.plot(proton_df.index, proton_2W_flux, '-', color='red', label= '6.5 MeV')
#plt.plot(proton_df.index, proton_3W_flux, '-', color='orange', label= '11.6 MeV')
#plt.plot(proton_df.index, proton_4W_flux, '-', color='green', label = '30.6 MeV')
#plt.plot(proton_df.index, proton_5W_flux, '-', color='blue', label= '63.1 MeV')
#plt.plot(proton_df.index, proton_6W_flux, '-', color='purple', label = '165 MeV')

proton_df['P2W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='red', label= '6.5 MeV')
proton_df['P3W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='orange', label= '11.6 MeV')
proton_df['P4W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='green', label = '30.6 MeV')
proton_df['P5W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='blue', label= '63.1 MeV')
proton_df['P6W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='purple', label = '165 MeV')
proton_df['P7W_UNCOR_FLUX'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color='violet', label = '433 MeV')



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

plt.savefig('proton.png', format='png', dpi=900)
plt.show()
#plt.clf()