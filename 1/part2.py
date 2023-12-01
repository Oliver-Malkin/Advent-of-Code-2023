import re

with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
sum = 0

for i in data:
    # You cant delete the word completely, either end of the work could "break" the words next to it
    temp = re.sub("one", "one1one", i) 
    temp = re.sub("two", "two2two", temp)
    temp = re.sub("three", "three3three", temp)
    temp = re.sub("four", "four4four", temp)
    temp = re.sub("five", "five5five", temp)
    temp = re.sub("six", "six6six", temp)
    temp = re.sub("seven", "severn7severn", temp)
    temp = re.sub("eight", "eight8eight", temp)
    temp = re.sub("nine", "nine9nine", temp)
    temp = re.sub("[^0-9]", "", temp)

    sum += int(temp[0] + temp[-1]) # first and last

print(sum)