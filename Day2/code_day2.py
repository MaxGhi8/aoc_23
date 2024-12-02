import re

#### Advent of code: day 2
Dict = {'red': 12, 'green': 13, 'blue': 14}

def sum_digits(filename):
    fh = open(filename, mode = 'r')
    total_sum = 0
    for line in fh:
        flag = True
        line = line.strip().split(":")
        line = [line[0]] + line[1].split(";")
        for n in range(len(line)):
            if n == 0:
                id_game = int(line[n].strip().split(" ")[-1])
            else:
                tmp = line[n]
                tmp = tmp.strip().split(",")
                for m in range(len(tmp)):
                    ball = tmp[m].strip().split(" ")
                    if Dict[ball[1]] <  int(ball[0]):
                        flag = False
        if flag:
            total_sum += id_game
    return total_sum

def sum_digits2_0(filename):
    fh = open(filename, mode = 'r')
    total_sum = 0
    for line in fh:
        line = line.strip().split(":")
        line = line[1].split(";")
        Max_line = {'red': 0, 'green': 0, 'blue': 0}
        for n in range(len(line)):
            tmp = line[n]
            tmp = tmp.strip().split(",")
            for m in range(len(tmp)):
                ball = tmp[m].strip().split(" ")
                Max_line[ball[1]] = max(Max_line[ball[1]], int(ball[0]))
                
        total_sum += Max_line['red']*Max_line['green']*Max_line['blue']
    return total_sum

if __name__ == '__main__':
    print("Advent of code: day 2")
    
    filename = "input.txt"
    print(sum_digits(filename))
    
    print(sum_digits2_0(filename))
    