#!/usr/bin/env python3

num = input("Give me a number: ")
fnum = float(num)
inum = int(fnum)

if fnum == inum:
    print("This number is an integer.")
else:
    print("This number is a decimal.")