import collections

def iterateNeighbors(coordinates):
    x, y, z = coordinates
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                if dx == dy == dz == 0:
                    continue
                yield (x+dx, y+dy, z+dz)

def cycles(previous):
    actCount = collections.defaultdict(int)
    for coord in previous:
        for neighbor in iterateNeighbors(coord):
            actCount[neighbor] += 1
    new = []
    for coord in previous:
        count = actCount.pop(coord, 0)
        if count in (2, 3):
            new.append(coord)
    for coord, count in actCount.items():
        if count == 3:
            new.append(coord)
    return new

def part1(input):
    actCoords = []
    for y, line in enumerate(input):
        for x, i in enumerate(line):
            if i == '#':
                actCoords.append((x, y, 0))
    for something in range(6):
        actCoords = cycles(actCoords)
    answer = len(actCoords)
    print("Part 1:", answer)

def secondIterateNeighbors(coord):
    x, y, z, w = coord
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dw in (-1, 0, 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    yield (x+dx, y+dy, z+dz, w+dw)

def cyclesAgain(previous):
    actCount = collections.defaultdict(int)
    for coord in previous:
        for neighbor in secondIterateNeighbors(coord):
            actCount[neighbor] += 1
    new2 = []
    for coord in previous:
        count = actCount.pop(coord, 0)
        if count in (2, 3):
            new2.append(coord)
    for coord, count in actCount.items():
        if count == 3:
            new2.append(coord)
    return new2

def part2(input):
    actCoords = []
    for y, line in enumerate(input):
        for x, i in enumerate(line):
            if i == "#":
                actCoords.append((x, y, 0, 0))
    for something in range(6):
        actCoords = cyclesAgain(actCoords)
    answer = len(actCoords)
    print("Part 2:", answer)

data = open("day17.input").read().strip().splitlines()
part1(data)
part2(data)