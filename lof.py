import math
import numpy as np


#NOTE set parameters at the buttom of the script!!



def euclid(p,o):
    """
    o and p vectors of same length
    :param o: vector
    :param p: vector
    :return:
    """
    return math.sqrt(sum([(v[0] - v[1]) ** 2 for v in zip(o, p)]))

def manhat(p,o):

    return np.sum(abs((np.array(p)-np.array(o))))



def xdist(p,k):

    dat = data[:]
    dat.remove(p)

    temp = np.sort([dist(p,o) for o in dat])

    return(temp[k])


def knn(p):

    dat = data[:]
    dat.remove(p)
    temp = [dist(p, o) for o in dat]

    dict1 = {a: b for a, b in list(zip(dat, temp))}
    t = k
    while dict1[sorted(dict1, key=dict1.get)[t]] == dict1[sorted(dict1, key=dict1.get)[t + 1]]:
        t += 1
    return sorted(dict1, key=dict1.get)[:t + 1]


def reachdist(p,o):
    return max(xdist(o,k),dist(p,o))

def lrd(p):

    return 1/(sum([reachdist(p,o) for o in knn(p)]) /len(knn(p)))

def lof(p):




    def lrd_calc(p,o):
        return lrd(o)/lrd(p)

    return (sum([lrd_calc(p, o) for o in knn(p)]) / len(knn(p)))



#set parameters here
data = [(1,1),(1,2),(2,1),(2,2),(3,5),(3,9),(3,10),(4,10),(4,11),(5,10),(7,10),(10,9),(9,4),(9,5),(10,3),(10,4),(10,5),(10,6),(11,4),(11,5)]
p = (10,5)
dist = manhat # choose distance function (manhat and euclid implemented)
k = 2

#preparing global variables:
k -= 1 #NOTE since python is 0 indexed, k needs to be set to one less

#calling lof
print(lof(p))
