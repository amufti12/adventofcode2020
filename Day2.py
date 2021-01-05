
with open('day02.input', 'r') as file:
    text = file.read().splitlines()

def parseInput(min, max, letter, password):
    if password.count(letter) >= min and password.count(letter) <= max:
        return True

def position(min, max, letter, password):
    if (password[min] == letter and password[max] != letter):
        return True
    elif (password[min] != letter and password[max] == letter):
        return True

count = 0
count2 = 0
for line in text:
    median = str(line.partition(":")[0])
    max = int(median.partition("-")[2].partition(' ')[0])
    min = int(median.partition("-")[0])
    letter = str(median.partition("-")[2].partition(' ')[2])
    password = str(line.partition(":")[2])

    # if parseInput(min, max, letter, password):
    #     count +=1
    #     print(count)

    if position(min, max, letter, password):
        count2 += 1
        print(count2)

# parseInput = {'min': int(line[0]), 'max': int(line[1]), 'character': line[2], 'password': line[3]}
