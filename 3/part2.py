import re

with open("input.txt", "r") as file:
    data = file.read().split('\n')

# remap the numbers 467 -> 111, 114 -> 222 etc (must be a unique key)
current_char = 10000
char_map = {} # randome char -> number
new_data = data[:]

start_pos = end_pos = None # None so it can know if a part has "started" yet
current_part = '' # stores the current part

for row, line in enumerate(data): # Iterate over each row
    for pos, char in enumerate(line): # Iterate the row
        if char.isdigit() is True:
            if start_pos is None:
                start_pos = pos # Set the start pos
            current_part = current_part + char # Add the char to the running total

        if char.isdigit() is False or pos+1 == len(data[0]):
            if start_pos is not None:
                end_pos = pos-1 # Set the end of the word
                char_map[current_char] = current_part
                new_data[row] = new_data[row].replace(current_part, chr(current_char)*len(current_part), 1)
                current_char += 1
                start_pos = end_pos = None
                current_part = ''

def check_gear(row: int, pos: int):
    adjacent_parts = 0
    keys = []
    for i in range(-1, 2):
        if row+i != -1 and row+i != len(data): # Is it not top or bottom row?
            if pos == 0: # Start of a row
                current_row = data[row+i][pos:pos+2]
                map_row = new_data[row+i][pos:pos+2]
            elif pos == len(data[0])-1: # End of a row
                current_row = data[row+i][pos-1:pos+1]
                map_row = new_data[row+i][pos-1:pos+1]
            else:
                current_row = data[row+i][pos-1:pos+2]
                map_row = new_data[row+i][pos-1:pos+2]

            adjacent_parts += len(re.sub("[^0-9]", " ", current_row).split()) # How many individual numbers are there?

            for j in range(len(map_row)):
                if map_row[j] not in keys:
                    keys.append(map_row[j])

    if adjacent_parts == 2:
        return keys
    else:
        return False # Not a gear

total = 0
for i, line in enumerate(data):
    for pos, char in enumerate(line):
        if char == '*': # Find line and position of all *
            check = check_gear(i, pos)
            if check != False:
                sub_total = []
                for j in check:
                    try:
                        sub_total.append(int(char_map[ord(j)]))
                    except KeyError:
                        pass # not in the map, will be a . or * etc
                total += sub_total[0]*sub_total[1]

print(total)