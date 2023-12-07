from collections import Counter

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split()

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
    "A": "a",
    "K": "b",
    "Q": "c",
    "J": "n", # Updated to be the lowest valued card
    "T": "e",
    "9": "f",
    "8": "g",
    "7": "h",
    "6": "i",
    "5": "j",
    "4": "k",
    "3": "l",
    "2": "m" 
}

for i in range(0, len(data), 2):
    counter = Counter(data[i]) # Counts all the cards in the hand
    cards = set(data[i]) # Get all individual cards in the hand
    count = [] # Number of all the individual card counts

    for card in cards:
        count.append((counter[card], card)) # Hand AAKKQ -> [(2, A), (2, K), (1, Q)]

    count = sorted(count, key=lambda x: x[0])

    hand = data[i]
    bid = data[i+1]
    mapped_hand = []

    for j in hand:
        mapped_hand.append(value_map[j])

    mapped_hand = "".join(mapped_hand)

    if count[-1][1] == "J":
        try:
            mapped_hand_j = mapped_hand.replace(value_map['J'], value_map[count[-2][1]])
        except IndexError:
            mapped_hand_j = mapped_hand.replace(value_map['J'], value_map[count[-1][1]])
    else:
        mapped_hand_j = mapped_hand.replace(value_map['J'], value_map[count[-1][1]])

    # Need to re count the mapped hand
    counter = Counter(mapped_hand_j)
    count = [] # Number of all the individual card counts

    for card in set(mapped_hand_j):
        count.append((counter[card], card)) # Hand AAKKQ -> [(2, A), (2, K), (1, Q)]
        
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