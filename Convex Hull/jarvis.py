#Using cross product to determine the side p3(x3,y3) lies on of the line though p1(x1,y1) and p2(x2,y2)
# |x2-x1  x3-x1|
# |y2-y1  y3-y1|    =   (x2-x1)(y3-y1) - (x3-x1)(y2-y1)
# Positive if point is above (left side), 0 if point is on the line
# and negative if point is below the line (right side)
def distance(p, q):
    x, y = q[0] - p[0], q[1] - p[1]
    return x*x + y*y
 
def CCW_point(points, p):
    q = p
    for r in points:
        direction = ((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]))
        if direction < 0 or direction == 0 and distance(p, r) > distance(p, q):
            q = r
    return q
 
def convex_hull(points):
    hull = [min(points)]
    for p in hull:
        q = CCW_point(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull

# Read file and discard the 3rd coordinate
cordinates =[]
with open("sample.txt") as f:
    lines = f.readlines()
    for line in lines:
        u = line.split()
        cordinates.append([float(u[0]),float(u[1])])

convex_hull_points = convex_hull(cordinates)
for point in convex_hull_points:
    print point
print "There are a total of " + str(len(convex_hull_points)) + " points in the convex hull"