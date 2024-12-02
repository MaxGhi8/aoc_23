#### Advent of code: day 
def detective_first(hand):
    Dict_card = {}
    for char in hand:
        Dict_card[char] = Dict_card.get(char, 0) + 1
    
    val_hand = list(Dict_card.values())
    max_hand = max(val_hand)
    if max_hand == 5:
        return 7
    elif max_hand == 4:
        return 6
    elif (max_hand == 3) and (min(val_hand) == 2):
        return 5
    elif max_hand == 3:
        return 4
    elif max_hand == 2:
        val_hand.remove(2)
        if max(val_hand) == 2:
            return 3
        else:
            return 2
    else:
        return 1

Dict_part1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, 
        '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

def detective_second(hand, Dict):
    Ls = []
    for char in hand:
        Ls.append(Dict[char])
    return Ls

def solution_part1(filename):
    fh = open(filename, mode = 'r')
    Hands = []
    for line in fh:
        Ls = line.split()
        tmp = [[detective_first(Ls[0])] + detective_second(Ls[0], Dict_part1), 
               int(Ls[1])]
        Hands.append(tmp)
        
    
    Hands.sort(key = lambda x: x[0])
    return sum(list(map(lambda x : (x[0] + 1)*(x[1][-1]), enumerate(Hands))))
                
#########################################
Dict_part2 = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, 
        '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

def detective_first_part2(hand):
    Dict_card = {}
    flag = 0
    if hand == 'JJJJJ':
        hand = 'AAAAA'
    for char in hand:
        if char == 'J':
            flag += 1
        else:
            Dict_card[char] = Dict_card.get(char, 0) + 1
    
    val_hand = list(Dict_card.values())
    max_hand = max(val_hand) + flag
    if max_hand == 5:
        return 7
    elif max_hand == 4:
        return 6
    elif (max_hand == 3) and (min(val_hand) == 2):
        return 5
    elif max_hand == 3:
        return 4
    elif max_hand == 2:
        if flag == 0:
            val_hand.remove(2)
        else:
            val_hand.remove(2-flag)
        if max(val_hand) == 2:
            return 3
        else:
            return 2
    else:
        return 1
    
    
def solution_part2(filename):
    fh = open(filename, mode = 'r')
    Hands = []
    for line in fh:
        Ls = line.split()
        tmp = [[detective_first_part2(Ls[0])] + detective_second(Ls[0], Dict_part2), 
               int(Ls[1])]
        Hands.append(tmp)
        
    
    Hands.sort(key = lambda x: x[0])
    return sum(list(map(lambda x : (x[0] + 1)*(x[1][-1]), enumerate(Hands))))
    

if __name__ == '__main__':
    print("Advent of code: day 7")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    