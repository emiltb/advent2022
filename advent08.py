import numpy as np

with open('inputs/input08_example.txt','r') as f:
    raw_data = f.readlines()

data = np.array([[c for c in s.strip()] for s in raw_data])
data
len_y,len_x = data.shape

n_visible = 0
for (x,y), h in np.ndenumerate(data):
    if ((x==0) or (y==0) or (x==len_x-2) or (y==len_y-1)):
        # We are at an edge
        n_visible += 1
    else:
        print("Checker:", x, y)
        check_columns = np.all(np.all(data[x,y] > data[:x,y]) and np.all((data[x,y] > data[(x+1):,y])))
        check_rows = np.all(np.all(data[x,y] > data[x,:y]) and np.all((data[x,y] > data[x,(y+1):])))
        if (check_columns and check_rows):
            n_visible += 1

print(n_visible)

all(data[1,1] > data[:1,1] and data[1,1] > data[2:,1])