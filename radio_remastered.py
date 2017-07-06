from spacepy import pycdf

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

print(voltage_rad1)

