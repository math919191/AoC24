with open('input/day2.txt') as f: s = f.read()
q = s.split('\n')

grid_array = [l.split(" ") for l in q]
grid = {}
for i in range(len(grid_array)):
    for j in range(len(grid_array[i])):
        grid[(i,j)] = int(grid_array[i][j])
        grid_array[i][j] = int(grid_array[i][j])


total = 0
for row in grid_array:

    direction = "inc" if row[0] < row[1] else "dec"
    safe = True
    for item1, item2 in zip(row[:-1], row[1:]):
        dif = item1 - item2
        if abs(dif) > 3: # any difference of greater than 3 is unsafe
            safe = False
            break

        if dif == 0: #if there is not an increase of decrease
            safe = False
            break

        if (direction == "inc" and dif > 0) or (direction == "dec" and dif < 0): # if we know we should be increasing AND we're not, break
            safe = False
            break

    if safe:
        total += 1


print(f"total: {total}")