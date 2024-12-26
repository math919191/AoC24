
directions_to_coor = {
    '<': (0, -1),
    '>': (0, 1),
    'v': (1, 0),
    '^': (-1, 0),
}

def print_dict(dict):
    width, height = max(dict)
    for i in range(width+1):
        for j in range(height+1):
            print(dict[i,j], end=' ')
        print()
    print()

# this does all the boxy work.
    # given a box, it checks to see if there are additional boxes to moved based off of that.
    # it does this recursively
    # it returns a list of all the affected boxes, or if it hits something, it returns "bumped"

def check_for_more_affected_boxes(dir, affected_box, grid_dict, affected_boxes_to_return):

    if dir == "<" or dir == ">":
        return affected_boxes_to_return

    # one forward in curr direction of the box on the left side
    places_to_check_l = affected_box[0][0] + directions_to_coor[dir][0], affected_box[0][1] + directions_to_coor[dir][1]
    one_left_of_left_check = places_to_check_l[0] + directions_to_coor["<"][0], places_to_check_l[1] + directions_to_coor["<"][1]

    places_to_check_r = affected_box[1][0] + directions_to_coor[dir][0], affected_box[1][1] + directions_to_coor[dir][1]
    one_right_of_right_check = places_to_check_r[0] + directions_to_coor[">"][0], places_to_check_r[1] + directions_to_coor[">"][1]

    if grid_dict[places_to_check_l] == "#" or grid_dict[places_to_check_r] == "#":
        affected_boxes_to_return = "bumped"
        return affected_boxes_to_return

    if grid_dict[places_to_check_r] == "[":
        affected_boxes_to_return.append(places_to_check_r)
        affected_boxes_to_return.append(one_right_of_right_check)
        affected_boxes_to_return = check_for_more_affected_boxes(dir, (places_to_check_r, one_right_of_right_check), grid_dict, affected_boxes_to_return)
        if affected_boxes_to_return == "bumped":
            return affected_boxes_to_return

    if grid_dict[places_to_check_l] == "]":
        affected_boxes_to_return.append(places_to_check_l)
        affected_boxes_to_return.append(one_left_of_left_check)
        affected_boxes_to_return = check_for_more_affected_boxes(dir, (one_left_of_left_check, places_to_check_l), grid_dict, affected_boxes_to_return)

        if affected_boxes_to_return == "bumped":
            return affected_boxes_to_return

    if grid_dict[places_to_check_r] == "]" or grid_dict[places_to_check_l] == "[":
        affected_boxes_to_return.append(places_to_check_l)
        affected_boxes_to_return.append(places_to_check_r)
        affected_boxes_to_return = check_for_more_affected_boxes(dir, (places_to_check_l, places_to_check_r), grid_dict, affected_boxes_to_return)

        if affected_boxes_to_return == "bumped":
            return affected_boxes_to_return

    return affected_boxes_to_return

# function moves the robot, and the boxes around appropriately
def move(direction, curr_x, curr_y, grid_dict):
    original_coor = curr_x, curr_y
    moved_one = curr_x + directions_to_coor[direction][0], curr_y + directions_to_coor[direction][1]
    new_coor = original_coor

    affected_boxes = []

    while True:
        new_coor = new_coor[0] + directions_to_coor[direction][0], new_coor[1] + directions_to_coor[direction][1]
        if grid_dict[new_coor] == '.':

            # if no boxes were affected
            if not affected_boxes:
                grid_dict[original_coor] = '.'
                grid_dict[new_coor] = 'O'
                grid_dict[moved_one] = '@'

            else:

                box_types = [grid_dict[coor] for coor in affected_boxes]

                # reset everything
                for coor in affected_boxes: grid_dict[coor] = '.'

                # mark the new spots
                for index, box in enumerate(affected_boxes):
                    new_box_coor = box[0] + directions_to_coor[direction][0], box[1] + directions_to_coor[direction][1]
                    grid_dict[new_box_coor] = box_types[index]

                # move the robot
                grid_dict[moved_one] = '@'
                grid_dict[original_coor] = '.'

            # return the new coordinate
            return moved_one

        elif grid_dict[new_coor] == '#':
            return original_coor

        # if we hit a box, we will call another function to handle some of it for us.
        elif grid_dict[new_coor] == "[" or grid_dict[new_coor] == "]":
            if grid_dict[new_coor] == "[":
                affected_boxes.append(new_coor)
                affected_boxes.append( (new_coor[0], new_coor[1]+1) )
                more_boxes = check_for_more_affected_boxes(dir, (new_coor, (new_coor[0], new_coor[1]+1)), grid_dict,
                                              [])
                # check for more affected boxes checks to see if we are running into a #, returns "bumped" if so
                if more_boxes == "bumped":
                    return original_coor

                for box in more_boxes: affected_boxes.append(box)

            elif grid_dict[new_coor] == "]":
                affected_boxes.append(new_coor)
                affected_boxes.append( (new_coor[0], new_coor[1] - 1) )
                more_boxes = check_for_more_affected_boxes(dir, ((new_coor[0], new_coor[1]-1), new_coor), grid_dict,
                                              [])
                # check for more affected boxes checks to see if we are running into a #, returns "bumped" if so
                if more_boxes == "bumped":
                    return original_coor

                for box in more_boxes: affected_boxes.append(box)

with open('input/day15.txt') as f: s = f.read()

grid, directions = s.split('\n\n')

directions = directions.replace("\n", "")

grid = grid.replace("#", "##")
grid = grid.replace(".", "..")
grid = grid.replace("O", "[]")
grid = grid.replace("@", "@.")

grid_dict = {}

grid_dict = {
    (x,y): item
    for x, line in enumerate(grid.split('\n'))
    for y, item in enumerate(line)
}

print_dict(grid_dict)

curr_coor = ()
for i in grid_dict:
    if grid_dict[i] == '@':
        curr_coor = i
        break

for index, dir in enumerate(directions):
    curr_coor = move(dir, curr_coor[0], curr_coor[1], grid_dict)

print_dict(grid_dict)

print(sum(x * 100 + y for x, y in grid_dict if grid_dict[x,y] == '['))