def get_neighbors(x, y, z):
    neighbors = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                neighbors.add((x+i, y+j, z+k))
    neighbors.remove((x, y, z))
    return neighbors


active = set()
neighbors = set()
next_active = set()
next_neighbors = set()

with open("input.txt") as f:
    for y, row in enumerate(f.readlines()):
        for x, col in enumerate(row):
            if col == "#":
                active.add((x, y, 0))
                for neighbor in get_neighbors(x, y, 0):
                    neighbors.add(neighbor)

neighbors = neighbors - active

for i in range(6):
    for cell in active:
        cell_neighbors = get_neighbors(*cell)
        living_neighbors = sum([1 for cell_neighbor in cell_neighbors if cell_neighbor in active])
        if living_neighbors == 2 or living_neighbors == 3:
            next_active.add(cell)
    for cell in neighbors:
        cell_neighbors = get_neighbors(*cell)
        living_neighbors = sum([1 for cell_neighbor in cell_neighbors if cell_neighbor in active])
        if living_neighbors == 3:
            next_active.add(cell)
            
    for cell in next_active:
        next_neighbors = next_neighbors.union(get_neighbors(*cell))
    next_neighbors = next_neighbors - next_active

    active = next_active
    next_active = set()
    neighbors = next_neighbors
    next_neighbors = set()

print(len(active))

def get_neighbors(x, y, z, w):
    neighbors = set()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    neighbors.add((x+i, y+j, z+k, w+l))
    neighbors.remove((x, y, z, w))
    return neighbors


active = set()
neighbors = set()
next_active = set()
next_neighbors = set()

with open("input.txt") as f:
    for y, row in enumerate(f.readlines()):
        for x, col in enumerate(row):
            if col == "#":
                active.add((x, y, 0, 0))
                for neighbor in get_neighbors(x, y, 0, 0):
                    neighbors.add(neighbor)

neighbors = neighbors - active

for i in range(6):
    for cell in active:
        cell_neighbors = get_neighbors(*cell)
        living_neighbors = sum([1 for cell_neighbor in cell_neighbors if cell_neighbor in active])
        if living_neighbors == 2 or living_neighbors == 3:
            next_active.add(cell)
    for cell in neighbors:
        cell_neighbors = get_neighbors(*cell)
        living_neighbors = sum([1 for cell_neighbor in cell_neighbors if cell_neighbor in active])
        if living_neighbors == 3:
            next_active.add(cell)
            
    for cell in next_active:
        next_neighbors = next_neighbors.union(get_neighbors(*cell))
    next_neighbors = next_neighbors - next_active

    active = next_active
    next_active = set()
    neighbors = next_neighbors
    next_neighbors = set()

print(len(active))
