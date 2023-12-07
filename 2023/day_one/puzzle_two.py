# Solution without using regex

def check_for_word(word):
    word_nums = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    try: 
        return str(word_nums[word])
    except:
        return False
def find_num(line):
    i, j = 0, len(line)-1
    num_one, num_two = '', ''

    while num_one == '' or num_two == '':
        try:
            num_one = int(line[i])
        except:
            pass
        try: 
            num_two = int(line[j])
        except:
            pass
        
        if num_one == '':
            if check_for_word(line[i:i+3]) != False:
                num_one = check_for_word(line[i:i+3])
            if check_for_word(line[i:i+4]) != False:
                num_one = check_for_word(line[i:i+4])
            if check_for_word(line[i:i+5]) != False:
                num_one = check_for_word(line[i:i+5])
            i+=1

        if num_two == '':
            if check_for_word(line[j-3:j]) != False:
                num_two = check_for_word(line[j-3:j])
            if check_for_word(line[j-4:j]) != False:
                num_two = check_for_word(line[j-4:j])
            if check_for_word(line[j-5:j]) != False:
                num_two = check_for_word(line[j-5:j])
            j-=1

    return int(f'{num_one}{num_two}')



def main():
    running_total = 0
    with open('puzzle_input.txt', 'r') as file:
        for line in file:
            running_total += find_num(line)
    print(running_total) 
if __name__ == '__main__':
    main()