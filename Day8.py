import copy

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'

def bootCode(instructions: list) -> [bool, int]:
    accumulator = 0
    visited = [False for _ in instructions]
    ix = 0
    while (0 <= ix < len(instructions)) and (not visited[ix]):
        visited[ix] = True
        operation, arg = instructions[ix]
        if operation == ACC:
            accumulator += arg
            ix += 1
        elif operation == JMP:
            ix += arg
        elif operation == NOP:
            ix += 1

    is_terminated = ix == len(instructions)
    return is_terminated, accumulator


def part1(instructions):
    blank, accumulator = bootCode(instructions)
    return accumulator

def part2(instructions):
    for ix, instruction in enumerate(instructions):
        operation, arg = instruction
        if operation in (NOP, JMP):
            instructions_copy = copy.deepcopy(instructions)
            instructions_copy[ix][0] = JMP if operation == NOP else NOP

            is_terminated, accumulator = bootCode(instructions_copy)
            if is_terminated:
                return accumulator
    return 0


def extract_data(lines: list) -> list:
    instructions = []
    for line in lines:
        operation, arg = line.split(' ')
        instructions.append([operation, int(arg)])

    return instructions


with open('day08.input') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    #print(extract_data(inputs))
    print("Part 1:", part1(extract_data(inputs)))
    print("Part 2:", part2(extract_data(inputs)))