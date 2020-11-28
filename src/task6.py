#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:56:52 2020

@author: Ayca
"""
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

#%%
"""


ALL UPPERCASE METHODS ARE PSEUDO


"""
#lim_(n->infinite) P[û != u] = 0


for number in range(2**3): 
    #calculate u with decoder implemented in task5
    error_counter = [] #per bits?
    for length in range(7,10**6): ##of bits of x start from 7 to some value
        x = ENCODER_TASK5(u,length) #length = # of bits of x
        u_decoded = DECODER_TASK5(x)
        u = "{0:04b}".format(number)
        if HAMMING_DISTANCE(u,u_decoded) != 0: #should we use bitwise comparison here??
            error_counter.append(HAMMING_DISTANCE(u,u_decoded))
    
    #plot for each u
    pyplot.hist(error_counter, bins=2**3)
    pyplot.show()
    
#%%    
#Mutual Information lim_(n->infinite) I(u;z) = 0
#I(u;z) = H(z) - H(z|u)
#H(z) = -(sum[p(z)*log_2 p(z)] for all z in Z)
#H(z|u) = sum[p(u)*H(z| u=a)] for all u in U
#I(u;z) = H(z) + H(u) - H(u,z)
#Also I(u;z) can be represented w/same formula in task4
#ref: https://www2.isye.gatech.edu/~yxie77/ece587/Lecture2.pdf
    
from collections import Counter
dict_z = Counter(vect_z)
inf = 0

#WILL CALCULATE BELOW VALUES
p_u = 
p_uz = 
cardinality_z = 
for i in dict_z.keys():
    tmp = (p_u*(dict_z[i]/cardinality_z) #p(u)*p(z)
    tmp = (p_uz)/tmp
    inf += (p_uz)*(math.log(tmp,2))
    
print("Mutual Information I(u,z):",inf)

#%%
#Upperbound = [cardinality_y * | T_z|x |] / [| T_y|x | * cardinality_z]


