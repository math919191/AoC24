
import itertools

from itertools import product
debug = True

with open('input/day7.txt') as f: s = f.read()
lines = s.split('\n')

targets_and_equations = []

for line in lines:
    target, nums = line.split(": ")
    nums = nums.split(" ")
    nums = [int(num) for num in nums]
    targets_and_equations.append((int(target),nums))


answer = 0
for target, nums in targets_and_equations:
    n = len(nums)
    options = product([1, 0, 2], repeat=len(nums) - 1)
    for opt in options:

        total = nums[0]
        string2 = []
        for i in range(1, len(nums)):
            op = opt[i-1]
            if op == 1:
                total = total * nums[i]
                string2.append(f"* {total}")
            elif op == 0:
                total = total + nums[i]
                string2.append(f"+ {total}")
            else:
                total = int(str(total) + str(nums[i]))
                string2.append(f"|| {total}")
        if debug:
            print(string2)
        if total == target:
            print("HOORAY!")
            print(target)
            answer += target
            break

print(f"Answer {answer}")



# Brute force... took a little time to run 95297119227552