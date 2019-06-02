import math
import pprint

import numpy as np

data2 = [[(1, 2), (2, 3), (1, 3)], [(4, 5), (4, 6), (1, 1)], [(10, 12), (11, 12), (14, 17)]]
data = [[(1, 5), (2, 3), (3, 4), (10, 1)], [(6, 8), (7, 7), (7, 8), (7, 9)]]


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


def dist_other_cluster():
    return 1


def remove_from_cluster(cluster, p):
    return [x for x in cluster if x != p]


def dist_to_Rest_of_cluster(cluster, p, dist):
    c = remove_from_cluster(cluster, p)
    cluster_dist = get_centroid(c)
    d = dist(p, cluster_dist)
    return d


def get_centroid(cluster):
    a = sum([x[0] for x in cluster]) / len(cluster)
    b = sum([x[1] for x in cluster]) / len(cluster)

    return (a, b)


def get_min(clusters, dist, p):
    other_clusters = [x for x in clusters if p not in x]
    other_centroids = [get_centroid(x) for x in other_clusters]
    # print(other_centroids)
    return min([dist(p, x) for x in other_centroids])


def silhouette(clusters, dist):
    for cluster in clusters:
        for p in cluster:
            print(p)
            a = dist_to_Rest_of_cluster(cluster, p, dist)
            b = get_min(clusters, dist, p)
            print((b - a) / (max(a, b)))


def get_medoid(cluster, dist):
    centroid = get_centroid(cluster)

    medoid_list = [dist(centroid, p) for p in cluster]
    # print(medoid_list)
    # print(medoid_list.index(min(medoid_list)))
    return cluster[medoid_list.index(min(medoid_list))]


def simple_silhouette(clusters, dist, representatives):
    if representatives == 0:
        all_medoids = [get_medoid(cluster, dist) for cluster in clusters]
    else:
        all_medoids = representatives
    result = []
    for i in range(0, len(clusters)):
        for points in clusters[i]:
            my_medoid = get_medoid(clusters[i], dist)
            other_medoids = [x for x in all_medoids if my_medoid != x]

            a = dist(points, my_medoid)
            b = min([dist(points, x) for x in other_medoids])

            r = (b - a) / (max(a, b))
            result.append((points, r))
    pprint.pprint(result)


simple_silhouette(data, manhat,
                  0)  # give representatives as third input. if representatives are not given give 0 as input

# silhouette(data,manhat)
