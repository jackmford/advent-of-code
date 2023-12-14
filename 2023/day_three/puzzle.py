import regex as re
import copy
from pprint import pprint

def main():
    with open('puzzle_input.txt', 'r') as file:
        lines = file.readlines()

    original_lines = copy.copy(lines)
    for l in range(len(lines)):
        line = lines[l].strip()
        for i, char in enumerate(line):
            if re.search('[^\.^\ \d]', char) is not None:
                if l > 0 and l < len(lines)-1:
                    top_line = lines[l-1]
                    mid_line = lines[l]
                    bot_line = lines[l+1]

                    lines[l-1] = str(top_line[:i]+' '+top_line[i+1:])
                    lines[l] = str(mid_line[:i]+' '+mid_line[i+1:])
                    lines[l+1] = str(bot_line[:i]+' '+bot_line[i+1:])
    
    subtract = 0
    for line in lines:
        nums = re.findall('\.\d+\.', line, overlapped=True)
        begin_nums = re.findall('^\d+\.', line)
        end_nums = re.findall('\.\d+$', line)
        if end_nums:
            subtract+=int(end_nums[0].strip('.'))
        if begin_nums:
            subtract+=int(begin_nums[0].strip('.'))

        if nums:
            for num in nums:
                subtract += int(num.strip('.'))
    
    total = 0
    for line in original_lines:
        nums = re.findall('\d+', line)
        if nums:
            for num in nums:
                total += int(num)

    print('Total: ' + str(total-subtract))
    

if __name__ == '__main__':
    main()