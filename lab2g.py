#!/usr/bin/env python3
#Author: Eliza May Silvestre
#Author ID: esilvestre@myseneca.ca
#Program Name: lab2g.py
#Date Created: 2024/05/22

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")