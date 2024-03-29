from collections import defaultdict
with open('puzzle_input.txt', 'r') as file:
    lines = file.readlines()

graph = [[char for char in line.strip('\n')] for line in lines]
row_length = len(graph[0])
num = 0
total = 0
total2 = 0
valid = False
gear = False
gears = defaultdict(list)
for x in range(len(graph)):
    if valid:
        total+=num
    if gear:
        gears[(gearx, geary)].append(num)
    num = 0
    valid = False
    gear = False
    for y in range(row_length):
        if graph[x][y].isdigit():
            num = num*10+int(graph[x][y])
            for j in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if y+z > 0 and x+j > 0 and x+j < row_length and y+z < row_length:
                        if not(graph[x+j][y+z].isdigit()) and graph[x+j][y+z] != '.':
                            valid=True
                            if graph[x+j][y+z] == '*':
                                gear = True
                                gearx = x+j
                                geary = y+z
        else:
            if valid:
                total+=num
            if gear:
                gears[(gearx, geary)].append(num)
            num = 0
            valid = False
            gear = False
for k, v in gears.items():
    if len(v) == 2:
        total2 += gears[k][0]*gears[k][1]
print(total)
print(total2)

