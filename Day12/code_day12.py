#### Advent of code: day 12
from functools import lru_cache


def check_arrangement(string, Ls):
    As = list(filter(lambda x: x != '', string.split('.')))
    As = list(map(lambda x: len(x), As))
    return As == Ls

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    total_sum = 0
    for line in fh:
        line = line.strip().split(' ')
        string = line[0]
        tmp = [string]
        Ls = [int(i) for i in line[1].split(',')]
        for i in range(string.count('?')):
            tmp = list(map(lambda x: x.replace('?', '.', 1), tmp)) + list(map(lambda x: x.replace('?', '#', 1), tmp))
        
        total_sum += sum(list(map(lambda x: int(check_arrangement(x, Ls)), tmp)))
    
    return total_sum


#########################################
@lru_cache(maxsize = None)
def check_valid(string, Ls):
    if string[0] == '?':
        return True
    string = string.split('?')[0]
    
    As = tuple([x for x in string.split('.') if x != ''])
    As = tuple([len(x) for x in As])
    if len(As) == 0:
        return True
    if len(As) > len(Ls):
        return False
    if string[-1] == '#':
        if As[:-1] == Ls[:len(As)-1]:
            return As[-1] <= Ls[len(As)-1]
    return As == Ls[:len(As)]

def solution_part2(filename):
    fh = open(filename, mode = 'r')
    total_sum = 0
    for line in fh:
        line = line.strip().split(' ')
        string = line[0]
        tmp = tuple([string + 4*('?'+string)])
        Ls = tuple([int(i) for i in line[1].split(',')]*5)
        for _ in range(tmp[0].count('?')):
            tmp = tuple([x.replace('?', '.', 1) for x in tmp] + [x.replace('?', '#', 1) for x in tmp])
            tmp = tuple([x for x in tmp if check_valid(x, Ls)])

        total_sum += len(tmp)
    
    return total_sum

if __name__ == '__main__':
    print("Advent of code: day 12")
    
    # filename = "input_part1.txt"
    # print(solution_part1(filename))

    # print(check_valid('???.###',  [1,1,3]))
    # print(check_valid('#??.###',  [1,1,3]))
    # print(check_valid('.??.###',  [1,1,3]))
    # print(check_valid('.#?.###',  [1,1,3]))
    # print(check_valid('..#.###',  [1,1,3]))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    