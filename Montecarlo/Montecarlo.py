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
    t = int(input("Enter how many times to repeat: ")) # Number of times to repeat the process

    r = 1 # Radius of the circumference
    pis = [] # List of values of Pi in each round

    for i in range(t):

        c = 0 # Count of points inside the circumference in this round
        random.seed() # Init the seed with the actual time

        for j in range(n):

            x = random.uniform(-r,r) # Random value for the abscissa (x axis)
            y = random.uniform(-r,r) # Random value for ordinates (y axis)
            m = math.sqrt((x*x) + (y*y)) # Module (distance from the coordinate center)

            if m < r:
                c += 1 # If m < r, this means that is inside the circumference, so we count it

        pis.append(4.0*float(c)/float(n)) # When the round is finished, we calculate the Pi

    pi = sum(pis) / float(len(pis)) # Calculate the average of pi obtained

    print ("\nRESULT")
    print ("N = " + str(n))
    print ("T = " + str(t))
    print ("π = " + '{0:.16f}'.format(pi))
    print ("")
    print ("Reference value: " + str(math.pi))
    print ("")

if __name__ == "__main__":
    main(sys.argv)

# By Xoán Carlos Cosmed Peralejo
