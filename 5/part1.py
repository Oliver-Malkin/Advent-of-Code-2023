with open("input.txt", "r") as file:
    data = file.read().split('\n')

maps = []

seeds = list(map(int, data[0].split("seeds: ")[1].split()))
data = data[2:]

temp = []
for i in data:
    try:
        if i[0].isdigit(): # ignore the labels
            temp.append(list(map(int, i.split())))
    except IndexError: # new map "block"
        maps.append(temp)
        temp = []
maps.append(temp)

locations = []
# Each map [destination, source, range]
for seed in seeds: # All the seeds
    for m in maps: # All the maps
        for r in m: # The single map
            if r[1] + (r[2]-1) >= seed and r[1] <= seed: # In the range
                seed_diff = seed - r[1]
                seed = seed_diff+r[0]
                break
    locations.append(seed)

print(min(locations))
