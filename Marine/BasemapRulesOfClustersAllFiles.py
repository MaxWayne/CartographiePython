# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:41:08 2015

@author: admin
"""

import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import os
from random import randint
from os import makedirs
from os.path import exists

# Open the earthquake data file.
filename = 'C:/Users/admin/Dropbox/Gotham/Parking/RulesGeoloc/'
pathDest = 'C:/Users/admin/Documents/PlanetWorld/MapClustersRulesParking/'

if not exists(pathDest):
    makedirs(pathDest)

# Create empty lists for the data we are interested in.
lats, lons = [], []
rayons = []
colorList = np.asarray(['go','ro','bo'])
compte = 0



ListFiles = os.listdir(filename)
ListAllClusters = []
for fileCluster in ListFiles:
    idCluster = fileCluster.find('_Rule')
    ListAllClusters.append(fileCluster[0:idCluster])

ListClusters = np.unique(ListAllClusters)

ListFiles = np.asarray(ListFiles)
for Cluster in ListClusters:
    IdCluster = np.nonzero(np.in1d(ListAllClusters,Cluster))[0]
    ListFilesCluster = ListFiles[IdCluster]
    
    latC, longC = Cluster.split('_')
    latC = float(latC)
    longC = float(longC)
    
    numRule = 0
    for filerule in ListFilesCluster:

        plt.figure(figsize=(16,12))
        
        eq_map = Basemap(projection='merc', resolution = 'h', area_thresh = 1.0,
                         llcrnrlon= longC - 30, llcrnrlat= latC - 25,
                         urcrnrlon= longC + 30, urcrnrlat= latC + 25)
        eq_map.drawcoastlines()
        eq_map.drawcountries()
        eq_map.fillcontinents(color = 'gray')
        eq_map.drawmapboundary()
        eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
        eq_map.drawparallels(np.arange(-90, 90, 30),labels=[1,0,0,0])
        
        cl = colorList[randint(0,2)]
        
        x,y = eq_map(longC, latC)
        eq_map.plot(x, y, 'yo', markersize = 20)
    
        f = filename + filerule
        with open(f) as lf:
            # Create a csv reader object.
            reader = csv.reader(lf)
            # Ignore the header row.
            # Store the latitudes and longitudes in the appropriate lists.
            numrow = 0
            for row in reader:
                if numrow != 0:
                    lats.append(float(row[0]))
                    lons.append(float(row[1]))
                    #rayons.append(float(row[0]))
                    # Min & Max des longitudes et latitudes:
                    longiMax = np.max(lons)
                    longiMin = np.min(lons)
                    latiMax = np.max(lats)
                    latiMin = np.min(lats)
                numrow += 1
            compte += 1

            for lon, lat in zip (lons, lats):
                x,y = eq_map(lon, lat)
                eq_map.plot(x, y, cl, markersize= 10)
                
        
        title_string = "Hadrian Marine : Rule " + str(numRule) + " of Cluster " + Cluster
        plt.title(title_string)
        
        plt.savefig(pathDest + Cluster + '_Rule_' + str(numRule) + '.png')
        numRule += 1
