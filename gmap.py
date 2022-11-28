# -*- coding: utf-8 -*-
"""
Created on Thu May 27 17:39:07 2021

@author: srcdo
"""

import gmplot

# lat = [19.0790 , 19.0810 , 19.0850]
# lang = [72.890, 72.910, 72.930]
lat1 = [19.0790]
lang1 = [72.890]
lat2 = [19.0810]
lang2 = [72.910]
gmapOne = gmplot.GoogleMapPlotter(19.0760, 72.8777, 15 )
gmapOne.scatter(lat1,lang1,'green', size=50, marker=True , symbol='o')
#gmapOne.plot(lat1,lang1,'green',edge_width=2.5)
gmapOne.scatter(lat2,lang2,'red', size=50, marker=True , symbol='o')
#gmapOne.plot(lat2,lang2,'red',edge_width=2.5)
gmapOne.draw("map.html")