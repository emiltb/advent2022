voxels = [[int(n) for n in v.strip().split(',')] for v in open("inputs/input18.txt").readlines()]

s = 0
for x,y,z in voxels:
    print((x,y,z))
    #for t in [[x+1,y,z],[x-1,y,z][x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]]:
    #    print(t)
        #if t not in voxels:
        #    s += 1
print(s)
