import numpy as np

with open('input/day4.txt') as f: s = f.read()
grid_array = s.split('\n')

print(grid_array)

def countXMAS(str):
    return str.count("XMAS") + str.count("SAMX")

total = 0

# count the rows
for row in grid_array:
    total += countXMAS(row)

# count the cols
for col in range(len(grid_array)): # the "x" coordinate -- the column we are looking at
    str = [grid_array[row][col] for row in range(len(grid_array[0]))]
    total += countXMAS(''.join(str))


# modify the array to make a numpy array
np_array = []
for index, row in enumerate(grid_array):
    np_array.append([l for l in row])

# left to right diagonals top left
np_array = np.array(np_array)
for i in range(0, len(np_array)+1):
    subarray = np_array[:i, :i]
    diagonal_flipped = np.fliplr(subarray).diagonal()
    total += countXMAS(''.join(diagonal_flipped))

# left to right diagonals bottom right
for i in range(len(np_array), 0, -1):
    subarray = np_array[i:, i:]
    diagonal_flipped = np.fliplr(subarray).diagonal()
    total += countXMAS(''.join(diagonal_flipped))

# top left to right diagonals (bottom left)
n = len(np_array)
for i in range(len(np_array)+1):
    subarray = np_array[n-i:, :i] # 0, 10, 1 9
    total += countXMAS(''.join(subarray.diagonal()))

# top left to right diagonals (top right)
n = len(np_array)
for i in range(len(np_array)):
    subarray = np_array[:i, n-i:] # 0, 10, 1 9
    total += countXMAS(''.join(subarray.diagonal()))

print(total)
