import re


with open('input/day3.txt') as f: s = f.read()


sum = 0
regex = re.findall("mul\([0-9]+,[0-9]+\)", s)

for mul in regex:
    a,b = mul[4:-1].split(",")
    sum += (int(a)*int(b))

print(sum)
