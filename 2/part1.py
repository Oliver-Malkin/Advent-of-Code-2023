import re

maxs = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0 # Stores the sum from the total number of games

with open("input.txt", "r") as file:
    data = file.read().split("\n") # Split the data by new lines

j = 1
for i in data:
    game = i.split(': ')
    del game[0] # removes the game number
    game = game[0].split('; ')

    valid = True

    for k in game:
        temp_red = 0
        temp_green = 0
        temp_blue = 0

        element = re.sub(",", "", " "+k)
        
        for colour in re.finditer("red|green|blue", element):
            start = colour.start()
            value = int(re.sub("[^0-9]", "", element[start-3:start-1]))

            match colour.group():
                case "blue":
                    temp_blue += value
                case "green":
                    temp_green += value
                case "red":
                    temp_red += value
        
            if temp_blue > maxs['blue'] or temp_green > maxs['green'] or temp_red > maxs['red']:
                valid = False
                break
        
    if valid:
        total += j
    j += 1 # Stores the game number

print(total)