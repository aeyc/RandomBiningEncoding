#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:56:52 2020

@author: Ayca
"""
from task5 import flipBinStr
from task2_2 import encode 
from task4 import randomComplement
from task3 import decrypt as decode 
import random
from matplotlib import pyplot 
import math
from collections import Counter



#every u can be mapped to 2^4 different x values
#e.g u = '000' x = {0, 1, 2, 4, 8, 16, 32, 63, 64, 95, 111, 119, 123, 125, 126, 127}
#e.g u = '101' x = {10, 21, 34, 40, 42, 43, 46, 58, 69, 81, 84, 85, 87, 93, 106, 117}
# p(u=a) = 1/8 -> u = {'000', '001', '010', '011', '100', '101', '110', '111'}
# p(x=b|u=a) = p(x=b&u=a)/p(u=a) = [(1/16)(1/8)]/(1/8) = 1/16
# decoding u via x
u_dict = dict()
u_dict = {}
for number in range(2**7):
    x = "{0:07b}".format(number)
    u_decoded = decode(x)
    #print("x:{},u:{}".format(x,u))
    if u_decoded in u_dict:
        u_dict[u_decoded].append(int(x,2))
    else:
        u_dict[u_decoded] = [int(x,2)]
        
# #|Z| = 128, |Y| = 128
        
# print("")

x_assumption = "0100000" 
y_a_dict = dict()
y_a_dict = {}
for i in range(10**4):
    y_assumption = flipBinStr(x_assumption,0.2)
    if y_assumption in y_a_dict:
        y_a_dict[y_assumption]+=1
    else:
        y_a_dict[y_assumption]=1
#%%
"""


P[u! = u]
"""
#lim_(n->infinite) P[û != u] = 0 #cannot change n since decoder is built for 7,4
error_counter = dict()
error_counter = {}
error_rate = 0

dict_z_total = dict()
dict_z_total ={}
dict_y_total = dict()
dict_y_total ={}

# stats_z = dict()
vect_z = [] # Vector af all z's
stats_z = [] # Will save every stats_z_d

vect_y = [] # Vector af all z's
stats_y = [] # Will save every stats_z_d
#dependency -> pip install textdistance
for number in range(2**3):
    u = "{0:04b}".format(number)
    current_error = []
    
    vect_z_d = [] # Vector of all z given one u=d 
    stats_z_d = [0]*(2**7) #Map having stas_z_d[z] = <counted times>; for a given u=d
    dict_y_local = dict()
    dict_y_local ={} 
    
    dict_z_local = dict()
    dict_z_local ={} 
    
    vect_y_d = [] # Vector of all y given one u=d 
    stats_y_d = [0]*(2**7) #Map having stas_y_d[y] = <counted times>; for a given u=d
    
    for i in range(10**4):
        x = encode(u)
        x_r = randomComplement(x)
        #epsilon<delta for make secrecy possible
        epsilon = round(random.uniform(0, 0.25), 2)
        delta = round(random.uniform(0.25, 0.5), 2)
        y = flipBinStr(x, epsilon) # we can have more than one error in a single codeword over the legitimate channel 
        z = flipBinStr(x_r, delta)
        
        # Count how many times each z appears 
        stats_z_d[int(z,2)] += 1 
        # Saves what z we get
        vect_z_d.append(int(z,2))
        
        # Count how many times each y appears 
        stats_y_d[int(y,2)] += 1 
        # Saves what y we get
        vect_y_d.append(int(y,2))
        
        u_decoded = decode(y)
        u = "{0:03b}".format(number)
        if u != u_decoded:
            dist = 1
        else:
            dist = 0
            
        #for analyzing y mappings per u
        if y in dict_y_local:
            dict_y_local[y] +=1
        else:
            dict_y_local[y] =1
            
        if z in dict_z_local:
            dict_z_local[z] +=1
        else:
            dict_z_local[z] =1
            
        current_error.append(dist)
    # Appending oll of the data from one loop, for calculus later
    stats_z.append(stats_z_d)
    vect_z.append(vect_z_d)
    
    # Appending oll of the data from one loop, for calculus later
    stats_y.append(stats_y_d)
    vect_y.append(vect_y_d)
    
    dict_y_total[u] = dict_y_local
    dict_z_total[u] = dict_z_local
    error_counter[u] = current_error
    error_rate = sum(current_error)/10**4
    print("Error rate = {} when u = {}".format(error_rate,u))
    pyplot.plot(current_error,"ro",label="Error rate:{}".format(error_rate))
    pyplot.title("u_decoded != u \nu = {}".format(u))
    pyplot.ylabel("error per bits")     
    pyplot.xlabel("sample u_decoded size") 
    pyplot.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    pyplot.show()     

    
    
#%%    
# Mutual Information lim_(n->infinite) I(u;z) = 0
# I(u;z) = H(z) - H(z|u)
# H(z) = -(sum[p(z)*log_2 p(z)] for all z in Z)
# H(z|u) = sum[p(u)*H(z| u=a)] for all u in U
# I(u;z) = H(z) + H(u) - H(u,z)
# Also I(u;z) can be represented w/same formula in task4
# ref: https://www2.isye.gatech.edu/~yxie77/ece587/Lecture2.pdf
    

number = 0
#plot z distribution given u
for i in vect_z:
    pyplot.hist(i, bins=2**7)
    pyplot.title("Emprical conditional pmd of z given u = {}".format("{0:03b}".format(number)))
    pyplot.ylabel("Occurence")
    pyplot.xlabel("Value of z")
    pyplot.show()
    number+=1

for i in vect_z:
    dict_z = Counter(i)
    inf = 0
    
    #p(uz) = 1/128 ->len(dict_z) 
    #p(u) = 1/8 {000,001,010,011,100,101,110,111}
    #p(z) = dict_z.values[i]/10**4
    for j in dict_z.keys():
        tmp = (1/8)*(dict_z[j]/10000) #p(u)*p(z)
        tmp = ((1/8)*(1/128))/tmp #p(uz) = 1/8 * 1/128
        inf += (1/128)*(math.log(tmp,2))
        
    print("Mutual Information I(u,z):",inf)



#%%
#Upperbound = [cardinality_y * | T_z|x |] / [| T_y|x | * cardinality_z]
#10**4 realizations 
cardinality_y = 2**7 #7 bit binary string
cardinality_z = 2**7 #7bit binary string
keys = list(dict_z_total["000"].keys())
keys_u = list(dict_z_total.keys())
upper_bound_est =[]
for u_key in keys_u:
    for key in keys:
        n_yx = dict_y_total[u_key][key]/10000
        n_zx = dict_z_total[u_key][key]/10000
        upper_bound = n_zx/n_yx
        upper_bound_est.append(upper_bound)
        
