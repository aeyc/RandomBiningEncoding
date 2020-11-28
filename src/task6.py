#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:56:52 2020

@author: Ayca
"""
import task3
import task5
import random
from matplotlib import pyplot
import math

u_dict = dict()
u_dict = {}
vect_z = []


#every u can be mapped to 2^4 different x values
#e.g u = '000' x = {0, 1, 2, 4, 8, 16, 32, 63, 64, 95, 111, 119, 123, 125, 126, 127}
#e.g u = '101' x = {10, 21, 34, 40, 42, 43, 46, 58, 69, 81, 84, 85, 87, 93, 106, 117}
# p(u=a) = 1/8 -> u = {'000', '001', '010', '011', '100', '101', '110', '111'}
# p(x=b|u=a) = p(x=b&u=a)/p(u=a) = [(1/16)(1/8)]/(1/8) = 1/16

for number in range(2**7):
    x = "{0:07b}".format(number)
    #task3
    u = task3.decrypt(x.strip()) 
    if u in u_dict:
        u_dict[u].append(int(x,2))
    else:
        u_dict[u] = [int(x,2)]
    z_dict = dict()
    z_dict = {}
    for i in range(10**4):
        #if epsilon < delta -> no secrecy possible
        epsilon = round(random.uniform(0, 0.5), 2) #random float number with 2 decimal places
        delta = round(random.uniform(0, 0.5), 2)
        y = task5.flipBinStr(x, epsilon)
        z = task5.flipBinStr(x, delta)
        vect_z.append(z)

#|Z| = 128, |Y| = 128
        
print("")

pyplot.hist(vect_z, bins=2**7)
pyplot.show()


from collections import Counter
dict_z = Counter(vect_z)



