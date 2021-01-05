#setting the bit to 1
def setOneBit(value: int, bit: int):
    return value | (1 << bit)

#setting bit to 0
def setZeroBit(value: int, bit: int):
    return value & ~(1 << bit)

def bitMask(maskStr: str, value: int) -> int:
    result = value
    for i, bval in enumerate(maskStr):
        bindex = len(maskStr)-1-i

        if bval == '0':
            result = setZeroBit(result, bindex)
        elif bval == '1':
            result = setOneBit(result, bindex)
    return result


def getDecodedAddrs(maskStr: str, value: int, memAddr: int) -> set:
    initialAddr = memAddr
    count = 0
    for i in range(len(maskStr)):
        if maskStr[len(maskStr)-1-i] == '1':
            initialAddr = setOneBit(initialAddr, i)

    currentAddrs = set([initialAddr])
    for i in range(len(maskStr)):
        if maskStr[len(maskStr)-1-i] == 'X':
            newAddrs = set()
            for addr in currentAddrs:
                newAddrs.add(setOneBit(addr, i))
                newAddrs.add(setZeroBit(addr, i))
            currentAddrs = currentAddrs.union(newAddrs)
    return currentAddrs

isPart1 = False #change to true for part 1
maskStr = ''
memDict = {}
with open('day14.input') as file:
    line = file.readline()
    while line:
        items = line.strip().split()
        if line.startswith('mask'):
            maskStr = items[2]
        else:
            memAddr, value = int(items[0][4:-1]), int(items[2])
            if isPart1:
                memDict[memAddr] = bitMask(maskStr, value)
            else:
                for addr in getDecodedAddrs(maskStr, value, memAddr):
                    memDict[addr] = value
        line = file.readline()

resultSum = 0
for memValue in memDict.values():
    if memValue != 0:
        resultSum += memValue

if isPart1:
    print('Part 1', resultSum)
else:
    print('Part 2', resultSum)