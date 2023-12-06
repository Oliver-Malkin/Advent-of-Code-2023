import multiprocessing

with open("input.txt", "r") as file:
    data = file.read().split('\n')

maps = []

seeds = list(map(int, data[0].split("seeds: ")[1].split()))
new_seeds = []
for i in range(0, len(seeds), 2):
    new_seeds.append((seeds[i], seeds[i]+seeds[i+1]))

seeds = new_seeds

# Don't change anything past this
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

# parse a range of values using a tuple eg get_min(start, end), both inclusive
def get_min(r) -> int:
    location = float("inf")
    # Each map [destination, source, range]
    for seed in range(r[0], r[1]):
        for m in maps: # All the maps
            for r in m: # The single map
                if r[1] + (r[2]-1) >= seed and r[1] <= seed: # In the range
                    seed_diff = seed - r[1]
                    seed = seed_diff+r[0]
                    break
        if seed < location:
            location = seed
    return location

def test(f):
    return f[0]+f[1]

if __name__ == '__main__':
    multiprocessing.freeze_support()
    with multiprocessing.Pool(len(new_seeds)) as p:
        locations = p.map(get_min, new_seeds)
        print(min(locations))
