# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 15:56:56 2013

@author: dima
"""

import csv
import dateutil.parser
import onedrive

def read_gps(gpsstr):
    """
    input gpsstr is [latstr, lonstr]
    """
    return onedrive.Gps(float(gpsstr[0]), float(gpsstr[1]))

def read_data(datafile):
    """
    returns {drive_id:OneDrive} gathered from the input datafile
    note: currently takes about 4 min to run for all data
    """

    drives = {}
    everything = csv.reader(datafile, delimiter='\t')
    
    for row in everything:
        drive_id = int(row[0])
        datetime = dateutil.parser.parse(row[1])
        gps = read_gps(row[2:4])
        
        if drive_id in drives:
            drives[drive_id].append(datetime, gps)
        else:
            drives[drive_id] = onedrive.OneDrive(drive_id)
    
    return drives
