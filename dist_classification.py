import itertools

import dist


def is_reflexive(points, func):
    print("Checking reflexive")
    for x in points:
        for y in points:
            if x == y and not func(x, y) == 0:
                print("Reflexivity failed for x:{}, y:{}".format(x, y))
                return 0
    print("..passed..")
    return 1


def is_symmetric(points, func):
    print("Checking symmetric")
    for x in points:
        for y in points:
            if func(y, x) != func(x, y):
                print("Symmetry failed for x:{}, y:{}".format(x, y))
                return 0
    print("..passed..")
    return 1


def is_strict(points, func):
    print("Checking strict")
    for x in points:
        for y in points:
            if func(x, y) == 0 and not x == y:
                print("Strict failed for x:{}, y:{}".format(x, y))
                return 0
    print("..passed..")
    return 1


def is_triangle_inadequate(points, func):
    print("UNSAFE: DONT TRUST")
    print("Checking triangle inequality")
    for x in points:
        for y in points:
            for z in points:
                # print("POINTS:", x,y,z)
                # print("FIRST :", func(x,z), "SECOND :", func(x,y), "THIRD:", func(y, z))
                if func(x, z) > func(x, y) + func(y, z):
                    print("Triangle inequality failed for x:{}, y:{}, z:{}".format(x, y, z))
                    return 0
    print("..passed..")
    return 1


def classify(func):
    points = list(itertools.permutations(range(-5, 5), 2))

    res = [0, 0, 0, 0]

    res[0] = is_reflexive(points, func)
    res[1] = is_symmetric(points, func)
    res[2] = is_strict(points, func)
    res[3] = is_triangle_inadequate(points, func)

    if sum(res) == 4:
        print("Metric!")
    elif sum(res) == 3 and res[2] == 0:
        print("Pseudo-metric")
    elif sum(res) == 3 and res[3] == 0:
        print("Semi-metric, Ultra-metric")
    elif sum(res) == 2 and res[2] == 0 and res[3] == 0:
        print("(Symmetric) Pre-metric")
    elif sum(res) == 1 and res[0] == 1:
        print("Dissimilarity function")
    else:
        print("Nothing fit! -> Unknown type")


def unknown_func(p1, p2):
    # return sum(1 if val[0] != val[1] else 0 for val in zip(p1, p2))
    return (sum([abs(pair[0] - pair[1]) ** 0.01 for pair in zip(p1, p2)])) ** 2


classify(unknown_func)
# classify(dist.manhat)
# print(unknown_func((1, 2), (2, 3)))

"""
print(unknown_func(
    (0, 1),
    (0, 5)
))

print(
    unknown_func(
        (0, 1),
        (0, 3)
    )
    +
    unknown_func(
        (0, 3),
        (0, 5)
    )
)
"""
