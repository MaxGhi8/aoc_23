#### Advent of code: day 3

import re

def solution_part1(filename):
    board = list( open(filename, mode = 'r') )
    chars = {(r, c): [] for r in range(len(board)) for c in range(len(board[0].strip()))
                        if board[r][c] not in '0123456789.'}

    for r, row in enumerate(board):
        for n in re.finditer('\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end()+1)}

            for o in edge & chars.keys():
                chars[o].append( int(n.group()) )

    return sum(sum(p) for p in chars.values())
#########################################
import math 
def solution_part2(filename):
    board = list( open(filename, mode = 'r') )
    chars = {(r, c): [] for r in range(len(board)) for c in range(len(board[0].strip()))
                        if board[r][c] not in '0123456789.'}

    for r, row in enumerate(board):
        for n in re.finditer('\d+', row):
            edge = {(r, c) for r in (r-1, r, r+1)
                        for c in range(n.start()-1, n.end()+1)}

            for o in edge & chars.keys():
                chars[o].append( int(n.group()) )

    return sum(math.prod(p) for p in chars.values() if len(p)==2)

if __name__ == '__main__':
    print("Advent of code: day 3")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    