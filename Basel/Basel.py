#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a very simple way to culculate the famous number of Pi, which is very use in mathematics ans science. We can call this 'the magical number', because it appears naturally in a lot of formulas and scopes.
# With this program we calculate Pi with a technique based on numerical series called "Problem of Basel (Basilea)", which was solved by Leonhard Euler. With the solution that Euler arrived, we know that sum(1/(n^2),inf)=((pi^2)/6), so we just have to use a lot of numbers in the series to get an approximate value of Pi.
# GitHub repository: https://github.com/xoancosmed/Calculate-Pi

import sys
import math

def main(argv):

    print ("")
    print ("This program can calculate the number Pi using Basel problem.")
    print ("To know more abaut this, please visit https://github.com/xoancosmed/Calculate-Pi.")
    print ("")
    n = int(input("Enter the number of terms to add: ")) # Number of terms to use in the Basel problem

    summation = 0.0 # Here we are going to add each term

    for i in range(n):
        summation = summation + (1/float((int(i)+1)**2)) # We add one term to the summation

    pi = math.sqrt(6*summation) # The result of clearing Pi from summation=((pi^2)/6)

    print ("\nRESULT")
    print ("N = " + str(n))
    print ("π = " + '{0:.16f}'.format(pi))
    print ("")
    print ("Reference value: " + str(math.pi))
    print ("")

if __name__ == "__main__":
    main(sys.argv)

# By Xoán Carlos Cosmed Peralejo
