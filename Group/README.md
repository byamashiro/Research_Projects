# Group Tasks

**Table of Contents**

- [Current Tasks and Errors](#current-tasks-and-errors)
- [Required Python Modules](#required-python-modules)
- [Running Scripts](#running-scripts)
- [Data](#data)
- [Completed Tasks](#completed-tasks)
- [Resolved Errors](#resolved-errors)



# Current Tasks and Errors


- [ ] Gather proton flux data from GOES-13 (https://satdat.ngdc.noaa.gov/sem/goes/data/avg/)
  - Use time averaged data, 5 minute intervals
   - [ ] Proton max flux
   - [ ] Proton max flux time

- [ ] Plotting
  - [ ] Max proton flux vs. max Xray intensity
  - [ ] Max proton flux vs. CME speed





# Completed Tasks

<details><summary>Completed Task List</summary>
<p>

- [x] Finish solar parameter catalog (01/16/2018)
  - Flare (http://www.lmsal.com/solarsoft/latest_events_archive.html)
    - Flare start time, max time, end time
    - Flare location
    - Flare classification
  - Coronal Mass Ejection
    - CDAW (https://cdaw.gsfc.nasa.gov/CME_list/)
      - CME Time
      - CME Speed
      - PA Angle
    - DONKI (https://kauai.ccmc.gsfc.nasa.gov/DONKI/search/)
      - CME Time
      - CME Speed
      - Half width
  - Solar Energetic Particles
    - GOES
      - Proton "start time" (https://cdaw.gsfc.nasa.gov/CME_list/sepe/)
  - Geomagnetic Storm
    - Disturbance Storm Time (http://wdc.kugi.kyoto-u.ac.jp/dstdir/index.html)
      - Dst minimum date
      - Dst minimum equatorial value
    - Kp Index (ftp://ftp.swpc.noaa.gov/pub/indices/old_indices/)
      - Kp maximum date
      - Kp maximum index

</p>
</details>







<details><summary>Current Tasks and Errors</summary>
<p>

<details><summary>Key</summary>
<p>
### Error Name (Resolution Date)
* **Resolution**: Resolution Description
- Description of the error and preemptive ideas to solve the error
</p>
</details>

</p>
</details>


# Required Python Modules
<details><summary>Current Python: Version 3.6.1</summary>
<p>

Module       | Submodule(s) | as | Uses
------------ | ------------- | ------------- | -------------
**pandas**       | -                | pd              | DataFrames, indexing, plotting, downloading http url data, csv_reader()
**numpy**        | -                | np              | NaN values
**spacepy**      | pycdf            | -               | Reading Common Data Format
**urllib**       | error            | -               | For HTTPError recognition
**random**       | -                | -               | Randomizer for random colors
**matplotlib**   | .pyplot, .mdates | plt, mdates, cm | Plotting, subplots, date formatting, color map (viridis)
**datetime**     | -                | -               | Datetime indexing, datetime strings, datetime conversion from strings
**sys**          | -                | -               | Exiting script
**wget**         | -                | -               | Downloading files online (.cdf, .csv, .ascii, .txt)
**os**           | -                | -               | Remove files through script
**calendar**     | -                | -               | Retrieves final date of the month specified
**shutil**       | -                | -               | Moves files into specified directories

</p>
</details>


## Installing Dependencies
<details><summary>pip install</summary>
<p>

- matplotlib
- numpy
- pandas
- datetime
- <details><summary>spacepy (dependencies collapsed)</summary>
  <p>

  - numpy
  - matplotlib
  - ffnet
    - gcc
    - gfortran
  - scipy
  - networkx

  </p>
  </details>

</p>
</details>


# Data Sources

<details><summary>Currently Implemented</summary>
<p>

Data       | Instrument | Detector | Source | URL
------------ | ------------- | ------------- | -------------| -------------
**GOES Proton Flux**            | GOES-13,15        | EPEAD               | NOAA   | https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/
**Legacy GOES Proton Flux**     | GOES-08,10        | EPS                 | NOAA   | https://satdat.ngdc.noaa.gov/sem/goes/data/new_avg/
**TypeIII Radio Burst**         | Wind              | RAD1 (20-1040 kHz)  | CDAW   | https://cdaweb.gsfc.nasa.gov/pub/data/wind/waves/wav_h1/
**GOES Xray Flux**              | GOES-15           | XRS                 | NOAA   | https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/
**Neutron Monitor Counts**      | NM Stations       | IGY, NM64           | NMDB   | http://www.nmdb.eu/nest/
**ACE Solar Wind Parameters**   | ACE               | SWEPAM              | CDAW   | https://cdaweb.gsfc.nasa.gov/pub/data/ace/swepam/level_2_cdaweb/swe_h0/
**Wind Solar Wind Parameters**  | Wind              | SWE                 | CDAW   | https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_k0/
**STEREO-A/B Proton Flux**      | STEREO            | HET                 | IMPACT | http://stereo.ssl.berkeley.edu/

</p>
</details>

<details><summary>Prospective Data Sets</summary>
<p>

**Kp Index**     | Ground Based Magnetometers                | Planetary           | NOAA | ftp://ftp.swpc.noaa.gov/pub/indices/old_indices/
**Dst Index**          | Ground Based Magnetometers                | Kyoto           | WDC | http://wdc.kugi.kyoto-u.ac.jp/
**AE Index**         | -                | -           | - | -
**SOHO Proton Flux**           | SOHO                | ERNE           | SRL | https://srl.utu.fi/export/
****           | -                | -           | - | -
****           | -                | -           | - | -
****           | -                | -           | - | -

</p>
</details>



# Running Scripts

### Code Name ([omni_script_v4](https://github.com/byamashiro/Research_Projects/blob/master/Scripts/pandas_test_omni.py))

<details><summary>Command Line Example</summary>
<p>

```shell
Template for running the code
```

</p>
</details>

<img src="Plots/omni_full_test_v4.png" width="700">






# Data
The data consists of mainly flux data from instruments on the ground, Earth orbit, and at the L1 Lagrange point. The data includes a sample from (2012 March), not normalized, and complete in intervals of about 30 seconds to a minute. Data values that were not accepted are denoted at extreme negative values around -9999. The specifics of each data set is commented in each header.



<details><summary>Data Caveats</summary>
<p>

Data labeled as -99999.0 and 0.0 are converted to 'np.nan' values for all current working scripts.

Data Set | Normalized (Y/N) | Bad Data Specifiers
------------ | ------------- | -------------
Proton Flux | N | -99999.0, 0.0
Xray Flux | N | -99999.0, 0.0
Neutron Monitor Rate | N | n/a 
Radio Burst | N | n/a
Solar Wind Speed | N | < 0.0

</p>
</details>

<details><summary>Data Originals</summary>
<p>

GOES-13 Proton Flux  
GOES-15 Xray Flux  
ACE Magnetic Field Components  
ACE Solar Wind Parameters  
OULU Neutron Monitor Data  

</p>
</details>

<details><summary>Sample Data Format</summary>
<p>

#### Sample Type III Radio Burst Data
```
                             12            16        20        24        28  \
12_16                                                                         
2012-03-01 00:00:30  01-03-2012  00:00:30.000  1.182980  1.179540  1.176100   
2012-03-01 00:01:30  01-03-2012  00:01:30.000  1.281410  1.202890  1.124380   
2012-03-01 00:02:30  01-03-2012  00:02:30.000  1.021370  1.043250  1.065120   
2012-03-01 00:03:30  01-03-2012  00:03:30.000  1.107890  1.114680  1.121480 
...
```
#### Neutron Monitor Data
```
                        OULU     INVK
datetime                             
2012-03-06 00:00:00  106.625  190.810
2012-03-06 00:05:00  105.342  189.426
2012-03-06 00:10:00  106.199  188.382
2012-03-06 00:15:00  105.591  191.880
2012-03-06 00:20:00  104.626  191.370
...
```

#### Proton Flux Data
```
      P3W_QUAL_FLAG  P3W_UNCOR_CR  P3W_UNCOR_FLUX  P4W_QUAL_FLAG  \
0               NaN           NaN             NaN            NaN   
1               0.0      0.030488        0.093809            0.0   
2               NaN           NaN             NaN            NaN   
3               0.0      0.030488        0.093809            0.0   

...
```

</p>
</details>


# Completed Tasks

<details><summary>Completed Task List</summary>
<p>

- [x] OMNI Type III Radio Bursts (12/30/2017)
  - [x] Implement the radio detection for a given frequency and duration limit (12/30/2017)
   - [x] Integrate radio burst detection algorithm into OMNI script (11/22/2017)
    - [x] Horizontal line for t3 threshold and vertical lines for start and end time of event (11/22/2017)
    - [x] Plot lines/shaded area for corresponding radio burst (12/30/2017)
    - [x] Set an intensity threshold as a static parameter in the preamble (11/22/2017)
    - [x] Threshold must be low for backside events (i.e 20120723) (12/30/2017)
    - [x] Include every detected radio burst in the given range (12/30/2017)

- [x] GOES-13 xray flux (12/30/2017)
  - [x] Add markers and tags to certain xray flux magnitudes (12/30/2017)
  - [x] Add GOES-13 xray flux (9/6/2017)

- [x] Create an projection of the Sun using cartopy/basemap/aitoff (12/30/2017)
  - [x] Sun projection from -180 to 180, including the back side (12/30/2017)
  - [x] Plot individual events on the Sun (12/30/2017)

- [x] Corrected GOES proton flux (10/23/2017)
  - [x] Change all proton flux from new_full to new_avg data (10/18/2017)
  - [x] Add an 'if' statement to deal with an overlap of monthly data (i.e Jan. - Feb.) (10/23/2017)

- [x] Bartels' Rotation Converter (09/27/2017)
  - [x] Function to convert date to Bartels' rotation number (09/27/2017)

- [x] Local file code conversion (09/10/2017)
  - [x] GOES-13/15 Proton flux (8/30/2017)
  - [x] WIND Type III Radio Burst (8/30/2017)
  - [x] ACE Solar Wind speed (09/10/2017)
  - [ ] ~~Neutron Monitor counts/s~~ (NM data is downloaded specifically for each event, therefore data is too unique to save)
  - [x] GOES-13/15 Xray flux (09/10/2017)

- [x] Create a folder for local data. (.../Research_Projects/**Data**) (8/26/2017)
  - [x] Separate into mission names (i.e GOES, WIND, ACE, etc.) (8/26/2017)
  - [x] Remove 'sample_data' folder from Scripts directory. (8/22/2017)


- [x] Revamp the radio burst script (8/08/2017)
  - [x] Plot all frequencies on separate plots (8/08/2017)
  - [x] Find the most optimal subplot (8/08/2017)


- [x] Add feature to add a line for extrema (i.e max, min, etc.) (7/22/2017)


- [x] Switch all GOES proton flux from GOES-15 to GOES-13 (7/19/2017)


- [x] Collect GOES-15 Xray data (7/18/2017)
- [x] Incorporate online databases for radio and proton data (7/18/2017)

- [x] Remake GOES Proton Flux scripts (7/18/2017)
  - [x] Automate script to download File name: g15_epead_p27e_32s_20120307_20120307 from https://satdat.ngdc.noaa.gov/sem/goes/data/new_full/2012/03/goes15/csv/ (7/10/2017)
  - [x] Energy range flux selections (6 channels) (7/10/2017)
  - [x] Collect GOES data from legacy satellites if specific date is not found (7/18/2017)
    - [x] Integrate GOES 8-13 satellites for date ranges (7/18/2017)
    - [x] Collect "new_avg" data (7/18/2017)
      - [x] Collect the same "new_full" data in the modern proton event dates (7/18/2017)
    - [x] Specify energy range to be collected, must be over 100 MeV (7/18/2017)
    - [x] Script must be modified for changes in strings in the "new_avg" files (7/18/2017)
      - [x] Attempt to pull specific GOES model from file string (i.e g10, 10) (7/18/2017)


- [x] Integrate all data into subplots (7/15/2017)
  - [x] Incorporate all pandas data frames from other scripts into one script (7/13/2017)
  - [x] Dynamic subplots (7/15/2017)
  - [x] Fix all subplot axis labels and legends (7/15/2017)
  - [x] Set appropriate logscale (7/15/2017)

- [x] Remake Radio Burst script using CDF and online databases (7/8/2017)
  - [x] Use pycdf **(module: spacepy)** to read CDF data (7/6/2017)
  - [x] Push data into pandas dataframe (7/7/2017)
  - [x] Set up automated url inputs (7/8/2017)

- [x] Fix issues with matplotlib DateFormatter "year out of range" (7/5/2017)
  - [x] Added issue with null errors in data frames (7/5/2017)


- [x] Proton Flux (7/3/2017)
- [x] Neutron Monitor (7/3/2017)
- [x] Type III Radio Bursts (7/3/2017)

</p>
</details>

# Resolved Errors

<details><summary>Resolved Errors and Tasks</summary>
<p>


<details><summary>Key</summary>
<p>

### Error Name (Resolution Date)
* **Resolution**: Resolution Description
- Description of the error and preemptive ideas to solve the error

</p>
</details>


### A single radio burst event was separated into two detections (12/30/2017)
* **Resolution**: Increased the detection time from 5 minutes to 10 minutes. The entire radio burst is now detected as one event. 
- The threshold length is most likely too short, which means that there is a data gap longer than the threshold.
- Error can be recreated by running pandas_test_omni.py script for 20140901 or 20140910. The thresholds were set to "datetime.timedelta(minutes=5)". The specific lines of code are provided below.
- Increasing the threshold from 5 minutes to 10 minutes will most likely resolve the problem.

```python
...
    elif len(rb_list_temp) >= 1:
      if (i - rb_list_temp[-1]) <= datetime.timedelta(minutes=10): # originally 5 minutes
        rb_list_temp.append(i)

      elif (i - rb_list_temp[-1]) > datetime.timedelta(minutes=10): # originally 5 minutes
        if (rb_list_temp[-1] - rb_list_temp[0]) >= datetime.timedelta(minutes=10):
          rb_list_event.append(rb_list_temp)
          rb_list_temp = []
          rb_list_temp.append(i)

        elif (rb_list_temp[-1] - rb_list_temp[0]) < datetime.timedelta(minutes=10):
          rb_list_temp = []
          rb_list_temp.append(i)
...
```


### Change long plot option (09/20/2017)
* **Resolution**: Made an 'if' statement to change figure sizes according to the amount of datasets chosen. If there are more than 4 options, change the figure size.
- Change the current 'long_plot_option' to be an automated feature. Instead of setting a long plot, set up a statement that, 'if' there are more than 4 options, default the figure size from (10,6) to (10,12).

### Ordinal error for radio_remastered.py script (09/14/2017)
* **Resolution**: For this particular event, there is a lack of data. Instead of a '< 0' value, 0.0 is used. This creates a void in data when 0.0 values are dropped throughout the program and thus there are no ordinals for the program to plot. The program is set to plot data from the 0th hour to the 23rd hour, therefore the lack of data from 17-23 hr caused the ordinal error.

- Value error reached when plotting data for 20130929. This occurs when the values of the "data_rad1" is manipulated to be np.NaN values instead of 0.0. Removal of the line of code results in no errors and full script execution. Figure out why this occurs only for 20130929, possibly the values of the index are being turned into nan values.
```data_rad1[data_rad1 <= 0.0] = np.nan```
- Error can be emulated by running 'radio_event_remastered.py' for the day 20130929. The other events in the 'radio_list.txt' were commented out for testing.

```python
Plotting Type III Data: [20130929 21:00:00 -- 20130929 23:00:00]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/Users/bryanyamashiro/Documents/Research_Projects/Scripts/radio_event_remastered.py in <module>()
    250 
    251                 #plt.locator_params(axis='x', nbins=5)
--> 252                 plt.setp(ax.xaxis.get_majorticklabels(), rotation=0, horizontalalignment='center')

...

ValueError: ordinal must be >= 1
```

### For loops in GOES event detector (09/14/2017)
- Create a 'for' loop to iterate through the list of event dates and plot. Use slices of each event list, getting the first and last day of each event with [0] and [-1].


### Multiple event query for OMNI script (9/12/2017)
- Current script works for a single day. Increase the functionality by allowing for a list of dates to parse.

### Plot the Type III Radio Bursts in all frequencies (8/08/2017)
- Current correlations do not agree linearly between frequencies vs. intensities.
- Plot every frequency bin between 20 to 1040 individually.

### GOES legacy data (7/22/2017)
* **Resolution**: The GOES Proton script was broken up into two functioning scripts. Eventually the two scripts will be merged again, but since there is discrepancy between older GOES satellites, they were split. The older GOES satellites (8 and 10) do not have flux in specific energy bins, but rather energy ranges (i.e 80.0 - 165.0 MeV). This type of binning is discontinued in the GOES-13/15 satellites as each bin corresponds to one specific energy (i.e 165 MeV). Since the Wind satellite was functional in 1995 and beyond, the subplot functionality is kept with the Type III and solar wind data. Older neutron monitors were also online during the legacy period and older detectors can be selected.
- GOES proton flux data requires modifications to omni code. GOES-13 does not cover years in the early 2000's, therefore older GOES satellites must be used. Older satellites do not have full "new_data" as in the GOES-13 to GOES-15 models, therefore the time averaged data "new_avg" will be used, the specific energy range needs to be determined. Safeguards in the omni script to stop data collection from before 2011 must also be manipulated to allow for these dates. 


### Dynamic subplots and modifications to the Omni script (7/15/2017)
* **Resolution**: Set up a global variable to initialize a dynamic variable that would allow for slicing with a defined set. To make this work, the .axes slicing method was invoked, but required an overhaul on the plot function for each dataset (i.e. every plot function needed to be the same, with only the global index changing). Using the .axes slices allowed for subplots, but in turn, .plt functions did not edit all subplots. The .plt functions only edit the final added subplot, therefore changes must be added right after the plot function for each subplot using the .axes methods.

- Devise a way to plot selected datasets on subplots. The script runs with all data is loaded, but breaks with selections. Although the script is dynamic, there currently must be a static plot to host the first plot, and then subplots are appended to that "anchor" plot. Therefore, if the static anchor dataset is not chosen, the script cannot build on an empty canvas. The optimal solution seems to be unpacking different subplots (i.e. fig, (ax1, ax2, ...)). This solution requires that ax1, etc. must be literals and not strings, which removes options such as "for" loops with a list. An idea was to force a string to be a variable name, but this option should not be used if possible. A lambda function was also considered, but wildcard logic doesn't seem optimal for data frames while calling .index and columnized data.
- Minor tick gridlines for y-axis should be added with minorticks on. Add legends for each subplot and y-axis labels with units. but also reduce size of the legend and y-axis labels. Neutron monitor data seems to be cut off past the ~23 hour mark, include the rest of that data. Insert an "if" statement to deter plotting of neutron monitor data (long-term changes) and type III radio burst data (short-term changes) on the same canvas. 



### Set up online CDF reader through Python (7/8/2017)
* **Resolution**: Used wget instead of requests and urllib library. The .cdf is downloaded locally and removed after the data is inserted into a data variable.

- Add online functionality to ([radio_script_v2](https://github.com/byamashiro/Research_Projects/blob/master/Scripts/radio_remastered.py)). The script currently runs offline with local data files. Attempt was made using urllib and requests, but response is in binary/byte format and cannot be read with .json() methods. Possibly encode/decode into ascii format and run through CDF methods. **Note**: Each .cdf file might contain different versions (i.e _v02) for string recognition.
- The easier and less efficient option would be to download the data from each site and run the .cdf reader locally.


### Null values (resolved 7/5/2017)
* **Resolution**: There were three spaces in front of the null values, delimit whitespace to removed them. As a quick fix, 3 spaces were added to the 'na_values' argument, '   null', ``` na_values=['   null']```.  

- Some values are being registered as 'null'. Tried to add ``` na_values=['null']``` to the read_csv function, but the null is still being processed and results in a plotting error. To recreate error, run the 'pandas_test_nm.py' script for 20120307-20120309 (full) for stations (2) INVK and OULU.
- Resolution will probably consist of removing null values, list comprehension on all null values in pandas dataframe.  
```TypeError: Empty 'DataFrame': no numeric data to plot```

```python
                       OULU     INVK
datetime                            
2012-03-08 17:28:00  96.459  176.470
2012-03-08 17:29:00  98.389  173.920
2012-03-08 17:30:00  94.656     null
2012-03-08 17:31:00  92.282  172.800
2012-03-08 17:32:00  94.688  175.980
2012-03-08 17:33:00  97.718  175.790
2012-03-08 17:34:00  97.269  177.460
2012-03-08 17:35:00  98.304  176.330
```


### DateFormatter (resolved 7/5/2017)
* **Resolution**: Used the matplotlib plot function instead of the pandas plot function. The new function used was ``` plt.plot(nm_data.index, nm_data[f'{i}'], color=rand_color, label=f'{i}')``` instead of ``` nm_data[f'{i}'].loc[f'{event_obj_start_str_date}':f'{event_obj_end_str_date}'].plot(color=rand_color, label= f'{i}')```.

- Code breaks when trying to format the x-axis labels using the DateFormatter function from matplotlib in the script, 'pandas_test_nm.py'.
- Potentially the index are of a different definition, although each index shows the correct format 'yyyy-mm-dd hh:mm:ss' in the specified time interval between 20120307-20120309. Also test if delimiter could be changed to 'delim_whitespace=True' in read_csv function.  
```ValueError: year 60740 is out of range```

```python
import matplotlib.dates as mdates

myFmt = mdates.DateFormatter('%m/%d\n%H:%M')
ax.xaxis.set_major_formatter(myFmt) #this is line that breaks code (ValueError: year 60740 is out of range)
```

</p>
</details>
