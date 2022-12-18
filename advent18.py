voxels = [
    [int(n) for n in v.strip().split(",")]
    for v in open("inputs/input18.txt").readlines()
]

s = 0
# Check all voxels
for x, y, z in voxels:
    # Examine all immediate neighbours.
    for t in [
        [x + 1, y, z],
        [x - 1, y, z],
        [x, y + 1, z],
        [x, y - 1, z],
        [x, y, z + 1],
        [x, y, z - 1],
    ]:
        # If the neighbour does not exist it contributes to
        # surface area
        if t not in voxels:
            s += 1
print("Surface area of obsidian:", s)
