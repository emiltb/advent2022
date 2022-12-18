voxels = [
    [int(n) for n in v.strip().split(",")]
    for v in open("inputs/input18_example.txt").readlines()
]

s = 0
air_voxels = []  # For part 2
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
            air_voxels.append(t)
            s += 1
print("Surface area of obsidian:", s)

# Part 2

trapped_voxels = 0
for x, y, z in air_voxels:
    neighbours = [
        [x + 1, y, z],
        [x - 1, y, z],
        [x, y + 1, z],
        [x, y - 1, z],
        [x, y, z + 1],
        [x, y, z - 1],
    ]
    if all([n in voxels for n in neighbours]):
        trapped_voxels += 1

print(trapped_voxels)

surface_area = s - trapped_voxels
print(surface_area)
