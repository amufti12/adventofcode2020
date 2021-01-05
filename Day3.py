with open('day03.input', 'r') as file:
    text = file.read().splitlines()

def tree(slopeRow, slopeCol, rows):
    row = 0
    col = 0
    count = 0
    while row < len(rows):
        if rows[row][col] == "#":
            count += 1
        row += slopeRow
        col = (col + slopeCol) % len(rows[0])
    return count

print(tree(1, 3, text))
print(tree(1, 1, text) * tree(1, 3, text) * tree(1, 5, text) *
      tree(1, 7, text) * tree(2, 1, text))