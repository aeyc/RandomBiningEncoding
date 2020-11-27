import random 

K = 4
#works only for 7,4

def encode(s):
    # Read in K=4 bits at a time and write out those plus parity bits
    s = '0' + s
    while len(s) >= K:
        nibble = s[0:K]
        #print(hamming(nibble))
        s = s[K:]
    h = hamming(nibble)
    k = ''
    for i in range(0, len(h)):      #calculate binary complement
        if(h[i]=='0'):
            k = k + '1'
        if(h[i]=='1'):
            k = k + '0'
    rn = random.randint(0, 1)      #random value equal to 0 or 1
    x = ''
    if(rn == 0):         #set x equal to encoded text or its complement with probability 50%
        x = h
    else:
        x = k
    return x

def hamming(bits):
    # Return given 4 bits plus parity bits for bits (1,2,3), (2,3,4) and (1,3,4)
    t1 = parity(bits, [0,1,3])
    t2 = parity(bits, [0,2,3])
    t3 = parity(bits, [1,2,3])
    return bits + t1 + t2 + t3  #again saying, works only for 7,4

def parity(s, indicies):
    # Compute the parity bit for the given string s and indicies
    sub = ""
    for i in indicies:
        sub += s[i]
    return str(str.count(sub, "1") % 2)

if __name__ == "__main__":
    print("Enter Input String of bits - ") #get in input the plaintext
    input_string = input().strip()
    #input_string = '0' + input_string
    x = encode(input_string)       #get the encoded text
    # k = ''
    # for i in range(0, len(h)):      #calculate binary complement
    #     if(h[i]=='0'):
    #         k = k + '1'
    #     if(h[i]=='1'):
    #         k = k + '0'
    # rn = random.randint(0, 1)      #random value equal to 0 or 1
    # x = ''
    # if(rn == 0):         #set x equal to encoded text or its complement with probability 50%
    #     x = h
    # else:
    #     x = k
    print('ciphertext  x: ' + x)      #print in output the ciphertext
    