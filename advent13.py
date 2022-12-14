data = [s.splitlines() for s in open("inputs/input13.txt").read().strip().split("\n\n")]


def compare(a, b):
    if type(a) == int:
        if type(b) == int:
            # If both values are integers, the lower value should come first
            # This means that a negative result here indicates wrong order
            return a - b
        else:
            # If exactly one value is an integer, convert the integer to a list
            # which contains that integer as its only value, then retry the comparison.
            return compare([a], b)

    elif type(b) == int:
        # If exactly one value is an integer, convert the integer to a list
        # which contains that integer as its only value, then retry the comparison.
        return compare(a, [b])

    # Otherwise both values are lists
    for n, m in zip(a, b):
        # Compare the first value of each list, then the second value, and so on.
        value = compare(n, m)
        if value:
            return value

    # If the left list runs out of items first, the inputs are in the right order.
    # If the right list runs out of items first, the inputs are not in the right order.
    return len(a) - len(b)


test = []

for i, (a, b) in enumerate(data):
    if compare(eval(a), eval(b)) < 0:
        test.append(i + 1)
print(sum(test))
