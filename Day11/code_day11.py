#### Advent of code: day 11
import numpy as np

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    rows = []
    cols = []
    gal_idx = []
    for r, line in enumerate(fh):
        row = [char for char in line.strip()]
        if not '#' in row:
            rows.append(r)
        else:
            remove_idx = 0
            while '#' in row:
                index = row.index('#')
                index += remove_idx
                gal_idx.append((r, index))
                if index not in cols:
                    cols.append(index)
                row.remove('#')
                remove_idx += 1

    cols = list(filter(lambda x: x not in cols, [i for i in range(len(line.strip()))]))

    n_gal = len(gal_idx)
    tot_distance = 0
    for i, gal in enumerate(gal_idx):
        for j in range(i+1, n_gal):
            start = gal
            end = gal_idx[j]
            # print(start, end)
            flag_x = sum(list( map(lambda x: int(x in rows), 
                                   range(min(start[0], end[0]) + 1, max(start[0], end[0])) ) ))
            
            flag_y = sum(list( map(lambda x: int(x in cols), 
                                  range(min(start[1], end[1]) + 1, max(start[1], end[1])) ) ))
            # print(flag_x, flag_y)
            # print(flag_x + flag_y + abs(end[0] - start[0]) + abs(end[1] - start[1]))
            tot_distance += flag_x + flag_y + abs(end[0] - start[0]) + abs(end[1] - start[1])

    return tot_distance
        

#########################################
def solution_part2(filename):
    fh = open(filename, mode = 'r')
    rows = []
    cols = []
    gal_idx = []
    for r, line in enumerate(fh):
        row = [char for char in line.strip()]
        if not '#' in row:
            rows.append(r)
        else:
            remove_idx = 0
            while '#' in row:
                index = row.index('#')
                index += remove_idx
                gal_idx.append((r, index))
                if index not in cols:
                    cols.append(index)
                row.remove('#')
                remove_idx += 1

    cols = list(filter(lambda x: x not in cols, [i for i in range(len(line.strip()))]))
    
    n_gal = len(gal_idx)
    expansion = 1000000 - 1
    tot_distance = 0
    for i, gal in enumerate(gal_idx):
        for j in range(i+1, n_gal):
            start = gal_idx[i]
            end = gal_idx[j]
            flag_x = sum(list( map(lambda x: int(x in rows)*expansion, 
                                   range(min(start[0], end[0]) + 1, max(start[0], end[0])) ) ))
            
            flag_y = sum(list( map(lambda x: int(x in cols)*expansion, 
                                  range(min(start[1], end[1]) + 1, max(start[1], end[1])) ) ))
            tot_distance += flag_x + flag_y + abs(end[0] - start[0]) + abs(end[1] - start[1])

    return tot_distance

if __name__ == '__main__':
    print("Advent of code: day 11")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    