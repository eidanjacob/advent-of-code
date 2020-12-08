with open("./input.txt") as f:
    parens = f.read()
    print(sum([1 if c =="(" else -1 for c in parens]))
    floor = 0
    index = 0
    while floor >= 0:
        floor += (1 if parens[index] =="(" else -1)
        index += 1
    print(index)
