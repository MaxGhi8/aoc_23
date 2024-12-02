import numpy as np

#### Advent of code: day 2
Dict = {'red': 12, 'green': 13, 'blue': 14}

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    solution = 1
    
    # Parsing
    Ls = []
    for line in fh:
        tmp1 = line.split()
        tmp2 = []
        for el in tmp1:
            try:
                tmp2 += [int(el.strip())]
            except:
                continue
        Ls.append(tmp2)
            
    # solve inequalities
    for t, d in zip(Ls[0], Ls[1]):
        flag = 0
        if (t**2 - 4*d) > 0:
            min_time = (t - np.sqrt(t**2 - 4*d))/2
            max_time = (t + np.sqrt(t**2 - 4*d))/2
            if np.ceil(np.ceil(min_time) - min_time) == 0:
                flag += 1
            if np.ceil(np.ceil(max_time) - max_time) == 0:
                flag += 1
            solution *= (np.floor(max_time) - np.ceil(min_time) + 1 - flag)
        
    return int(solution)
            

def solution_part2(filename):
    fh = open(filename, mode = 'r')
    solution = 1
    
    # Parsing
    Ls = []
    for line in fh:
        tmp1 = line.split()
        tmp2 = ''.join(tmp1[1:])
        Ls.append(int(tmp2))
            
    # solve inequalities
    t, d = Ls[0], Ls[1]
    flag = 0
    if (t**2 - 4*d) > 0:
        min_time = (t - np.sqrt(t**2 - 4*d))/2
        max_time = (t + np.sqrt(t**2 - 4*d))/2
        if np.ceil(np.ceil(min_time) - min_time) == 0:
            flag += 1
        if np.ceil(np.ceil(max_time) - max_time) == 0:
            flag += 1
        solution *= (np.floor(max_time) - np.ceil(min_time) + 1 - flag)
        
    return int(solution)

if __name__ == '__main__':
    print("Advent of code: day 2")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    