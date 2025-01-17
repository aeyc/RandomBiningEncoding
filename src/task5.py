import random 

from task2_2 import encode 
from task3 import decrypt as decode 

# @return bit flipped with probability prob
def flipBit(bit, prob): 
    if random.random() < prob: 
        # flip the bit 
        if bit == "1": 
            return "0"
        else: 
            return "1"
    # otherwise return the bit received (not flipped) 
    return bit 

# @param bin_str: binary string to flip 
# @pram prob: probability to flip each bit 
# @return flipped_str: binary string in which each bit has been flipped with probability prob 
def flipBinStr(bin_str, prob): 
    flipped_str = ""
    
    # loop to flip with probability prob each bit   
    for bit in bin_str:
        flipped_str += flipBit(bit, prob)
    return flipped_str 

# @return a random binary string with requested length 
def randBinStr(length):
    bin_str = "" 
    for i in range(length): 
        bin_str += str(random.randint(0,1))
    return bin_str
if __name__ == "__main__":    
    # params of binary symmetric channel 
    epsilon = 0.2 
    delta = 0.4
    
    # long binary sequence 
    x = randBinStr(10 ** 6)
    
    y = flipBinStr(x, epsilon)
    z = flipBinStr(x, delta) 
    
    # print("X: %s\nY: %s\nZ: %s" % (x, y, z))
    
    ## estimate the value of epsilon and delta, looking at the nuber of flipped bits in y and z  
    y_flippedBits = sum(val != y[index] for index, val in enumerate(x))
    estimated_epsilon = float(y_flippedBits) / len(x)
    print("Epsilon: %f - Estimated epsilon: %f" % (epsilon, estimated_epsilon))
    
    z_flippedBits = sum(val != z[index] for index, val in enumerate(x))
    estimated_delta = float(z_flippedBits) / len(x)
    print("Delta: %f - Estimated delta: %f" % (delta, estimated_delta))
    
    ## connect the wiretap channel to the random binning encoder - decoder, and simulate several trasmissions 
    for i in range(10 ** 8):
        x = randBinStr(3) 
        
        # encoder 
        x_encoded = encode(x) 
        
        # wiretap channel 
        y = flipBinStr(x_encoded, epsilon) # we can have more than one error in a single codeword over the legitimate channel 
        z = flipBinStr(x_encoded, delta) 
        
        # decoder 
        y_decoded = decode(y) 
        z_decoded = decode(z) 
            
        # print("X: %s, Encoded X: %s, Y: %s, Decoded Y: %s, Z: %s, Decoded Z: %s" % (x, x_encoded, y, y_decoded, z, z_decoded))
