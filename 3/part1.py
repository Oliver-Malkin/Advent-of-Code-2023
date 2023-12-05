import re

with open("input.txt", "r") as file:
    data = file.read().split('\n')

# Give a row, start and end pos to check if the part is an engine part
def check_part(row: int, start: int, end: int) -> bool:
    is_part = False

    if start == 0:
        start = 1
    if end == len(data[0])-1:
        end -= 1

    for i in range(-1, 2):
        try:
            if row+i != -1 and row+i < len(data):
                current_row = re.sub("[0-9.]", "", data[row+i][start-1:end+2])
                if current_row != '':
                    is_part = True
        except IndexError:
            pass
    
    return is_part

start_pos = end_pos = None # None so it can know if a part has "started" yet
total = 0
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
                if check_part(row, start_pos, end_pos):
                    total += int(current_part) # Add the part
                # Reset everything
                start_pos = end_pos = None
                current_part = ''

print(total)