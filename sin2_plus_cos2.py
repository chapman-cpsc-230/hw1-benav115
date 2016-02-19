"""
File: <sin2_plus_cos2.py>
Copyright (c) 2016 <Rachel Benavente>
License: MIT

This code highlights the various math and equation
capabilities described in chapter 1.
"""
#do all three parts in one file
#part a
from math import sin, cos, pi
x = pi/4
val1 = sin(x) ** 2 + cos(x) ** 2 #import math for sin,cos
print val1   #can't have a number at the beginning of a name for a file

#part b
v0 = 3 #m/s
t = 1 #s
a = 2 #m/s ** 2
s = v0 * t + 0.5 * a * t ** 2
print s

#part c
a = 3.3
b = 5.3

a2 = a ** 2
b2 = b ** 2

eq1_sum = a ** 2 + 2 * a * b + b ** 2
eq2_sum = a ** 2 + 2 * a * b + b ** 2

eq1_pow = (a + b) ** 2
eq2_pow = (a - b) ** 2

print "First equation: %s = %s" % (eq1_sum, eq1_pow)
print "Second equation: %s = %s" %( eq2_pow, eq2_pow)
