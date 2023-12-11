with open("input.txt", "r") as file:
    data = file.read().split('\n')

instructions = data[0]
nodes = {}

# Dict it
for i, node in enumerate(data[2:]):
    split_node = node.split()
    start = split_node[0] # Dict key
    left = split_node[2].replace("(", "").replace(",", "")
    right = split_node[3].replace(")", "")

    nodes[start] = (left, right) # Tuple of left and right nodes in a dict

finished = False
next_node = "AAA" # Set to the starting node
steps = 1
while not finished:
    for i, direction in enumerate(instructions):
        if direction == "L":
            next_node = nodes[next_node][0]
        else:
            next_node = nodes[next_node][1]

        if next_node == "ZZZ":
            finished = True
            break
        else:
            steps += 1

print(steps)