#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a very simple way to culculate the famous number of Pi, which is very use in mathematics ans science. We can call this 'the magical number', because it appears naturally in a lot of formulas and scopes.
# With this program we calculate Pi with the polygons' method, which consists in calculate the Pi from two polygons, one inscribed with a circungerence and other circumscribed. The precision depends on how many sides have the polygons, because as you know, the more sides a polygon has, the more it looks like a circle.
# GitHub repository: https://github.com/xoancosmed/Calculate-Pi

import sys
import math

def main(argv):

    print ("")
    print ("This program can calculate the number Pi using the polygons method.")
    print ("To know more abaut this, please visit https://github.com/xoancosmed/Calculate-Pi.")
    print ("")
    n = int(input("Enter the number of sides: ")) # Number of sides of the polygons (set by the user)

    r = 1 # Radius of the circumference
    m = 4 # Number of sides of the initial polygons (square)
    A = 4*math.sqrt(2)*r # Initial perimeter of the inscribed polygon (perimeter of the inside square)
    B = 8*r # Initial perimeter of the circumscribed polygon (perimeter of the outside square)

    while (m*2) <= n: # We make the operations until the numer of sides reaches the limit

        B = 2*A*B/(A+B) # New perimeter of the circumscribed polygon
        A = math.sqrt(A*B) # New perimeter of the inscribed polygon
        m = m*2 # New numer of sides

    pi = (((A/2)/r) + ((B/2)/r)) / 2 # Calculate the Pi number
    error = abs(((A/2)/r) - ((B/2)/r)) / 2 # Calculate the error in the calculation

    print ("\nRESULT")
    print ("N = " + str(n))
    print ("π = " + '{0:.16f}'.format(pi) + " ± " + str(error))
    print ("")

if __name__ == "__main__":
    main(sys.argv)

# By Xoán Carlos Cosmed Peralejo
