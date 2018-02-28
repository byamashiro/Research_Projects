import pandas as pd
from os.path import dirname, join


data_to_generate = 'proton'
data_date = ['201106','201203','201409', '201205']

DATA_DIR = 'conversion_folder'

if data_to_generate == 'proton':
    for i in data_date:
        cpflux_names = ['time_tag','ZPGT1E_QUAL_FLAG', 'ZPGT1E', 'ZPGT5E_QUAL_FLAG', 'ZPGT5E', 'ZPGT10E_QUAL_FLAG', 'ZPGT10E', 'ZPGT30E_QUAL_FLAG', 'ZPGT30E', 'ZPGT50E_QUAL_FLAG', 'ZPGT50E', 'ZPGT60E_QUAL_FLAG', 'ZPGT60E', 'ZPGT100E_QUAL_FLAG', 'ZPGT100E', 'ZPGT1W_QUAL_FLAG', 'ZPGT1W', 'ZPGT5W_QUAL_FLAG', 'ZPGT5W', 'ZPGT10W_QUAL_FLAG', 'ZPGT10W', 'ZPGT30W_QUAL_FLAG', 'ZPGT30W', 'ZPGT50W_QUAL_FLAG', 'ZPGT50W', 'ZPGT60W_QUAL_FLAG', 'ZPGT60W', 'ZPGT100W_QUAL_FLAG', 'ZPGT100W', 'ZPEQ5E_QUAL_FLAG', 'ZPEQ5E', 'ZPEQ15E_QUAL_FLAG', 'ZPEQ15E', 'ZPEQ30E_QUAL_FLAG', 'ZPEQ30E', 'ZPEQ50E_QUAL_FLAG', 'ZPEQ50E', 'ZPEQ60E_QUAL_FLAG', 'ZPEQ60E', 'ZPEQ100E_QUAL_FLAG', 'ZPEQ100E', 'ZPEQ5W_QUAL_FLAG', 'ZPEQ5W', 'ZPEQ15W_QUAL_FLAG', 'ZPEQ15W', 'ZPEQ30W_QUAL_FLAG', 'ZPEQ30W', 'ZPEQ50W_QUAL_FLAG', 'ZPEQ50W', 'ZPEQ60W_QUAL_FLAG', 'ZPEQ60W', 'ZPEQ100W_QUAL_FLAG', 'ZPEQ100W']
        dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
        
        fname = f'goes_{i}.csv' # join(DATA_DIR, 'table_%s.csv' % ticker.lower())
        data = pd.read_csv(f'{DATA_DIR}/{fname}', skiprows=718, date_parser=dateparse, names=cpflux_names,index_col='time_tag', header=0)
    
        data = data['ZPGT100W']
    
        data.to_csv(f'conversion_folder/goes_modified_{i}.csv',sep=',',index=True)

elif data_to_generate == 'xray':
    
    xray_names = ['time_tag','A_QUAL_FLAG','A_NUM_PTS','A_AVG','B_QUAL_FLAG','B_NUM_PTS','B_AVG']

    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
    
    fname = f'goes_xray.csv' # join(DATA_DIR, 'table_%s.csv' % ticker.lower())
    data = pd.read_csv(f'{DATA_DIR}/{fname}', skiprows=167, date_parser=dateparse, names=xray_names,index_col='time_tag', header=0)

    data = data['A_AVG']

    data.to_csv('goes_modified_xray.csv',sep=',',index=True)