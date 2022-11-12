#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: Encryption
    # @version: I
    #- Creation: 05/11/2022
    #- Last modification: 11/11/2022

# Variables & lists
default = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # dictionary
p = 0
q = 0
e = 0
text = ""
text1 = ""
encryptedText = ""
decryptedText = ""
run = True

# While cycle for the menu
while run:
    print("\n")
    print("--- What would you like to do? ---")
    print("1. Encrypt message.")
    print("2. Decrypt message.")
    
    option = input("\nType the number that corresponds to the option you wanna execute: ")
    
    # First option || Message encryption
    if option == "1":
        list2= list()
        # Inputs
        p, q, e = input("Enter three prime numbers in this order p, q & e separated by space: \n").split(" ")
        p = int(p)
        q = int(q)
        e = int(e)
        n = p * q
        φ = (p - 1) * (q - 1)
        publicKey = (e, n)
        # Message
        text = input("Enter the message you would like to encrypt: \n")
        encryptedText = ""
        length = len(text)
        # Logic
        for i in range(length):
            answer = default.index(text[i])
            if(answer < 10):
                casting = "0" + str(answer)
                list2.append(casting)
            else:
                casting = str(answer)
                list2.append(casting)
    blocksQuantity = str(len(default) - 1)
    flag = False
    charactersN= 1
    while flag == False:
        if int(blocksQuantity) > n:
            flag = True
            charactersN= charactersN - 1
        else:
            charactersN= charactersN + 1
            blocksQuantity = blocksQuantity + str(len(default))
    firstEncryption = ''
    secondEncryption = ''
    for i in range(charactersN):
            firstEncryption = firstEncryption + list2[i]
            secondEncryption = secondEncryption + list2[i + 2]
    finalblock  = int(firstEncryption)**e % n
    finalblock1 = int(secondEncryption)**e % n
    encryptedText = finalblock, finalblock1
    # Base code from: https://github.com/awnonbhowmik/RSA-Python/blob/master/RSA_Python.py
    print("The encrypted message is: ",encryptedText)
    
    # Second option || Message decryption
    if option == "2":
        # Inputs
        p, q, e = input("Enter three prime numbers in this order p, q & e separated by space: \n").split(" ")
        p = int(p)
        q = int(q)
        e = int(e)
        n = p * q
        φ = (p - 1) * (q - 1)
        # Message
        text1 = input("Enter the message you would like to decrypt: \n")
        # Logic
        for k in range(1, φ):
            if((e % φ)*(k % φ) % φ == 1):
                K = k
                text1S = text1.split(" ")
                block = int(text1S[0])
                block1 = int(text1S[1])
                a = block **K %n
                b = block1 **K  %n
        if(a < 1000):
            astr = "0" + str (a)
        else:
            astr = str (a)
        if(b < 1000):
            bstr = "0" + str (b)
        else:
            bstr = str (b)
        part = astr[0] + astr[1]
        part1 = astr[2] + astr[3]
        part2 = bstr[0] + bstr[1]
        part3 = bstr[2] + bstr[3]
        decryptedText = default[int(part)]+ default[int(part1)] + default[int(part2)] + default[int(part3)]
        # Base code from: https://github.com/awnonbhowmik/RSA-Python/blob/master/RSA_Python.py
        print("\nThe decrypted message is: ",decryptedText)
    else:
        run = False