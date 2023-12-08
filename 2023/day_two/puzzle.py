import re

key = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def get_game_cubes(sets):
    max_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    possible = True
    for pair in sets:
        pair = pair.split(' ')
        if int(pair[0]) > key[pair[1]]:
            possible = False
        if int(pair[0]) > max_cubes[pair[1]]:
            max_cubes[pair[1]] = int(pair[0])
    return possible, (max_cubes['red']*max_cubes['green']*max_cubes['blue'])


def main():
    game_sum = 0
    game_sum_two = 0
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            possible, power = get_game_cubes(re.findall('\d+ \w+', line.split(':')[1]))
            game_sum_two += power
            if possible:
                game_sum += int(re.findall('\d+', line.split(':')[0])[0])
        
    print(game_sum)
    print(game_sum_two)

if __name__ == '__main__':
    main()