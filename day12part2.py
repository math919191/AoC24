
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

dia_up_right = (1,1)
dia_up_left = (1,-1)
dia_down_right = (-1,1)
dia_down_left = (-1,-1)

diagonals = [dia_up_right, dia_up_left, dia_down_right, dia_down_left]
all_dirs = dirs[:] + diagonals

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


def is_surorunded(item, enclosed_area):
    for dir in all_dirs:
        if add(item, dir) not in enclosed_area:
            return False
    return True

def determine_valid_dir_edge(item, edges):
    valid_dirs = []
    for dir in dirs:
        if add(item, dir) in edges:
            valid_dirs.append(dir)
    return valid_dirs

def calc_num_sides(enclosed_area):
    edges = []
    sides = 0
    for edge in enclosed_area:
        if not is_surorunded(edge, enclosed_area):
            edges.append(edge)

    valid_edges_from_point = {}
    for edge in edges:
        valid_edges_from_point[edge] = determine_valid_dir_edge(edge, edges)
        print(edge, determine_valid_dir_edge(edge, edges))

    change_direction = 0
    curr_point = edges[0]
    start = edges[0]
    curr_direction = valid_edges_from_point[curr_point][0]
    while True:

        valid_edges_from_point[curr_point].remove(curr_direction)

        new_point = add(curr_point, curr_direction)


        if curr_point not in valid_edges_from_point:
            print("AHHH")




        if curr_point == start:
            break

    start_edge = edges[0]



    return total

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
    print(calc_num_sides(enclosed_area))
    print()
    answer += (total * calc_fence(enclosed_area))

print(f"Answer: {answer}")
