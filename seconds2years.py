"""
File: <seconds2years.py>
Copyright (c) 2016 <Rachel Benavente>
License: MIT

This code highlights the various math and equation
capabilities described in chapter 1.
"""
#Can a newborn baby in Norway expect to live for 10^9 seconds?
#write a python program to answer the question
B= 10 ** 9
T= B / (60 * 60 * 24 * 365)

if T <= 81:
    print "A newborn baby in Norway can expect to live for this amount of time."
else:
    print "No, a newborn baby cannot expect to live for this amount of time."
