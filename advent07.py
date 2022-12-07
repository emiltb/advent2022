with open("inputs/input07.txt", "r") as f:
    data = f.readlines()

terminal = [s.strip() for s in data]


def parse_command(l):
    global path
    if l.startswith("cd"):
        dir = l[3:]
        if dir == "/":
            path = dir
        elif dir == "..":
            path = path.rsplit("/", 2)[0] + "/"
        else:
            path = path + dir + "/"


def parse_content(l):
    if l[0].isdigit():
        fileinfo = l.split()
        contents.append([path] + [int(fileinfo[0]), fileinfo[1]])


path = ""
contents = []

for l in terminal:
    if l[0] == "$":
        parse_command(l[2:])
    else:
        parse_content(l)


folders = {p[0] for p in contents}

folder_sizes = []
for c in folders:
    print(c)
    print([x[1] for x in contents if x[0].startswith(c)])
    print("---")
    folder_sizes.append([c, sum([x[1] for x in contents if x[0].startswith(c)])])

sum_of_folders_to_delete = sum([f[1] for f in folder_sizes if f[1] <= 100000])
sum_of_folders_to_delete
