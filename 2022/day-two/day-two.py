def shape_points(shape):
    if 'X' in shape or 'A' in shape:
        return 1
    elif 'Y' in shape or 'B' in shape:
        return 2
    else:
        return 3

def tie(line):
    if line[0] == 'C' and line[2] == 'Z':
        return 3
    elif line[0] == 'A' and line[2] == 'X':
        return 3
    elif line[0] == 'B' and line[2] == 'Y':
        return 3

    return 0

def winner(line):
    if line[0] == line[2]:
        return 3
    elif line[2] == 'X' and line[0] == 'C':
        return 6
    elif line[2] == 'Y' and line[0] == 'A':
        return 6
    elif line[2] == 'Z' and line[0] == 'B':
        return 6

    return 0

def need_to_lose(line):
    if 'A' in line:
        return shape_points('Z')
    elif 'B' in line:
        return shape_points('X')
    else:
        return shape_points('Y')

def need_to_win(line):
    if 'A' in line:
        return shape_points('Y')
    elif 'B' in line:
        return shape_points('Z')
    else:
        return shape_points('X')

def part_two(file):
    total_score = 0
    for line in file: 
        if 'X' in line:
            total_score += need_to_lose(line)
        elif 'Y' in line:
            total_score += shape_points(line[0])
            total_score += 3
        else:
            total_score += need_to_win(line)
            total_score += 6
    print(total_score)

def part_one(file):
    total_score = 0
    for line in file: 
       total_score += shape_points(line[2])
       total_score += tie(line)
       total_score += winner(line)
    print(total_score)
    
if __name__ == '__main__':

    f = open('input.txt', 'r')
    part_one(f)
    f.close()

    f = open('input.txt', 'r')
    part_two(f)
    f.close()
