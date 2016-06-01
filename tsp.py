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

def all_pairs(size,shuffle=random.shuffle):
    r1=range(size)
    r2=range(size)
    if shuffle:
        shuffle(r1)
        shuffle(r2)
    for i in r1:
        for j in r2:
            yield (i,j)
def reversed_sections(tour):
    '''generator to return all possible variations 
      where the section between two cities are swapped'''
    for i,j in all_pairs(len(tour)):
        if i != j:
            copy=tour[:]
            if i < j:
                copy[i:j+1]=reversed(tour[i:j+1])
            else:
                copy[i+1:]=reversed(tour[:j])
                copy[:j]=reversed(tour[i+1:])
            if copy != tour: # no point returning the same tour
                yield copy
def hillclimb(
    init_function,
    move_operator,
    objective_function,
    max_evaluations):
    '''
    hillclimb until either max_evaluations
    is reached or we are at a local optima
    '''
    best=init_function()
    best_score=objective_function(best)
    
    num_evaluations=1
    
    while num_evaluations < max_evaluations:
        # examine moves around our current position
        move_made=False
        for next in move_operator(best):
            if num_evaluations >= max_evaluations:
                break
            
            # see if this move is better than the current
            next_score=objective_function(next)
            num_evaluations+=1
            if next_score > best_score:
                best=next
                best_score=next_score
                move_made=True
                break # depth first search
            
        if not move_made:
            break # we couldn't find a better move 
                     # (must be at a local maximum)
    
    return (num_evaluations,best_score,best)

def init_random_tour(tour_length):
   tour=range(tour_length)
   random.shuffle(tour)
   return tour

#############################
#MAIN
#############################
move_operator = reversed_sections
max_iterations = 500 
filename="tsp_example_3.txt" 
cities=readinstance(filename)

matrix=cartesian_matrix(cities)
init_function=lambda: init_random_tour(len(cities))
objective_function=lambda tour: -tour_length(matrix, tour)
iterations,score,best=hillclimb(init_function,move_operator,objective_function,max_iterations)

print tour_length(matrix,best)









