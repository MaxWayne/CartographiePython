# -*- coding: utf-8 -*-

import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Open the earthquake data file.
filename = 'C:/Users/admin/Desktop/TestCluster.csv'

# Create empty lists for the data we are interested in.
lats, lons = [], []
radius = []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Ignore the header row.
    #next(reader)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        radius.append(float(row[2]))
        # Min & Max des longitudes et latitudes:
        longiMax = np.max(lons)
        longiMin = np.min(lons)
        latiMax = np.max(lats)
        latiMin = np.min(lats)

def get_marker_color(radius):
    if radius > 0.0:
        return (int(radius*220),'g',0.4)
    else:
        return ( 100,'r', 1)

# Make this plot larger.
plt.figure(figsize=(16,8))

eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 0.01,
                 llcrnrlon= longiMin - 2, llcrnrlat= latiMin - 2,
                 urcrnrlon= longiMax + 2, urcrnrlat= latiMax + 2)
eq_map.bluemarble()
eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
eq_map.drawparallels(np.arange(-90, 90, 30),labels=[0,0,0,1])

for lon, lat, rad  in zip(lons, lats, radius):
    x,y = eq_map(lon, lat)
    marker_radius, marker_color, marker_alpha = get_marker_color(rad)
    eq_map.scatter(x, y, s= marker_radius, c = marker_color, alpha = marker_alpha)
    
title_string = "Port Barhain: rule 0"

plt.title(title_string)

plt.show()