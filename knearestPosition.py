def Kclosest(points, target, K):
    sortedPoints = sorted(points, key=lambda p: distance(p, target))
    return sortedPoints[:K]


def distance(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2
