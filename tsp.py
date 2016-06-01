#!/usr/bin/python

import math, re, sys

def readinstance(filename):
    # each line of input file represents a city given by three integers:
    # identifier x-coordinate y-coordinate (space separated)
    # city identifiers are always consecutive integers starting with 0
	f = open(filename,'r')
	line = f.readline()
	cities = []
	while len(line) > 1:
		lineparse = re.findall(r'[^,;\s]+', line)
		cities.append((int(lineparse[1]),int(lineparse[2])))
		line = f.readline()
	f.close()
	return cities

def cartesian_matrix(cities):
    #create a distance matrix for the city coords
    #Takes a Python list of (x,y) tuples and outputs a Python dictionary that contains the distance
    #between the distances between any two cities
	matrix={}
	for i,(x1,y1) in enumerate(cities):
		for j,(x2,y2) in enumerate(cities):
			dx,dy=x1-x2,y1-y2
			dist=int(round(math.sqrt(dx*dx + dy*dy)))
			matrix[i,j]=dist
	return matrix


filename="tsp_example_1.txt" 
cities=readinstance(filename)
print cartesian_matrix(cities)














