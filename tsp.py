#!/usr/bin/python

import math, re, sys

def readinstance(filename):
    # each line of input file represents a city given by three integers:
    # identifier x-coordinate y-coordinate (space separated)
    # city identifiers are always consecutive integers starting with 0
    # (although this is not assumed here explicitly,
    #    it will be a requirement to match up with the solution file)
	f = open(filename,'r')
	line = f.readline()
	cities = []
	while len(line) > 1:
		lineparse = re.findall(r'[^,;\s]+', line)
		cities.append((int(lineparse[1]),int(lineparse[2])))
		line = f.readline()
	f.close()
	return cities


filename="tsp_example_1.txt" 
print readinstance(filename)















