#	Take input of file containing list of points
#	in the format (x1,y1) separated by space or new line

TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

def turn(p, q, r):
    return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
        hull.pop()
    return (not len(hull) or hull[-1] != r) and hull.append(r) or hull

def distance(p, q):
    x, y = q[0] - p[0], q[1] - p[1]
    return x*x + y*y

def _graham_scan(points):
    points.sort()
    lh = reduce(_keep_left, points, [])
    uh = reduce(_keep_left, reversed(points), [])
    return lh.extend(uh[i] for i in xrange(1, len(uh) - 1)) or lh

def _rtangent(hull, p):
    l, r = 0, len(hull)
    l_prev = turn(p, hull[0], hull[-1])
    l_next = turn(p, hull[0], hull[(l + 1) % r])
    while l < r:
        c = (l + r) / 2
        c_prev = turn(p, hull[c], hull[(c - 1) % len(hull)])
        c_next = turn(p, hull[c], hull[(c + 1) % len(hull)])
        c_side = turn(p, hull[l], hull[c])
        if c_prev != TURN_RIGHT and c_next != TURN_RIGHT:
            return c
        elif c_side == TURN_LEFT and (l_next == TURN_RIGHT or
                                      l_prev == l_next) or \
                c_side == TURN_RIGHT and c_prev == TURN_RIGHT:
            r = c               # Tangent touches left chain
        else:
            l = c + 1           # Tangent touches right chain
            l_prev = -c_next    # Switch sides
            l_next = turn(p, hull[l], hull[(l + 1) % len(hull)])
    return l

def _min_hull_pt_pair(hulls):
    h, p = 0, 0
    for i in xrange(len(hulls)):
        j = min(xrange(len(hulls[i])), key=lambda j: hulls[i][j])
        if hulls[i][j] < hulls[h][p]:
            h, p = i, j
    return (h, p)

def _next_hull_pt_pair(hulls, pair):
    p = hulls[pair[0]][pair[1]]
    next = (pair[0], (pair[1] + 1) % len(hulls[pair[0]]))
    for h in (i for i in xrange(len(hulls)) if i != pair[0]):
        s = _rtangent(hulls[h], p)
        q, r = hulls[next[0]][next[1]], hulls[h][s]
        t = turn(p, q, r)
        if t == TURN_RIGHT or t == TURN_NONE and distance(p, r) > distance(p, q):
            next = (h, s)
    return next

def convex_hull(pts):
    for m in (1 << (1 << t) for t in xrange(len(pts))):
        hulls = [_graham_scan(pts[i:i + m]) for i in xrange(0, len(pts), m)]
        hull = [_min_hull_pt_pair(hulls)]
        for throw_away in xrange(m):
            p = _next_hull_pt_pair(hulls, hull[-1])
            if p == hull[0]:
                return [hulls[h][i] for h, i in hull]
            hull.append(p)


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