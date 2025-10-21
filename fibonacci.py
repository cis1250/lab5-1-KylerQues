#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def main():
    

  def get_terms():
      while True:
          terms = input("Enter number of terms: ")
          if terms.isdigit() and int(terms) > 0:
              return int(terms)
          else:
              print("Please enter a positive integer.")
  def calculate(terms):
      nums = []
      for n in range(terms):
          fib = round((((1 + 5**0.5)/2)**n - ((1 - 5**0.5)/2)**n) / (5**0.5)) # Binet's formula
          nums.append(fib)
      return nums

  def print_out(output):
      print("Fibonacci sequence:")
      for i in output:
          print(i)

  terms = get_terms()
  output = calculate(terms)
  print_out(output)
main()
