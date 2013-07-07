# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 16:46:53 2013

@author: dima
"""

class Gps:     
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class OneDrive:
    """
    OneDrive is an ordered list of TimeGps coordinates.
    """
    
    class TimeGps:
        def __init__(self, datetime, gps):
            self.datetime = datetime
            self.gps = gps
            
    def __init__(self, drive_id):
        self.drive_id = drive_id
        self.coords = []
    
    def append(self, datetime, gps):
        self.coords.append(self.TimeGps(datetime, gps))