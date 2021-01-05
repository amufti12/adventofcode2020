with open("day18.input") as file:
    data = file.read()

def part1(expression):
    # Evaluates a string based on the new rules!
    # Current operation
    operator = ""
    # Current value
    curValue = 0
    # Value that we are accumulating inside the loop
    prevValue = ""
    # Loop through the expression, evaluating as we go
    index = 0
    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            prevValue += char
        elif char in ["+", "*"]:
            # Evaluate the previous operation
            if operator != "":
                if operator == "+":
                    curValue += int(prevValue)
                else:
                    curValue *= int(prevValue)

            else:
                # No operations have been done before
                curValue = int(prevValue)

            prevValue = ""
            operator = char

        elif char == "(":
            # Balance the parentheses to get to the end
            lefts = 1 # Lefts
            rights = 0 # Rights
            startIndex = index + 1

            while lefts != rights and index < len(expression):
                index += 1
                lefts += expression[index] == "("
                rights += expression[index] == ")"

            # Lefts and rights are balanced, evaluate what's inside
            insideParen = expression[startIndex:index]
            prevValue = part1(insideParen)
        index += 1

    # At the end, perform the operation
    if operator != "":
        if operator == "+":
            curValue += int(prevValue)
        else:
            curValue *= int(prevValue)

    return curValue


def part2(expression):
    # print("expression:", expression)
    # Goal: get rid of all the addition signs
    multiplicands = []

    # These still exist
    prevValue = ""

    # Current index
    index = 0

    # Boolean to tell whether the last argument is part of a sum
    lastIsAddition = False

    while index < len(expression):
        char = expression[index]

        if char.isdigit():
            prevValue += char

        elif char == "+":
            # Find where it ends!
            summands = [int(prevValue)]
            prevValue = ""
            index += 1

            while index < len(expression):
                char = expression[index]

                if char.isdigit():
                    prevValue += char

                elif char == "(":
                    # Balance the parentheses to get to the end
                    lefts = 1  # Lefts
                    rights = 0  # Rights
                    startIndex = index + 1

                    while lefts != rights and index < len(expression):
                        index += 1
                        lefts += expression[index] == "("
                        rights += expression[index] == ")"

                    # Lefts and rights are balanced, evaluate what's inside
                    insideParen = expression[startIndex:index]
                    prevValue = part2(insideParen)

                elif char == "*":
                    break

                elif char == "+":
                    summands.append(int(prevValue))
                    prevValue = ""

                index += 1

            if index == len(expression):
                lastIsAddition = True

            if prevValue != "":
                summands.append(int(prevValue))

            # print("summands:", summands)
            multiplicands.append(sum(summands))
            prevValue = ""

        elif char == "*":
            multiplicands.append(int(prevValue))
            prevValue = ""

        elif char == "(":
            # Balance the parentheses to get to the end
            lefts = 1  # Lefts
            rights = 0  # Rights
            startIndex = index + 1

            while lefts != rights and index < len(expression):
                index += 1
                lefts += expression[index] == "("
                rights += expression[index] == ")"

            # Lefts and rights are balanced, evaluate what's inside
            insideParen = expression[startIndex:index]
            # print("inside:", insideParentheses)
            prevValue = part2(insideParen)

        index += 1

    # Get the last multiplicand
    if prevValue != "" and not lastIsAddition:
        multiplicands.append(int(prevValue))

    # print(multiplicands)
    product = 1
    for i in multiplicands:
        product *= i

    return product

p1answer = 0
p2answer = 0
for expression in data.split("\n"):
    expression = expression.replace(" ", "")
    p1answer += part1(expression)
    p2answer += part2(expression)

print("Part 1:", p1answer)
print("Part 2:", p2answer)
# 70722650566361