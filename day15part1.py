
directions_to_coor = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (1, 0),
    '^': (-1, 0),
}

def print_dict(dict):
    width, height = max(dict)
    for i in range(height+1):
        for j in range(width+1):

            print(dict[i,j], end=' ')
        print()

def move(direction, curr_x, curr_y, grid_dict):
    original_coor = curr_x, curr_y
    moved_one = curr_x + directions_to_coor[direction][0], curr_y + directions_to_coor[direction][1]

    new_coor = original_coor
    while True:
        new_coor = new_coor[0] + directions_to_coor[direction][0], new_coor[1] + directions_to_coor[direction][1]
        if grid_dict[new_coor] == '.':
            grid_dict[original_coor] = '.'
            grid_dict[new_coor] = 'O'
            grid_dict[moved_one] = '@'
            return moved_one
        elif grid_dict[new_coor] == '#':
            return original_coor

with open('input/day15.txt') as f: s = f.read()

grid, directions = s.split('\n\n')

directions = directions.replace("\n", "")

grid_dict = {}

grid_dict = {
    (x,y): item
    for x, line in enumerate(grid.split('\n'))
    for y, item in enumerate(line)
}


curr_coor = ()
for i in grid_dict:
    if grid_dict[i] == '@':
        curr_coor = i
        break

for dir in directions:
    curr_coor = move(dir, curr_coor[0], curr_coor[1], grid_dict)
    # print_dict(grid_dict)

print_dict(grid_dict)

print(sum(x * 100 + y for x, y in grid_dict if grid_dict[x,y] == 'O'))