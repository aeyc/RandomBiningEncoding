#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random 

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

# @param x: binary string 
# @param dist: hamilton distance to apply 
# @return l: binary string with distance dist from x 
def applyDistance(x, dist):
    return xor(x, genBinStr(len(x), dist))
    
# function used to generate a binary string with length len 
# and a number of bit at 1 equals to nOf1 
def genBinStr(len, nOf1): 
    str = "1" * nOf1 + "0" * (len-nOf1) # generate trivial binary string 
    l = list(str) # convert the string to list (to edit it) 
    random.shuffle(l) # shuffle randomly the string str
    return ''.join(l) # convert list to string and return it 
    
# TASK 1 
x = "1001000"
y_dist = random.randint(0, 1)
y = applyDistance(x, y_dist) # generate y starting from y, and applying 0 or 1 errors  
z_dist = random.randint(0, 3)
z = applyDistance(x, z_dist) # generate y starting from y, and applying 0, 1, 2 or 3 errors 

print("X: %s\nY: %s\tDistance of y: %s\nZ: %s\tDistance of z: %s" % (x, y, y_dist, z, z_dist)) 
