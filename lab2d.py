#!/usr/bin/env python3
#Author: Eliza May Silvestre
#Program Name: lab2d.py
#Date Created: May 22, 2024

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()
    
name = str(sys.argv[1])
age = str(sys.argv[2])

print(f"Hi {name}, you are {age} years old.")