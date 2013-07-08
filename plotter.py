# -*- coding: utf-8 -*-
"""
Created on Mon Jul 08 01:21:36 2013

@author: dima
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def distance_plot(drives):
    distances = []
    for d in drives:
        distances.append(d.distance) 
    distances.sort()
    
    X = np.arange(1, 0, -1.0/len(drives))
    Y = np.array(distances)

    plt.plot(X, Y)
    plt.title("distances of uber rides cdf")
    plt.xlabel("fraction of rides longer than this")
    plt.ylabel("distance (mi) ")
    ax = plt.axes()
    ax.set_yscale("log")
    ax.set_yticks([0.5, 1, 1.5, 2.5, 5, 10, 20])
    ax.get_yaxis().set_major_formatter(mpl.ticker.ScalarFormatter())
    plt.xlim(0, 1)
    plt.ylim(0.5, 25)
    plt.show()

    
def max_overlap_fractions_plot(drives):
    
    max_overlap_fractions = []
    for d in drives:
        if d.distance == 0:
            continue
        max_d = 0
        for olap in d.overlaps:
            if olap.od.distance > max_d:
                max_d = olap.od.distance
        max_overlap_fractions.append(max_d / d.distance)
    max_overlap_fractions.sort()
    
    X = np.arange(1, 0, -1.0/len(max_overlap_fractions))
    Y = np.array(max_overlap_fractions)
    plt.plot(X, Y)
    plt.title("overlaps of uber rides cdf")
    plt.xlabel("fraction of rides overlapping more than this")
    plt.ylabel("overlap fraction")
    plt.xlim(0, 1)
    plt.show()
    