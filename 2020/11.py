seats = open("input.txt").readlines()

def count_adj_occ(row, col, seating):
    adj_occ = 0
    adj_occ += 0 if col == 0 else int(seating[row][col-1] == "#")
    adj_occ += 0 if col == (len(seating[0])-1) else int(seating[row][col+1] == "#")
    adj_occ += 0 if row == 0 else int(seating[row-1][col] == "#")
    adj_occ += 0 if row == (len(seating)-1) else int(seating[row+1][col] == "#")

    adj_occ += 0 if col == 0 or row == 0 else int(seating[row-1][col-1] == "#")
    adj_occ += 0 if col == (len(seating[0])-1) or row == (len(seating)-1) else int(seating[row+1][col+1] == "#")
    adj_occ += 0 if row == 0 or col == (len(seating[0])-1) else int(seating[row-1][col+1] == "#")
    adj_occ += 0 if row == (len(seating)-1) or col == 0 else int(seating[row+1][col-1] == "#")
    return adj_occ

old_seats = [row.replace("\n", '') for row in seats]

while True:
    new_seats = [["." if old_seats[i][j] == "." else
                  "L" if (old_seats[i][j] == "#" and count_adj_occ(i, j, old_seats) >= 4) else
                  "#" if (old_seats[i][j] == "L" and count_adj_occ(i, j, old_seats) == 0) else
                  old_seats[i][j] for j in range(len(old_seats[0]))] for i in range(len(old_seats))]
    if old_seats == new_seats:
        break
    old_seats = new_seats

print(sum([sum([1 for seat in row if seat == "#"]) for row in old_seats]))

def north(row, col, seating):
    if row == 0:
        return 0
    elif seating[row-1][col] == ".":
        return north(row-1, col, seating)
    elif seating[row-1][col] == "#":
        return 1
    else:
        return 0
    
def south(row, col, seating):
    if row == len(seating)-1:
        return 0
    elif seating[row+1][col] == ".":
        return south(row+1, col, seating)
    elif seating[row+1][col] == "#":
        return 1
    else:
        return 0

def west(row, col, seating):
    if col == 0:
        return 0
    elif seating[row][col-1] == ".":
        return west(row, col-1, seating)
    elif seating[row][col-1] == "#":
        return 1
    else:
        return 0
    
def east(row, col, seating):
    if col == len(seating[0])-1:
        return 0
    elif seating[row][col+1] == ".":
        return east(row, col+1, seating)
    elif seating[row][col+1] == "#":
        return 1
    else:
        return 0

def northwest(row, col, seating):
    if row == 0 or col == 0:
        return 0
    elif seating[row-1][col-1] == ".":
        return northwest(row-1, col-1, seating)
    elif seating[row-1][col-1] == "#":
        return 1
    else:
        return 0

def northeast(row, col, seating):
    if row == 0 or col == len(seating[0])-1:
        return 0
    elif seating[row-1][col+1] == ".":
        return northeast(row-1, col+1, seating)
    elif seating[row-1][col+1] == "#":
        return 1
    else:
        return 0
    
def southeast(row, col, seating):
    if row == len(seating)-1 or col == len(seating[0])-1:
        return 0
    elif seating[row+1][col+1] == ".":
        return southeast(row+1, col+1, seating)
    elif seating[row+1][col+1] == "#":
        return 1
    else:
        return 0
    
def southwest(row, col, seating):
    if row == len(seating)-1 or col == 0:
        return 0
    elif seating[row+1][col-1] == ".":
        return southwest(row+1, col-1, seating)
    elif seating[row+1][col-1] == "#":
        return 1
    else:
        return 0

def count_occ_vis(row, col, seating):
    return east(row, col, seating) + west(row, col, seating) + north(row, col, seating) + south(row, col, seating) + \
northeast(row, col, seating) + northwest(row, col, seating) + southeast(row, col, seating) + southwest(row, col, seating)

old_seats = [row.replace("\n", '') for row in seats]

while True:
    new_seats = [["." if old_seats[i][j] == "." else
                  "L" if (old_seats[i][j] == "#" and count_occ_vis(i, j, old_seats) >= 5) else
                  "#" if (old_seats[i][j] == "L" and count_occ_vis(i, j, old_seats) == 0) else
                  old_seats[i][j] for j in range(len(old_seats[0]))] for i in range(len(old_seats))]
    if old_seats == new_seats:
        break
    old_seats = new_seats

print(sum([sum([1 for seat in row if seat == "#"]) for row in old_seats]))
