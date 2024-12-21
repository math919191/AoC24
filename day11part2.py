
stones = ['125', '17'] # test input
stones = ['112', '1110', '163902', '0', '7656027', '83039', '9', '74'] # my input

stone_counts = {}

# stones = ['1']
stone_dict = {}
for stone in stones:
    if stone not in stone_dict:
        stone_dict[stone] = 1
    else:
        stone_dict[stone] += 1


# how many of each type of stone? eg
# 1: 20, 2: 3, 96: 1
# then when we split, then we can also multiply and move the piles accordingly.

for i in range(75):

    new_stones = {}
    def update_dict(stone, amount):
        if stone in new_stones:
            new_stones[stone] += amount
        else:
            new_stones[stone] = amount

    for stone in stone_dict.keys():
        amount = stone_dict[stone]
        if stone == '0':
            update_dict('1', amount)
        elif len(stone) % 2 == 0:
            left_stone = stone[:len(stone)//2]
            right_stone = stone[len(stone)//2:]
            if (int(left_stone) == 0): left_stone = '0'
            if (int(right_stone) == 0): right_stone = '0'

            update_dict(str(int(left_stone)), amount)
            update_dict(str(int(right_stone)), amount)

        else:
            new_stone = int(stone) * 2024
            update_dict(str(new_stone), amount)
    stone_dict = new_stones

total = 0
for key in stone_dict:
    print(key, ": ", stone_dict[key])
    total += int(stone_dict[key])

print("Answer:")
print(total)