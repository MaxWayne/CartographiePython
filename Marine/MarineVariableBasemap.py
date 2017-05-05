# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:41:11 2015

@author: admin
"""

import csv
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Open the earthquake data file.
filename = 'C:/Users/admin/Desktop/IMO_Suspect_Port/9levVMcuXMDmYGkB0dy4l3ETVMEdCl80JmutnKFDfjk.csv'

# Create empty lists for the data we are interested in.
lats, lons, trajs = [], [], []
rayons = []
colorList = np.asarray(['blueviolet','brown','coral','cyan','deeppink','forestgreen',
             'greenyellow','lime','orange','salmon','slategray','tomato',
             'turquoise','sienna','rosybrown','olive','magenta','linen','moccasin',
             'burlywood'])

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open(filename) as f:
    # Create a csv reader object.
    reader = csv.reader(f)
    
    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        lats.append(float(row[1]))
        lons.append(float(row[2]))
        trajs.append(float(row[0]))

    # Min & Max des longitudes et latitudes:
    longiMax = np.max(lons)
    longiMin = np.min(lons)
    latiMax = np.max(lats)
    latiMin = np.min(lats)      
    lats = np.asarray(lats)
    lons = np.asarray(lons)
    trajs = np.asarray(trajs).astype(int)


# Make this plot larger.



UniqueTrajs = np.unique(trajs)
for traj in UniqueTrajs:
    
    plt.figure(figsize=(16,8))
    
    eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 1.0,
                     llcrnrlon= longiMin - 2, llcrnrlat= latiMin - 2,
                     urcrnrlon= longiMax + 2, urcrnrlat= latiMax + 2)
    #              lat_0=0, lon_0=-130)
    eq_map.drawcoastlines()
    eq_map.drawcountries()
    eq_map.fillcontinents(color = 'gray')
    eq_map.drawmapboundary()
    eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,1,0])
    eq_map.drawparallels(np.arange(-90, 90, 30),labels=[0,0,0,1])    

    IdTraj = np.where(trajs == traj)[0]
    trajLoc = trajs[IdTraj]
    lonsLoc = lons[IdTraj]
    latsLoc = lats[IdTraj]
     
    X = lonsLoc[0:-1]
    X = X.reshape(len(X),1)
    Y = latsLoc[0:-1]
    Y = Y.reshape(len(Y),1)
    U = lonsLoc[1:]
    U = U.reshape(len(U),1)
    V = latsLoc[1:]
    V = V.reshape(len(V),1)
    #variable de la couleur:
    C = trajLoc


    MatLons = np.append(X,U,axis = 1)
    MatLats = np.append(Y,V,axis = 1)
    for matLon, matLat, colo in zip(MatLons, MatLats, C):
        lon0 = matLon[0]
        lon1 = matLon[1]
        lat0 = matLat[0]
        lat1 = matLat[1]
        
        x,y = eq_map(lon0, lat0)
        u,v = eq_map(lon1, lat1)
        cololor = colorList[colo]
        
        eq_map.quiver(x, y, u, v, linewidth = 0.25, color = cololor)
        
    title_string = "Hadrian Marine Clusters"
    #title_string += "%s through %s" % (timestrings[-1][:10], timestrings[0][:10])
    plt.title(title_string)
    
    plt.show()