# -*- coding: utf-8 -*-
"""
Data Visualizations

Author: Fernando A. Acosta-Perez
"""

import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

class visualize:
    
    def __init__(self, data):
        """
        Parameters
        ----------
        data : Power outage data gathered from the web scrapper. 

        Returns
        -------
        None.

        """
        self.data=data
        
    def HistClientsWithoutService(self, regions= None, start_date= None, end_date= None):
        """
        Chart Descritpion: This plot will showcase the total number of clients without power as a function of time.
        It can also be stratified by regions and a date range.
        
        Parameters
        ----------
        regions : TYPE, list of strings
            DESCRIPTION. A list with the regions that will be included in the visualization.
            
        start_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The first date that the visualization will consider. 
            If None, it will use the earliest available date in the data.
            
        end_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The last date that the visualization is considered.
            If None, it will use the latest available date in the data.

        Returns
        -------
        fig: Interactive plotly figure that can be deployed in a web app
        """
        
        # Filter data based on the selected dates
        if regions != None:
            self.data=self.data[self.data['region_id'].isin(regions)].copy()
        
        if start_date != None:
            self.data=self.data[self.data['data_fetched_on']>=start_date]
        
        if end_date != None:
            self.data=self.data[self.data['Datetime']<=end_date]
            
        # Add calculated field
        self.data['Porcentaje de Recuperacion']= (1-self.data['clients_without_power_service']/self.data['total_clients'])
        self.data['data_fetched_on'] = pd.to_datetime(self.data['data_fetched_on'])
        self.data= self.data.sort_values(by= 'data_fetched_on')
        
        # Make plot
        plt.Figure()
        fig= px.line(self.data, x= 'data_fetched_on', y= 'Porcentaje de Recuperacion', color= 'region_id', labels= {'data_fetched_on': ''})
        plt.show()
        plt.close()
        
        return fig
        
    
    def SignificantOutages(self, regions= None, start_date= None, end_date= None):
        """
        
        Chart Descritpion: This plot will showcase the total number of significant outages by region in the defined date range.
        A significant outage is an event in which more than 5% of the total population of a region had no service. 

        Parameters
        ----------
        regions : TYPE, list of strings
            DESCRIPTION. A list with the regions that will be included in the visualization.
            
        start_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The first date that the visualization will consider. 
            If None, it will use the earliest available date in the data.
            
        end_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The last date that the visualization is considered.
            If None, it will use the latest available date in the data.

        Returns
        -------
        fig: Interactive plotly figure that can be deployed in a web app

        """
        
        
        # Filter data based on the selected dates
        if regions != None:
            self.data=self.data[self.data['region_id'].isin(regions)].copy()
        
        if start_date != None:
            self.data=self.data[self.data['data_fetched_on']>=start_date]
        
        if end_date != None:
            self.data=self.data[self.data['data_fetched_on']<=end_date]
            
        # Add Calculated field
        self.data['Porcentaje de Recuperacion']= (1-self.data['clients_without_power_service']/self.data['total_clients'])
        self.data['data_fetched_on'] = pd.to_datetime(self.data['data_fetched_on'])
        self.data['Significant Outage']= (self.data['Porcentaje de Recuperacion'] <= 0.95)
        
        # Grouped Data
        grouped_data= self.data[['region_id', 'Significant Outage']].groupby(by= ['region_id'], as_index=False).sum()
        grouped_data= grouped_data.sort_values(by= 'Significant Outage', ascending= False)
        # Plot Bar
        fig= px.bar(grouped_data, x= 'region_id', y= 'Significant Outage')
        
        return fig
            
    
    def MeanClientsNoService(self, regions= None, start_date= None, end_date= None):
        """
        
        Chart Descritpion: This plot will showcase the average number of people without service by region in a defined date range.
        A significant outage is an event in which more than 5% of the total population of a region had no service. 
        
        start_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The first date that the visualization will consider. 
            If None, it will use the earliest available date in the data.
            
        end_date : TYPE, date time string 'mm/dd/yyyy'
            DESCRIPTION. The last date that the visualization is considered.
            If None, it will use the latest available date in the data.

        Returns
        -------
        fig: Interactive plotly figure that can be deployed in a web app
        """
        
        # Filter data based on the selected dates
        if regions != None:
            self.data=self.data[self.data['region_id'].isin(regions)].copy()
        
        if start_date != None:
            self.data=self.data[self.data['data_fetched_on']>=start_date]
        
        if end_date != None:
            self.data=self.data[self.data['data_fetched_on']<=end_date]
            
        # Add Calculated field
        self.data['Porcentaje de Recuperacion']= (1-self.data['clients_without_power_service']/self.data['total_clients'])
        self.data['data_fetched_on'] = pd.to_datetime(self.data['data_fetched_on'])
        self.data['Significant Outage']= (self.data['Porcentaje de Recuperacion'] <= 0.95)
        
        # Grouped Data
        grouped_data= self.data[['region_id', 'Porcentaje de Recuperacion']].groupby(by= ['region_id'], as_index=False).mean()
        grouped_data= grouped_data.sort_values(by= 'Porcentaje de Recuperacion', ascending= False)
        
        # Plot Bar
        fig= px.bar(grouped_data, x= 'region_id', y= 'Porcentaje de Recuperacion')
        
        return fig
    
# Read Data
data= pd.read_csv('outage_data.csv')

# Test the class
chart= visualize(data)
chart.HistClientsWithoutService()
chart.SignificantOutages()
chart.MeanClientsNoService()



