with open("inputs/input06.txt", "r") as f:
    data = f.read()

def slider(obj, w):
    window = obj[:w]
    yield window

    for s in obj[w:]:
        window = window[1:]
        window += s
        yield window

# Part 1
width = 4
objslider = slider(data, width)

for i, code in enumerate(objslider):
    if len(set(code)) == 4:
        print(i, code)
        startpos = i
        endpos = i + width
        break

print("First marker:", endpos)

# Part 2
width = 14
objslider = slider(data, width)

for i, code in enumerate(objslider):
    if len(set(code)) == width:
        print(i, code)
        startpos = i
        endpos = i + width
        break

print("First message:", endpos)
