# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 23:58:42 2013

@author: dima
"""

import helpermath as hm
import onedrive as od

class Overlap:
    """
    given drives da and db, and their corresponding timeseries coordinates
    da_i and db_i, the Overlap is the longest segment {da_i->da_j},
    such that there exists a segment db_k->db_l and
        
    *distance between da_i and db_k is less than dist_tol
    *time between da_i and db_k is less than time_tol
    *distance between da_j and db_l is less than dist_tol
    *time between da_j and db_l is less than time_tol
    
    note that we presently don't care about the proximity of intermediate
    points
    """
    def __init__(self, da, db, start, end):
        olap_id = str(da.drive_id)+":"+str(db.drive_id)
        self.od = od.OneDrive(olap_id)
        for pt in da.coords:
            if pt.time >= start.time and pt.time <= end.time:
                self.od.append_coord(pt)
        self.od.set_distance()
    
def compute_overlap(da, db, dist_tol, time_tol):
    """
    returns the TimeGps set [da_i, da_j, db_k, db_l] or False if no overlap
    """
    
    #look for matches by time and distance
    matches = []
    for pta in da.coords:
        for ptb in db.coords:
            
            #times are chronological
            if ptb.time-pta.time > time_tol:
                break
            if pta.time-ptb.time > time_tol:
                continue
            
            if hm.approx_dist(pta.gps, ptb.gps) < dist_tol:
                matches.append([pta, ptb])
            
    #determine the furthest apart pair of matches
    largest_dist = 0
    furthest_pair = False
    for pair1 in matches:
        for pair2 in matches:
            this_dist = hm.haversine_dist(pair1[0].gps, pair2[0].gps)
            if this_dist > largest_dist:
                largest_dist = this_dist
                furthest_pair = [pair1[0], pair2[0], pair1[1], pair2[1]]
                
    return furthest_pair