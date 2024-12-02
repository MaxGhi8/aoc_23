#### Advent of code: day 4

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    solution = 0
    for line in fh:
        line = line.split(':')[1].split('|')
        win_num = list(map(lambda x: int(x.strip()), line[0].strip().split()))
        num = list(map(lambda x: int(x.strip()), line[1].strip().split()))
        num = list(filter(lambda x: x in win_num, num))
        solution += int(2**(len(num) - 1) )*int(len(num) > 0)
    return int(solution)
#########################################

def solution_part2(filename):
    fh = open(filename, mode = 'r')
    Dict_wins = {} # Dict with points per copy
    Dict_copies = {} # Dict of number of each copy
    for line in fh:
        line = line.split(':')
        game_num = int(line[0].split()[-1].strip()) # number of the game
        line = line[1].strip().split('|')
        win_num = list(map(lambda x: int(x.strip()), line[0].strip().split())) # numeri vincenti
        num = list(map(lambda x: int(x.strip()), line[1].strip().split()))
        num = list(filter(lambda x: x in win_num, num)) # numeri uguali ai numeri vincenti
        Dict_wins[game_num] = int(2**(len(num) - 1) )*int(len(num) > 0) # punteggio
        for i in range(len(num)):
            Dict_copies[game_num + i + 1] = Dict_copies.get(game_num + i + 1, 1) + Dict_copies.get(game_num, 1)
    return sum(list(map(lambda x: Dict_copies.get(x, 1), Dict_wins.keys())))

if __name__ == '__main__':
    print("Advent of code: day 4")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    