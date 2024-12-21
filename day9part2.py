with open('input/day9.txt') as f: s = f.read()
lines = s.split('\n')

sizes_and_spaces = [int(l) for l in lines[0]]
sizes_and_spaces_orig = sizes_and_spaces[:]

all = []

for index, num in enumerate(sizes_and_spaces):
    if index % 2 == 0:
        for i in range(num):
            all.append(index // 2)
    else:
        for i in range(num):
            all.append(".")

print(all)

new_list = []
all_copy = all[:]
reversed_sizes_and_spaces = sizes_and_spaces[::-1]
reversed(reversed_sizes_and_spaces)

# going in backwards order, try to move the given item to an available open space
for index, needed_space in enumerate(reversed_sizes_and_spaces[::2]):
    print(index, needed_space)
    # go over in forwards order to try to find an open space (::2 indicates looking at every other)
    open_spaces = sizes_and_spaces[1::2]
    for index2, open_space in enumerate(open_spaces):

        if len(sizes_and_spaces) - index*2 < index2*2:
            continue

        if open_space >= needed_space:
            # set it to the new size
            sizes_and_spaces[index2*2 + 1] = open_space - needed_space
            # update the other new size
            if (index == 0):
                pass
            else:
                sizes_and_spaces[-(index)*2] += needed_space

            # update the all_spaces accordingly for later scoring
            id = (len(sizes_and_spaces) - index*2) // 2

            # Remove the moved number from original position
            start_index_of_moved_disk = all_copy.index(id)
            for i in range(needed_space):
                all_copy[start_index_of_moved_disk + i] = '.'

            # mark the position for future scoring
            start_index_of_open_space = all_copy.index('.', sum(sizes_and_spaces_orig[:index2*2]))
            for i in range(needed_space):
                all_copy[start_index_of_open_space + i] = id
            break

total = 0
for index, item in enumerate(all_copy):
    if item != ".":
        total += (index * item)

print(f"Total: {total}")
