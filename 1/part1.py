import re

with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
sum = 0

for i in data:
    temp = re.sub("[^0-9]", "", i)
    if len(temp) == 1:
        sum += int(temp*2) # two number
    else:
        sum += int(temp[0] + temp[len(temp)-1]) # first and last

print(sum)