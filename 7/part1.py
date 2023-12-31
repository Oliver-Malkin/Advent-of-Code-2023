from collections import Counter

with open("input.txt", "r") as file:
    data = file.read().split() # [hand_0, bid_0, ..., hand_n, bid_n]

# Arrays of all the different hands
high_card = [] # Nothing, just 5 cards (5 type)

pair = [] # Two of the same card (4 types)

two_pair = [] # Two of the same card twice (3 types)
three = [] # Three of the same card (3 types, must contain 3 of the same card)

house = [] # Three of the same and a pair (2 types)
four = [] # Four of the same (2 types, must contain 4 of the same card)

five = [] # All of the same card (1 type)

# Makes it so much easier to sort
value_map = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M" 
}

for i in range(0, len(data), 2):
    counter = Counter(data[i]) # Counts all the cards in the hand
    cards = set(data[i]) # Get all individual cards in the hand
    count = [] # Number of all the individual card counts
    
    for card in cards:
        count.append((counter[card], card)) # Hand AAKKQ -> [(2, A), (2, K), (1, Q)]

    hand = data[i]
    bid = data[i+1]
    mapped_hand = []

    for j in hand:
        mapped_hand.append(value_map[j])

    mapped_hand = "".join(mapped_hand)

    # Whats the hand?
    match len(count):
        case 5: # High card
            high_card.append((mapped_hand, bid))

        case 4: # 1 pair
            pair.append((mapped_hand, bid))

        case 3: # Could be two pair or three of a kind
            if any(3 in sublist for sublist in count):
                three.append((mapped_hand, bid))
            else:
                two_pair.append((mapped_hand, bid))

        case 2: # Could be full house or 4 of a kind
            if any(4 in sublist for sublist in count):
                four.append((mapped_hand, bid))
            else:
                house.append((mapped_hand, bid))

        case 1: # Five of a kind
            five.append((mapped_hand, bid))

total = 0

# sorted(list, key=lambda x: x[0]) sort elements by first item in the tuple
# lists in order of best to worst

# yes this is ugly : )
sorted = sorted(five, key=lambda x: x[0]) + sorted(four, key=lambda x: x[0]) + sorted(house, key=lambda x: x[0]) + sorted(three, key=lambda x: x[0]) + sorted(two_pair, key=lambda x: x[0]) + sorted(pair, key=lambda x: x[0]) + sorted(high_card, key=lambda x: x[0])
sorted = sorted[::-1]

for i, hand in enumerate(sorted):
    total += int(hand[1])*(i+1)

print(total)