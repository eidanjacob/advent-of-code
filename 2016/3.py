import itertools

triangles = [[int(x) for x in line.strip().split()] for line in open("input.txt").readlines()]

n_valid = 0
for triangle in triangles:
    n_valid += int(all([p[0] + p[1] > p[2] for p in itertools.permutations(triangle)]))

print(n_valid)

col_1, col_2, col_3 = list(), list(), list()
for l in open("input.txt").readlines():
    a, b, c = l.strip().split()
    col_1.append(int(a))
    col_2.append(int(b))
    col_3.append(int(c))

triangle_cols = [[col[i:(i+3)] for i in range(0, len(col), 3)] for col in [col_1, col_2, col_3]]
n_valid = 0
for triangles in triangle_cols:
    for triangle in triangles:
        n_valid += int(all([p[0] + p[1] > p[2] for p in itertools.permutations(triangle)]))

print(n_valid)