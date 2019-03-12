# LeetCode 973: K Closest Points to Origin
# We have a list of points on the plane.  
# Find the K closest points to the origin (0, 0).

import random

def kClosest(points, K):
    if len(points) == K:
        return points

    if len(points) <= 0:
        return []

    pivotIndex = 0
    if len(points) > 1:
        pivotIndex = random.randint(0, len(points) - 1)

    pivot = points[pivotIndex]
    pivotDist = pivot[0] ** 2 + pivot[1] ** 2

    bigger = []
    smaller = []

    for idx, value in enumerate(points):
        if idx == pivotIndex:
            continue
        elif value[0] ** 2 + value[1] ** 2 > pivotDist:
            bigger.append(value)
        else:
            smaller.append(value)

    if len(smaller) == K:
        return smaller
    elif len(smaller) > K:
        return kClosest(smaller, K)
    else:
        return smaller + [pivot] + kClosest(bigger, K - len(smaller) - 1)

def main():
    print(kClosest([[1,3],[-2,2]], 1))
    print(kClosest([[3,3],[5,-1],[-2,4]], 2))

if __name__ == "__main__":
    main()