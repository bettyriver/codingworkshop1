#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:47:28 2023

# Determine Andromeda location in ra/dec degrees

@author: ymai0110
"""

from math import cos, pi
from random import uniform


def get_radec():
    '''
    Determine Andromeda location in ra/dec degress

    Returns
    -------
    ra : TYPE
        DESCRIPTION.
    dec : TYPE
        DESCRIPTION.

    '''
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'
    
    # convert to decimal degrees
    
    
    d, m, s = DEC.split(':')
    dec = int(d)+int(m)/60+float(s)/3600
    
    h, m, s = RA.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)
    return (ra,dec)


def make_stars(ra,dec,num_stars):
    
    '''return num_stars within 1 deg of Andromeda'''



    
    
    # make 1000 stars within 1 degree of Andromeda
    
    ras = []
    decs = []
    for i in range(num_stars):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))
    return (ras,decs)

nsrc = 1000000

if __name__=='__main__':

    ra, dec = get_radec()
    ras, decs = make_stars(ra, dec, num_stars=nsrc)
    
    
    # now write these to a csv file for use by my other program
    with open('catalog.csv','w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(nsrc):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    
    
# test


