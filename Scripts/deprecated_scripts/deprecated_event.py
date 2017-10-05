#!/usr/bin/python
from ROOT import gStyle , TCanvas , TGraphErrors, TMultiGraph, TF1 , TGraph
from array import array
from astropy.io import fits as fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from datetime import datetime, timedelta
import pandas as pd
import ast
from astropy.time import Time, TimePlotDate
import csv                         #
from collections import defaultdict     #
import matplotlib.dates as mdates
import sys
from time import time as tclock

'''
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print sys.argv[1]
'''
#Region to check for max
eventdate = datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
#print eventdate

tstart = eventdate - timedelta(days=2)
tstop = eventdate + timedelta(days=5) #7
#idx = np.where(eventdate >= eventdate-timedelta(days=2) and eventdate <= eventdate+timedelta(days=5))

#print(idx)
#exit(0)
myFmt = mdates.DateFormatter('%m/%d')


#print tstart.year
#print tstart.month

'''
tstart = datetime(2012, 3, 7)
tstop = datetime(2012, 3, 13)
'''


#=========GOES Proton Flux

#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_epead/{}_protonfluxgoesepead.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_epead/{}_protonfluxgoesepead.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

goes_proton_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	goes_proton_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
goes_proton_time = np.array(goes_proton_time)
ordinals = np.array(ordinals)

#data = np.genfromtxt('201203_protonfluxgoesepead.dat')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_epead/{}_protonfluxgoesepead.txt'.format(tstart.year))


p_flux_1 = np.array(data[:,2]) #30.6 MeV
p_flux_1[p_flux_1 < 10.0**(-4)] = np.nan

p_flux_2 = np.array(data[:,3]) #30.6 MeV
p_flux_2[p_flux_2 < 10.0**(-4)] = np.nan

p_flux_3 = np.array(data[:,4]) #30.6 MeV
p_flux_3[p_flux_3 < 10.0**(-4)] = np.nan

region_indices = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))
max_index = region_indices[0][0] + np.nanargmax(p_flux_1[region_indices]) #changed np.nanargmax to 


#=========GOES Electron Flux (LOW)

#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_low_electronfluxgoesepead.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_low_electronfluxgoesepead.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

goes_electron_time_low = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	goes_electron_time_low.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
goes_electron_time_low = np.array(goes_electron_time_low)
ordinals = np.array(ordinals)

#data = np.genfromtxt('201203_protonfluxgoesepead.dat')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_low_electronfluxgoesepead.txt'.format(tstart.year))


e_flux_1 = np.array(data[:,3]) #30.6 MeV
e_flux_1[e_flux_1 == -99999.0] = np.nan

#region_indices = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))
#max_index = region_indices[0][0] + np.nanargmax(p_flux_1[region_indices]) #changed np.nanargmax to 

#=========GOES Electron Flux (HIGH)

#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Epead/{}{}_protonfluxgoesepead.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_high_electronfluxgoesepead.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_high_electronfluxgoesepead.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

goes_electron_time_high = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	goes_electron_time_high.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
goes_electron_time_high = np.array(goes_electron_time_high)
ordinals = np.array(ordinals)

#data = np.genfromtxt('201203_protonfluxgoesepead.dat')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/full_electron/{}_high_electronfluxgoesepead.txt'.format(tstart.year))


e_flux_2 = np.array(data[:,3]) #30.6 MeV
e_flux_2[e_flux_2 == -99999.0] = np.nan

#region_indices = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))
#max_index = region_indices[0][0] + np.nanargmax(p_flux_1[region_indices]) #changed np.nanargmax to nans



#=========WIND Type III Radio Bursts

if tstart.year == 2011 or tstart.year == 2012 or tstart.year == 2013 or tstart.year == 2014 and tstart.month == 1 or tstart.year == 2014 and tstart.month == 2 or tstart.year == 2014 and tstart.month == 3 or tstart.year == 2014 and tstart.month == 4 or tstart.year == 2014 and tstart.month == 5 or tstart.year == 2014 and tstart.month == 6 or tstart.year == 2014 and tstart.month == 7 or tstart.year == 2014 and tstart.month == 8 or tstart.year == 2014 and tstart.month == 9:
	date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/converted/wind/full_delimited/windt3_{}{}_final.txt'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
	time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/converted/wind/full_delimited/windt3_{}{}_final.txt'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)
	
	time_format = '%Y-%m-%d %H:%M:%S.%f'
	
	t3_wind_time = list([])
	ordinals = list([])
	#time_arr=np.array([])
	#print dtime
	#time_str = "%s %s" %(dtime[:][0], dtime[:][1])
	
	for i in range(len(time)):
		time_str = date[i] + ' ' + time[i]
		#print time_str
		#time_obj = Time(time_str)
		#time_arr = np.append(time_arr, time_obj)
		time_lister_1 = datetime.strptime(time_str, time_format)
		t3_wind_time.append(time_lister_1)
		ordinals.append(time_lister_1.toordinal())
	t3_wind_time = np.array(t3_wind_time)
	ordinals = np.array(ordinals)
	
	data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/Type3/converted/wind/full_delimited/windt3_{}{}_final.txt'.format(tstart.year, '{:02}'.format(tstart.month)))
	
	t3_wind_intensity = np.array(data[:,2]) #t3 average
	#t3_intensity[t3_intensity < 10**(-4)] = np.nan
	#region_indices_t3_wind = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))
	#max_index_t3_wind = region_indices_t3_wind[0][0] + np.nanargmax(t3_wind_intensity[region_indices_t3_wind]) #changed np.nanargmax to nans
else:
	print "No Type III Data"
'''
elif tstart.year == 2014 and tstart.month == 10:
	print "No Type III Data"
elif tstart.year == 2014 and tstart.month == 11:
	print "No Type III Data"
elif tstart.year == 2014 and tstart.month == 12:
	print "No Type III Data"
'''


#print datetime(2012, 3, 5) > datetime(2012, 3, 7)
#p_flux_max = np.nanargmax(p_flux_1, axis=0) #changed to nans
#print p_flux_1[2118-1]
	
'''
#===========SOHO data
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/soho_data/soho_full_{}.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/soho_data/soho_full_{}.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

soho_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	soho_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
soho_time = np.array(soho_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/soho_data/soho_full_{}.txt'.format(tstart.year))


soho_1 = np.array(data[:,2]) #32-40 MeV
soho_2 = np.array(data[:,3]) #40-50 MeV
soho_3 = np.array(data[:,4]) #80-100 MeV
soho_4 = np.array(data[:,5]) #100-130 MeV

soho_1[soho_1 < 1e-5] = np.nan
soho_2[soho_2 < 1e-5] = np.nan
soho_3[soho_3 < 1e-5] = np.nan
soho_4[soho_4 < 1e-5] = np.nan

#s4mask = np.isfinite(solar_wind)
'''
#===========WIND-Solar Wind Speed
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)
date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/windswefinal{}.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/windswefinal{}.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

solar_wind_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	solar_wind_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
solar_wind_time = np.array(solar_wind_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/windswefinal{}.txt'.format(tstart.year))


solar_wind = np.array(data[:,2]) #30.6 MeV
solar_wind[solar_wind < 0.0] = np.nan
s4mask = np.isfinite(solar_wind)


#===========ACE-Solar Wind Speed
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/swepamfinal{}.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/swepamfinal{}.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

ace_wind_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	ace_wind_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
ace_wind_time = np.array(ace_wind_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/swepamfinal{}.txt'.format(tstart.year))


ace_wind = np.array(data[:,2]) #30.6 MeV
ace_wind[ace_wind < 0.0] = np.nan
s5mask = np.isfinite(ace_wind)

#===========OMNI Solar Wind Temperature
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/omni_data/temperature/temperature_converted/omni_temp_{}_final.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/omni_data/temperature/temperature_converted/omni_temp_{}_final.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%d-%m-%Y %H:%M:%S.%f'

omni_temp_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	omni_temp_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
omni_temp_time = np.array(omni_temp_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/omni_data/temperature/temperature_converted/omni_temp_{}_final.txt'.format(tstart.year))


omni_temp = np.array(data[:,2]) #30.6 MeV
omni_temp[omni_temp == 1.00000E+07] = np.nan

'''
#===========GOES Forbush
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/forbush_epead/{}{}_forbushgoes.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/forbush_epead/{}{}_forbushgoes.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

forbush_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	forbush_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
forbush_time = np.array(forbush_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/forbush_epead/{}{}_forbushgoes.dat'.format(tstart.year, '{:02}'.format(tstart.month)))


goes_forbush = np.array(data[:,2]) #110-900 MeV
goes_forbush[goes_forbush < 0.0] = np.nan
#s4mask = np.isfinite(goes_forbush)
'''
'''
#===========DST (1min)
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted_dec/Dst_{}.dat'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted_dec/Dst_{}.dat'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)
#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

dst_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	dst_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
dst_time = np.array(dst_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted_dec/Dst_{}.dat'.format(tstart.year))
#data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)))


dst_index = np.array(data[:,2]) #110-900 MeV
#dst_index[dst_index < 0.0] = np.nan
#s4mask = np.isfinite(goes_hepad)
'''
#===========AE Index (HOUR_INDEX)
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/ae_{}_final.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/ae_{}_final.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)
#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

ae_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	ae_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
ae_time = np.array(ae_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/ae_{}_final.txt'.format(tstart.year))
#data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)))


ae_index = np.array(data[:,3]) #110-900 MeV

region_indices_ae = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))

max_index_ae = region_indices_ae[0][0] + np.nanargmax(ae_index[region_indices_ae]) #changed np.nanargmax to nans
min_index_ae = region_indices_ae[0][0] + np.nanargmin(ae_index[region_indices_ae]) #changed np.nanargmax to nans /nanargmax
#dst_index[dst_index < 0.0] = np.nan
#s4mask = np.isfinite(goes_hepad)

#===========DST Index (HOUR_INDEX)
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/dst_{}_final.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/dst_{}_final.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)
#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)

time_format = '%Y-%m-%d %H:%M:%S.%f'

dst_hour_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	dst_hour_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
dst_hour_time = np.array(dst_hour_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/kyoto/converted/dst_{}_final.txt'.format(tstart.year))
#data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/dst/converted/Dst_{}_{}.dat'.format(tstart.year, '{:02}'.format(tstart.month)))


dst_hour_index = np.array(data[:,3]) #110-900 MeV

region_indices_dst = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))

max_index_dst = region_indices_dst[0][0] + np.nanargmax(dst_hour_index[region_indices_dst]) #changed np.nanargmax to nans
min_index_dst = region_indices_dst[0][0] + np.nanargmin(dst_hour_index[region_indices_dst]) #changed np.nanargmax to nans /nanargmax
#dst_index[dst_index < 0.0] = np.nan
#s4mask = np.isfinite(goes_hepad)

'''
#===========Cutoff
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/cutoff/march.txt', usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/cutoff/march.txt', usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

cutoff_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	cutoff_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
cutoff_time = np.array(cutoff_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/testproton/cutoff/march.txt')


cutoff_0 = np.array(data[:,2]) #110-900 MeV
cutoff_1 = np.array(data[:,3]) #110-900 MeV
cutoff_1 = np.array(data[:,4]) #110-900 MeV
cutoff_2 = np.array(data[:,5]) #110-900 MeV
cutoff_2 = np.array(data[:,6]) #110-900 MeV
cutoff_3 = np.array(data[:,7]) #110-900 MeV
cutoff_bh = np.array(data[:,8]) #110-900 MeV


#dst_index[dst_index < 0.0] = np.nan
#s4mask = np.isfinite(goes_hepad)

'''
'''
#===========GOES HEPAD
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Hepad/{}{}_protonfluxgoeshepad.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Hepad/{}{}_protonfluxgoeshepad.dat'.format(tstart.year, '{:02}'.format(tstart.month)), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

hepad_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	hepad_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
hepad_time = np.array(hepad_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/GOES/converted/Hepad/{}{}_protonfluxgoeshepad.dat'.format(tstart.year, '{:02}'.format(tstart.month)))


goes_hepad = np.array(data[:,5]) #110-900 MeV
goes_hepad[goes_hepad < 0.0] = np.nan
#s4mask = np.isfinite(goes_hepad)
'''



#===========Magnetic field
#date = np.genfromtxt('windswefinal2012.txt', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('windswefinal2012.txt', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/magfinal{}.txt'.format(tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/magfinal{}.txt'.format(tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S.%f'

mag_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	mag_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())
mag_time = np.array(mag_time)
ordinals = np.array(ordinals)


#data = np.genfromtxt('windswefinal2012.txt')
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/ACEWIND/converted/full/magfinal{}.txt'.format(tstart.year))


mag_field_x = np.array(data[:,2]) #30.6 MeV
mag_field_x[mag_field_x < -9000.0] = np.nan

mag_field_y = np.array(data[:,3]) #30.6 MeV
mag_field_y[mag_field_y < -9000.0] = np.nan

mag_field_z = np.array(data[:,4]) #30.6 MeV
mag_field_z[mag_field_z < -9000.0] = np.nan



#===========Neutron Monitor OULU (1 min time)
#date = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=1,delimiter=' ', dtype=None)

#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year), usecols=1, delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/converted_relative/{}/{}_NMDB_OULU_unnormalized.dat'.format(tstart.year,tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/converted_relative/{}/{}_NMDB_OULU_unnormalized.dat'.format(tstart.year,tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S'

nm_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	nm_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())

nm_time = np.array(nm_time)
ordinals = np.array(ordinals)

#data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year))
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/converted_relative/{}/{}_NMDB_OULU_unnormalized.dat'.format(tstart.year,tstart.year))
#invk = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_INVK_normalized.dat'.format(tstart.year,tstart.year))


nm_data = np.array(data[:,2])
nm_data[nm_data < -9000] = np.nan

region_indices_nm = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))

max_index_nm = region_indices_nm[0][0] + np.nanargmax(nm_data[region_indices_nm]) #changed np.nanargmax to nans
min_index_nm = region_indices_nm[0][0] + np.nanargmin(nm_data[region_indices_nm]) #changed np.nanargmax to nans /nanargmax

#===========Neutron Monitor OULU (1 HOUR, 60 min time)
#date = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=1,delimiter=' ', dtype=None)

#date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year), usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year), usecols=1, delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/data_1hr/{}/NMDB_OULU_{}_final.txt'.format(tstart.year,tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/data_1hr/{}/NMDB_OULU_{}_final.txt'.format(tstart.year,tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S'

nm_1hr_time = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	nm_1hr_time.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())

nm_1hr_time = np.array(nm_1hr_time)
ordinals = np.array(ordinals)

#data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_OULU_normalized.dat'.format(tstart.year,tstart.year))
data = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/data_1hr/{}/NMDB_OULU_{}_final.txt'.format(tstart.year,tstart.year))
#invk = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_INVK_normalized.dat'.format(tstart.year,tstart.year))


nm_1hr_data = np.array(data[:,2])
nm_1hr_data[nm_1hr_data < -9000] = np.nan

region_indices_nm_1hr = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))

max_index_nm_1hr = region_indices_nm_1hr[0][0] + np.nanargmax(nm_1hr_data[region_indices_nm_1hr]) #changed np.nanargmax to nans
min_index_nm_1hr = region_indices_nm_1hr[0][0] + np.nanargmin(nm_1hr_data[region_indices_nm_1hr]) #changed np.nanargmax to nans /nanargmax

#region_indices_1hr_nm = np.where(np.logical_and(tstart.toordinal() < ordinals, ordinals < tstop.toordinal()))
#max_1hr_index_nm = region_indices_1hr_nm[0][0] + np.nanargmax(nm_1hr_data[region_indices_nm]) #changed np.nanargmax to nans
#min_1hr_index_nm = region_indices_1hr_nm[0][0] + np.nanargmin(nm_1hr_data[region_indices_nm]) #changed np.nanargmax to nans /nanargmax

'''
#===========Neutron Monitor INVK
#date = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=0, delimiter=' ', dtype=None)
#time = np.genfromtxt('2012_NMDB_OULU_normalized.dat', usecols=1,delimiter=' ', dtype=None)

date = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_INVK_normalized.dat'.format(tstart.year,tstart.year), usecols=0, delimiter=' ', dtype=None)
time = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_INVK_normalized.dat'.format(tstart.year,tstart.year), usecols=1, delimiter=' ', dtype=None)


time_format = '%Y-%m-%d %H:%M:%S'

nm_time_invk = list([])
ordinals = list([])
#time_arr=np.array([])
#print dtime
#time_str = "%s %s" %(dtime[:][0], dtime[:][1])

for i in range(len(time)):
	time_str = date[i] + ' ' + time[i]
	#print time_str
	#time_obj = Time(time_str)
	#time_arr = np.append(time_arr, time_obj)
	time_lister_1 = datetime.strptime(time_str, time_format)
	nm_time_invk.append(time_lister_1)
	ordinals.append(time_lister_1.toordinal())

nm_time_invk = np.array(nm_time_invk)
ordinals = np.array(ordinals)


invk = np.genfromtxt(u'/Users/bryanyamashiro/Desktop/GoddardInternship2/Data_Reduction_final/nmdata/normalized/{}/{}_NMDB_INVK_normalized.dat'.format(tstart.year,tstart.year))


nm_data_invk = np.array(invk[:,2])
nm_data_invk[nm_data_invk < -9000] = np.nan
'''
#=============Plotting
f, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, sharex=True, sharey=False) #plt.subplots(4, sharex=True, sharey=False)

ax1.axvline(goes_proton_time[max_index], color='black', linewidth=1)
ax2.axvline(goes_proton_time[max_index], color='black', linewidth=1)
ax3.axvline(goes_proton_time[max_index], color='black', linewidth=1)
ax4.axvline(goes_proton_time[max_index], color='black', linewidth=1)
ax5.axvline(goes_proton_time[max_index], color='black', linewidth=1)

ax1.axvline(dst_hour_time[min_index_dst], color='blue', linewidth=1)
ax2.axvline(dst_hour_time[min_index_dst], color='blue', linewidth=1)
ax3.axvline(dst_hour_time[min_index_dst], color='blue', linewidth=1)
ax4.axvline(dst_hour_time[min_index_dst], color='blue', linewidth=1)
ax5.axvline(dst_hour_time[min_index_dst], color='blue', linewidth=1)

ax1.axvline(ae_time[max_index_ae], color='red', linewidth=1)
ax2.axvline(ae_time[max_index_ae], color='red', linewidth=1)
ax3.axvline(ae_time[max_index_ae], color='red', linewidth=1)
ax4.axvline(ae_time[max_index_ae], color='red', linewidth=1)
ax5.axvline(ae_time[max_index_ae], color='red', linewidth=1)

ax1.axvline(nm_1hr_time[min_index_nm_1hr], color='green', linewidth=1)
ax2.axvline(nm_1hr_time[min_index_nm_1hr], color='green', linewidth=1)
ax3.axvline(nm_1hr_time[min_index_nm_1hr], color='green', linewidth=1)
ax4.axvline(nm_1hr_time[min_index_nm_1hr], color='green', linewidth=1)
ax5.axvline(nm_1hr_time[min_index_nm_1hr], color='green', linewidth=1)




ax1.plot(goes_proton_time, p_flux_1, color='r', label='30.6 MeV')
ax1.plot(goes_proton_time, p_flux_2, color='b', label='63.1 MeV')
ax1.plot(goes_proton_time, p_flux_3, color='lime', label='165 MeV')
ax1.set_title('Event Data {} {} {}'.format(eventdate.year,'{:02}'.format(eventdate.month),'{:02}'.format(eventdate.day)))
ax1.set_xlim([tstart, tstop]) #ax1.set_xlim([datetime(2012, 3, 5), datetime(2012, 3, 13)])
ax1.set_ylim([0.0001, 1000])
ax1.set_yscale('log')
ax1.set_ylabel('Proton Flux\n[pfu]')
ax1.minorticks_on
ax1.grid(True)
#ax1.legend(loc=4, prop={'size':6})
#ax1.locator_params(numticks=5, axis='y')
ax1.locator_params(numticks=5, axis='y')
ax1.legend(loc='upper right', prop={'size':6}).set_zorder(5)


if tstart.year == 2011 or tstart.year == 2012 or tstart.year == 2013 or tstart.year == 2014 and tstart.month == 1 or tstart.year == 2014 and tstart.month == 2 or tstart.year == 2014 and tstart.month == 3 or tstart.year == 2014 and tstart.month == 4 or tstart.year == 2014 and tstart.month == 5 or tstart.year == 2014 and tstart.month == 6 or tstart.year == 2014 and tstart.month == 7 or tstart.year == 2014 and tstart.month == 8 or tstart.year == 2014 and tstart.month == 9:
	ax7 = ax1.twinx()
	ax7.plot(t3_wind_time, t3_wind_intensity, color='magenta',linewidth=1.0, label='Wind T3')
	#ax6.set_ylim([dst_hour_index[min_index_dst]-10.0, dst_hour_index[max_index_dst]+10.0])
	ax7.set_xlim([tstart, tstop])
	#ax7.set_ylim([-250,100])
	#ax6.set_yscale('log')
	ax7.set_ylabel('TIII Int. [sfu]')
	ax7.minorticks_on
	ax7.set_yscale('log')
	#ax6.grid(True)
	ax7.legend(loc=4, prop={'size':6}).set_zorder(5)
	ax7.locator_params(numticks=5, axis='y')
else:
	print "No Type III Data"


ax3.plot(ace_wind_time, ace_wind,'.', ms=2, color='magenta', label='ACE')
ax3.plot(solar_wind_time, solar_wind,'.', ms=2, color='darkorchid', label='WIND')
ax3.set_xlim([tstart, tstop])
ax3.set_ylim([200,900])
ax3.set_ylabel('Solar Wind\nSpeed [km/s]')
ax3.minorticks_on
ax3.grid(True)
ax3.legend(loc=4, prop={'size':6})
#ax3.locator_params(nbins=5, axis='y')

ax8 = ax3.twinx()
ax8.plot(omni_temp_time, omni_temp, color='purple',linewidth=1.0, label='OMNI Temp')
#ax6.set_ylim([dst_hour_index[min_index_dst]-10.0, dst_hour_index[max_index_dst]+10.0])
ax8.set_xlim([tstart, tstop])
#ax8.set_ylim([-250,100])
#ax6.set_yscale('log')
ax8.set_ylabel('Temp [K]')
ax8.ticklabel_format(style='sci',useOffset=False, axis='y', scilimits=(0,0))
ax8.minorticks_on
#ax6.grid(True)
ax8.legend(loc='lower right', prop={'size':6})
ax3.legend(loc='upper right', prop={'size':6})
ax3.locator_params(nbins=5, axis='y')
ax8.locator_params(nbins=5, axis='y')
#ax8.axhline(y=-50.0,linestyle = '-.', color='orange',  linewidth=1)
#ax8.axhline(y=-100.0,linestyle = '-.', color='red',  linewidth=1)

'''
ax2.plot(forbush_time, goes_hepad, color='magenta', label='110-900 MeV')
ax2.set_xlim([tstart, tstop])
ax2.set_ylim([1e-1,1e2])
ax2.set_yscale('log')
ax2.set_ylabel('Proton Flux\n[counts/s]')
ax2.minorticks_on
ax2.grid(True)
ax2.legend(loc=4, prop={'size':6})
'''
'''
ax2.plot(hepad_time, goes_hepad, color='purple', label='>700 MeV')
ax2.set_xlim([tstart, tstop])
ax2.set_ylim([1e-5,6e-4])
ax2.set_yscale('log')
ax2.set_ylabel('Proton Flux\n[pfu]')
ax2.minorticks_on
ax2.grid(True)
ax2.legend(loc=4, prop={'size':6})
'''

ax2.plot(ae_time, ae_index, color='red', label='AE')
ax2.set_xlim([tstart, tstop])
ax2.set_ylim([0,2000])
#ax2.set_yscale('log')
ax2.set_ylabel('AE-Index\n[nT]')
ax2.minorticks_on
ax2.grid(True)


ax6 = ax2.twinx()
ax6.plot(dst_hour_time, dst_hour_index, color='blue',linewidth=2.0, label='Dst')
#ax6.set_ylim([dst_hour_index[min_index_dst]-10.0, dst_hour_index[max_index_dst]+10.0])
ax6.set_xlim([tstart, tstop])
ax6.set_ylim([-250,100])
#ax6.set_yscale('log')
ax6.set_ylabel('Dst-Index [nT]')
ax6.minorticks_on
#ax6.grid(True)
ax6.legend(loc='upper right', prop={'size':6})
ax2.legend(loc=4, prop={'size':6})
ax2.locator_params(nbins=5, axis='y')
ax6.locator_params(nbins=5, axis='y')
ax6.axhline(y=-50.0,linestyle = '-.', color='orange',  linewidth=1)
ax6.axhline(y=-100.0,linestyle = '-.', color='red',  linewidth=1)


'''
ax3.plot(mag_time, mag_field_x, color='red', label='Bx')
ax3.plot(mag_time, mag_field_y, color='orange', label='By')
ax3.plot(mag_time, mag_field_z, color='blue', label='Bz')
ax3.set_xlim([tstart, tstop])
ax3.set_ylim([-40,40])
ax3.set_ylabel('B-Field\n[nT]')
ax3.minorticks_on
ax3.grid(True)
ax3.legend(loc=4, prop={'size':6})
'''
'''
ax3.plot(cutoff_time, cutoff_0, label='0.5 GV')
ax3.plot(cutoff_time, cutoff_1, label='1.0 GV')
ax3.plot(cutoff_time, cutoff_1, label='1.5 GV')
ax3.plot(cutoff_time, cutoff_2, label='2.0 GV')
ax3.plot(cutoff_time, cutoff_2, label='2.5 GV')
ax3.plot(cutoff_time, cutoff_3, label='3.0 GV')
ax3.plot(cutoff_time, cutoff_bh, label='|B$_h$|')
ax3.set_xlim([tstart, tstop])
ax3.set_ylim([0.5,3.1])
ax3.set_ylabel('Norm. Geo.\nCutoff')
ax3.minorticks_on
ax3.grid(True)
ax3.legend(loc=4, prop={'size':6})
'''

#ax4.plot(nm_time_invk,nm_data_invk, color='crimson', label='INVK')
ax4.plot(nm_time,nm_data, color='limegreen', label='OULU 1 min')
ax4.plot(nm_1hr_time,nm_1hr_data, color='blue', linewidth=3.0, label='OULU 1 hour')
ax4.set_xlim([tstart, tstop])
ax4.set_ylim([nm_data[min_index_nm]-1.0, nm_data[max_index_nm]+1.0])
#ax4.set_ylim(min(nm_data)-2.0, max(nm_data[tstop])+2.0)
#ax4.set_ylim([int(min((math_formula(nm_data) for nm_data in xrange(tstart,tstop)))), int(max((math_formula(nm_data) for nm_data in xrange(tstart,tstop))))])

'''
if tstart.year == 2011:
	ax4.set_ylim([85.0,115.0]) #0.2 1.1
elif tstart.year == 2012:
	ax4.set_ylim([85.0,115.0]) #0.2 1.1
elif tstart.year == 2013:
	ax4.set_ylim([85.0,115.0]) #0.2 1.1
elif tstart.year == 2013:
	ax4.set_ylim([85.0,115.0]) #0.2 1.1
elif tstart.year == 2014:
	ax4.set_ylim([85.0,115.0]) #0.2 1.1
elif tstart.year == 2015:
	ax4.set_ylim([-2., 2])
else:
	print "Enter a valid year"
	exit(0)
'''


ax4.set_ylabel('NM Rel.Scl.\n[% inc.]')
ax4.minorticks_on
#ax4.relim()
#ax4.autoscale(enable=True, axis='y', tight=False)
#ax4.autoscale_view()
#ax4.autoscale_view(True,False,True)

ax4.grid(True)
ax4.xaxis.set_major_formatter(myFmt)
ax4.legend(loc=4, prop={'size':6})

'''
ax5.plot(soho_time, soho_1, color='red', label='32-40 MeV')
ax5.plot(soho_time, soho_2, color='orange', label='40-50 MeV')
ax5.plot(soho_time, soho_3, color='green', label='80-100 MeV')
ax5.plot(soho_time, soho_4, color='blue', label='100-130 MeV')
ax5.set_xlim([tstart, tstop])
ax5.set_ylim([1e-5,2])
ax5.set_yscale('log')
ax5.set_ylabel('Proton\nIntensity') #[1/(cm$^2$srsMeV)]
ax5.set_xlabel('Time [UT]')
ax5.minorticks_on
ax5.grid(True)
ax5.legend(loc=4, prop={'size':6})
'''
ax5.plot(mag_time, mag_field_x, color='red', label='Bx')
ax5.plot(mag_time, mag_field_y, color='orange', label='By')
ax5.plot(mag_time, mag_field_z, color='blue', label='Bz')
ax5.set_xlim([tstart, tstop])
ax5.set_ylim([-40,40])
ax5.set_ylabel('ACE B-Field\n[nT]')
ax5.minorticks_on
ax5.set_xlabel('Time [UT]')
ax5.minorticks_on
ax5.grid(True)
#ax5.legend(loc=4, prop={'size':6})
#ax5.locator_params(nbins=5, axis='y')

ax9 = ax5.twinx()
ax9.plot(goes_electron_time_high, e_flux_2, color='turquoise',linewidth=1.0, label='2.0 MeV')
ax9.plot(goes_electron_time_low, e_flux_1, color='lime',linewidth=1.0, label='0.8 MeV')
#ax6.set_ylim([dst_hour_index[min_index_dst]-10.0, dst_hour_index[max_index_dst]+10.0])
ax9.set_xlim([tstart, tstop])
ax9.set_ylim([10.0**(-1.0),10.0**(7.0)])
ax9.set_yscale('log')
ax9.set_ylabel('Electron Flux [pfu]')
ax9.minorticks_on
#ax6.grid(True)
ax9.legend(loc='upper right', prop={'size':6})
ax5.legend(loc=4, prop={'size':6})
ax5.locator_params(nbins=5, axis='y')
ax9.locator_params(numticks=5, axis='y')
#ax9.axhline(y=-50.0,linestyle = '-.', color='orange',  linewidth=1)
#ax9.axhline(y=-100.0,linestyle = '-.', color='red',  linewidth=1)


# Fine-tune figure; make subplots close to each other and hide x ticks for
# all but bottom plot.
f.subplots_adjust(hspace=.15)
#plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False, rotation=25)
plt.setp(ax5.xaxis.get_majorticklabels(), rotation=0)


#print "Date: ", eventdate, "Min Dst (nT): ", dst_hour_index[min_index_dst], "Max AE Index (nT): ", ae_index[max_index_ae]
with open('myfile.txt', 'a') as f:
    print >> f, eventdate,dst_hour_index[min_index_dst],ae_index[max_index_ae],nm_1hr_data[min_index_nm_1hr]



#plt.savefig('FD_{}{}{}.pdf'.format(eventdate.year,'{:02}'.format(eventdate.month),'{:02}'.format(eventdate.day)), format='pdf', dpi=72)
plt.savefig('FD_{}{}{}.png'.format(eventdate.year,'{:02}'.format(eventdate.month),'{:02}'.format(eventdate.day)), format='png', dpi=600)


#plt.show()
'''
plt.plot(time_lister_2, p_flux_1, 'o')
plt.xlabel('Time [UT]', fontname="Arial", fontsize = 14)
plt.ylabel('Proton Flux [pfu]', fontname="Arial", fontsize = 14)



plt.minorticks_on()
plt.grid(True)
plt.savefig('protonflux_test.pdf', format='pdf', dpi=900)
plt.show()

#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
'''

exit(0)

