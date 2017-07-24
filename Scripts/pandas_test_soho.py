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

#===========Specify energy range bins
print('Energy Channels\n======================\n1: 6.5 MeV\n2: 11.6 MeV\n3: 30.6 MeV\n4: 63.1 MeV\n5: 165 MeV\n6: 433 MeV')
soho_energy_bin_set = set()

while True: # energy_bin != 'done':
	soho_energy_bin = input('Enter Energy Channel(s) or "full": ')
	if soho_energy_bin != 'done':
		if soho_energy_bin == 'full':
			soho_energy_bin_set.add('1')
			soho_energy_bin_set.add('2')
			soho_energy_bin_set.add('3')
			soho_energy_bin_set.add('4')
			soho_energy_bin_set.add('5')
			soho_energy_bin_set.add('6')
			break
		if int(soho_energy_bin) < 7:
			soho_energy_bin_set.add(soho_energy_bin)
			#print(len(energy_bin_set))

			if len(soho_energy_bin_set) >= 6:
				#print('len very long')
				break
	elif soho_energy_bin == 'done':
		break

soho_energy_bin_list = []
for i in soho_energy_bin_set:
	if '1' in i:
		soho_energy_bin_list.append(['PH1','13 - 16 MeV', 'red'])
	elif '2' in i:
		soho_energy_bin_list.append(['PH5','32 - 40 MeV','orange'])
	elif '3' in i:
		soho_energy_bin_list.append(['PH7','50 - 64 MeV','green'])
	elif '4' in i:
		soho_energy_bin_list.append(['PH8','64 - 80 MeV','blue'])
	elif '5' in i:
		soho_energy_bin_list.append(['PH9','80 - 100 MeV','purple'])
	elif '6' in i:
		soho_energy_bin_list.append(['PH10','100 - 130 MeV','violet'])


soho_df = pd.DataFrame([])

for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		#print(event_date[0:6])
		#soho_name = f'https://srl.utu.fi/export/{event_date}_{event_date}.csv'
		#soho_url = f'https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/{event_date[:4]}/{event_date[4:6]}/goes15/csv/{proton_name}'
		soho_in = wget.download()
		soho_in = glob.glob(wget.download('http://srl.utu.fi/export/erne-1995.12.10-1996.01.31-36.tgz'))

sys.exit(0)
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

sys.exit(0)
#=========Proton flux
print(f'\nPlotting GOES-15W Proton Flux Data: [{event_obj_start_str} -- {event_obj_end_str}]')
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

color_count = []
for i in sorted(energy_bin_list):
	#color_list = ['red','orange','yellow','green','blue','purple'] #,'yellow'
	#color_list = list(set(color_list) - set(color_count))

	#rand_color = random.choice(color_list)
	#color_count.append(rand_color)

	proton_df[f'{i[0]}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=f'{i[2]}', label= f'{i[1]}')


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

plt.savefig('proton_remastered.png', format='png', dpi=900)
plt.show()
#plt.clf()