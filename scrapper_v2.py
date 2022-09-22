#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21: 13:51:15 2022
Dynamic Scraping of Power Outage Webage: Clients Without Service
@author: fernandoacosta-perez
"""

from re import L
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np
from datetime import datetime

# Step 0: Read Current Data
saved_data= pd.read_csv('no_service_data.csv')
now = str(datetime.now())

# Step 1: Deine the list of links that we want to scrape data
links= {'Arecibo':  'https://poweroutage.us/area/county/5468', 
        'Bayamon':  'https://poweroutage.us/area/county/5469',
        'Carolina': 'https://poweroutage.us/area/county/5471',
        'Caguas':   'https://poweroutage.us/area/county/5470',
        'Mayaguez': 'https://poweroutage.us/area/county/5472', 
        'Ponce':    'https://poweroutage.us/area/county/5473', 
        'San Juan': 'https://poweroutage.us/area/county/5474',
         }

# Step 2: Define the Xpath, in this case is equal for every link
customers_out_xpath= '/html/body/div[2]/table/tbody/tr[2]/td/div[3]'
customers_tracked_xpath= '/html/body/div[2]/table/tbody/tr[2]/td/div[2]'
last_update_xpath= '/html/body/div[2]/div[2]/div[4]/div/div[2]/item'

# Step 3: Scrape data
table_data= []
for county in list(links):
    row_data= []
    # Step 3.1: Access Power Outage page
    DRIVER_PATH = '/Users/fernandoacosta-perez/Downloads/edgedriver_mac64/msedgedriver'
    driver = webdriver.Edge(executable_path=DRIVER_PATH)
    driver.implicitly_wait(15)
    driver.get(links[county])

    # Step 2: Scrape Data
    #last_update= driver.find_element('xpath', last_update_xpath).get_attribute("value")
    customers_out= driver.find_element('xpath', customers_out_xpath).text
    customers_tracked= driver.find_element('xpath', customers_tracked_xpath).text

    # Step 3: Save Data
    saved_data.loc[len(saved_data.index)] = [now, county, customers_tracked, customers_out]

# Step 4: Save new data
saved_data.to_csv('no_service_data.csv', index= False)




