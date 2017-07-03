import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import glob



#proton_path = 'Data/GOES_proton_flux'

start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter a end date (yyyymmdd): ')

def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )



#===========Define Paths
full_proton_path_start = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/{start_date[0:6]}'
full_proton_path_end = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/{end_date[0:6]}'
full_proton_path = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/original/Epead/'



#===========Data
start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )

proton_df = pd.DataFrame([])

for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		#print(event_date[0:6])
		proton_df_ind = pd.read_csv(f'{full_proton_path}/{event_date[0:6]}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
		proton_df = proton_df.append(proton_df_ind)
	except:
		print(f'Missing data for {date}')
		continue



''' #works for 2 files perfectly
for date in daterange( start, end ):
	try:
		event_date = str(date).replace('-','')
		print(event_date)
		#proton_df_ind = pd.read_csv(f'{proton_path}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
		if event_date[0:6] == start_date[0:6]:
			proton_df_ind = pd.read_csv(f'{full_proton_path_start}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
			proton_df = proton_df.append(proton_df_ind)
		elif event_date[0:6] != start_date[0:6]:
			proton_df_ind = pd.read_csv(f'{full_proton_path_end}/g15_epead_p27w_32s_{event_date}_{event_date}.csv', skiprows=282, header=0)
			proton_df = proton_df.append(proton_df_ind)
	except:
		print(f'Missing data for {date}')
		continue
'''
proton_df.loc[proton_df['P3W_UNCOR_FLUX'] <= 0.0] = np.nan #11.6 MeV
proton_df.loc[proton_df['P4W_UNCOR_FLUX'] <= 0.0] = np.nan #30.6 MeV
proton_df.loc[proton_df['P5W_UNCOR_FLUX'] <= 0.0] = np.nan #63.1 MeV
proton_df.loc[proton_df['P6W_UNCOR_FLUX'] <= 0.0] = np.nan #165 MeV

proton_time = pd.to_datetime(proton_df['time_tag']) #xray_time = xray_df[['time_tag']]

proton_3W_flux = proton_df['P3W_UNCOR_FLUX']	#11.6 MeV
proton_4W_flux = proton_df['P4W_UNCOR_FLUX']	#30.6 MeV
proton_5W_flux = proton_df['P5W_UNCOR_FLUX']	#63.1 MeV
proton_6W_flux = proton_df['P6W_UNCOR_FLUX']	#165 MeV

#=========xray flux
myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(proton_time, proton_3W_flux, '-', color='red', label= '11.6 MeV')
plt.plot(proton_time, proton_4W_flux, '-', color='orange', label = '30.6 MeV')
plt.plot(proton_time, proton_5W_flux, '-', color='green', label= '63.1 MeV')
plt.plot(proton_time, proton_6W_flux, '-', color='blue', label = '165 MeV')

plt.title('GOES-15 Proton Flux', fontname="Arial", fontsize = 14)
plt.xlabel('Time', fontname="Arial", fontsize = 14)
plt.ylabel('Flux [pfu]', fontname="Arial", fontsize = 14)
plt.minorticks_on()
plt.grid(True)
plt.yscale('log')
plt.legend(loc='lower right')
#plt.savefig('xray.pdf', format='pdf', dpi=900)
plt.tight_layout()


ax.xaxis.set_major_formatter(myFmt)

plt.show()
#plt.clf()