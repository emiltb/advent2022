import matplotlib.pyplot as plt

lines = []
with open("inputs/input14.txt") as f:
    for line in f:
        lines.append(line.strip().split("->"))

coords = [[[int(n) for n in c.split(",")] for c in l] for l in lines]


all_cords = set()
for c in coords:
    for i, (x, y) in enumerate(c):
        if i < len(c) - 1:
            nx = c[i + 1][0]
            ny = c[i + 1][1]
            all_cords.add((x, y))
            [all_cords.add((new_x, y)) for new_x in range(min([x, nx]), max([x, nx]))]
            [all_cords.add((x, new_y)) for new_y in range(min([y, ny]), max([y, ny]))]

src = (500, 0)

sand_coords = set()

bottom_reached = False
y_limit = max([y for (x, y) in all_cords])

last_path = []


while bottom_reached is False:
    # Create a new unit of sand
    sx = src[0]
    sy = src[1] + 1
    next_is_vacant = True

    while next_is_vacant:
        # Check if the next position below is vacant
        if (sx, sy + 1) not in all_cords and (sx, sy + 1) not in sand_coords:
            sy += 1
        elif (sx - 1, sy + 1) not in all_cords and (sx - 1, sy + 1) not in sand_coords:
            sy += 1
            sx -= 1
        elif (sx + 1, sy + 1) not in all_cords and (sx + 1, sy + 1) not in sand_coords:
            sy += 1
            sx += 1
        else:
            next_is_vacant = False
            sand_coords.add((sx, sy))

        if len(sand_coords) == 97 and next_is_vacant == True:
            last_path.append([sx, sy])

        if sy == y_limit:
            bottom_reached = True
            break

print(len(sand_coords))

fig = plt.figure(figsize=(20 / 2.53, 20 / 2.54), dpi=150)
ax = plt.axes()

ax.scatter(src[0], src[1], c="green", s=1, marker="s")
ax.scatter(sx, sy, c="red", s=1, marker="s")
ax.scatter([x[0] for x in all_cords], [x[1] for x in all_cords], s=1, marker="s")
ax.scatter(
    [x[0] for x in sand_coords],
    [x[1] for x in sand_coords],
    s=1,
    marker="s",
    c="orange",
)
ax.scatter(
    [x[0] for x in last_path],
    [x[1] for x in last_path],
    s=1,
    marker="s",
    c="cyan",
)
ax.invert_yaxis()
last_path
