light_grid = open("input.txt").readlines()

def neighbors(x, y):
    on_neighbors = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx == 0 and dy == 0) or (x + dx < 0) or (x + dx > 99) or (y + dy < 0) or (y + dy > 99):
                continue
            on_neighbors += int(light_grid[x+dx][y+dy] == "#")
    return on_neighbors

def get_state(x, y):
    on_neighbors = neighbors(x, y)
    return on_neighbors in [2, 3] if light_grid[x][y] == "#" else on_neighbors == 3

n_steps = 100
for _ in range(n_steps):
    next_grid = [["#" if get_state(x, y) else "." for y in range(100)] for x in range(100)]
    light_grid = next_grid

print(sum([sum([x == "#" for x in light_grid_row]) for light_grid_row in light_grid]))

def is_corner(x,y):
    return True if (x,y) in [(0, 0), (0, 99), (99, 0), (99, 99)] else False

light_grid = open("input.txt").readlines()
for _ in range(n_steps):
    next_grid = [["#" if get_state(x, y) or is_corner(x, y) else "." for y in range(100)] for x in range(100)]
    light_grid = next_grid
print(sum([sum([x == "#" for x in light_grid_row]) for light_grid_row in light_grid]))
