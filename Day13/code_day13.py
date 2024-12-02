#### Advent of code: day 13
import torch

def convert(string):
    Ls = []
    for char in string:
        if char == '.':
            Ls.append(0)
        else:
            Ls.append(1)
    return Ls

def count_sym(Tensor):
    X, Y = Tensor.size()
    res_x = []
    res_y = []
    # simmetria rispetto riga orizzontale
    for x in range(1, X):
        row = min(x, X-x)
        if x == row:
            if torch.equal(Tensor[:x, :], Tensor[x : x+row, :].flip(0)):
                
                res_x.append(x)
        else:
            if torch.equal(Tensor[x-row : x, :], Tensor[x:, :].flip(0)):
                
                res_x.append(x)
    for y in range(1, Y):
        col = min(y, Y-y)
        if y == col:
            if torch.equal(Tensor[:, :y], Tensor[:, y : y+col].flip(1)):
                res_y.append(y)
        else:
            if torch.equal(Tensor[:, y-col : y], Tensor[:, y:].flip(1)):
                res_y.append(y)

    return sum(res_y) + 100*sum(res_x)

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    tmp = []
    sol = 0
    for line in fh:
        if len(line.strip()) == 0:
            sol += count_sym(torch.tensor(tmp))
            tmp = []
        else:
            tmp.append(convert(line.strip()))
    # the last group
    sol += count_sym(torch.tensor(tmp))
    
    return sol
#########################################
def count_sym_part2(Tensor):
    X, Y = Tensor.size()
    res_x = []
    res_y = []
    flag = 0
    # simmetria rispetto riga orizzontale
    for x in range(1, X):
        row = min(x, X-x)
        if x == row:
            if torch.sum( 
                torch.tensor(torch.eq(Tensor[:x, :], Tensor[x : x+row, :].flip(0)), dtype = torch.int) - 1 ) == 0:
                res_x.append(x)
            elif torch.sum( 
                torch.tensor(torch.eq(Tensor[:x, :], Tensor[x : x+row, :].flip(0)), dtype = torch.int) - 1 ) == -1 and flag == 0:
                res_x.append(x)
                flag = 1
                mask = torch.logical_not(torch.eq(Tensor[:x, :], Tensor[x : x+row, :].flip(0)))
                Tensor[:x, :][mask] = abs(Tensor[:x, :][mask]-1)
        else:
            if torch.sum(torch.tensor(torch.eq(Tensor[x-row : x, :], Tensor[x:, :].flip(0)), dtype = torch.int) - 1 ) == 0:
                res_x.append(x)
            elif torch.sum( 
                torch.tensor(torch.eq(Tensor[x-row : x, :], Tensor[x:, :].flip(0)), dtype = torch.int) - 1 ) == -1 and flag == 0:
                res_x.append(x)
                flag = 1
                mask = torch.logical_not(torch.eq(Tensor[x-row : x, :], Tensor[x:, :].flip(0)))
                Tensor[x-row : x, :][mask] = abs(Tensor[x-row : x, :][mask]-1)

    for y in range(1, Y):
        col = min(y, Y-y)
        if y == col:
            if torch.sum(torch.tensor(torch.eq(Tensor[:, :y], Tensor[:, y : y+col].flip(1)), dtype = torch.int) - 1 ) == 0:
                res_y.append(y)
            elif torch.sum( 
                torch.tensor(torch.eq(Tensor[:, :y], Tensor[:, y : y+col].flip(1)), dtype = torch.int) - 1 ) == -1 and flag == 0:
                res_y.append(y)
                flag = 1
                mask = torch.logical_not(torch.eq(Tensor[:, :y], Tensor[:, y : y+col].flip(1)))
                Tensor[:, :y][mask] = abs(Tensor[:, :y][mask]-1)
        else:
            if torch.sum(torch.tensor(torch.eq(Tensor[:, y-col : y], Tensor[:, y:].flip(1)), dtype = torch.int, requires_grad=False) - 1 ) == 0:
                res_y.append(y)
            elif torch.sum( 
                torch.tensor(torch.eq(Tensor[:, y-col : y], Tensor[:, y:].flip(1)), dtype = torch.int) - 1 ) == -1 and flag == 0:
                res_y.append(y)
                flag = 1
                mask = torch.logical_not(torch.eq(Tensor[:, y-col : y], Tensor[:, y:].flip(1)))
                Tensor[:, y-col : y][mask] = abs(Tensor[:, y-col : y][mask]-1)
            

    return sum(res_y) + 100*sum(res_x)


def solution_part2(filename):
    fh = open(filename, mode = 'r')
    tmp = []
    sol = 0
    for line in fh:
        if len(line.strip()) == 0:
            sol += count_sym_part2(torch.tensor(tmp, requires_grad=False))
            tmp = []
        else:
            tmp.append(convert(line.strip()))
    # the last group
    sol += count_sym_part2(torch.tensor(tmp))
    
    return sol

if __name__ == '__main__':
    print("Advent of code: day 13")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    