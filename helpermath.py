# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 22:41:37 2013

@author: dima
"""

import math

def haversine_dist(gpsa, gpsb):
    """
    determines distance by haversine formula.
    returns distance in miles.
    """
    lata, latb, lona, lonb =  map(math.radians, 
                                  [gpsa.lat, gpsb.lat, gpsa.lon, gpsb.lon])
    dlat, dlon = latb - lata, lonb - lona
    a = math.sin(dlat)**2 + math.cos(lata)*math.cos(latb)*math.sin(dlon)**2
    arc = 2*math.asin(math.sqrt(a))
    return arc*3961.3