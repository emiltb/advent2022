import re

data = [
    [int(n) for n in re.findall("[\d]+", s)]
    for s in open("inputs/input15.txt").read().strip().splitlines()
]

sensors = [(a, b) for (a, b, *_) in data]
beacons = [(c, d) for (*_, c, d) in data]

y_target = 2000000

x_ranges = []
for s, b in zip(sensors, beacons):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])

    min_y, max_y = s[1] - dist, s[1] + dist
    if min_y < y_target < max_y:
        dist_x = dist - abs(y_target - s[1])
        min_x, max_x = s[0] - dist_x, s[0] + dist_x
        x_ranges.append([min_x,max_x])

xvals = set()
for (x1,x2) in x_ranges:
    for x in range(x1,x2):
        xvals.add(x)

print(len(xvals))
