#coding:utf-8
import numpy
import random

class Kmean:
	""" 
	If you would like to cluster specific dataset and cluster numbers, Use
	kmean = Kmean(dataset=[[1,1],[2,2],[3,3]], centroid=8)
	else the program would random select dataset, and auto choose a good centroid
	"""
	@classmethod
	def __init__(self, dataset=None, centroid=None):
		self.dataset = dataset
		self.centroid = centroid

	""" Should have a algorithm to select a reasonable cluster number here """
	@classmethod
	def get_centroid_numbers(self):
		return 2

	""" Generate ranom number """
	@classmethod
	def get_random_points(self, numbers, begin=1, end=10):
		dataset = [[random.uniform(begin, end), random.uniform(begin, end)] for i in range(numbers)]
		dataset = [[float("{0:.2f}".format(data)) for data in point] for point in dataset]
		return dataset

	""" Get distance between two point """
	@classmethod
	def get_distance(self, point_a, point_b):
		return numpy.sqrt(sum((numpy.array(point_a) - numpy.array(point_b)) ** 2))

	""" Split all number into k groups """
	@classmethod
	def get_clusters_points(self, dataset, centroids):
		clusters_points = []
		for i in range(len(centroids)):
			clusters_points.append([])
		for point in dataset:
			distances = [self.get_distance(point, centroid) for centroid in centroids]
			belonging_cluster_id = distances.index(min(distances))
			clusters_points[belonging_cluster_id].append(point)
		return clusters_points

	""" Move centroids to a more reasonable place """
	@classmethod
	def move_centroids(self, clusters_points):
		mu = []
		for points in clusters_points:
			mu.append(numpy.mean(points, axis=0))
		return mu

	""" Check if two group of centroids has changed """
	@classmethod
	def converged(self, old_mu, new_mu):
		for (i, k) in zip(old_mu, new_mu):
			for (x, y) in zip(i, k):
				if x != y: return False
		return True

	""" 
	Main method to get centroids and clusters 
	Return a set that include two list.
	@return {mu} is the centroids coordinates
	@return {clusters_points} is all the points divided in groups.
	
	Example:
		clusters_points[0] means the points belongs to the mu[0]
	"""
	@classmethod
	def get_clusters(self):
		if self.dataset == None:
			self.dataset = self.get_random_points(100)
		if self.centroid == None:
			self.centroid = self.get_centroid_numbers()
		# Choose random points as cluster centroid
		mu = self.get_random_points(self.centroid)
		last_mu = self.get_random_points(self.centroid)
		# Avoid the situation that first pick of two sets are converged.
		first_loop = True
		while first_loop or not self.converged(last_mu, mu):
			if first_loop: first_loop = False
			last_mu = mu
			# Divided the points into K clusters.
			clusters_points = self.get_clusters_points(self.dataset, mu)
			# Move the centroids towords to the center
			mu = self.move_centroids(clusters_points)
		return (mu, clusters_points)

