with open('input/day5.txt') as f: s = f.read()
rules, lists = s.split('\n\n')

rules = rules.split('\n')
lists = lists.split('\n')

rules = [ rule.split("|") for rule in rules]
rules = [ [int(rule[0]), int(rule[1])] for rule in rules]
lists = [list.split(",") for list in lists]

rule_dict = {}
list_of_start = [rule[0] for rule in rules]
for start in list_of_start:
    rule_dict[start] = []

for rule in rules:
    value = rule_dict[rule[0]]
    value.append(rule[1])
    rule_dict[rule[0]] = value

for index, list in enumerate(lists):
    lists[index] = [int(l) for l in list]

total = 0
for list in lists:
    good_list = True
    for i in range(len(list)-1, -1, -1):
        curr = list[i]
        if curr not in rule_dict:
            continue
        for item in rule_dict[curr]:
            if item in list[:i]:
                good_list = False
                break
        if good_list == False:
            break
    if good_list:
        print("bueno! :", list)
        print(len(list)//2, list[len(list)//2])
        total += list[len(list)//2]

print(f"total: {total}")

# current thought:
# - iterate over all the ordering rules and make it so each number is in
#       a dictionary with a set of numbers that have to come after it
#       go through a list, start at pg # -1, turn the rest of the list into a set
#       if anything in that set contains numbers that must be after, then it is no good.


# 47 | 53 indicates that 47 has to come before 53
# the bottom indicate page orderigns
# we have to determine if hte page orderings are valid

# should be 161 (middle numbers of the following)
# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13