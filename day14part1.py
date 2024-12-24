
import re

with open('input/day14_test.txt') as f: s = f.read()
# systems = s.split('\n\n')
machine_regex = re.compile(
    r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
)

matches = machine_regex.findall(s)
# width = 11
# height = 7
width = 101
height = 103
bugs = []
for match in matches:
    p1, p2, v1, v2 = int(match[0]), int(match[1]), int(match[2]), int(match[3])
    print(p1, p2, v1, v2)
    bugs.append( {"p1": p1, "p2": p2, "v1": v1, "v2": v2} )

for i in range(100):

    for bug in bugs:
        p1 = bug["p1"]
        p2 = bug["p2"]
        v1 = bug["v1"]
        v2 = bug["v2"]

        bug["p1"] = (bug["p1"] + v1) % width
        bug["p2"] = (bug["p2"] + v2) % height


    array =  [[ 0 for _ in range(width)] for _ in range(height)]
    for bug in bugs:
        # print(bug["p1"], bug["p2"])
        array[bug["p2"]][bug["p1"]] += 1
    print()

    for i in array:
        for j in i:
            p = '.' if j == 0 else j
            print(p, end='')
        print()

def get_section(bug):
    p1 = bug["p1"]
    p2 = bug["p2"]
    if p1 < width // 2 and p2 < height // 2:
        return 1
    if p1 < width // 2 and p2 > height // 2:
        return 2
    if p1 > width // 2 and p2 < height // 2:
        return 3
    if p1 > width // 2 and p2 > height // 2:
        return 4



sections = {1: 0, 2:0, 3:0, 4:0}
for bug in bugs:
    section_num = get_section(bug)
    if section_num is None: continue
    sections[section_num] += 1

total = 1
for i in range(1,5):
    print(sections[i])
    total *= sections[i]
print(total)

# 92099592 is too low
# 220971520