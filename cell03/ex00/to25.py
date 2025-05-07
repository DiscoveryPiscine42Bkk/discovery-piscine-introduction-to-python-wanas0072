#!/usr/bin/env python3

print("Enter a number less than 25")

x = int(input())

if x > 25:
    print("Error")
else:
    while x <= 25:
        print("Inside the loop, my variable is",x)
        x += 1