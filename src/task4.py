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





# Generate u
u = "000" # <-- insert u here
u = "0" + u

# Random Binning Encode u
x = task2.encode(u)

# Add error to y to make it z
z_maxDistance = 3
z = task1.applyMaxDistance(x, z_maxDistance) # generate z starting from x, with maximum hamming distance of z_maxDistance

print("from plain= {0}, x= {1}, z= {2} ".format(u, x, z))

# stats_z = dict()
vect_z = [] # Vector af all z's
stats_z = [] # Will save every stats_z_d

#---------------- Gathering data

for number in range(2**3):
    u = "{0:04b}".format(number)
    vect_z_d = [] # Vector of all z given one u=d
    stats_z_d = [0]*(2**7) #Map having stas_z_d[z] = <counted times>; for a given u=d

    for i in range(10**4):
        x = task2.encode(u)
        x = randomComplement(x)
        z = task1.applyMaxDistance(x, z_maxDistance)

        # Count how many times each z appears 
        stats_z_d[int(z,2)] += 1 
        # Saves what z we get
        vect_z_d.append(int(z,2))
    
    # Appending oll of the data from one loop, for calculus later
    stats_z.append(stats_z_d)
    vect_z.append(vect_z_d)


print("")

#----------Time to plot things
x_axis= range(0,2**7,1) # X axis for plotting
y_axis = []

for d in range(8):
    single_y = [0] * (2**7) # Need empty array
    single_y[0] = stats_z[d][0] / 10**4 # Fill first elem of array
    for i in range(1,len(stats_z[d])):
        # Calculate pmd for u = d
        single_y[i] = (stats_z[d][i] / 10**4) + single_y[i-1] #Fill other cells
    y_axis.append(single_y)


pyplot.plot(x_axis, y_axis[0], 'r', label = "u = 000")
pyplot.plot(x_axis, y_axis[1], 'g', label = "u = 001")
pyplot.plot(x_axis, y_axis[2], 'b', label = "u = 010")
pyplot.plot(x_axis, y_axis[3], 'c', label = "u = 011")
pyplot.plot(x_axis, y_axis[4], 'm', label = "u = 101")
pyplot.plot(x_axis, y_axis[5], 'y', label = "u = 110")
pyplot.plot(x_axis, y_axis[6], 'k', label = "u = 111")
pyplot.plot(x_axis, y_axis[7])

pyplot.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
pyplot.title("P_(z|u) (c|d)")
pyplot.show()

number = 0
#plot z distribution given u
for i in vect_z:
    pyplot.hist(i, bins=2**7)
    pyplot.title("Emprical conditional pmd of z given u = {}".format("{0:03b}".format(number)))
    pyplot.ylabel("Occurence")
    pyplot.xlabel("Value of z")
    
    pyplot.show()
    number+=1

from collections import Counter
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

