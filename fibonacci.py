#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
running = True
while running == True:
  terms = input("Enter number of terms: ")
  if int(terms) > 0:
    print("Calculating first " + terms + " terms of fibonacci sequence")
    for n in range(int(terms)):
      fib = round((((1 + 5**0.5)/2)**n - ((1 - 5**0.5)/2)**n) / (5**0.5)) # Binet's formula
      print(fib)
