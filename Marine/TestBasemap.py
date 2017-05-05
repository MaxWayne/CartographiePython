# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:24:12 2015

@author: Max
"""

import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Open the earthquake data file.
filename = 'C:/Users/admin/Desktop/SusGeolocByTypes/_TBq_dL9JKhzLg8jerLbuCZj24YT1uojzvYEiiZ-qT0.csv'
# Create empty lists for the data we are interested in.
lats, lons = [], []
TypeMove = []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        TypeMove.append(row[2])
        # Min & Max des longitudes et latitudes:
        longiMax = np.max(lons)
        longiMin = np.min(lons)
        latiMax = np.max(lats)
        latiMin = np.min(lats)

def get_marker_color(typeMove):
        if typeMove == 'Boucle':
            return ('go',5)
        elif typeMove == 'Trajets':
            return('yo',6)
        else:
            return('ro',8)


# Make this plot larger.
plt.figure(figsize=(16,8))

eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 10.0,
                 llcrnrlon= longiMin - 14, llcrnrlat= latiMin - 14,
                 urcrnrlon= longiMax + 14, urcrnrlat= latiMax + 14)
eq_map.bluemarble()
eq_map.drawcoastlines()
eq_map.drawcountries()
#eq_map.fillcontinents(color = 'lightgray')
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
eq_map.drawparallels(np.arange(-90, 90, 30),labels=[0,0,0,1])

for lon, lat, typ  in zip(lons, lats, TypeMove):
    x,y = eq_map(lon, lat)
    #marker_string, marker_size = get_marker_color(dat)
    eq_map.plot(x, y, 'ro', markersize=20)
title_string = "_TBq_dL9JKhzLg8jerLbuCZj24YT1uojzvYEiiZ-qT0"
#title_string += "%s through %s" % (timestrings[-1][:10], timestrings[0][:10])
plt.title(title_string)

plt.show()