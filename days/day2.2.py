horizontal_position = 0
depth = 0
aim = 0
with open('../inputs/input2') as f:
    navigation_instructions = f.readlines()

for i in navigation_instructions:
    if 'forward' in i:
        number = i[-2]
        horizontal_position += int(number)
        if aim != 0:
            depth += int(number) * aim
    if 'down' in i:
        number = i[-2]
        aim += int(number)
    if 'up' in i:
        number = i[-2]
        aim -= int(number)

final_result = horizontal_position * depth
print(final_result)
