import numpy as np


def euclid(p1, p2):
    a = np.array(p1)
    b = np.array(p2)
    return np.linalg.norm(a - b)


def manhat(p1, p2):
    return sum([abs(pair[0] - pair[1]) for pair in zip(p1, p2)])


def maximum(p1, p2):
    return max([abs(pair[0] - pair[1]) for pair in zip(p1, p2)])


def weighted_euclidian(p1, p2, w):
    return sum([vals[2] * (vals[0] - vals[1]) ** 2 for vals in zip(p1, p2, w)])


def quadratic(p1, p2, M):
    """

    :param p1: (1, 2)
    :param p2: (3, 4)
    :param M: [[1, 2], [3, 4]]
    :return:
    """
    a = np.array(p1)
    b = np.array(p2)
    m = np.array(M)

    return ((a - b) @ m @ (a - b).T) ** 0.5


if __name__ == "__main__":
    print(quadratic((2, 3, 5), (4, 7, 8), [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
