# read in aoc input
data = open("day09.input").read().strip().split('\n')

# setup vars to track
pre = 25
pos = 25

# solve for part 1
while True:
    p1 = int(data[pos])
    # grab all valid values to check through
    options = [int(x) for x in data[pos - pre: pos]]

    for i in options:
        # check to see if the needed amount is in the options
        if p1 - i != i and p1 - i in options:
            pos += 1
            break
    else:
        break

print(f'Part 1: {p1}')

# solve for part 1

seen = set()

# set beginning and end values for range to sum
for beg in range(len(data) - 1):
    for end in range(beg + 1, len(data)):
        # grab range and convert ints for ease of summing
        subset = list(map(int, data[beg:end + 1]))

        # to speed things up keeping track of seen totals and skipping invalid ranges
        if sum(subset) in seen or max(subset) > p1 or sum(subset) > p1:
            break
        else:
            seen.add(sum(subset))

        # if range equals part 1 quit looking
        if sum(subset) == p1:
            p2 = subset
            break

print(f'Part 2: {min(p2) + max(p2)}')