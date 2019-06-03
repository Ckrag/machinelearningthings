from scipy.spatial import distance
from scipy.special import gamma
import numpy as np
import math


def kthneighbor(p,k,neighbors):
    neighbor = neighbors[0]
    dist = distance.cityblock(p,neighbor)
    for n in neighbors:
        _dist = distance.cityblock(p,n)
        if _dist >= dist:
            neighbor = n
            dist = _dist
    return (neighbor,dist)

def kneighbor(p,k,points):
    return sortByDistance(p,points)[k] #0 indexed so p is at 0

#fixed k
def density(x,k,points):
    d = x.shape[0]
    n = len(points)
    neighbork = kneighbor(x,k,points)
    dist = distance.cityblock(x,neighbork)
    #Vk = (math.pow(math.pi,d/2)/(gamma((d/2) + 1)))*math.pow(dist,d) #hypersphere formula
    Vk = 2*math.pow(dist,d) #hypercube volume <-- LIKELY HAVE TO CHANGE THIS
    #print(d,dist,Vk)
    return (k+1)/(n*Vk) #k+1?

def densityFixedVol(x,points,r):
    return -1
    #find k from Vk, see slides, then make method.


def sortByDistance(p,points):
    return sorted(points, key=lambda point: distance.cityblock(p,point))


# REMEMBER TO SET VOLUME FORMULAR ON LINE 27!!!

#20 points in dataset
#point = np.array([1,1])
points = np.array([
[1,1],
[1,2],
[2,1],
[2,2],
[3,5],
[3,9],
[3,10],
[4,10],
[4,11],
[5,10],
[7,10],
[9,4],
[9,5],
[10,3],
[10,4],
[10,5],
[10,6],
[10,9],
[11,4],
[11,5],
])

for p in points:
    print(density(p,2,points))

#print(density(points[0],2,points))