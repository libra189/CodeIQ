# coding: utf-8

import math

num = 500
prime = []
for i in range(2, num + 1):
    for j in range(2, int(math.sqrt(i)) + 1):
        if(i % j == 0):
            break
    else:
        prime.append(i)

for i in prime:
    for j in reversed(prime):
        if((j - i) == 6):
            print("(%d,%d)" % (i, j))