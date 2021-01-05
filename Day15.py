
input = [7,12, 1, 0, 16, 2]
test = [1, 3, 2]
spoken = []
recentNumber = {}

for i, n in enumerate(input):
    if i != len(input) - 1:
        recentNumber[n] = i
        # print(recentNumber)

while len(input) < 30000000:
    previousNumber = input[-1]
    thirdPrevious = recentNumber.get(previousNumber, -1)
    recentNumber[previousNumber] = len(input) -1
    if thirdPrevious == -1:
        after = 0
    else:
        after = len(input) - 1 - thirdPrevious
    input.append(after)
    # print(input)
    if len(input) == 2020:
        print("Part 1:", after)
print("Part 2:", input[-1])