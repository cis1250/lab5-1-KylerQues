#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
running = true
while running = true:
  terms = input("Enter number of terms: ")
  if terms > 0:
    print("Calculating first " + terms + " terms of fibonacci sequence")
    for x in range(terms):
      for y in range(1, terms):
        num = x
        num2 = y + x
        print(num)
        print(num2)
      
