#### Advent of code: day 1
# OSS --> re.findall trova stringe che non si opverlappano
import re

def sum_digits(filename):
    fh = open(filename, mode = 'r')
    total_sum = 0
    for line in fh:
        digits = re.findall("\d", line.strip())
        total_sum += int(digits[0])*10 + int(digits[-1])
    return total_sum

def sum_digits2_0(filename):
    fh = open(filename, mode = 'r')
    
    replacements_dictionary = {'one' : 'on1e', 'two' : 'tw2o', 'three' : 'thr3e','four': 'fo4ur', 'five':'fi5ve','six': 'si6x','seven': 'sev7en',
                               'eight' : 'ei8ght','nine':'ni9ne'}
    total_sum = 0
    
    for line in fh:
        for key,value in replacements_dictionary.items():
            line = line.replace(key, value)
            
        digits = re.findall("\d", line.strip())
        total_sum += int(digits[0] + digits[-1]) # sum with string
    return total_sum

if __name__ == '__main__':
    print("Advent of code: day 1")
    
    filename = "input.txt"
    total_sum = sum_digits(filename)
    print(f"Solution part 1: {total_sum}")
    
    total_sum = sum_digits2_0(filename)
    print(f"Solution part 2: {total_sum}")