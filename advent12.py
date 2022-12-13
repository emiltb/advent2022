from string import ascii_lowercase
import networkx as nx
import matplotlib.pyplot as plt


with open("inputs/input12.txt", "r") as f:
    raw_data = f.readlines()

data = [[c for c in s.strip()] for s in raw_data]
letters = {l: (ord(l) - 96) for l in ascii_lowercase}
letters["S"] = 1
letters["E"] = 26
heights = [[letters[c] for c in s.strip()] for s in raw_data]


pos = {}
for i, y in enumerate(data):
    for j, x in enumerate(y):
        if x == "S":
            pos["start"] = (i, j)
        if x == "E":
            pos["end"] = (i, j)
print(pos)

direction = {"up": [0, -1], "down": [0, 1], "left": [-1, 0], "right": [1, 0]}

fig = plt.figure(figsize=(20 / 2.54, 10 / 2.54), dpi=150)
ax = plt.axes()

ax.imshow(heights)

G = nx.Graph()
x = len(heights[0])
y = len(heights)
for i in range(x):
    for j in range(y):
        neighbours = {
            "up": [sum(x) if j > 0 else None for x in zip([i, j], direction["up"])],
            "down": [
                sum(x) if j < y - 1 else None for x in zip([i, j], direction["down"])
            ],
            "left": [sum(x) if i > 0 else None for x in zip([i, j], direction["left"])],
            "right": [
                sum(x) if i < j - 1 else None for x in zip([i, j], direction["right"])
            ],
        }
        for key, item in neighbours.items():
            if None not in item:
                height_diff = abs(heights[j][i] - heights[item[1]][item[0]])

                if height_diff <= 1:
                    ax.plot([i, item[0]], [j, item[1]], color="red", linewidth=1)

                # print(height_diff, f"{i},{j}", f"{item[1]},{item[0]}")
                if height_diff <= 1:
                    G.add_edge(f"{i},{j}", f"{item[0]},{item[1]}")

ax.plot(pos["start"][1], pos["start"][0], "g.")
ax.plot(pos["end"][1], pos["end"][0], "g.")
print(G)
astar_path = nx.astar_path(
    G, f"{pos['start'][1]},{pos['start'][0]}", f"{pos['end'][1]},{pos['end'][0]}"
)

nx.dijkstra_path(
    G, f"{pos['start'][1]},{pos['start'][0]}", f"{pos['end'][1]},{pos['end'][0]}"
)

print(len(astar_path) - 1)
