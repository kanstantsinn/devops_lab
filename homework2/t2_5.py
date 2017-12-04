#!/usr/bin/python3


def letter ():
    l = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    while True:
        k = str(raw_input("Input one letter:\n"))
        if l.count(k) == 0:
            print (len(k))
            print (k)
            print ("!!!Not allowed input!!!\n")
            continue
        break
    p = l.index(k)
    if p == (len(l)-1):
        print ("Next latter is -{}-".format(l[0].upper()))
    else:
        print("Next latter is -{}-".format(l[p+1].upper()))

triger = 0
while True:
    if triger == 0:
        letter()
    n = str(raw_input("One more time? Y/N\n"))
    if (n == "y") or (n == "Y"):
        triger = 0
        continue
    if (n == "n") or (n == "N"):
        break
    else:
        print ("Choose Y/N")
        triger = 1

