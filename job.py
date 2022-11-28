# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 18:39:39 2022

@author: Lenovo
"""
from pandas import *
import pandas as pd
import csv
import gmplot
# Open the csv file
data = pd.read_csv(r'city_location.csv')
interestingRow = data[data["City"] == "Kasarwadi"]
print (interestingRow)
interestingRow = interestingRow[data["Status"] == "Plumber"]
print (interestingRow)
df = interestingRow.drop(['ID', 'City', 'Status'], axis = 1)
print("--------------------------------------------------------")
print("Finding Location of Job:")
print("--------------------------------------------------------")
print(df)
df.to_csv('lat_long.csv', sep=',', encoding='utf-8', index=False)
# reading CSV file
data = read_csv("lat_long.csv")
 
# converting column data to list
Latitude_list = data['Latitude'].tolist()
Longitude_list = data['Longitude'].tolist()

gmapOne = gmplot.GoogleMapPlotter(18.606088, 73.822791, 15 )
gmapOne.scatter(Latitude_list,Longitude_list,'green', size=50, marker=True , symbol='o')
gmapOne.draw("map13.html")