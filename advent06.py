def slider(obj, w):
    window = obj[:w]
    yield window

    for s in obj[w:]:
        window = window[1:]
        window += s
        yield window

def find_code(data, width):
    objslider = slider(data, width)

    for i, code in enumerate(objslider):
        if len(set(code)) == width:
            print(i, code)
            endpos = i + width
            break
    return endpos

with open("inputs/input06.txt", "r") as f:
    data = f.read()

# Part 1
first_marker = find_code(data, 4)
print("First marker:", first_marker)

# Part 2
first_message = find_code(data, 14)
print("First message:", first_message)
