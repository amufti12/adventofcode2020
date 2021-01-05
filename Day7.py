
text = [line for line in open("day07.input", "r").read().strip().split("\n")]
# print(text)

rules = {}
def p1(text):
    for bags in text:
        value = bags[:-1].split(' contain ')
        bagColor = value[0][:-5]
        # print(bagColor)
        for baglist in value[1].split(', '):
            if baglist != 'no other bags':
                color = ' '.join(baglist.split(' ')[1:-1])
                # print(color)
                if color not in rules:
                    rules[color] = set({})
                rules[color].add(bagColor)

    gold = {'shiny gold'}
    inBag = True
    while inBag:
        inBag = False
        length = len(gold)
        for color in gold:
            if color in rules:
                gold = gold | rules[color]
        if len(gold) > length:
            inBag = True
    return len(gold) -1

# def p2(text):
for bags in text:
    value = bags[:-1].split(' contain ')
    bagColor = value[0][:-5]
    for baglist in value[1].split(', '):
        if baglist != 'no other bags':
            color = ' '.join(baglist.split(' ')[1:-1])
            num = int(baglist.split(' ')[0])
            if bagColor not in rules:
                rules[bagColor] = set({})
            rules[bagColor].add((color, num))
        else:
            rules[bagColor] = set({})
        # return color

def appendColor(color):
    total = 0
    for someColor, num in rules[color]:
        total += num * (1 + appendColor(someColor))
    return total

# print(p1(text)) #undo for p1
print(appendColor('shiny gold'))

