'''
Given two line segments (xStart, yStart, xEnd, yEnd), find and return the intersection point if it exists
If it doesn't exists, or if they're parallel, return nil.
It's guaranteed that x values are increasing
'''

import numpy as np

# Define the function
def findIntersect(point1, point2):
    # Check if the points are parallel
    slope1 = (point1[3] - point1[1]) / (point1[2] - point1[0])
    slope2 = (point2[3] - point2[1]) / (point2[2] - point2[0])
    if slope1 == slope2: return None

    # Find the intersection point (treat segments as infinite lines)
    a = np.array([[slope1, -1], [slope2, -1]])
    b = np.array([point1[0]*slope1 - point1[1], point2[0]*slope2 - point2[1]])
    intersection = np.linalg.solve(a, b)

    # Check if's on both of the points
    point1 = sorted([point1[0], point1[2]]) + sorted([point1[1], point1[3]])
    point2 = sorted([point2[0], point2[2]]) + sorted([point2[1], point2[3]])
    if intersection[0] >= point1[0] and intersection[0] <= point1[1] and intersection[1] >= point1[2] and intersection[1] <= point1[3]:
        if intersection[0] >= point2[0] and intersection[0] <= point2[1] and intersection[1] >= point2[2] and intersection[1] <= point2[3]:
            return intersection
    return None


# Define points for testing
point1 = (0,0,10,10)
point2 = (10,10,20,0)
print findIntersect(point1, point2)

point1 = (0,0,10,10)
point2 = (0,10,10,0)
print findIntersect(point1, point2)

point1 = (0,0,10,10)
point2 = (1,1,11,11)
print findIntersect(point1, point2)

point1 = (0,0,10,10)
point2 = (10,10,20,0)
print findIntersect(point1, point2)