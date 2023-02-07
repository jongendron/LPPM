# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:35:27 2023

@author: jonge
"""

import json
import urllib.request

#json_data_source = 'temperature_anomaly.json'
#json_data_source = 'https://www.ncdc.noaa.gov/cag/time-series/global/globe/land_ocean/ytd/12/1880-2021/data.json'
#https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series
json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/national/time-series/110/tavg/1/12/1895-2022.json?base_prd=true&begbaseyear=1901&endbaseyear=2000'

#%% read local file
#with open(json_data_source, encoding='utf-8') as data:
#    anomalies = json.load(data) # load data and decode from json

#%% read remote input stream (file) from url
with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8') # string: must decode after reading instead of up-front and save as string
    anomalies = json.loads(data) # json.loads and json.dumps read and write strings in json format rather than file

#%%
#print(anomalies['description'])
#print(anomalies['citation'])
for yrmo, dat in anomalies['data'].items():
    yr, mo = int(yrmo[:4]), int(yrmo[4:])
    value, anomaly = float(dat['value']), float(dat['anomaly'])
    print(f'{yr} ... {mo} ... {value:6.2f} ... {anomaly:6.2f}')
print('*' * 80)

