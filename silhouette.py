import math
import numpy as np
import pprint


def centroid(cluster):
    return (sum([x[0] for x in cluster])) / len(cluster), (sum([y[1] for y in cluster])) / len(cluster)


def find_own_cluster(clusters, p):
    return [x for x in clusters if p in x]


def find_other_clusters(clusters, p):
    return [x for x in clusters if p not in x]


def find_mediod(cluster, centroid, dist):
    return [x for x in (min([dist(p, centroid) for p in cluster]))]


def silhouette(clusters, dist):
    result = []
    for cluster in clusters:
        for p in cluster:
            own_cluster = find_own_cluster(clusters, p)
            other_clusters = find_other_clusters(clusters, p)
            other_centroids = [centroid(c) for c in other_clusters]
            own_cluster_without_self = [x for x in own_cluster[0] if x != p]
            own_centroid = [centroid(c) for c in [own_cluster_without_self]]
            dist_to_own_cluster = dist(p, own_centroid[0])
            dist_to_closest_cluster = min(dist(p, o) for o in other_centroids)
            result.append((p,
                           (dist_to_closest_cluster - dist_to_own_cluster) / max(dist_to_own_cluster,
                                                                                 dist_to_closest_cluster)))
    pprint.pprint(result)


def simple_silhouette(clusters, dist):
    own_mediod_distances = []
    other_mediod_distances = []
    for cluster in clusters:
        for p in cluster:
            own_cluster = find_own_cluster(clusters, p)
            other_clusters = find_other_clusters(clusters, p)
            other_centroids = [centroid(c) for c in other_clusters]
            own_centroid = [centroid(c) for c in [own_cluster][0]]
            own_mediod = (p, dist(own_centroid, p))
            own_mediod_distances.append(own_mediod)
        print("CLUSTER 1")
        pprint.pprint(other_mediod_distances)


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


# silhouette([[(1, 2), (1, 3), (4, 2)], [(5, 6), (4, 7), (8, 4), (4, 5)], [(10, 12), (14, 13), (15, 23)]], manhat)

simple_silhouette([[(4, 2), (1, 3), (4, 2)], [(5, 6), (4, 7), (8, 4), (4, 5)], [(10, 12), (14, 13), (15, 23)]], manhat)
