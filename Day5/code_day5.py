#### Advent of code: day 5
from functools import reduce

def solution_part1(filename):
    seeds, *mappings = open('data.txt').read().split('\n\n')
    seeds = map(int, seeds.split()[1:])

    def lookup(start, mapping):
        for m in mapping.split('\n')[1:]:
            dst, src, len = map(int, m.split())
            delta = start - src
            if delta in range(len):
                return dst + delta
        else: return start

    return min(reduce(lookup, mappings, int(s)) for s in seeds)
#########################################

def solution_part2(filename):

    seeds, *mappings = open('data.txt').read().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

    def lookup(inputs, mapping):
        for start, length in inputs:
            while length > 0:
                for m in mapping.split('\n')[1:]:
                    dst, src, len = map(int, m.split())
                    delta = start - src
                    if delta in range(len):
                        len = min(len - delta, length)
                        yield (dst + delta, len)
                        start += len
                        length -= len
                        break
                else: yield (start, length); break

    print(*[min(reduce(lookup, mappings, s))[0] for s in [
        zip(seeds, [1] * len(seeds)),
        zip(seeds[0::2], seeds[1::2])]])

if __name__ == '__main__':
    print("Advent of code: day 5")
    
    filename = "input_part1.txt"
    print(solution_part1(filename))
    
    filename = "input_part2.txt"
    print(solution_part2(filename))
    