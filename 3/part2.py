import re

with open("input.txt", "r") as file:
    data = file.read().split('\n')

data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
....7.9...
..568*456.""".split('\n')


def check_gear(row: int, pos: int) -> bool:
    adjacent_parts = 0
    for i in range(-1, 2):
        if row+i != -1 and row+i != len(data): # Is it not top or bottom row?
            if pos == 0: # Start of a row
                current_row = data[row+i][pos:pos+2]
            elif pos == len(data[0])-1: # End of a row
                current_row = data[row+i][pos-1:pos]
            else:
                current_row = data[row+i][pos-1:pos+2]
            print(current_row)
            adjacent_parts += len(re.sub("[^0-9]", " ", current_row).split()) # How many individual numbers are there? 

    if adjacent_parts == 2:
        return True # Its a gear
    else:
        return False # Not a gear

def get_ratio(row: int, pos: int) -> int:
    pass

total = 0
for i, line in enumerate(data):
    for pos, char in enumerate(line):
        if char == '*': # Find line and position of all *
            if check_gear(i, pos):
                total += get_ratio(i, pos) # Add the ratio to the total
