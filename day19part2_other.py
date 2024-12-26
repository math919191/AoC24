import sys
from functools import cache

@cache
def possible(design, towels):
    if not design:
        return 1
    return sum(possible(design[len(towel):], towels)
               for towel in towels if design.startswith(towel))

with open('input/day19.txt') as f: s = f.read()
lines = s.split('\n\n')

valid = lines[0].split(", ")

possibilities = lines[1].split("\n")


towels = tuple(lines[0].rstrip().split(', '))
designs = lines[1].split()
pos = [possible(design, towels) for design in designs]
for p in pos: print(p)
print(sum(map(bool, pos)))
print(sum(pos))

# Note: this is someone else's code (https://github.com/Praful/advent_of_code/blob/main/2024/src/day19.py)
# I tried it on my own for awhile before using theirs. I understand how it works and learned a lot from their solution

# ie
# @cache
# sum
# split lines for list comprehension