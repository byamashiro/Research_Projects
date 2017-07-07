from spacepy import pycdf
import pandas as pd

cdf = pycdf.CDF('wi_h1_wav_20120307_v01.cdf')


time_rb = []

for i in cdf['Epoch']:
	time_rb.append(i)

#print(time_rb)

freq_rad = []

for i in cdf['Frequency_RAD1']:
	freq_rad.append(i)

#print(freq_rad)

voltage_rad1 = []
for i in cdf['E_VOLTAGE_RAD1']:
	voltage_rad1.append(i)

#print(voltage_rad1)


data_time = pd.DataFrame(time_rb)
freq_panda = pd.DataFrame(freq_rad)
freq_panda.columns = ['freq']
data_volt = pd.DataFrame(voltage_rad1)
data_volt.columns = freq_panda['freq']
#full_data = pd.concat([data_time, data_volt], axis=1)

'''
data_full = pd.DataFrame({
	'datetime': time_rb,
	'interesting': voltage_rad1
})
'''


