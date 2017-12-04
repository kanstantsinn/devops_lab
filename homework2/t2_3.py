#!/usr/bin/python3

def self_dev (L,R):
    LR = [i for i in range(L, R + 1)]
    S_L = []
    for i in range(len(LR)):
        p = (str(LR[i]))
        #n = len(p)
        for j in range (len (p)):
            if (p[j] == "0") or (LR[i] % int(p[j]) != 0):
                break

        else:
            S_L.append(LR[i])
    return S_L


LL = int(input("Input left:\n"))
RR = int(input("Input right:\n"))
print (self_dev(LL, RR))




