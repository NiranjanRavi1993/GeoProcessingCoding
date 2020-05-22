
import pandas as pd
import numpy as np
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import folium
from folium.plugins import FastMarkerCluster
import os
import webbrowser
locator = Nominatim(user_agent="myGeocoder")


excel_file = "C:/Users/Acer/Desktop/test/sampletestCSV.csv"
readOp = pd.read_csv(excel_file)
"""
readOp = readOp[(readOp.matrix == "well") | (readOp.matrix == "water")]
readOp['State']="Indiana, USA"
readOp['address'] =readOp['site'].str.cat(readOp['location'], sep=", ")
readOp['address'] =readOp['address'].str.cat(readOp['State'], sep=", ")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(locator.geocode, min_delay_seconds=5)
readOp['location'] = readOp['address'].apply(geocode)
readOp['point'] = readOp['location'].apply(lambda loc: tuple(loc.point) if loc else None)

readOp[['latitude', 'longitude', 'altitude']] = pd.DataFrame(readOp['point'].tolist(), index=readOp.index)

readOp.to_csv('C:/Users/Acer/Desktop/test/extracted_csv_new.csv', index = False)

folium_map = folium.Map(location=[39.7683331,-86.1583502],
                        zoom_start=250,
                        tiles='CartoDB dark_matter')


FastMarkerCluster(data=list(zip(readOp['latitude'].values, readOp['longitude'].values))).add_to(folium_map)
folium.LayerControl().add_to(folium_map)

filepath = 'C:/Users/Acer/Desktop/test/map.html'
m = folium.Map()
m.save(filepath)
webbrowser.open('file://' + filepath)
"""
readOp['collector'] = np.where(readOp['collector'] == "Billy","Basiccc", readOp['collector'] )
readOp.to_csv('C:/Users/Acer/Desktop/test/dropna.csv', index = False)
readOp.groupby['binary'].mean()
readOp.head()
