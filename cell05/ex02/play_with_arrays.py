#!/usr/bin/env python3
import numpy as np

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []

for num in arr:
  new_arr.append(num + 2)

new_arr = new_arr[num > 5]
#new_arr = new_arr[new_arr]
print(arr)
print(new_arr)

#not yet