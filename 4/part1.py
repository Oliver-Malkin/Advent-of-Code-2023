with open("input.txt", "r") as file:
    data = file.read().split('\n')

# Remove the card numbers and split the data into two arrays [winning number, my numbers]
for i, card in enumerate(data):
    data[i] = card.split(':')[1].split('|')
    data[i] = [data[i][0].split(), data[i][1].split()]

total = 0
for i, card in enumerate(data):
    card_total = 0
    for j, winner in enumerate(card[0]):
        if winner in card[1]:
            card_total += 1
    if card_total != 0:
        total += 2**(card_total-1)

print(total)