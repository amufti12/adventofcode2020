
grid = [list(line.strip()) for line in open('day11.input')]

# # Part 1 - comment out part 1 for part 2 answer
#
# def countOcc(grid, i, j, x, y):
#     rules = [
#         # NW
#         i > 0 and j > 0 and grid[i - 1][j - 1] == '#',
#         # N
#         i > 0 and grid[i - 1][j] == '#',
#         # NE
#         i > 0 and j < y - 1 and grid[i - 1][j + 1] == '#',
#         # W
#         j > 0 and grid[i][j - 1] == '#',
#         # E
#         j < y - 1 and grid[i][j + 1] == '#',
#         # SW
#         i < x - 1 and j > 0 and grid[i + 1][j - 1] == '#',
#         # S
#         i < x - 1 and grid[i + 1][j] == '#',
#         # SE
#         i < x - 1 and j < y - 1 and grid[i + 1][j + 1] == '#',
#     ]
#     return sum(int(c) for c in rules)
#
#
# def goThrough(grid):
#     x = len(grid)
#     y = len(grid[0])
#     new_grid = []
#     hasChanged = False
#     for i in range(x):
#         new_row = []
#         for j in range(y):
#             if grid[i][j] == 'L' and countOcc(grid, i, j, x, y) == 0:
#                 new_row.append('#')
#                 hasChanged = True
#             elif grid[i][j] == '#' and countOcc(grid, i, j, x, y) >= 4:
#                 new_row.append('L')
#                 hasChanged = True
#             else:
#                 new_row.append(grid[i][j])
#         new_grid.append(new_row)
#     return new_grid, hasChanged
#
#
# while True:
#     grid, hasChanged = goThrough(grid)
#     if not hasChanged:
#         break
#
# print("Part 1:", sum(row.count("#") for row in grid))

# Part 2

x = len(grid)
y = len(grid[0])
neighbors = [[list() for _ in range(y)] for _ in range(x)]

# east-west
for i, row in enumerate(grid):
    seats = [j for j, node in enumerate(row) if node != "."]
    for j1, j2 in zip(seats[:-1], seats[1:]):
        neighbors[i][j1].append((i, j2))
        neighbors[i][j2].append((i, j1))

# north-south
for j in range(y):
    seats = [i for i in range(x) if grid[i][j] != "."]
    for i1, i2 in zip(seats[:-1], seats[1:]):
        neighbors[i1][j].append((i2, j))
        neighbors[i2][j].append((i1, j))

coordinates = [(i, j) for j in range(y) for i in range(x) if grid[i][j] != '.']

# diagonal \
d = x - 1
while True:
    this_coord = [(u, v) for u, v in coordinates if u - v == d]

    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d -= 1

# diagonal /
d = 0
while True:
    this_coord = [(u, v) for u, v in coordinates if u + v == d]

    if len(this_coord) == 0:
        break
    for ((i1, j1), (i2, j2)) in zip(this_coord[:-1], this_coord[1:]):
        neighbors[i1][j1].append((i2, j2))
        neighbors[i2][j2].append((i1, j1))
    d += 1

this_grid = [[v for v in row] for row in grid]

changed = True
while changed:
    new_grid = []
    changed = False
    for i, row in enumerate(this_grid):
        new_row = []
        for j, seat in enumerate(row):
            cur_val = this_grid[i][j]
            if cur_val == ".":
                new_row.append(".")
            else:
                occupied = sum(int(this_grid[u][v] == '#') for u, v in neighbors[i][j])
                if occupied == 0 and cur_val == "L":
                    new_row.append("#")
                    changed = True
                elif occupied >= 5 and cur_val == "#":
                    new_row.append("L")
                    changed = True
                else:
                    new_row.append(cur_val)
        new_grid.append(new_row)
    this_grid = new_grid

print("Part 2:", [v for row in this_grid for v in row].count("#"))