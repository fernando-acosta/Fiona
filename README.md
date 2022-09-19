# Fiona
Fiona is a computer program that scrapes outages data from Luma power outages webpage (Luma is the current power distribution operator in Puerto Rico as of september 2022). Puerto Rico has a long history with hurracaines, and this repository was created in response the hurricane Fiona, a category one hurricane that landed in Puerto Rico during the afternoon of September 18, 2022. The purpose of this computer program is to construct a time series dataset with information about clients without service as a function of time. This information is not currently  available online.

 ## What can we do with Fiona?
The Fiona computer program will enable us to construct a dataset to answer questions like: how long it will take to bring back up the power grid? What regions take more time to connect? The dataset will be constructed by running the script on a recurring basis. For now, the run will be performed manually, but eventually a server could be used to run the script automatically. 

## Data source
This the webpage being scraped: https://miluma.lumapr.com/outages/clientsWithoutService. It presents real time data on the effect of power outages in the different regions of Puerto Rico. See the following example:

<p align="center">
<img src="https://github.com/fernando-acosta/Fiona/blob/b43114aec5037c1cba61c27e64d3c81c2faa3af0/Pictures/luma.png"/>
</p>
