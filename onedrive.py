# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 16:46:53 2013

@author: dima
"""
import helpermath as hm

class Gps:     
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class TimeGps:
    def __init__(self, time, gps):
        self.time = time
        self.gps = gps


class OneDrive:
    """
    OneDrive is an ordered list of TimeGps coordinates.
    
    We also store other information about the drive as it becomes available.
    """
            
    def __init__(self, drive_id):
        self.drive_id = drive_id
        self.coords = []
        self.overlaps = []
    
    def append_coord(self, timegps):
        self.coords.append(timegps)
    
    def set_distance(self):
        cum_dist = 0
        for i in range(len(self.coords)-1):
            cum_dist += hm.haversine_dist(self.coords[i].gps, 
                                          self.coords[i+1].gps)
        self.distance = cum_dist
    
    def append_overlap(self, olap):
        self.overlaps.append(olap)
    
    
        