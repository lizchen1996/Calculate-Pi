#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a very simple way to culculate the famous number of Pi, which is very use in mathematics ans science. We can call this 'the magical number', because it appears naturally in a lot of formulas and scopes.
# With this program we calculate Pi with the Montecarlo's method, which consists in calculating the area of the circle in respect to a square. This method works by getting random points, and after obtaining many, calculate the proportion of how many fell within the area. Knowing this we have an approximate proportion of the area of the circle with respect to the area of the square on which it is inscribed.
# GitHub repository: https://github.com/xoancosmed/Calculate-Pi

import sys
import math
import random

def main(argv):

    print ("")
    print ("This program can calculate the number Pi using the Montecarlo's method.")
    print ("To know more abaut this, please visit https://github.com/xoancosmed/Calculate-Pi.")
    print ("")
    n = int(input("Enter the number of points: ")) # Number of points to generate randomly

    random.seed() # Init the seed with the actual time
    r = 1 # Radius of the circumference
    c = 0 # Count of points inside the circumference

    for i in range(n):

        x = random.uniform(-r,r)
        y = random.uniform(-r,r)
        m = (x*x) + (y*y)

        if m < (r*r):
            c += 1

    pi = 4.0*float(c)/float(n)

    print ("\nRESULT")
    print ("N = " + str(n))
    print ("π = " + '{0:.16f}'.format(pi))
    print ("")

if __name__ == "__main__":
    main(sys.argv)

# By Xoán Carlos Cosmed Peralejo
