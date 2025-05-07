#!/usr/bin/env python3

print("Enter the first number:")
x = int(input())
print("Enter the second number:")
y = int(input())

sum = x * y

print(x," x ",y ,"=" ,sum)

if sum == 0:
    print("The result is positive and negative.")
elif sum > 0:
    print("The result is positive.")
else :
    print("The result is negative.")