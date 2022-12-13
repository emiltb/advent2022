# Failed to solve this one.
# Adapted from https://github.com/matheusstutzel/adventOfCode/blob/main/2022/12/p1.py
with open("inputs/input12.txt", "r") as f:
    raw_data = f.readlines()


def convert_height(h):
    if h == "S":
        return "a"
    if h == "E":
        return "z"
    return h


def compare(n1, n2):
    n1 = ord(convert_height(n1))
    n2 = ord(convert_height(n2))
    return n2 <= (n1 + 1)


def dijkstra(start, mat, cost):
    q = []
    cost[start] = 0
    q.append((start, 0))

    while len(q) > 0:
        n, c = q.pop()  # node, cost

        if cost[n] != c:
            continue
        for v in mat[n]:
            if cost[v] > (c + 1):
                cost[v] = c + 1
                q.append((v, c + 1))


l = [l.strip() for l in raw_data]

lines = len(l)
cols = len(l[0])

mat = []
for i in range(lines):
    for j in range(cols):
        pos = j + i * cols
        v = l[i][j]
        if v == "S":
            start = pos
        if v == "E":
            end = pos

        adj = []
        # top
        if i > 0 and compare(v, l[i - 1][j]):
            adj.append(j + (i - 1) * cols)
        # left
        if j > 0 and compare(v, l[i][j - 1]):
            adj.append(j - 1 + i * cols)
        # down
        if i + 1 < lines and compare(v, l[i + 1][j]):
            adj.append(j + (i + 1) * cols)
        # right
        if j + 1 < cols and compare(v, l[i][j + 1]):
            adj.append(j + 1 + i * cols)

        mat.append(adj)

cost = [999] * (lines * cols)
dijkstra(start, mat, cost)

print(cost[end])


# Part 2
# Solution adapted from https://github.com/matheusstutzel/adventOfCode/blob/main/2022/12/p2.py
# since I really struggled with this one.


def compare(n1, n2):
    n1 = ord(convert_height(n1))
    n2 = ord(convert_height(n2))
    return n2 >= (n1 - 1)


mat = []
for i in range(lines):
    for j in range(cols):
        pos = j + i * cols
        v = l[i][j]
        if v == "S":
            start = pos
        if v == "E":
            end = pos

        adj = []
        # top
        if i > 0 and compare(v, l[i - 1][j]):
            adj.append(j + (i - 1) * cols)
        # left
        if j > 0 and compare(v, l[i][j - 1]):
            adj.append(j - 1 + i * cols)
        # down
        if i + 1 < lines and compare(v, l[i + 1][j]):
            adj.append(j + (i + 1) * cols)
        # right
        if j + 1 < cols and compare(v, l[i][j + 1]):
            adj.append(j + 1 + i * cols)

        mat.append(adj)

cost = [999] * (lines * cols)
dijkstra(end, mat, cost)

# for i in range(lines):
#    for j in range(cols):
#        print("%03d%s"%(cost[ j + i*cols], l[i][j]), end=" ")
#    print("")
print(min([c for idx, c in enumerate(cost) if l[idx // cols][idx % cols] == "a"]))
