
with open('input/day6.txt') as f: s = f.read()
lines = s.split('\n')

grid_array = [ [ l for l in line] for line in lines ]

grid_dict = {}
start = ()
for index, line in enumerate(grid_array):
    for index2, l in enumerate(line):
        # set the dictionary
        grid_dict[index, index2] = l

        if l == "^":
            start = (index, index2)

curr_x, curr_y = start
curr = start

up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)


dirs = [up, right, down, left]

curr_dir_index = 0 # add one to go up


while True:
    grid_dict[curr] = "X"
    grid_array[curr[0]][curr[1]] = "X"
    curr_dir = dirs[curr_dir_index]
    if not ((curr[0] + curr_dir[0], curr[1] + curr_dir[1]) in grid_dict):
        break

    if grid_dict[(curr[0] + curr_dir[0], curr[1] + curr_dir[1])] != "#":
        # move forward
        curr = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])
    else:
        curr_dir_index = (curr_dir_index + 1) % 4


total = 0
for item in grid_dict.keys():
    if grid_dict[item] == "X":
        total += 1

print(total)

for row in grid_array:
    print(row)

