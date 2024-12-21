
# with open('input/day11_test.txt') as f: s = f.read()
# stones = s.split(' ')

stones = ['125', '17']
stones = ['112', '1110', '163902', '0', '7656027', '83039', '9', '74']

for i in range(25):
    print(i)
    new_stones = []

    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            left_stone = stone[:len(stone)//2]
            right_stone = stone[len(stone)//2:]
            if (int(left_stone) == 0): left_stone = '0'
            if (int(right_stone) == 0): right_stone = '0'

            new_stones.append(str(int(left_stone)))
            new_stones.append(str(int(right_stone)))
        else:
            new_stone = int(stone) * 2024
            new_stones.append(str(new_stone))
    stones = new_stones
    # print(stones)

print(len(stones))