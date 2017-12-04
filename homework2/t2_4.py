#!/usr/bin/python3
import re


n = int(input("Number of words:\n"))
l_w = []
for i in range(n):
    while True:
        w = str(input("word-{} ".format(i + 1)))
        for j in range(len(w)):
            if re.search("[a-z]", w[j]):
                continue
            else:
                print("Not appowed input, only lowercase English")
                break
        else:
            l_w.append(w)
            break


l_u = []
for i in range(n):
    if l_u.count(l_w[i])== 0:
        l_u.append(l_w[i])

print ("Number of distinct words:{}".format(len(l_u)))
for i in range (len(l_u)):
    print (l_w.count(l_u[i]), end=" ")
print (" ")

