#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:51:15 2022
Dynamic Scraping of LUMA Webage: Clients Without Service
@author: fernandoacosta-perez
"""

from itertools import product
import pandas as pd
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
from datetime import datetime

# Get Date
now = str(datetime.now())

DRIVER_PATH = '/Users/fernandoacosta-perez/Downloads/edgedriver_mac64/msedgedriver'
driver = webdriver.Edge(executable_path=DRIVER_PATH)
driver.implicitly_wait(15) 
driver.get("https://miluma.lumapr.com/outages/clientsWithoutService")

# Step 1: Getting data
table_data= []
for region in range(2,9):
    region_data= [now]
    for field in range(1, 4):
        data= driver.find_element('xpath', '//*[@id="root"]/div/div[2]/main/div/div/div[' + str(region) + ']/div[' +str(field)+ ']').text
        region_data.append(data)
    table_data.append(region_data)

# Step 2: Save Data
saved_data= pd.read_csv('no_service_data.csv').values
table_data= np.concatenate((saved_data, np.array(table_data)), axis=0)
table_data_df= pd.DataFrame(data= table_data, columns= ['Datetime', 'Region', 'Total de Clientes', 'Clientes sin Servicio'])
table_data_df.to_csv('no_service_data.csv', index= False)
