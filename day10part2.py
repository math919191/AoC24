
with open('input/day10.txt') as f: s = f.read()
lines = s.split('\n')

grid_array = [[l for l in line] for line in lines]

grid_dict = {}
starts = []
for index, line in enumerate(grid_array):
    for index2, l in enumerate(line):
        # set the dictionary
        grid_dict[index, index2] = int(l)

        if l == "0":
            start = (index, index2)
            starts.append(start)
            print(start)

up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)
dirs = [up, right, down, left]

TOP_HEIGHT = 9

def add(coor, coor2):
    return coor[0] + coor2[0], coor[1] + coor2[1]

full_total = 0

for start in starts:
    q = [[start]]
    total = 0
    found = []
    while q:
        curr_path = q.pop(-1)
        curr = curr_path[-1]
        for dir in dirs:
            after_step = add(curr, dir)
            if after_step not in grid_dict: continue # out of bounds
            if after_step in curr_path: continue # would loop
            # if after_step in found: continue # already found it

            if grid_dict[after_step] - grid_dict[curr] == 1:
                if grid_dict[after_step] == TOP_HEIGHT:
                    found.append(after_step)
                    total += 1
                    continue
                path_to_add = curr_path[:]
                path_to_add.append(after_step)
                q.append(path_to_add)

    print(f"Total {start}: {total}")
    full_total += total

print(f"Full total: \n{full_total}")