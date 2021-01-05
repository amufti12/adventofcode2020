with open('day10.input') as f:
    plugs = list(x for x in map(int, f.readlines()))
    plugs.append(0)
    plugs.sort()
    plugs.append(plugs[-1] + 3)
print(plugs)
diffs = list(x - y for x,y in zip(plugs[1:], plugs[:-1]))
print(diffs)
ones = len([x for x in diffs if x == 1])
print(ones)
threes = len([x for x in diffs if x == 3])
print(threes)
print(ones * threes)

N = len(plugs)
counts=[0] * N
counts[-1]=1
for i in range(N - 2, -1, -1):
    s = 0
    for j in range(i + 1, N):
        if plugs[j] - plugs[i] <= 3:
            s += counts[j]
        else:
            break
    counts[i] = s
print(counts[0])