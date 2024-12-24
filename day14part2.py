
import re

import sys

orig_stdout = sys.stdout
f = open('out_day_14.txt', 'w')
sys.stdout = f

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

curr_section_num = 500
for i2 in range(10000):

    for bug in bugs:
        p1 = bug["p1"]
        p2 = bug["p2"]
        v1 = bug["v1"]
        v2 = bug["v2"]

        bug["p1"] = (bug["p1"] + v1) % width
        bug["p2"] = (bug["p2"] + v2) % height



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

    print()
    print(i2)
    array =  [[ 0 for _ in range(width)] for _ in range(height)]
    for bug in bugs:
        array[bug["p2"]][bug["p1"]] += 1

    to_print = ""
    for i in array:
        for j in i:
            p = '.' if j == 0 else 'X'
            to_print += p
        to_print += '\n'

    if to_print.__contains__("XXXXX"):
        print(to_print)
    else:
        print("nope...")

sys.stdout = orig_stdout
f.close()

# 6355 is the answer!