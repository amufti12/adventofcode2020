from collections import defaultdict
def answer(input):
    # class: 1-3 or 5-7
    # row: 6-11 or 33-44
    # seat: 13-40 or 45-50

    # your ticket:
    # 7,1,14

    # nearby tickets:
    # 7,3,47
    # 40,4,50
    # 55,2,20
    # 38,6,12

    rules = {}
    selfTicket = []
    nearbyTicket = []

    s = 0
    for z in input:
        if (z == ""):
            s = s + 1

        elif s == 0:
            rule, f = z.split(": ")

            r1, r2 = [[int(i) for i in r.split("-")] for r in f.split(" or ")]

            rules[rule] = (r1, r2)

        elif s == 1:
            s = s + 1

        elif s == 2:
            selfTicket = [int(x) for x in z.split(",")]

        elif s == 3:
            s = s + 1

        elif s == 4:
            nearbyTicket.append([int(x) for x in z.split(",")])

    validTickets = []

    rate = 0
    for ticket in nearbyTicket:
        validT = True
        for value in ticket:
            valid = False
            for rule, ((low1, high1), (low2, high2)) in rules.items():
                if (low1 <= value <= high1) or (low2 <= value <= high2):
                    valid = True

            if not valid:
                rate += value
                validT = False

        if validT:
            validTickets.append(ticket)

    print("Part 1:", rate)

    posValid = defaultdict(lambda: [])
    for field in range(len(selfTicket)):
        for rule, ((low1, high1), (low2, high2)) in rules.items():
            valid = True
            for ticket in validTickets:
                if not ((low1 <= ticket[field] <= high1) or (low2 <= ticket[field] <= high2)):
                    valid = False

            if valid:
                posValid[rule].append(field)

    conf = {}
    while True:
        for rule, possible in posValid.items():
            p = possible[:]
            for v in conf.values():
                try:
                    p.remove(v)
                except ValueError:
                    pass

            if len(p) <= 1 and rule not in conf.keys():
                conf[rule] = p[0]

        if len(conf.keys()) >= len(selfTicket):
            break

    prod = 1
    for j, k in conf.items():
        if j.startswith("departure"):
            # print(k)
            prod *= selfTicket[k]

    print("Part 2:", prod)

data = open("day16.input").read().strip().split('\n')
answer(data)