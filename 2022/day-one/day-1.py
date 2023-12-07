if __name__ == '__main__':
    f = open('input.txt', 'r')
    
    calorie_ctr = 0
    
    calorie_totals = []
    
    for line in f:
        if line != '\n':
            calorie_ctr += int(line.strip())
        else:
            calorie_totals.append(calorie_ctr)
            calorie_ctr = 0
    
    sorted_cals = sum(sorted(calorie_totals)[-3:])
    print(sorted_cals)
