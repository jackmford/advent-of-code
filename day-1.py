f = open('input.txt', 'r')

position = 0
calories = 0

position_ctr = 1
calorie_ctr = 0

for line in f:
    if line != '\n':
        calorie_ctr += int(line.strip())
    else:
        if calorie_ctr > calories:
            calories = calorie_ctr
            position = position_ctr
        position_ctr += 1
        calorie_ctr = 0

print(position)
print(calories)
