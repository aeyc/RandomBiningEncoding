import task2
import task1
from matplotlib import pyplot
import random

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




def main():
    # Generate u
    u = "000" # <-- insert u here
    u = "0" + u

    # Random Binning Encode u
    x = task2.encode(u)

    # Add error to y to make it z
    z_maxDistance = 3
    z = task1.applyMaxDistance(x, z_maxDistance) # generate z starting from x, with maximum hamming distance of z_maxDistance

    print("from plain= {0}, x= {1}, z= {2} ".format(u, x, z))

    stats_z = dict()
    vect_z = []
    for number in range(2**3):
        u = "{0:04b}".format(number)
        for i in range(10**4):
            x = task2.encode(u)
            x = randomComplement(x)
            z = task1.applyMaxDistance(x, z_maxDistance)

            vect_z.append(int(z,2))


            # if z is already in the dictionary, increase its number of occurrencies 
            # otherwise set it to 1 
            #if z in stats_z: 
            #    stats_z[z] += 1
            #else: 
            #    stats_z[z] = 1
    
    print("")
    
    pyplot.hist(vect_z, bins=2**7)
    pyplot.show()



if __name__ == "__main__":
    main()