#!/usr/bin/env python3

row = 0

while row <= 10:
    col = 0
    print(f"Table de {row}:", end=" ")
    while col <= 10:
        result = row * col
        print(result, end=" ")
        col += 1
    print()
    row += 1