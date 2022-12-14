lines = []
with open("inputs/input14.txt") as f:
    for line in f:
        lines.append(line.strip().split("->"))

coords = [[[int(n) for n in c.split(",")] for c in l] for l in lines]

coords
