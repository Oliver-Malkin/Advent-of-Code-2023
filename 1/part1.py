import re

with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
sum = 0

for i in data:
    temp = re.sub("[^0-9]", "", i) # strip the characters away
    sum += int(temp[0] + temp[-1]) # first and last

print(sum)