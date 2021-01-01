instructions = open("input.txt").readlines()
current_instruction = 0
a = 1 # change this to 0 for part 1, 1 for part 2
b = 0
while 0 <= current_instruction < len(instructions):
    instr = instructions[current_instruction].split(" ")
    if instr[0] == "hlf":
        if instr[1].strip() == "a":
            a /= 2
        else:
            b /= 2
        current_instruction += 1
    elif instr[0] == "tpl":
        if instr[1].strip() == "a":
            a *= 3
        else:
            b *= 3
        current_instruction += 1
    elif instr[0] == "inc":
        if instr[1].strip() == "a":
            a += 1
        else:
            b += 1
        current_instruction += 1
    elif instr[0] == "jmp":
        if instr[1][0] == "+":
            current_instruction += int(instr[1][1:].strip())
        else:
            current_instruction -= int(instr[1][1:].strip())
    elif instr[0] == "jie":
        if instr[1][0] == "a" and a % 2 == 0:
            if instr[2][0] == "+":
                current_instruction += int(instr[2][1:].strip())
            else:
                current_instruction -= int(instr[2][1:].strip())
        elif instr[1][0] == "b" and b % 2 == 0:
            if instr[2][0] == "+":
                current_instruction += int(instr[2][1:].strip())
            else:
                current_instruction -= int(instr[2][1:].strip())
        else:
            current_instruction += 1
    else:
        if instr[1][0] == "a" and a == 1:
            if instr[2][0] == "+":
                current_instruction += int(instr[2][1:].strip())
            else:
                current_instruction -= int(instr[2][1:].strip())
        elif instr[1][0] == "b" and b == 1:
            if instr[2][0] == "+":
                current_instruction += int(instr[2][1:].strip())
            else:
                current_instruction -= int(instr[2][1:].strip())
        else:
            current_instruction += 1

print(b)
