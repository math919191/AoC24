

with open('input/day9.txt') as f: s = f.read()
lines = s.split('\n')

nums = [int(l) for l in lines[0]]

print(nums)

all = []

for index, num in enumerate(nums):

    if index % 2 == 0:
        for i in range(num):
            all.append(index // 2)
    else:
        for i in range(num):
            all.append(".")
print(all)

new_list = []
all_copy = all[:]

for index, item in enumerate(all):
    if index >= len(all_copy):
        break

    if item == ".":
        back = "."
        while back == ".":
            back = all_copy.pop(-1)

        if index >= len(all_copy): # weird edge case thing
            all_copy.append(back)
            break
        all_copy[index] = back

total = 0
for index, item in enumerate(all_copy):
    total += (index * item)

print(f"Total: {total}")

# for i in all_copy:
#     print(i, end='')
# print("\n0099811188827773336446555566")
# print(all_copy)