#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:53:33 2022
Analysis
@author: fernandoacosta-perez
"""

from db import get_connection, get_cursor
import pandas as pd

# Set enviroment Variables
import os
os.environ['SELENIUM_DRIVER_PATH']='/home/ec2-user/Fiona/chromedriver'
os.environ['DB_HOST']='ec2-35-171-25-246.compute-1.amazonaws.com'
os.environ['DB_NAME']='Fiona'
os.environ['DB_USER']='fiona_user'
os.environ['DB_PASSWORD']='iK7oHQ7m#5HO'
os.environ['DB_PORT']='5432'

with get_connection() as conn:
    with get_cursor(conn) as cursor:
        cursor.execute(""" 
            SELECT *
            FROM outage_data
        """)
        data= pd.DataFrame(cursor.fetchall())
        
