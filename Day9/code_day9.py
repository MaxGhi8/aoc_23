#### Advent of code: day 9

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    solution = 0
    for line in fh:
        line = list(map(lambda x: int(x), line.strip().split())) + [0]
        while list(filter(lambda x: x == 0, line[:-1])) != line[:-1]:
            line = list(map(lambda x, y: x-y, line[1:-1], line[:-2] )) + [line[-1] + line[-2]]
        solution += line[-1]
    return solution

#########################################
from functools import reduce

def solution_part2(filename):
    fh = open(filename, mode = 'r')
    solution = 0
    for line in fh:
        tmp = []
        line = list(map(lambda x: int(x), line.strip().split()))
        while list(filter(lambda x: x == 0, line)) != line:
            tmp.append(line[0])
            line = list(map(lambda x, y: x-y, line[1:], line[:-1] ))
        tmp.reverse()
        solution += reduce(lambda x, acc: acc - x, tmp, 0)
    return solution

if __name__ == '__main__':
    print("Advent of code: day 9")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    