
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

curr_dir_index = 0

total = 0

def get_X_spots(start, dirs):
    curr_dir_index = 0  # add one to go up
    curr = start

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

    for item in grid_dict.keys():
        if grid_dict[item] == "X":
            yield item




# if there was a previous path taken, with the same visited spot, and it DID NOT touch
#   the obstacle placed for that time through AND would NOT touch the new obstacle
#   then we can move on.

memoization = {}

# for index, row in enumerate(grid_array):
# for index2, item in enumerate(row):

# only loop over the ones that actually change it. (the X's in the path)
for i in get_X_spots(start, dirs):
    print(i)
    item = grid_dict[i]
    index = i[0]
    index2 = i[1]

    # check if non start and non #
    if item == "#" or item == "^":
        continue

    # set obstacle
    grid_dict[index, index2] = "#"
    grid_array[index][index2] = "#"

    curr_dir_index = 0
    curr = start
    looped = 0
    visited = []

    while True:
        if (curr, curr_dir_index) in visited:
            looped += 1
            print("LOOP")
            total += 1
            break

        visited.append((curr, curr_dir_index))

        curr_dir = dirs[curr_dir_index]

        if not ((curr[0] + curr_dir[0], curr[1] + curr_dir[1]) in grid_dict):
            break

        if grid_dict[(curr[0] + curr_dir[0], curr[1] + curr_dir[1])] != "#":
            curr = (curr[0] + curr_dir[0], curr[1] + curr_dir[1])
        else:
            curr_dir_index = (curr_dir_index + 1) % 4

    # unset obstacle
    grid_dict[index, index2] = "."
    grid_array[index][index2] = "."



print(f"TOTAL: {total}")

# Brute force ~ 30 minutes to run -- answer 1933


