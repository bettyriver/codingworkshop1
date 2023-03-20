#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:47:28 2023

# Determine Andromeda location in ra/dec degrees

@author: ymai0110
"""

from math import cos, pi
from random import uniform


# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

# convert to decimal degrees


d, m, s = DEC.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = RA.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

nsrc = 1000000

# make 1000 stars within 1 degree of Andromeda

ras = []
decs = []
for i in range(nsrc):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
f = open('catalog.csv','w')
print("id,ra,dec", file=f)
for i in range(nsrc):
    print("{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
    
    
# test


