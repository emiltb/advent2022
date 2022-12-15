import re

data = [
    [int(n) for n in re.findall("[\d]+", s)]
    for s in open("inputs/input15.txt").read().strip().splitlines()
]

sensors = [(a, b) for (a, b, *_) in data]
beacons = [(c, d) for (*_, c, d) in data]

covered = set()

for s, b in zip(sensors, beacons):
    covered.add(s)
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])

    min_x, max_x = s[0] - dist, s[0] + dist
    min_y, max_y = s[1] - dist, s[1] + dist
    print(min_x, max_x, min_y, max_y, (max_x - min_x) * (max_y - min_y))

    #for x in range(min_x, max_x + 1):
    #    for y in range(min_y, max_y + 1):
    #        if abs(s[0] - x) + abs(s[1] - y) <= dist:
    #            covered.add((x, y))
    #break

covered
