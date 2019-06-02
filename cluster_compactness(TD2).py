import numpy as np
import math


data2 = [[(1, 5), (2, 3), (3, 4), (10, 1)], [(6, 8), (7, 7), (7, 8), (7, 9)]]
data = [[(1, 5), (2, 3), (3, 4)],[(10, 1)], [(6, 8), (7, 7), (7, 8), (7, 9)]]

def get_centroid(cluster):
    a = sum([x[0] for x in cluster]) / len(cluster)
    b = sum([x[1] for x in cluster]) / len(cluster)

    return (a, b)

def euclid(p, o):
    """
    o and p vectors of same length
    :param o: vector
    :param p: vector
    :return:
    """
    return math.sqrt(sum([(v[0] - v[1]) ** 2 for v in zip(o, p)]))


def manhat(p, o):
    return np.sum(abs((np.array(p) - np.array(o))))

def TD(clusters, dist):

    TD_overall = 0
    for cluster in clusters:
        centroid = get_centroid(cluster)


        TD = sum([dist(p,centroid)**2 for p in cluster])
        print("The TD score for cluster ", cluster, " is ", TD)
        TD_overall += TD

    print("The TD score for all clusters is ", TD_overall)


TD(data,euclid)