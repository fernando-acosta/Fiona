#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:53:33 2022
Analysis
@author: fernandoacosta-perez
"""

from db import get_connection, get_cursor
import pandas as pd

with get_connection() as conn:
    with get_cursor(conn) as cursor:
        cursor.execute(""" 
            SELECT *
            FROM outage_data
        """)
        data= pd.DataFrame(cursor.fetchall())
        
