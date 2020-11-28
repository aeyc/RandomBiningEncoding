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

    
    pyplot.plot(x_axis, y_axis[0], 'r')
    pyplot.plot(x_axis, y_axis[1], 'g')
    pyplot.plot(x_axis, y_axis[2], 'b')
    pyplot.plot(x_axis, y_axis[3], 'c')
    pyplot.plot(x_axis, y_axis[4], 'm')
    pyplot.plot(x_axis, y_axis[5], 'y')
    pyplot.plot(x_axis, y_axis[6], 'k')
    pyplot.plot(x_axis, y_axis[7])
    pyplot.show()



    pyplot.hist(vect_z[1], bins=2**7)
    pyplot.show()



if __name__ == "__main__":
    main()