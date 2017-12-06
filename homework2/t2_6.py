#!/usr/bin/python3

import re

l_dict = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"]
alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
#deshif
def deshif (mes):
    f_mes = ""
    for i in range(len(mes)):
        f_mes += alfabet[l_dict.index(mes[i]) - (i % 27)]
    return f_mes

#shifrator
def shifrator (mes):
    f_mes = ""
    for i in range(len(mes)):

        f_mes += l_dict[(alfabet.index(mes[i]) + i) % 27]
    return f_mes

while True:
    w = str(input("Message to encript:\n"))
    for j in range(len(w)):
        if re.search("[a-z ]", w[j]):
            continue
        else:
            print("Not allowed input, input only a-z and space")
            break
    else:
        break

print (shifrator(w))

while True:
    w = str(input("Message to decript:\n"))
    for j in range(len(w)):
        if re.search("[0-9A-Q]", w[j]):
            continue
        else:
            print("Not allowed input, input only 0-9 or A-Q")
            break
    else:
        break

print (deshif(w))
