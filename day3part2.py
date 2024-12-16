import re
with open('input/day3.txt') as f: s = f.read()

sum = 0

while s:
    print(len(s))
    first_donot_index = s.find("don't()")

    curr_s = s[:first_donot_index]
    regex = re.findall("mul\([0-9]+,[0-9]+\)", curr_s)

    for mul in regex:
        a,b = mul[4:-1].split(",")
        sum += (int(a)*int(b))

    s = s[first_donot_index:]
    first_do_index = s.find("do()")
    s = s[first_do_index:]

    if first_donot_index == -1:
        break

# 72948684 is the answer
print(sum)
