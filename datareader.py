# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 15:56:56 2013

@author: dima
"""

import csv
import onedrive

def read_gps(gpsstr):
    """
    input gpsstr is [latstr, lonstr]
    """
    return onedrive.Gps(float(gpsstr[0]), float(gpsstr[1]))
    
def read_time(timestr):
    """
    this converts the time string in the input data to seconds since 
    0:00:00 1/1/2007 utc.  
    note that the time is not real;  see gpsdata/readme.txt for details
    
    we do this hack instead of using dateutil.parser because we don't need
    to allow for multiple formats/timezones and dateutil.parser is very slow.
    """
    return (int(timestr[8:10])-1)*86400+int(timestr[11:13])*3600+ \
           int(timestr[14:16])*60+int(timestr[17:19])

def read_data(datafile):
    """
    returns {drive_id:OneDrive} gathered from the input datafile
    note: currently takes about 4 min to run for all data
    """

    drives = {}
    everything = csv.reader(datafile, delimiter='\t')
    
    for row in everything:
        drive_id = int(row[0])
        datetime = read_time(row[1])
        gps = read_gps(row[2:4])
        
        if drive_id in drives:
            drives[drive_id].append(datetime, gps)
        else:
            drives[drive_id] = onedrive.OneDrive(drive_id)
    
    return drives
