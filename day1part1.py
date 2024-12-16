
with open('input/day1.txt') as f: s = f.read()

q = s.split('\n')
list1 = []
list2 = []
for i in q:
    a,b = i.strip().split("   ")
    list1.append(int(a))
    list2.append(int(b))

list1 = sorted(list1)
list2 = sorted(list2)

sum = 0
for a,b in zip(list1, list2):
    sum += (abs(a-b))

print(sum)