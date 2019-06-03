import numpy as np


#implementation of slide 642. Note that there is a mistake in dist formula on the slide. There should be a "()" around the last part.


#choose 2 points on the given line, and a point (x) to which the distance is calculated

p1 = np.array([6,0])
p2 = np.array([4,4])
x = np.array([6,2])

cluster1 = np.array([[1,1],[2,2.5],[2,4],[3,4],[2,6],[1,7],[0.5,8]])
cluster2 = np.array([[6,2],[7,3],[8,4],[8.5,2.5],[9,4.5],[7,6]])

###
w = np.multiply(np.array([-1, 1]),p1 - p2)[::-1]
#w = np.array([2,1])


b = np.dot(w,p1)

def dist(w,x, b):

    return(abs((1/(np.sqrt(np.dot(w, w)))) * (np.dot(w,x) - b)))

print("The points given as line representatives are (p1, p2)")

print(p1, p2)

print("the hyperplane formula is")

print(w,"* x", "+", b, " = 0")

print("the distance is")
print(dist(w, x, b))


cluster1_ = [dist(w, k, b) for k in cluster1]
cluster2_ = [dist(w, k, b) for k in cluster2]

print("the support vector for cluster 1 is ")
print(cluster1[cluster1_.index(min(cluster1_))])

print("the support vector for cluster 2 is ")
print(cluster2[cluster2_.index(min(cluster2_))])

