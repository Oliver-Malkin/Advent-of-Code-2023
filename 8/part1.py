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
next_node = list(nodes.keys())[0] # Set to the first node in the dict
while not finished:
    for i, direction in enumerate(instructions):
        
