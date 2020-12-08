with open("./input.txt") as f:
    sqfoot = 0
    ribbon = 0
    while line:= f.readline():
        dims = line.split("x")
        [l, w, h] = [int(d) for d in dims]
        sqfoot += 2 * (l * w + l * h + w * h) + min([l*w, l*h, w*h])
        perims = [l+w, l+h, w+h]
        ribbon += 2 * min(perims) + l*w*h
    print(sqfoot, ribbon)
