
from itertools import combinations


with open('input/day8.txt') as f: s = f.read()
lines = s.split('\n')

grid_array = [ [ l for l in line] for line in lines ]

freq_to_coor = {}

broadcasts = []

for index1, row in enumerate(grid_array):
    for index2, l in enumerate(row):
        if l == '.': continue
        if l not in freq_to_coor:
            freq_to_coor[l] = [(index1, index2)]
        else:
            freq_to_coor[l].append((index1, index2))
        broadcasts.append((index1, index2))

def in_range(coord1, n):
    return coord1[0] < n and coord1[1] < n and coord1[0] >= 0 and coord1[1] >= 0


n = len(grid_array)
total = 0

all_freq = []
for key in freq_to_coor.keys():
    coors = freq_to_coor[key]

    for combo in list(combinations(coors, 2)):
        a_coor,b_coor = combo[0], combo[1]

        x_dif = a_coor[0] - b_coor[0]
        y_dif = a_coor[1] - b_coor[1]

        a_coor = (a_coor[0]+x_dif, a_coor[1]+y_dif)
        b_coor = (b_coor[0]-x_dif, b_coor[1]-y_dif)

        if in_range(a_coor, n):
            all_freq.append(a_coor)
            grid_array[a_coor[0]][a_coor[1]] = "#"

        if in_range(b_coor, n):
            all_freq.append(b_coor)
            grid_array[b_coor[0]][b_coor[1]] = "#"


for row in grid_array:
    print()
    for l in row:
        print(l, end="")

print("\n\nAnswer:", len(set(all_freq)))

# 252 is low and wrong

# 271 is too high