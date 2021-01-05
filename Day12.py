with open('day12.input', 'r') as file:
    text = file.read().splitlines()#.readlines()

def part1(text):
    x, y = 0, 0
    dx, dy = 1, 0
    for c in text:
        dir, amt = c[0], int(c[1:])
        if dir == 'N':
            y += amt
        elif dir == 'S':
            y -= amt
        elif dir == 'W':
            x -= amt
        elif dir == 'E':
            x += amt
        elif dir == 'L':
            for i in range(amt // 90):
                dx, dy = -dy, dx
        elif dir == 'R':
            for i in range(amt // 90):
                dx, dy = dy, -dx
        else:
            x += dx * amt
            y += dy * amt
    return(abs(x) + abs(y))

def part2(text):
    x, y = 0, 0
    dxz, dyz = 10, 1
    for c in text:
        dir, amt = c[0], int(c[1:])
        if dir == 'N':
            dyz += amt
        elif dir == 'S':
            dyz -= amt
        elif dir == 'W':
            dxz -= amt
        elif dir == 'E':
            dxz += amt
        elif dir == 'L':
            for i in range(amt // 90):
                dxz, dyz = -dyz, dxz
        elif dir == 'R':
            for i in range(amt // 90):
                dxz, dyz = dyz, -dxz
        else:
            x += dxz * amt
            y += dyz * amt
    return(abs(x) + abs(y))

print("Part 1", part1(text))
print("Part 2", part2(text))