class Tile:

    def __init__(self, tile_id, image):
        self.id = tile_id
        self.image = image
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def Edges(self, flip = True):
        top = self.image[0:10]
        bottom = self.image[-10:]
        left = "".join([self.image[i] for i in range(0, 100, 10)])
        right = "".join([self.image[i] for i in range(9, 100, 10)])
        return [top, bottom, left, right, top[::-1], bottom[::-1], left[::-1], right[::-1]] if flip else [top, bottom, left, right]

    def Find_Neighbors(self, match_set):
        return [pair[1] for pair in match_set if pair[0] == self.id]

    def Rotate_CW(self):
        if any([neighbor is not None for neighbor in [self.top, self.bottom, self.right, self.left]]):
            raise Exception("Rotating a tile already in image.")
        self.image = "".join(["".join([self.image[x + 10 * y] for y in reversed(range(10))]) for x in range(10)])

    def Flip_Vertical(self):
        if any([neighbor is not None for neighbor in [self.top, self.bottom, self.right, self.left]]):
            raise Exception("Flipping a tile already in image.")
        temp = self.top
        self.top = self.bottom
        self.bottom = self.top
        self.image = "".join([self.image[y:(y+10)] for y in reversed(range(0, 100, 10))])

    def Rotate_And_Attach(self, other_tile):
        #print(self.id, other_tile.id)
        neighbor_exists = [neighbor is not None for neighbor in [self.top, self.bottom, self.left, self.right]]
        #if all(neighbor_exists):
        #    raise Exception("This tile,", str(self.id) + ",", "already has four neighbors; cannot attach tile", str(other_tile.id))
        my_edges = self.Edges(False)
        other_edges = other_tile.Edges()
        my_edge = [i for i, val in enumerate(my_edges) if val in other_edges]
        if len(my_edge) != 1:
            raise Exception("This tile,", str(self.id) + ",", "has", str(my_edge), "matching edges with tile", str(other_tile.id))
        other_edge = [i for i, val in enumerate(other_edges) if val in my_edges]
        #print(self.id, my_edge, other_tile.id, other_edge)
        my_edge = my_edge[0]
        other_edge = other_edge[0]
        case = my_edge + 4 * other_edge
        #print(my_edges[my_edge] == other_edges[other_edge])
        #for i in range(10):
        #    print(self.image[(i*10):(10+i*10)], other_tile.image[(i*10):(10+i*10)])
        if case in [0, 5, 27, 30]:
            #print("flipping vertically")
            other_tile.Flip_Vertical()
        elif case in [8, 13, 19, 22]:
            #print("rotating ccw")
            for i in range(3):
                other_tile.Rotate_CW()
        elif case in [3, 6, 9, 12]:
            #print("flipping and rotating cw")
            other_tile.Flip_Vertical()
            other_tile.Rotate_CW()
        elif case in [16, 21, 26, 31]:
            #print("rotating 180")
            for i in range(2):
                other_tile.Rotate_CW()
        elif case in [10, 15, 17, 20]:
            #print("flipping and rotating 180")
            other_tile.Flip_Vertical()
            for i in range(2):
                other_tile.Rotate_CW()
        elif case in [18, 23, 24, 29]:
            #print("rotating cw and flipping")
            other_tile.Rotate_CW()
            other_tile.Flip_Vertical()
        elif case in [2, 7, 25, 28]:
            #print("rotating cw")
            other_tile.Rotate_CW()
        if my_edge == 0:
            self.top = other_tile
            other_tile.bottom = self
        elif my_edge == 1:
            self.bottom = other_tile
            other_tile.top = self
        elif my_edge == 2:
            self.left = other_tile
            other_tile.left = self
        else:
            self.right = other_tile
            other_tile.left = self
        #input()
        return True

lbld_tiles = open("input.txt").read().split("\n\n")[:-1]

tile_by_id = dict()
        
for raw_tile in lbld_tiles:
    label, image = raw_tile.split(":\n")
    tile = Tile(label, image.replace("\n", ""))
    tile_by_id[label] = tile

neighbors = set()
nonneighbors = set()

def determine_if_neighbor(tile_1_id, tile_2_id, match_set, nonmatch_set):
    if tile_1_id == tile_2_id:
        return False
    if (tile_1_id, tile_2_id) in match_set.union(nonmatch_set):
        return (tile_1_id, tile_2_id) in match_set
    tile_1_edges = tile_by_id[tile_1_id].Edges()
    tile_2_edges = tile_by_id[tile_2_id].Edges()
    if any([edge in tile_2_edges for edge in tile_1_edges]):
        match_set.add((tile_1_id, tile_2_id))
        match_set.add((tile_2_id, tile_1_id))
        return True
    else:
        nonmatch_set.add((tile_1_id, tile_2_id))
        nonmatch_set.add((tile_2_id, tile_1_id))
        return False

for tile1 in tile_by_id.keys():
    for tile2 in tile_by_id.keys():
        determine_if_neighbor(tile1, tile2, neighbors, nonneighbors)

n_neighbors = {tile_id : sum([tile_id == pair[0] for pair in neighbors]) for tile_id in tile_by_id.keys()}
corner_tiles = [key for key, value in n_neighbors.items() if value == 2]
prod = 1
for c in corner_tiles:
    prod *= int(c.split(" ")[1])
print(prod)

top_left = tile_by_id[corner_tiles[0]]
for i in range(3):
    top_left.Rotate_CW()

frontier = [top_left]
added = set([top_left])

def image_with_edges(tl_tile):
    total_image = "\n"
    left_tile = tl_tile
    current_tile = left_tile
    while left_tile is not None:
        for i in range(10):
            image_row = ""
            while current_tile is not None:
                image_row += current_tile.image[(i*10):(10+i*10)] + " "
                current_tile = current_tile.right
            current_tile = left_tile
            total_image += image_row + "\n"
        left_tile = left_tile.bottom
        current_tile = left_tile
        total_image += "\n"
    return total_image

while len(added) < 144:
    tile = frontier.pop()
    for neighbor_id in tile.Find_Neighbors(neighbors):
        neighbor_tile = tile_by_id[neighbor_id]
        tile.Rotate_And_Attach(neighbor_tile)
        if neighbor_tile not in added:
            frontier.append(neighbor_tile)
        added.add(tile)

n_neighbors = {tile_id : sum([tile_id == pair[0] for pair in neighbors]) for tile_id in tile_by_id.keys()}

'''
    if tile.top is not None:
        for i in range(10):
            print(" " * 11 + tile.top.image[(i*10):(10+i*10)])
        print("")
    for i in range(10):
        row = ""
        if tile.left is None:
            row += " " * 11
        else:
            row += tile.left.image[(i*10):(10+i*10)] + " "
        row += tile.image[(i*10):(10+i*10)] + " "
        if tile.right is not None:
            row += tile.right.image[(i*10):(10+i*10)]
        print(row)
    if tile.bottom is not None:
        print("")
        for i in range(10):
            print(" " * 11 + tile.bottom.image[(i*10):(10+i*10)])
    #input()
'''

def image_no_edge(tl_tile):
    total_image = ""
    left_tile = tl_tile
    current_tile = left_tile
    while left_tile is not None:
        for i in range(1,9):
            image_row = ""
            while current_tile is not None:
                image_row += current_tile.image[(i*10+1):(9+i*10)]
                current_tile = current_tile.right
            current_tile = left_tile
            total_image += image_row + "\n"
        left_tile = left_tile.bottom
        current_tile = left_tile
    return total_image

row_1 = "                  # "
row_2 = "#    ##    ##    ###"
row_3 = " #  #  #  #  #  #   "
indices = [[i for i, char in enumerate(row) if char == "#"] for row in [row_1, row_2, row_3]]

def find_sea_monsters(image):
    n_monsters = 0
    image_rows = image.split("\n")
    for i in range(12 * 8 - 3):
        for j in range(12 * 8 - len(row_1)):
            n_monsters += int(all([all([all([char == "#" for char in image_rows[i + row][j + index]]) for index in indices[row]]) for row in range(3)]))
    return n_monsters

comp_image = image_no_edge(top_left)
n_pound = sum([char == "#" for char in comp_image])
roughness = []
for i in range(4):
    roughness.append(n_pound - 15 * find_sea_monsters(comp_image))
    comp_image = "\n".join(comp_image.split("\n")[(12*8-1)::-1])
    roughness.append(n_pound - 15 * find_sea_monsters(comp_image))
    comp_image = "\n".join(comp_image.split("\n")[(12*8-1)::-1])
    comp_image = "".join(["".join([comp_image[x + (8 * 12 + 1) * y] for y in reversed(range(12 * 8))]) for x in range(12 * 8)])
    comp_image = "\n".join([comp_image[(8 * 12 * i):((8 * 12) * (i + 1))] for i in range(12*8)])

print(min(roughness))
