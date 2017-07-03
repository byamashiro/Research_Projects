import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import sys
import time


start_date = input('Enter a start date (yyyymmdd): ')
end_date = input('Enter a end date (yyyymmdd): ')
if end_date == '':
	end_date = start_date


if len(start_date) != 8 or len(end_date) != 8:
	print('\nDATE ERROR: Dates must have 8 digits.')
	sys.exit(0)


event_start = input('Enter a start hour or "full": ').zfill(2)
if event_start.isdigit() == True:
	event_end = input('Enter a end hour: ').zfill(2)
	if start_date == end_date:
		if (int(event_end) - int(event_start)) < 0:
			print('\nTIME ERROR: Difference between two hours must be greater than zero.')
			sys.exit(0)
	elif int(event_end) > 24 or int(event_start) > 23:
		print('\nTIME ERROR: Hours must be between 0 and 23.')
		sys.exit(0)

if event_start.isdigit() == False:
	if event_start == 'full':
		event_start = '00'.zfill(2)
		event_end = '23'.zfill(2)
	else:
		print('\nTIME ERROR: Not a valid alternative hour.')
		sys.exit(0)


event_obj_start = datetime.datetime.strptime(f'{start_date} {event_start}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')

event_obj_end = datetime.datetime.strptime(f'{end_date} {event_end}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')

print(f'Parsing Type III Data: [{event_obj_start_str} -- {event_obj_end_str}]')



def daterange( start_date, end_date ):
    if start_date <= end_date: #
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )


start_time = time.clock()
#===========Define Paths
full_radio_path_start = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original/{start_date[0:6]}'
full_radio_path_end = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original/{end_date[0:6]}'
full_radio_path = f'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/original'



#===========Data input
start = datetime.date( year = int(f'{start_date[0:4]}'), month = int(f'{start_date[4:6]}') , day = int(f'{start_date[6:8]}') )
end = datetime.date( year = int(f'{end_date[0:4]}'), month = int(f'{end_date[4:6]}') , day = int(f'{end_date[6:8]}') )


radio_df = pd.DataFrame([])

event_date_start = str(start).replace('-','')
event_date_end = str(end).replace('-','')
list_header = [str(i) for i in range(12,1041,4)]

dateparse = lambda x: pd.datetime.strptime(x, '%d-%m-%Y %H:%M:%S.%f')

radio_df = pd.read_csv(f'{full_radio_path}/wind{event_date_start[0:6]}.txt',engine = 'python',delim_whitespace=True ,skiprows=40, names=list_header, skipfooter=3, parse_dates=[['12', '16']], date_parser=dateparse, index_col='12_16',keep_date_col=True, na_filter = False) #, header=0)
radio_df['avg'] = radio_df.mean(axis=1, numeric_only=True)

#====Plotting

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')

radio_df['avg'].loc[f'{event_date_start} {event_start}':f'{event_date_end} {event_end}'].plot(color='blue', label= '20 kHz - 1040 kHz')
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
ax.xaxis.set_major_formatter(myFmt)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')


end_time = time.clock()
print(f'Elapsed Time: {round(end_time - start_time , 2)} seconds')

plt.savefig('radio.pdf', format='pdf', dpi=900)
plt.show()
