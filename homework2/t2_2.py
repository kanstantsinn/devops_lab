#!/usr/bin/python3


#a = [ 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 1, 33, 33, 33 ]

n = int(input ("Input the lenth of a list\n"))
l = []
for j in range (0, n):
    y = int(input("Input namber from 1 to 100\n"))
    while True:
        if (y < 1) or (y > 100):
            print ("You have inputed not allowed number!!! Input only from 1 to 100")
            y = int(input())
            continue
        l.append(y)
        break

def list1 (x):
  len_x = len(x)
  resalt = {}
  c = 0
  for i in range (0, len_x):
    if x.count(x[i]) > c:
      c = x.count(x[i])
      resalt['count'] = c
      resalt['element'] = x[i]
  return resalt


print(list1(l))

