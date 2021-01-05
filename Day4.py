import re

with open('day04.input', 'r') as file:
    text = file.readlines()#.splitlines()
    print(text)

arrayList = []
passport = set()

def height(a):
    if 'cm' in a:
        x, y = a.split('cm', maxsplit=1)
        return y == '' and 150 <= int(x) <= 193
    if 'in' in a:
        x, y = a.split('in', maxsplit=1)
        return y == '' and 59 <= int(x) <= 76
    return False

def automaticValidation(group):
    field, value = group.split(':')
    if field == 'byr':
        return len(value) == 4 and 1920 <= int(value) <= 2002
    if field == 'iyr':
        return len(value) == 4 and 2010 <= int(value) <= 2020
    if field == 'eyr':
        return len(value) == 4 and 2020 <= int(value) <= 2030
    if field == 'hgt':
        return height(value)
    if field == 'hcl':
        return re.fullmatch(r"#[a-f0-9]{6}", value)
    if field == 'ecl':
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if field == 'pid':
        return re.fullmatch(r"[0-9]{9}", value)
    if field == "cid":
        return True
    return True

count = 0
for spaces in text:
    if spaces == '\n':
        arrayList.append(passport)
        passport = set()
        continue
    line = spaces.strip('\n')
    splitVal = line.split(' ')
    for fields in splitVal:
        key = fields.split(':')[0]
        # passport.add(key) #undo comment for Part 1 answer
        if automaticValidation(fields):
            passport.add(key)

arrayList.append(passport)


def isValid(input):
    group = set(input)
    group.add('cid')
    group.remove('cid')
    return len(group) == 7

# for i in range(0,len(arrayList)):
#     if isValid(arrayList[i]):
#         print("PASSPORT", str(i) + ": VALID")
#     else:
#         print("PASSPORT", str(i) + ": INVALID")

print("Number of VALID Passports: ", len(list(x for x in arrayList if isValid(x))))
# idk = list.count(arrayList)
print(len(arrayList))
# print("PASSPORT"+ counterThing + "INVALID")
