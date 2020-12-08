def part1(instructions): 
    visited = set()
    next_line = 0
    accumulator = 0
    loops = True
    while not next_line in visited:
        if next_line >= len(instructions):
            loops = False
            break
        visited.add(next_line)
        this_instruction = instructions[next_line]
        if this_instruction[0:3] == "jmp":
            next_line += int(this_instruction[4:])
        else:
            next_line += 1
            if this_instruction[0:3] == "acc":
                accumulator += int(this_instruction[4:])
    return loops, accumulator

with open("./input.txt") as f:
    instructions = f.readlines()
    print(part1(instructions)[1])

    for i, op in enumerate(instructions):
        if "acc" in op:
            continue
        elif "nop" in op:
            instructions[i] = op.replace("nop", "jmp")
        else:
            instructions[i] = op.replace("jmp", "nop")
        loops, val = part1(instructions)
        if not loops:
            print(val)
            break
        else:
            instructions[i] = op
