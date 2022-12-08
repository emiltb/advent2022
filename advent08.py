import numpy as np

with open("inputs/input08.txt", "r") as f:
    raw_data = f.readlines()

data = np.array([[c for c in s.strip()] for s in raw_data])
data
len_y, len_x = data.shape

# Part 1
n_visible = 0
for (x, y), h in np.ndenumerate(data):
    if (x == 0) or (y == 0) or (x == len_x - 1) or (y == len_y - 1):
        # We are at an edge
        n_visible += 1
    else:
        left = np.all(h > data[x, :y])  # Left
        right = np.all(h > data[x, (y + 1) :])  # right
        above = np.all(h > data[:x, y])  # Above
        below = np.all(h > data[(x + 1) :, y])  # Below

        if np.any([left, right, above, below]):
            n_visible += 1

print("Number of visible trees:", n_visible)


# Part 2
x = 0
y = 0
data[x, y]
data[x, :y]  # left
data[x, y] > data[x, :y]  # Left
data[x, y] > data[x, (y + 1) :]  # Right
data[x, y] > data[:x, y]  # Above
data[x, y] > data[(x + 1) :, y]  # Below
data
right = data[x, y] > data[x, (y + 1) :]  # Above
np.argmax(right)

scenic_score = np.zeros(data.shape)
for (x, y), h in np.ndenumerate(data):
    left = np.flip(data[x, y] > data[x, :y])  # Above
    right = data[x, y] > data[x, (y + 1) :]  # Above
    above = np.flip(data[x, y] > data[:x, y])  # Above
    below = data[x, y] > data[(x + 1) :, y]  # Above

    n1, n2, n3, n4 = 0, 0, 0, 0
    if left.size != 0:
        n1 = np.argmax(left == False) + 1

    if right.size != 0:
        n2 = np.argmax(right == False) + 1

    if above.size != 0:
        n3 = np.argmax(above == False) + 1

    if below.size != 0:
        n4 = np.argmax(below == False) + 1

    scenic_score[x, y] = n1 * n2 * n3 * n4

scenic_score
np.argmax((data[0, 0] > data[0, :0]) == False) + 1
np.argmax((data[0, 0] > data[0, 1:]) == False) + 1
