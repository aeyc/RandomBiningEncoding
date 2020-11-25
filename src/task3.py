def decrypt(msg):
    error = 0
    corrected = 0

    # Calculate syndrome
    s = [0, 0, 0]
    # D1 + D2 + D3 + H0
    s[0] = (int(msg[1]) + int(msg[2]) + int(msg[3]) + int(msg[6])) % 2

    # D0 + D2 + D3 + H1
    s[1] = (int(msg[0]) +  int(msg[2]) + int(msg[3]) + int(msg[5])) % 2

    # D0 + D1 + D3 + H2
    s[2] = (int(msg[0]) + int(msg[1]) + int(msg[3]) + int(msg[4])) % 2
    

    syndrome = (s[2] << 2) | (s[1] << 1) | s[0]
    #print(syndrome)
    msg = list(msg)
    if syndrome ==6:
        if msg[0]=='0':
            msg[0]='1'
        else:
            msg[0]='0'

    if syndrome ==5:
        if msg[1]=='0':
            msg[1]='1'
        else:
            msg[1]='0'

    if syndrome ==3:
        if msg[2]=='0':
            msg[2]='1'
        else:
            msg[2]='0'
    
    if syndrome ==7:
        if msg[3]=='0':
            msg[3]='1'
        else:
            msg[3]='0'

    out = ''
    if msg[0] == '1':
        if msg[1]=='0':
            out +='1'
        else:
            out +='0'

        if msg[2]=='0':
            out +='1'
        else:
            out +='0'

        if msg[3]=='0':
            out +='1'
        else:
            out +='0'
    else:
        out = msg[1] + msg[2] + msg[3]

    return out

if __name__ == "__main__":
    print("Enter Input String of bits - ") #get in input the ciphertext
    input_string = input().strip()
    h = decrypt(input_string)       #get the dencoded text
    
    print('ciphertext  u: ' + h)      #print in output the plaintext
   