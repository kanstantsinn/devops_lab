#!/usr/bin/python3
def cuboid ():
    x = int(input("Input N:\n"))
    y = int (input("Input Y:\n"))
    z = int (input("Input Z:\n"))
    n = int (input("Input N:\n"))
    r_l = []
    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                if (i + j + k) != n:
                    r_l.append([i, j, k])
    return r_l

print (cuboid ())
