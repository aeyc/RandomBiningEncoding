import task2
import task1
from matplotlib import pyplot
import random
import math

def randomComplement(h):
    
    rn = random.randint(0, 1)      #random value equal to 0 or 1
    if(rn == 0):         #set x equal to encoded text or its complement with probability 50%
        return h
    
    k = ''
    for i in range(0, len(h)):      #calculate binary complement
        if(h[i]=='0'):
            k = k + '1'
        if(h[i]=='1'):
            k = k + '0'
    return k

# Add error to y to make it z
z_maxDistance = 3

vect_z = []
for number in range(2**3):
    u = "{0:04b}".format(number)

    for i in range(10**4):
        x = task2.encode(u)
        x = randomComplement(x)
        z = task1.applyMaxDistance(x, z_maxDistance)

        vect_z.append(int(z,2))
print("")

pyplot.hist(vect_z, bins=2**7)
pyplot.show()
vect_z.count(52)
from collections import Counter
dict_z = Counter(vect_z)
inf = 0

#p(uz) = 1/128 ->len(dict_z) 
#p(u) = 1/8 {000,001,010,011,100,101,110,111}
#p(z) = dict_z.values[i]/10**4
for i in dict_z.keys():
    tmp = (1/8)*(dict_z[i]/10000) #p(u)*p(z)
    tmp = (1/128)/tmp
    inf += (1/128)*(math.log(tmp,2))
    
print("Mutual Information I(u,z):",inf)
#Mutual Information I(u,z): 0.001158799925930126
#Mutual Information I(u,z): 0.001346879886474384
#Mutual Information I(u,z): 0.00113748879397734
#Mutual Information I(u,z): 0.0014034513722299617
