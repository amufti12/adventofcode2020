
file = open('day06.input').read().rstrip()

arrayAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def p1(inputFile):
    summ = 0
    answers = inputFile.split("\n\n")
    for x in answers:
        totalAdded = sum(1 for y in arrayAlphabet if y in x)
        summ += totalAdded
    return summ

def p2(inputFile):
    summ = 0
    answers = inputFile.split("\n\n")
    for x in answers:
        line = x.split("\n")
        for letter in arrayAlphabet:
            if all([letter in y for y in line]):
                summ += 1
    return summ

print(p1(file))
print(p2(file))