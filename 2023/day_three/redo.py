with open('puzzle_input.txt', 'r') as file:
    lines = file.readlines()

graph = [[char for char in line.strip('\n')] for line in lines]
row_length = len(graph[0])
num = 0
total = 0
valid = False
for x in range(len(graph)):
    if valid:
        print(num)
        total+=num
    num = 0
    valid = False
    for y in range(row_length):
        if graph[x][y].isdigit():
            num = num*10+int(graph[x][y])
            for j in [-1, 0, 1]:
                for z in [-1, 0, 1]:
                    if y+z > 0 and x+j > 0 and x+j < row_length and y+z < row_length:
                        if not(graph[x+j][y+z].isdigit()) and graph[x+j][y+z] != '.':
                            valid=True
        else:
            if valid:
                print(num)
                total+=num
            num = 0
            valid = False
print(total)

