#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
count = 10

print(f"You are currently {age} years old.")

while count <= 30:
    age1 = age + count
    print(f"In {count} Years, you'll be {age1} years old.")
    count += 10