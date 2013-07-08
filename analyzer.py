# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 16:48:06 2013

@author: dima
"""

import datareader as dr
import overlap as ol
import plotter as pl

def calculate_overlaps(drives, dist_tol, time_tol):
    """
    for each drive, determines and sets Overlap with all other drives
    """
    
    for i1 in range(len(drives)-1):
        d1 = drives[i1]
        
        for i2 in range(i1+1, len(drives)):
            d2 = drives[i2]
            
            #stop trying if d1 ends more than time_tol before d2 starts
            #note that drives are chronologically ordered
            if d2.coords[0].time - d1.coords[-1].time > time_tol:
                break
            
            overlap = ol.compute_overlap(d1, d2, dist_tol, time_tol)
            if overlap:
                ol1 = ol.Overlap(d1, d2, overlap[0], overlap[1])
                d1.append_overlap(ol1)
                ol2 = ol.Overlap(d2, d1, overlap[2], overlap[3])
                d2.append_overlap(ol2)     
                
    
def calculate_distances(drives):
    """
    for each drive, determines and sets distance
    """
    for d in drives:
        d.set_distance()

def main():
    drives = dr.read_data(open("gpsdata/all.tsv"), 1000)
    calculate_distances(drives)
    calculate_overlaps(drives, 0.01, 900)
    pl.distance_plot(drives)
    pl.max_overlap_fractions_plot(drives)    
    
main()