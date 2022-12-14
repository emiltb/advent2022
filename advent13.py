data = [s.splitlines() for s in open("inputs/input13.txt").read().strip().split("\n\n")]


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            return a - b
        else:
            return compare([a], b)

    else:
        if type(b) == int:
            return compare(a, [b])

    for n, m in zip(a, b):
        value = compare(n, m)
        if value:
            return value

    return len(a) - len(b)


test = []

for i, (a, b) in enumerate(data):
    if compare(eval(a), eval(b)) < 0:
        test.append(i + 1)
print(sum(test))
