#coding: utf-8
import random
from kmean import Kmean

points = [[1, 2], [2, 1], [3, 1], [5, 4], [5, 5], [6, 5], [7, 9], [99, 96], [94, 91], [92, 89]]
algo = Kmean(points, 2)
mu, clusters_points = algo.get_clusters()

print mu
print clusters_points
