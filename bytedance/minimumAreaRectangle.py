'''
given an array of points in the xy plane points where points[i] = [xi, yi]
return the minimum area of a rectangle that can be formed with these points, with sides parallel to x and y axes

solution
- sort points

'''

def minArea(points):
    minSize = float('inf')

    visitedPoints = set()

    for (x1,y1) in points:
        for (x2, y2) in visitedPoints:
            if (x1, y2) in visitedPoints and (x2, y1) in visitedPoints:
                # we found a rectangle
                area = abs(y1 - y2) * abs(x1 - x2)
                minSize = min(minSize, area)

        visitedPoints.add((x1,y1))

    if minSize == float('inf'):
        return 0
    else:
        return minSize

points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(minArea(points))