#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:48:36 2020

@author: Ayca
"""

import textdistance
import itertools

def setDistance(x,distance):
    total = ["".join(seq) for seq in itertools.product("01", repeat=len(x))]
    l =[]
    for i in total:
        if textdistance.hamming(x,i)<=distance:
            l.append(i)
    return l
x = "1001000"
#find distance sets for both set y and set z
y_distance_set = setDistance(x, 1)
z_distance_set = setDistance(x, 3)

#we have string binary numbers, convert them to integer lists
#for perform xor operation
x = [int(i) for i in list(x)]

tmp =[]
for i in y_distance_set:
     tmp.append([int(j) for j in list(i)])
y_distance_set = tmp

tmp =[]
for i in z_distance_set:
     tmp.append([int(j) for j in list(i)])
z_distance_set = tmp

#perform xor operation with y_distance_set elements and x
#to find y_set
y_set = []
for i in y_distance_set:
    tmp =[]
    for j in range(0, len(x)):
        tmp.append(x[j]^i[j])
    y_set.append(tmp)

#perform xor operation with z_distance_set elements and x
#to find z_set
z_set = []    
for i in z_distance_set:
    tmp =[]
    for j in range(0, len(x)):
        tmp.append(x[j]^i[j])
    z_set.append(tmp)