#!/usr/bin/python

import math, re, sys, random

#References: John Montgomery blog post: Tackling the travelling salesman problem
#http://www.psychicorigami.com/2007/04/17/tackling-the-travelling-salesman-problem-part-one/			 

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
			dx=x1-x2
			dy=y1-y2
			dist=int(round(math.sqrt(dx*dx + dy*dy)))
			matrix[i,j]=dist
	return matrix

def tour_length(matrix,tour):
	#Determine the total tour given a list of cities as integers and a distance matrix
    total=0
    num_cities=len(tour)
    for i in range(num_cities):
        j=(i+1)%num_cities
        city_i=tour[i]
        city_j=tour[j]
        total+=matrix[city_i,city_j]
    return total
def greedy(matrix,tour):
	greedyTour= []
	currentCity=0	
	tour.remove(currentCity)	
	greedyTour.append(currentCity)
	distance=float("inf")
	tmp=0
	while (tour):
		distance=float("inf")
		for i in tour:
			tmp=matrix[currentCity,i]
			if (tmp<distance):
				distance=tmp
				visitedCity=i
		tour.remove(visitedCity)
		greedyTour.append(visitedCity)
		currentCity=visitedCity
	return greedyTour 

#############################
#MAIN
#############################
filename="test-input-7.txt" 
cities=readinstance(filename)

matrix=cartesian_matrix(cities)

tour=list(xrange(len(cities)))

greedyTour=greedy(matrix,tour)

print tour_length(matrix,greedyTour)

