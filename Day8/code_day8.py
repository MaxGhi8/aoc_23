#### Advent of code: day 8

def solution_part1(filename):
    # parsing
    fh = open(filename, mode = 'r')
    istruction = fh.readline().strip()
    fh.readline() # empty line
    Dict_nodes = {}
    for line in fh:
        line = line.split('=')
        line[0] = line[0].strip()
        line[1] = line[1].strip().replace('(', '').replace(')', '').split(',')
        Dict_nodes[line[0]] = (line[1][0].strip(), line[1][1].strip())
    
    # search zzz
    len_istr = len(istruction)
    start = 'AAA'
    iteration = 0
    Dict_rule = {'L': 0, 'R': 1}
    while start != 'ZZZ':
        rule = istruction[iteration % len_istr]
        start = Dict_nodes[start][Dict_rule[rule]]
        iteration += 1
    return iteration
#########################################
import numpy as np

def solution_part2(filename):
    # parsing
    fh = open(filename, mode = 'r')
    istruction = fh.readline().strip()
    fh.readline() # empty line
    Dict_nodes = {}
    for line in fh:
        line = line.split('=')
        line[0] = line[0].strip()
        line[1] = line[1].strip().replace('(', '').replace(')', '').split(',')
        Dict_nodes[line[0]] = (line[1][0].strip(), line[1][1].strip())
    
    # search zzz
    len_istr = len(istruction)
    start = list(filter(lambda x: x[-1] == 'A', Dict_nodes.keys()))
    iteration = 0
    Dict_rule = {'L': 0, 'R': 1}
    Ls = []
    while len(start) != 0:
        rule = istruction[iteration % len_istr]
        start = list(map(lambda x: Dict_nodes[x][Dict_rule[rule]], start))
        iteration += 1
        for el in start:
            if el[-1] == 'Z':
                Ls.append(iteration)
                start.remove(el)
        
    print(Ls)
    return np.lcm.reduce(Ls, dtype = object)

if __name__ == '__main__':
    print("Advent of code: day 8")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    