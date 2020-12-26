black_tiles = set()
directions = open("input.txt").readlines()

for direction in directions:
    i = 0
    tile = (0, 0)
    while i < len(direction):
        if direction[i] == "s":
            i += 1
            if direction[i] == "e":
                tile = (tile[0] + 1, tile[1] - 1)
            else:
                tile = (tile[0] - 1, tile[1] - 1)
        elif direction[i] == "n":
            i += 1
            if direction[i] == "e":
                tile = (tile[0] + 1, tile[1] + 1)
            else:
                tile = (tile[0] - 1, tile[1] + 1)
        elif direction[i] == "w":
            tile = (tile[0] - 2, tile[1])
        elif direction[i] == "e":
            tile = (tile[0] + 2, tile[1])
        i += 1
    if tile in black_tiles:
        black_tiles.remove(tile)
    else:
        black_tiles.add(tile)

print(len(black_tiles))

for i in range(100):
    white_tiles = dict()
    tomorrow = set()
    for tile in black_tiles:
        n_black = 0
        x, y = tile
        neighbors = [(x + 1, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 2, y), (x - 2, y)]
        for neighbor in neighbors:
            if neighbor in black_tiles:
                n_black += 1
            else:
                if neighbor in white_tiles.keys():
                    white_tiles[neighbor] = white_tiles[neighbor] + 1
                else:
                    white_tiles[neighbor] = 1
        if n_black in [1, 2]:
            tomorrow.add(tile)
    for tile, n_black in white_tiles.items():
        if n_black == 2:
            tomorrow.add(tile)
    black_tiles = tomorrow

print(len(black_tiles))
