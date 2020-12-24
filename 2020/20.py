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
        neighbor_exists = [neighbor is not None for neighbor in [self.top, self.bottom, self.left, self.right]]
        if all(neighbor_exists):
            raise Exception("This tile,", str(self.id) + ",", "already has four neighbors; cannot attach tile", str(other_tile.id))
        my_edges = self.Edges(False)
        other_edges = other_tile.Edges()
        my_edge = [i for i, val in enumerate(my_edges) if val in other_edges]
        if len(my_edge) != 1:
            raise Exception("This tile,", str(self.id) + ",", "has", str(my_edge), "matching edges with tile", str(other_tile.id))
        other_edge = [i for i, val in enumerate(other_edges) if val in my_edges]
        my_edge = my_edge[0]
        other_edge = other_edge[0]
        if neighbor_exists[my_edge]:
            raise Exception("Tile", str(self.id), "matches tile", str(other_tile.id), "on an edge that already has a neighbor.")
        case = my_edge + 4 * other_edge
        if case in [0, 5, 27, 30]:
            other_tile.Flip_Vertical()
        elif case in [8, 13, 19, 22]:
            for i in range(3):
                other_tile.Rotate_CW()
        elif case in [3, 6, 9, 12]:
            other_tile.Flip_Vertical()
            other_tile.Rotate_CW()
        elif case in [16, 21, 26, 31]:
            for i in range(2):
                other_tile.Rotate_CW()
        elif case in [10, 15, 17, 20]:
            other_tile.Flip_Vertical()
            for i in range(2):
                other_tile.Rotate_CW()
        elif case in [18, 23, 24, 29]:
            other_tile.Rotate_CW()
            other_tile.Flip_Vertical()
        elif case in [2, 6, 7, 25]:
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

frontier = []
for neighbor_id in top_left.Find_Neighbors(neighbors):
    top_left.Rotate_And_Attach(tile_by_id[neighbor_id])
    frontier.append(tile_by_id[neighbor_id])
