# ICS110 Individual Project

# Analytical Questions
- [ ] Is the maximum proton flux at Earth correlated to the intensity of solar flares on the Sun?

- [ ] Are properties of interplanetary space, such as solar wind speed or temperature, indicators of maximum proton flux at Earth?

- [ ] What are the statistical deviations from the background during intense solar events?

#Running Scripts

In [1]: run pandas_test_nm.py
Enter start date (yyyymmdd): 20120306
Enter a end date (yyyymmdd): 20120318
Enter a start hour or "full": full
How many stations to parse: 2
You are parsing 2 station(s)
Enter station names: INVK
Enter station names: OULU
Parsing the ['INVK', 'OULU'] stations

In [2]: run pandas_test_proton.py
Enter a start date (yyyymmdd): 20120305
Enter a end date (yyyymmdd): 20120316

In [3]: run pandas_test_radio.py
Enter a start date (yyyymmdd): 20120307
Enter a end date (yyyymmdd): 20120307
Enter a start hour or "full": 00
Enter a end hour: 04
Parsing Type III Data: [20120307 00:00:00 -- 20120307 04:00:00]
Elapsed Time: 16.31 seconds


# Evaluate and/or Investigate your Data
The python [script](https://github.com/byamashiro09/ICS110/blob/master/Final_Project/read_data.py) is 'read_data.py'

The script currently reads in [GOES-15 proton flux](https://github.com/byamashiro09/ICS110/tree/master/Final_Project/Data/GOES_proton_flux) (.csv), [GOES-15 Xray flux](https://github.com/byamashiro09/ICS110/tree/master/Final_Project/Data/GOES_xray_flux) (.csv), and [Neutron monitor (NM) data](https://github.com/byamashiro09/ICS110/blob/master/Final_Project/Data/NMDB_OULU_data.txt) (.txt).

Corrupted data is labeled as -99999.0, and 0.0 flux is most probable to be corrupted as well. Corrupted data is changed using the pandas replace function to np.nan.

###### Sample displayed data of pandas data:

### Sample Xray Flux Data
```
                    xrdate     xrflux1     xrflux2
0  2012-03-06 00:04:57.250  2.0555E-07  2.4972E-06
1  2012-03-06 00:04:59.300  2.0555E-07  2.4919E-06
2  2012-03-06 00:05:01.347  2.0778E-07  2.4919E-06
3  2012-03-06 00:05:03.397  2.1224E-07  2.5103E-06
4  2012-03-06 00:05:05.443  2.1669E-07  2.5208E-06
5  2012-03-06 00:05:07.490  2.1224E-07  2.5208E-06
6  2012-03-06 00:05:09.540  2.1001E-07  2.5208E-06
7  2012-03-06 00:05:11.587  2.1446E-07  2.5260E-06
8  2012-03-06 00:05:13.637  2.1112E-07  2.5391E-06
...
```
### Neutron Monitor Data
```
                  date    value
0  2012-03-01 00:00:00  101.902
1  2012-03-01 00:01:00  103.982
2  2012-03-01 00:02:00  100.691
3  2012-03-01 00:03:00  105.082
4  2012-03-01 00:04:00  104.729
5  2012-03-01 00:05:00  102.259
6  2012-03-01 00:06:00  102.670
7  2012-03-01 00:07:00   99.894
8  2012-03-01 00:08:00  103.253
...
```

### Proton Flux Data
```
                      date      pflux1      pflux2      pflux3      pflux4
0  2012-03-06 00:00:39.207  2.8143E-01  6.5707E-02  1.7703E-02  3.0488E-03
1  2012-03-06 00:01:11.973  4.6904E-01  6.5707E-02  1.1802E-02  3.0488E-03
2  2012-03-06 00:01:44.740  4.6904E-01  5.2565E-02  1.5736E-02  2.3713E-03
3  2012-03-06 00:02:17.507  3.7524E-01  4.5994E-02         NaN  3.0488E-03
4  2012-03-06 00:02:50.277  3.7524E-01  1.0513E-01  1.9670E-02  4.0650E-03
5  2012-03-06 00:03:23.043  2.8143E-01  5.2565E-02  1.3769E-02  3.7263E-03
6  2012-03-06 00:03:55.810  2.8143E-01  1.9712E-02  5.9009E-03  3.3875E-03
7  2012-03-06 00:04:28.580  1.8762E-01  3.9424E-02  1.3769E-02  5.4200E-03
8  2012-03-06 00:05:01.347  3.7524E-01  4.5994E-02  1.1802E-02  4.4038E-03
...
```


<img src="proton.pdf" width="500"><img src="radio.pdf" width="500"><img src="nm_data.pdf" width="500">

Data Set | Normalized (Y/N) | Bad Data Specifiers
------------ | ------------- | -------------
Proton Flux | N | -99999.0, 0.0
Xray Flux | N | -99999.0, 0.0
NM Scale | N | n/a 



# Data
The data consists of mainly flux data from instruments on the ground, Earth orbit, and at the L1 Lagrange point. The data includes a sample from (2012 March), not normalized, and complete in intervals of about 30 seconds to a minute. Data values that were not accepted are denoted at extreme negative values around -9999. The specifics of each data set is commented in each header.

GOES-13 Proton Flux

GOES-15 Xray Flux

ACE Magnetic Field Components

ACE Solar Wind Parameters

OULU Neutron Monitor Data
