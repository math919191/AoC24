
import re

import itertools

with open('input/day19.txt') as f: s = f.read()
lines = s.split('\n\n')

valid = lines[0].split(", ")

possibilities = lines[1].split("\n")

max_len = max(len(x) for x in possibilities)

cached = {}

for v in valid:
    cached[v] = True

def isValid(pos):
    if pos in cached:
        # print(pos, cached[pos])
        return cached[pos]

    cached_keys = list(cached.keys())
    for v in cached_keys:
        # print(f"on {v}")
        if v in cached and cached[v] and v == pos[:len(v)]:
            if isValid(pos[len(v):]):
                # print(pos[len(v):])
                cached[pos[len(v):]] = True
                return True

    cached[pos] = False
    return False

total = 0
for poss in possibilities:
    print(poss)
    print()
    result = isValid(poss)

    total += result

print(total)
print(valid)
print(possibilities)

