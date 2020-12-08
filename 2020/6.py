s = 0
with open("./input.txt") as f:
    group = set()
    first = True
    for line in f:
        if line != "\n" and line != "":
            if first:
                first = False
                [group.add(c) for c in line if c != "\n"]
            else:
                newgroup = set([c for c in group if c in line])
                group = newgroup
        else:
            first = True
            s += len(group)
            group = set()

    print(s + len(group))
