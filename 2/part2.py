import re

total = 0 # Stores the sum from the total number of games

with open("input.txt", "r") as file:
    data = file.read().split("\n") # Split the data by new lines

for i in data: # Each game
    # Get each game into a list ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
    game = i.split(': ')
    del game[0] 
    game = game[0].split('; ')

    num_red = num_green = num_blue = 0 # Each game new counter

    for k in game: # Each draw
        temp_green = temp_blue = temp_red = 0 # Each draw new counter

        element = re.sub(",", "", " "+k)
        
        for colour in re.finditer("red|green|blue", element):
            
            start = colour.start()
            value = int(re.sub("[^0-9]", "", element[start-3:start-1]))

            match colour.group():
                case "blue":
                    temp_blue = value
                case "green":
                    temp_green = value
                case "red":
                    temp_red = value
        
            if temp_blue > num_blue:
                num_blue = temp_blue

            if temp_red > num_red:
                num_red = temp_red 

            if temp_green > num_green:
                num_green = temp_green

    total += num_blue*num_red*num_green

print(total)