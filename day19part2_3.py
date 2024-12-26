
import re

import itertools

import sys
from functools import cache


with open('input/day19.txt') as f: s = f.read()
lines = s.split('\n\n')

valid = lines[0].split(", ")

possibilities = lines[1].split("\n")

max_len = max(len(x) for x in valid)

cached = {}

@cache
def isValid(pos, leaf_nodes):

    if pos in cached:
        return cached[pos]

    if not pos:
        return 1

    leaf_nodes = 0

    for v in valid:
        if v == pos[:len(v)]: #design.startswith(towel)
            leaf_nodes += isValid(pos[len(v):], leaf_nodes)

    cached[pos] = leaf_nodes

    return leaf_nodes



for i in valid:
    if len(i) == 1:
        cached[i] = 1

by_len = {}
for i in range(1, max_len+1): by_len[i] = []

for i in valid:
    by_len[len(i)].append(i)


for i in range(2, max_len+1):
    for len_i_valid in by_len[i]:
        cached[len_i_valid] = isValid(len_i_valid, 0) + 1


# cached['br'] = 2



total = 0
for poss in possibilities:
    result = isValid(poss, 0)
    print(f"{result}")
    total += result

print(total)
print(valid)
print(possibilities)

# 14676729835840917670 is too high
