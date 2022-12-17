import re
from functools import reduce
def overlaps(a,b):
    # Returns true if a and b overlaps
    return max([a[0],b[0]]) <= min([a[1],b[1]])

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

#xvals = set()
#for (x1,x2) in x_ranges:
#    for x in range(x1,x2):
#        xvals.add(x)

#print(len(xvals))

print(overlaps(x_ranges[0],x_ranges[1]))
def merge_ranges(x1,x2):
    if type(x1[0]) == list:
        return merge_ranges(x1[0],x1[1])
    if type(x2[0]) == list:
        return merge_ranges(x2[0],x2[1])
    if overlaps(x1,x2):
        return [min(x1[0],x2[0]),max(x1[1],x2[1])]
    else:
        return [x1,x2]

print(x_ranges[0], x_ranges[1])
print(merge_ranges(x_ranges[0], x_ranges[1]))

total_range = reduce(merge_ranges, x_ranges)
print(total_range[1] - total_range[0])

total_range = reduce(merge_ranges, [[0,10],[17,20],[5,15]])
print(total_range)

def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
    # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    print("The Merged Intervals are:", end=" ")
    for i in range(len(stack)):
        print(stack[i], end=" ")

arr = [[6,8],[1,9],[2,4],[4,7]]
print(arr)
print(mergeIntervals(arr))
arr = [[0,10],[17,20],[5,15]]
print(arr)
print(mergeIntervals(arr))
