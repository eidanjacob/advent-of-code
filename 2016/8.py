ops = [o.strip() for o in open("input.txt").readlines()]

grid = [[False for i in range(50)] for j in range(6)]

for op in ops:
    operation = op.split(" ")
    if operation[0] == "rect":
        width, height = [int(n) for n in operation[1].split("x")]
        for x in range(width):
            for y in range(height):
                grid[y][x] = True
    elif operation[1] == "row":
        row = int(operation[2].split("=")[1])
        pix = int(operation[-1])
        new_row = [grid[row][(i-pix) % 50] for i in range(50)]
        grid[row] = new_row
    else:
        col = int(operation[2].split("=")[1])
        pix = int(operation[-1])
        new_col = [grid[(i - pix) % 6][col] for i in range(6)]
        for i in range(6):
            grid[i][col] = new_col[i]
    '''
    print(op)
    print("\n".join([" ".join(["*" if b else "." for b in g]) for g in grid]))
    input()
    '''
print(sum([sum([int(b) for b in g]) for g in grid]))
print("\n".join([" ".join(["*" if b else " " for b in g]) for g in grid]))