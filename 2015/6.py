directions = open("input.txt").readlines()
arr = [[False for y in range(1000)] for x in range(999)]
for direction in directions:
    if "turn off" in direction:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[2].split(",")]
        corner_2 = [int(n) for n in txt_removed[4].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = False
    elif "turn on" in direction:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[2].split(",")]
        corner_2 = [int(n) for n in txt_removed[4].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = True
    else:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[1].split(",")]
        corner_2 = [int(n) for n in txt_removed[3].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = not arr[x][y]

print(sum([sum(row) for row in arr]))

arr = [[0 for y in range(1000)] for x in range(999)]
for direction in directions:
    if "turn off" in direction:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[2].split(",")]
        corner_2 = [int(n) for n in txt_removed[4].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = max(0, arr[x][y] - 1)
    elif "turn on" in direction:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[2].split(",")]
        corner_2 = [int(n) for n in txt_removed[4].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = arr[x][y] + 1
    else:
        txt_removed = direction.split(" ")
        corner_1 = [int(n) for n in txt_removed[1].split(",")]
        corner_2 = [int(n) for n in txt_removed[3].split(",")]
        for x in range(corner_1[0], corner_2[0]+1):
            for y in range(corner_1[1], corner_2[1]+1):
                arr[x][y] = arr[x][y] + 2

print(sum([sum(row) for row in arr]))

