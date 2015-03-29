# coding: utf-8

import math

for line in open('primenumber.txt', 'r'):   #素数読み込み
    num = int(line)

    prime = [2]
    i = 3
    while i <= num:
        j = 2
        flg = 0

        while j <= math.sqrt(i):
            if(i % j == 0):
                flg = 1
                break

            j = j + 1

        if(flg == 0):
            prime.append(i)

        i = i + 2

    print("%d" % len(prime))
    # print(prime)