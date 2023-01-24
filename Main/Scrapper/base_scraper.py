import os
import datetime

from selenium import webdriver
from db import get_connection, get_cursor
import pandas as pd

class BaseScraper:
    def __init__(self):
        self.regions = self.get_regions_with_source_specific_id()
        source = self.get_source()
        self.source_name = source['source_name']
        self.source_url = source['source_url']
        self.driver = self.get_webdriver()
        self._data = pd.DataFrame(columns=["total_clients", "clients_without_power_service", "region_id", "source_last_updated_on"])
        self._data_fetched_on = datetime.datetime.now()

    def get_data_source_id(self):
        return self._data_source_id
    
    def get_regions_with_source_specific_id(self):
        with get_connection() as conn:
            with get_cursor(conn) as cursor:
                cursor.execute("""
                    SELECT *
                    FROM regions
                        NATURAL INNER JOIN source_region_mappings
                    WHERE source_id = %s
                """, [self.get_data_source_id()])
                return cursor.fetchall()
    
    def get_webdriver(self):
        DRIVER_PATH = os.getenv("SELENIUM_DRIVER_PATH")
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.implicitly_wait(15)
        return driver
    
    def get_source(self):
        with get_connection() as conn:
            with get_cursor(conn) as cursor:
                cursor.execute(""" 
                    SELECT *
                    FROM data_sources
                    WHERE source_id = %s
                """, [self.get_data_source_id()])
                return cursor.fetchone()

    def save_to_database(self):
        for row in self._data.to_dict(orient='records'):
            self.insert_data_outage_row(row)

    def insert_data_outage_row(self, row):
        with get_connection() as conn:
            with get_cursor(conn) as cursor:
                cursor.execute("""
                    INSERT INTO outage_data 
                    (total_clients, clients_without_power_service, 
                    region_id, source_id,
                     source_last_updated_on, data_fetched_on)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, [row['total_clients'], row['clients_without_power_service'],
                 row['region_id'], self.get_data_source_id(),
                  row['source_last_updated_on'], self._data_fetched_on])
                conn.commit()
    
    def save_to_csv(self):
        self._data.to_csv('no_service_data.csv', index= False)

    def scrape(self):
        raise NotImplementedError()