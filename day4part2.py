import numpy as np

with open('input/day4.txt') as f: s = f.read()
grid_array = s.split('\n')

# modify the array to make a numpy array
np_array = []
for index, row in enumerate(grid_array):
    np_array.append([l for l in row])
grid_array = np.array(np_array)

def checkX_MAS(sub_array):
    if sub_array[1, 1] != 'A':
        return False

    top_left = sub_array[0,0]
    top_right = sub_array[0,2]
    bottom_right = sub_array[2,2]
    bottom_left = sub_array[2,0]

    return ((top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")) and ((top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"))

total = 0

for x in range(1, len(grid_array)-1):
    for y in range(1, len(grid_array)-1):
        sub_array = grid_array[ x-1:x+2, y-1:y+2]
        total += checkX_MAS(sub_array)

print(total)

