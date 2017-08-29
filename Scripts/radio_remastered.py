from spacepy import pycdf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys
import wget
import datetime
import os
import time
import numpy as np


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
#start_minute = '00'

end_date = input('Enter a end date (yyyymmdd): ')
if end_date == '':
	end_date = start_date

end_day = end_date[6:8]
end_month = end_date[4:6]
end_year = end_date[:4]
#end_minute = '00'

if start_year != end_year:
	print('\nDATE ERROR: Enter dates of the same year.')

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



event_obj_start = datetime.datetime.strptime(f'{start_date} {start_hour}', '%Y%m%d %H')
event_obj_start_str = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H:%M:%S')
event_obj_start_str_date = datetime.datetime.strftime(event_obj_start, '%Y%m%d %H')

event_obj_end = datetime.datetime.strptime(f'{end_date} {end_hour}', '%Y%m%d %H')
event_obj_end_str = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H:%M:%S')
event_obj_end_str_date = datetime.datetime.strftime(event_obj_end, '%Y%m%d %H')


start = datetime.date( year = int(f'{start_year}'), month = int(f'{start_month}') , day = int(f'{start_day}') )
end = datetime.date( year = int(f'{end_year}'), month = int(f'{end_month}') , day = int(f'{end_day}') )

#start_time = time.clock()

#==========Data
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

#=========Plotting
print(f'\nPlotting Type III Data: [{event_obj_start_str} -- {event_obj_end_str}]')
print('1: Full dataset\n2: Individual subplots (DO NOT USE)\n3: Averaged dataset')
plot_choice = input('Enter choice for plotting: ')

# =============== new plotting scheme subplots

# ========= one subplot for every 16 frequencies (total 256 frequencies)

if plot_choice == '1':
	from matplotlib.pyplot import cm
	import seaborn as sns


	myFmt = mdates.DateFormatter('%m/%d %H:%M')


	fig, axs = plt.subplots(4, 4, sharex = True, sharey = True, figsize=(12, 7))
	row_count = 0
	col_count = 0
	single_count = 0
	list_freq = []
		
	color_cm=iter(cm.viridis(np.linspace(0,1, 256 )))

	for i in range(20, 1041, 4):
		color_choice = next(color_cm)
		list_freq.append(i)

		axs[row_count, col_count].plot(rb_data[i].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],color=color_choice, label= f'{i}', zorder=3) # axs[row, column]
		

		single_count += 1

		if single_count == 16:

			min_freq = min(list_freq)
			max_freq = max(list_freq)
			axs[row_count, col_count].plot(rb_data['avg'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],color='black', linewidth=1, zorder=2)

			axs[row_count, col_count].legend(labels=[f'{min_freq} - {max_freq} kHz'], loc='upper right', ncol=3,fontsize=8)
			axs[row_count, col_count].grid(True)
			axs[row_count, col_count].minorticks_on()
			# axs[row_count, col_count].locator_params(axis='x',tight=True, nbins=4)


			single_count = 0
			list_freq = []
			col_count += 1
			if col_count == 4:
				row_count += 1
				col_count = 0


	plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
	fig.text(0.06, 0.5, 'Type III Radio Burst Intensity [sfu]', ha='center', va='center', rotation='vertical', fontname="Arial", fontsize = 12)

	plt.suptitle(f'WIND Type III Radio Bursts: RAD 1\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
	plt.xlabel('Time (UT)', fontname="Arial", fontsize = 12)


	ax = plt.gca()
	ax.xaxis.set_major_formatter(myFmt)
	
	#plt.locator_params(axis='x', nbins=5)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
	fig.autofmt_xdate()
	plt.savefig('remastered_radio_full.png', format='png', dpi=900)
	
	
	plt.show()

if plot_choice == '7':
	from matplotlib.pyplot import cm
	import seaborn as sns


	myFmt = mdates.DateFormatter('%m/%d %H:%M')
	fig, ax = plt.subplots(figsize = (12, 7))
	rb_data.drop('avg', axis=1, inplace=True)
	# plt.pcolormesh(rb_data.index, rb_data.columns, rb_data)
	radio_plot = ax.pcolormesh(rb_data.T, cmap=cm.rainbow)

	plt.colorbar(radio_plot)
	radio_plot.set_clim(vmin=-10, vmax=30)
	plt.show()




	''' # works but make a better solution
	fig, ax = plt.subplots(figsize=(12, 7))
	rb_data.drop('avg', axis=1, inplace=True)
	ax = sns.heatmap(rb_data.loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].T, cmap=cm.viridis)
	plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
	fig.autofmt_xdate()
	# plt.yscale('log')
	# plt.gca().invert_yaxis()

	for item in ax.get_yticklabels():
		item.set_rotation(0)

	# ax.xaxis.set_major_formatter(myFmt)
	plt.tight_layout()
	#plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

	# plt.title(f'WIND Type III Radio Bursts: RAD 1\n[{event_obj_start_str} -- {event_obj_end_str}]', fontname="Arial", fontsize = 14)
	# plt.xlabel('Time', fontname="Arial", fontsize = 14)
	# plt.ylabel('Intensity [sfu]', fontname="Arial", fontsize = 14)
	# plt.minorticks_on()
	# plt.grid(True)
	# #plt.yscale('log')
	# plt.legend(loc='upper right')
	# plt.tight_layout()
	# #ax = fig.add_subplot(111)
	# ax = plt.gca()
	# myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
	# ax.xaxis.set_major_formatter(myFmt)
	# plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')
	# #end_time = time.clock()
	# #print(f'Elapsed Time: {round(end_time - start_time , 2)} seconds')
	# #plt.savefig('remastered_radio_waves.png', format='png', dpi=900)
	plt.show()

	'''


# ====== individual subplots
if plot_choice == '2':
	from matplotlib.pyplot import cm 

	myFmt = mdates.DateFormatter('%m/%d\n%H:%M')


	wrange = range(20, 1041, 4) 
	
	fig, axs = plt.subplots(6, 5, sharex = True, sharey = True)
	
	row_count = 0
	col_count = 0
	

	color_cm=iter(cm.rainbow(np.linspace(0,1, len(range(20,980,32)) )))


	# one subplot for each frequency

	for i in range(20,980,32): # total of 256 different frequencies
		color_choice = next(color_cm)

		axs[row_count, col_count].plot(rb_data[i].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'],color=color_choice, label= f'{i}') # axs[row, column]
		axs[row_count, col_count].legend(loc='upper right', ncol=1,fontsize=8)


		col_count += 1
		if col_count == 6:
			row_count += 1
			col_count = 0

	# plt.xaxis.set_major_formatter(myFmt)
	plt.subplots_adjust(wspace = 0, hspace = 0, top=0.91)
	plt.show()












# ============== end new plotting scheme
if plot_choice == '3': 
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
	
	#end_time = time.clock()
	#print(f'Elapsed Time: {round(end_time - start_time , 2)} seconds')
	plt.savefig('remastered_radio_multi.png', format='png', dpi=900)
	
	plt.show()

