def read_nums(line):
    i, j = 0, len(line)-1
    num_one, num_two = '', ''

    while i <= j:
        if num_one != '' and num_two != '':
            break
        try: 
            num_one = int(line[i])
        except:
            i = i+1
        try: 
            num_two = int(line[j])
        except:
            j = j-1

    if num_one == '' and num_two == '':
        return 0

    return int(f"{num_one}{num_two}")

def main():
    word_nums = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9n',
    }
    running_total_one = 0
    running_total_two = 0
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            running_total_one += read_nums(line)
            for k, v in word_nums.items():
                line = line.replace(k, v)
            running_total_two +=  read_nums(line)

    print(running_total_one)
    print(running_total_two)
    
if __name__ == '__main__':
    main()