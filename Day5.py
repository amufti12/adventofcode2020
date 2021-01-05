
text = [line for line in open("day05.input", "r").read().strip().split("\n")]
replacedID = [int(line.replace('F', "0").replace('B', "1").replace('L', "0").replace('R', "1"), 2) for line in text]
print(text)
print(replacedID)
print(max(replacedID))
print(next(i for i in range(min(replacedID), max(replacedID)) if i not in replacedID))


# b = 1
# f = 0
# l = 0
# r = 1
# BFBBBBBLLR
#
# 63 127 B
# 63 94 F
# 80 94 B
# 88 94 B
# 92 94 B
# 93 94 B
# 94 B
# 0 3 L
# 0 1 L
# 1 R


