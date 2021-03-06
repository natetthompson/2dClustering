#!/usr/bin/python

#Author: Nathan Thompson
#Date: 3/19/2017
#python3

import random, math
import matplotlib.pyplot as plt #used for plotting
f = open('ClusteringOutput', 'w') #output file

start = [[1, 1], [1, 7], [3, 3], [3, 9], [4, 6], [4, 8], [5, 5], [6, 2], [7, 6], [8, 8], [9, 1], [10, 4], [10, 6], [10, 10], [12, 2], [18, 22]] # data to be clustered
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] # defines colors to be assigned to graph markers

def initialcuster(k, inpoints = [], *args): # finds the random starting position for clusters
	centroids = []

	for i in range(k):
		randomtemp = randomcluster(inpoints)
		 # randomly chooses between from points in data set to serve as a starting centroid
		while randomtemp in centroids: # while loop ensures that each random centroid is picked only once
			randomtemp = randomcluster(inpoints)

		centroids.append(randomtemp)

	print(centroids)
	s = ("Random initial centroids: " + str(centroids))
	f.write(str(s)+'\n')

	return centroids

def closestcluster( x, y, clusters = [], *args): # calulates the closest centroid for an individual point x,y
	mindist = 10000
	
	for i in range(len(clusters)):
		
		dist = math.hypot(x-clusters[i][0], y-clusters[i][1]) # math function hypot can be used to calculate the distance between points

		if dist < mindist: # if the distance is smaller than the distance from the previous centroid then this centroid is assigned to that point
			mindist = dist
			cluster = clusters[i]

	return cluster, [x,y]

def plot(centroids= [], groups = [], *args): # funciton for plotting resulting graph

	
	s = ("Final plot saved as FinalResult.jpg")    
	f.write(str(s)+'\n')
	fig = plt.figure()

	for j in range(len(groups)): # itterates through and plots all points and assigns the corresponding color 

		style = []
		color = colors[j]
		for k in range(len(groups[j])):

			if k != len(groups[j])-1:
				plt.scatter(groups[j][k][0],groups[j][k][1], marker = '.', color = color) # regular points are plotted as dots
			else:
				
				plt.scatter(groups[j][k][0],groups[j][k][1], marker = '+', color = color, s = 100) # centroids are plotted as +, also the size of each centroid decreases so that one centroid marker whill not completely cover another
	fig.show()
	fig.suptitle("FinalResult", fontsize=20)

	fig.savefig("FinalResult.jpg")

def randomcluster(inpoints = [], *args): #random method for finding a point fro mthe data

	cluster = inpoints[random.randint(0, len(inpoints)-1)]
	return cluster

def mean(inpoints = [], *args): # custom function to find the mean between a group of 2d points
	x = []
	y = []
	sumx = 0
	sumy = 0
	for i in range(len(inpoints)):
		x.append(inpoints[i][0])
		y.append(inpoints[i][1])
	for j in range(len(x)):
		sumx = sumx + x[j]
	meanx = sumx/len(x)
	for k in range(len(y)):
		sumy = sumy + y[k]
	meany = sumy/len(y)
	return [meanx, meany]

k = 4 # k value for clusters
maxiterations = 16 # number of iterations 
centroids = initialcuster(k,start) # calls the funciton to find initial clusters with k clusters

change = True
count = 0 # used for counting the number of iterations

while (change == True):

	groups = [] # used for holding the points that belong to each centroid
	newcentroids = [] # used for comparing centroids from the previous iteration
	results = []
	s = ("Iteration: " + str(count+1)+"|| Centroids: "+ str(centroids))

	f.write(str(s)+'\n')
	for i in range(len(start)):

		output = closestcluster(start[i][0], start[i][1], centroids)

		results.append(output)

	for i in range(len(centroids)): # the following 2 for loops iterate through the centroids and finds all 2d points that have been assigned to them

		group = []

		for j in range(len(results)):

			if results[j][0] == centroids[i]:

				group.append(results[j][1]) #then assigns the point to the corresponding centroid group

		group.append(centroids[i])
		if len(group) > 1: # used to see if the centroid is empty or not

			newcentroids.append(mean(group))
			groups.append(group)

	if newcentroids == centroids or (count >= maxiterations-1): # exit condition when there is no change in centroid positions or count goes above 10 (max itertions)
		change = False
		plot(newcentroids, groups)
				
	else:
		centroids = newcentroids # assigns newly found centroids to main centroid list
		count = count + 1
f.close # close write file
print("Done!")		
print("Output saved to CentroidOutput.txt and FinalResult.jpg")
		









 
	
	
	
	
