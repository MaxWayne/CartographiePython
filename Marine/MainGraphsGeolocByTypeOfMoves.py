# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:24:12 2015

@author: admin
"""

import csv
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

from os import listdir, makedirs
from os.path import isfile, join, exists

def readTxtFileX(fileName,strCharRet,strEmpty,strDelimiter):
    ins = open( fileName, "r" )
    Tab = []
    for line in ins:
        Tab.append( line )
    ins.close()
    X = []
    for t in Tab:
        temp = t.replace(strCharRet,"")
        temp2 = temp.replace(strEmpty,"")
        temp2 = temp2.split(strDelimiter)
        X.append(temp2[0:])
        
    return np.asarray(X)
    

# Open the earthquake data file.
mypathSusGeolocByTypes = 'C:/Users/admin/Desktop/SusGeolocByTypes/'
IMOsSus = [ f.replace('.csv','') for f in listdir(mypathSusGeolocByTypes) if isfile(join(mypathSusGeolocByTypes,f)) ]

pathDest = 'C:/Users/admin/Desktop/MapsGeolocByTypes/'

for imo in IMOsSus:
    filename = mypathSusGeolocByTypes + imo + '.csv'
    
    X = readTxtFileX(filename,'\n','',',')
    if len(X) <= 5000000:
        lats = X[1:,0].astype(float)
        lons = X[1:,1].astype(float)
        types = X[1:,2]
        
        longiMin = np.min(lons)
        longiMax = np.max(lons)
        
        latiMin = np.min(lats)
        latiMax = np.max(lats)
        
        def get_marker_color(typeMove):
            if typeMove == 'Boucle':
                return ('go',15)
            elif typeMove == 'Trajets':
                return('yo',12)
            else:
                return('ro',6)
        
        
        # Make this plot larger.
        plt.figure(figsize=(16,8))
        
        eq_map = Basemap(projection='merc', resolution = 'l', area_thresh = 10.0,
                         llcrnrlon= longiMin - 5, llcrnrlat= latiMin - 5,
                         urcrnrlon= longiMax + 5, urcrnrlat= latiMax + 5)
        eq_map.bluemarble()
        eq_map.drawcoastlines()
        eq_map.drawcountries()
        #eq_map.fillcontinents(color = 'lightgray')
        eq_map.drawmapboundary()
        eq_map.drawmeridians(np.arange(0, 360, 30),labels=[0,0,0,1])
        eq_map.drawparallels(np.arange(-90, 90, 30),labels=[0,0,0,1])
        
        for lon, lat, typeMove  in zip(lons[0:30], lats[0:30], types[0:30]):
            x,y = eq_map(lon, lat)
            marker_string, marker_size = get_marker_color(typeMove)
            eq_map.plot(x, y, marker_string, markersize=marker_size)
        title_string = 'Geolocalisation for imo : ' + imo
        
        plt.title(title_string)

        plt.savefig(pathDest + imo + '.png')