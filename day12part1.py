
with open('input/day12_test.txt') as f: s = f.read()
lines = s.split('\n')

grid_array = [[l for l in line] for line in lines]

grid_dict = {}
starts = []
for index, line in enumerate(grid_array):
    for index2, l in enumerate(line):
        # set the dictionary
        grid_dict[index, index2] = l


start = (0,0)

up = (-1,0)
right = (0,1)
down = (1,0)
left = (0,-1)

dirs = [up, right, down, left]


def add(coor, coor2):
    # if coor[0] + coor2[0] < 0 or coor[1] + coor2[1] < 0:
    #     return False

    return coor[0] + coor2[0], coor[1] + coor2[1]

def calc_fence(enclosed_area):
    fencing = 0
    for item in enclosed_area:
        for dir in dirs:
            if add(item, dir) not in enclosed_area:
                fencing += 1
    return fencing

answer = 0
while len(grid_dict):
    item = next(iter(grid_dict))
    curr_letter = grid_dict[item]

    q = [item]
    enclosed_area = [item]
    total = 1
    del grid_dict[item]
    while q:
        item = q.pop(-1)
        for dir in dirs:
            potential_coor = add(item, dir)
            if potential_coor in grid_dict and grid_dict[potential_coor] == curr_letter:
                q.append(potential_coor)
                enclosed_area.append(potential_coor)
                del grid_dict[potential_coor]

                total += 1
    print(curr_letter)
    print(total)
    print(calc_fence(enclosed_area))
    print(enclosed_area)
    print()
    answer += (total * calc_fence(enclosed_area))

print(f"Answer: {answer}")
