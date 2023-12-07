def read_nums(line):
    i, j = 0, len(line)
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

    return int(f"{num_one}{num_two}")

def main():
    running_total = 0
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            running_total += read_nums(line)
    print(running_total)
    
if __name__ == '__main__':
    main()