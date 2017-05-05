# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:04:43 2015

@author: admin
"""
import os
import csv
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Open the earthquake data file.
foldername = 'C://Users/admin/Desktop/UnBateau/'

# Create empty lists for the data we are interested in.
listfiles = []
lats, lons = [], []
trajets = []
timestrings = []
colorList = np.asarray(['blueviolet','brown','coral','cyan','deeppink','forestgreen',
             'greenyellow','lime','orange','salmon','slategray','tomato',
             'turquoise','sienna','rosybrown','olive','magenta','linen','moccasin',
             'burlywood'])
listfiles = os.listdir(foldername)

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
for filename in listfiles:
    strTraj = filename.replace('.csv','')
    with open(foldername + filename) as lf:
            
        # Create a csv reader object.
        reader = csv.reader(lf)
    
        # Store the latitudes and longitudes in the appropriate lists.
        for row in reader:
            lats.append(float(row[3]))
            lons.append(float(row[4]))
            trajets.append(int(row[1]))
            timestrings.append(row[2])
            # Min & Max des longitudes et latitudes:
            longiMax = np.max(lons)
            longiMin = np.min(lons)
            latiMax = np.max(lats)
            latiMin = np.min(lats) 
        lats = np.asarray(lats)
        lons = np.asarray(lons)

    plt.figure(figsize=(16,9))
    
    eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 1.0,
                     llcrnrlon= longiMin - 3, llcrnrlat= latiMin - 3,
                     urcrnrlon= longiMax + 3, urcrnrlat= latiMax + 3)
    
    eq_map.drawcoastlines()
    eq_map.drawcountries()
    eq_map.fillcontinents(color = 'gray')
    eq_map.drawmapboundary()
    #eq_map.bluemarble()
    eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
    eq_map.drawparallels(np.arange(-90, 90, 30),labels=[0,0,0,1])
    
    UniqueTraj = np.unique(trajets)
    for traj in UniqueTraj:
        IdTraj = np.where(trajets == traj)[0]
        colo = colorList[traj]
        latLoc = lats[IdTraj]
        lonLoc = lons[IdTraj]
        
       
        msize = 8
        for lon, lat in zip(lonLoc, latLoc):
            x,y = eq_map(lon, lat)
            eq_map.plot(x, y, colo, markersize=msize)
            plt.legend('trajet ' + str(traj))
        title_string = "Marine Trajet " + strTraj
        plt.title(title_string)
         
        plt.show()