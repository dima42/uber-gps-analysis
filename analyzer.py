# -*- coding: utf-8 -*-
"""
Created on Sun Jul 07 16:48:06 2013

@author: dima
"""

import datareader

def main():
    drives = datareader.read_data(open("gpsdata/all.tsv"))

main()