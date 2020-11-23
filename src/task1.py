#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random 
import math

# @param str1, str2 binary strings with the SAME SIZE 
# @return tmp: xor of str1 and str2 
def xor(str1, str2): 
    tmp = "" 

    for i in range(len(str1)): 
        if (str1[i] == str2[i]):  
            tmp += "0"
        else:  
            tmp += "1"
    return tmp  

# function used to generate a binary string with length len 
# and a number of bit at 1 equals to nOf1 
def genBinStr(length, nOf1): 
    str = "1" * nOf1 + "0" * (length-nOf1) # generate trivial binary string 
    l = list(str) # convert the string to list (to edit it) 
    random.shuffle(l) # shuffle randomly the string str
    return ''.join(l) # convert list to string and return it 

# @param x: binary string 
# @param dist: hamming distance to apply 
# @return l: binary string with distance dist from x 
def applyDistance(x, dist):
    return xor(x, genBinStr(len(x), dist))

# @param x: binary string 
# @param maxDistance: maximum hamming distance to apply 
# @return a binary string with at most maxDistance distance from x
def applyMaxDistance(x, maxDistance): 
    pop = [] # possible distances 
    weights = [] # weight of each distance 
    tot = 0;  
    
    for i in range(maxDistance+1): # from 0 to maxDistance 
        pop.append(i)
        prob = math.comb(len(x), i) 
        weights.append(prob)
        tot += prob 
    
    weights = [weight / tot for weight in weights]
    
    # select a distance 
    dist  = random.choices(population=pop, weights=weights)
    
    # return a binary string with distance dist[0] from x
    return applyDistance(x, dist[0])
    
    
# -- TASK 1 -- 
x = "1001000"

y_maxDistance = 1 
z_maxDistance = 3 

y = applyMaxDistance(x, y_maxDistance) # generate y starting from x, with maximum hamming distance of y_maxDistance
z = applyMaxDistance(x, z_maxDistance) # generate z starting from x, with maximum hamming distance of z_maxDistance

print("X: %s\nY: %s\nZ: %s" % (x, y, z)) 

## ---- STATS ---- 

# create two dictionaries to store frequencies of values of y and z 
stats_y = dict()
stats_z = dict()

# fixed x repeat the process for 10^4 times 
for i in range(10 ** 4): 
    y = applyMaxDistance(x, 1)
    z = applyMaxDistance(x, 3)
    
    # if y is already in the dictionary, increase its number of occurrencies 
    # otherwise set it to 1 
    if y in stats_y: 
        stats_y[y] += 1
    else: 
        stats_y[y] = 1
    
    # same as previous 
    if z in stats_z: 
        stats_z[z] += 1
    else: 
        stats_z[z] = 1

# print('Y distribution') 
# for i, (k, v) in enumerate(stats_y.items()):
#    print(k, v)
     
#print('Z distribution')
#for i, (k, v) in enumerate(stats_z.items()):
#    print(k, v)   