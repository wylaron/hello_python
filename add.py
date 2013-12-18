#!/usr/bin/python

n = input('Input the number: ')
sum = 0
for i in range(n):
    if (n+1) % 3 == 0 or (n+1) % 5 == 0:
        sum += i + 1
print sum
