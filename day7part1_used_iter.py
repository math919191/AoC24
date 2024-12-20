
import itertools

from itertools import product

with open('input/day7_test.txt') as f: s = f.read()
lines = s.split('\n')

targets_and_equations = []

for line in lines:
    target, nums = line.split(": ")
    nums = nums.split(" ")
    nums = [int(num) for num in nums]
    targets_and_equations.append((int(target),nums))

# gracias google AI for this answer
def number_to_binary(number, length):
    binary_string = bin(number)[2:]  # Convert to binary and remove '0b' prefix
    return binary_string.zfill(length)

answer = 0
for target, nums in targets_and_equations:
    n = len(nums)
    options = product([1, 0], repeat=len(nums) - 1)
    for opt in options:

        total = nums[0]
        string2 = []
        for i in range(1, len(nums)):
            op = opt[i-1]
            if op:
                total = total * nums[i]
                string2.append(f"* {total}")
            else:
                total = total + nums[i]
                string2.append(f"+ {total}")
        print(string2)
        if total == target:
            print("HOORAY!")
            print(target)
            answer += target
            break

print(f"Answer {answer}")

# 292046597038 is too LOW...
# 292032923680 is also TOO LOW...

# 8401132154762