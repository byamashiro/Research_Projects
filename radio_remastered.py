from spacepy import pycdf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys

'''
import urllib.request

url = 'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h0/2012/wi_h0_wav_20120307_v01.cdf'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
#text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

sys.exit(0)

#url = 'https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h0/2012/wi_h0_wav_20120307_v01.cdf'
url = urlopen("https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h0/2012/wi_h0_wav_20120307_v01.cdf")
'''

cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')


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

rb_data['avg'] = rb_data.mean(axis=1, numeric_only=True)

event_date_start = '20120307'
event_start = '00'
event_obj_start_str = '20120307'

event_date_end = '20120307'
event_end = '03'
event_obj_end_str = '20120307'

rb_data['avg'].loc[f'{event_date_start} {event_start}':f'{event_date_end} {event_end}'].plot(color='blue', label= '20 kHz - 1040 kHz')
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

plt.show()


'''
data_full = pd.DataFrame({
	'datetime': time_rb,
	'interesting': voltage_rad1
})
'''


