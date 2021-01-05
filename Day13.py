import sys
import functools

with open('day13.input' if len(sys.argv) < 2 else sys.argv[1]) as f:
    data = list(x.strip() for x in f)

min_to_wait = int(data[0])
busses = [int(x) for x in data[1].split(',') if x != 'x']

best_time = min_to_wait * 2
mybus = 0
for bus in busses:
    min_time = min_to_wait - (min_to_wait % bus) + bus
    best_time = min(best_time, min_time)
    if best_time == min_time:
        mybus = bus

print("Part 1:", mybus * (best_time - min_to_wait))

busses = [(int(x), n) for (n, x) in enumerate(data[1].split(',')) if x != 'x']

def findmulsgcd(a, b):
    if a < b:
        s = findmulsgcd(b, a)
        return (s[1], s[0], s[2])
    if b == 0:
        return (1, 0, a)
    c = a % b
    q = a // b
    (bmul, cmul, g) = findmulsgcd(b, c)
    # bmul * b + cmul * c = 1
    # bmul * b + cmul * (a - b*q) = 1
    # (bmul - q*cmul) * b + cmul * a = 1
    return (cmul, bmul - q*cmul, g)

def findans(a1, mod1, a2, mod2):
    (m1, m2, g) = findmulsgcd(mod1, mod2)
    assert g == 1
    x = a1*m2*mod2 + a2*m1*mod1
    x = x % (mod1*mod2)
    while (x < 0):
        # print(1)
        x += mod1*mod2

    return (x, mod1*mod2)

eqns = []
for bus in busses:
    eqns.append((bus[0] - bus[1], bus[0]))

print("Part 2:",
    functools.reduce(
        lambda ma1, ma2: findans(ma1[0], ma1[1], ma2[0], ma2[1]),
        eqns)[0])
