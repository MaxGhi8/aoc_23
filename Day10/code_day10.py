#### Advent of code: day 10
import numpy as np
def start_path(start, Ls):
    if Ls[start[0]][start[1]+ 1] in '-J7':
        current = (start[0], start[1] + 1)
        if Ls[current] == '-':
            next = 'right'
        elif Ls[current] == 'J':
            next = 'up'
        elif Ls[current] == '7':
            next = 'down'

    elif Ls[start[0] + 1][start[1]] in '|7F':
        current = (start[0] + 1, start[1])
        if Ls[current] == '|':
            next = 'up'
        elif Ls[current] == 'F':
            next = 'right'
        elif Ls[current] == '7':
            next = 'left'

    elif Ls[start[0] - 1][start[1]] in '|JL':
        current = (start[0] - 1, start[1])
        if Ls[current] == '|':
            next = 'down'
        elif Ls[current] == 'J':
            next = 'left'
        elif Ls[current] == 'L':
            next = 'right'

    elif Ls[start[0]][start[1] - 1] in '-LF':
        current = (start[0], start[1] - 1)
        if Ls[current] == '-':
            next = 'left'
        elif Ls[current] == 'F':
            next = 'down'
        elif Ls[current] == 'L':
            next = 'up'
    return current, next


def next_path(current, next, Ls):
    if next == 'right':
        current = (current[0], current[1] + 1)
        if Ls[current] == '-':
            next = 'right'
        elif Ls[current] == 'J':
            next = 'up'
        elif Ls[current] == '7':
            next = 'down'

    elif next == 'up':
        current = (current[0] - 1, current[1])
        if Ls[current] == '|':
            next = 'up'
        elif Ls[current] == 'F':
            next = 'right'
        elif Ls[current] == '7':
            next = 'left'

    elif next == 'down':
        current = (current[0] + 1, current[1])
        if Ls[current] == '|':
            next = 'down'
        elif Ls[current] == 'J':
            next = 'left'
        elif Ls[current] == 'L':
            next = 'right'

    elif next == 'left':
        current = (current[0], current[1] - 1)
        if Ls[current] == '-':
            next = 'left'
        elif Ls[current] == 'F':
            next = 'down'
        elif Ls[current] == 'L':
            next = 'up'

    return current, next

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    Ls = []
    for i, line in enumerate(fh):
        tmp = [char for char in line.strip()]
        Ls.append(tmp)
        if 'S' in tmp:
            j = tmp.index('S')
            start = (i, j)
    
    Ls = np.array(Ls)
    current, next = start_path(start, Ls)
    iteration = 1

    while current != start:
        # print(current, next, iteration)
        current, next = next_path(current, next, Ls)
        iteration += 1
        
    return iteration//2
#########################################
def solution_part2(filename):
    pass

if __name__ == '__main__':
    print("Advent of code: day 10")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    