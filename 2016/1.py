directions = open("input.txt").read().strip().split(", ")

x = 0
y = 0
facing = "N"
turns = { "N" : { "R" : "E", "L" : "W" }, "S" : { "R" : "W", "L" : "E" }, "E" : { "R" : "S", "L" : "N" }, "W" : { "R" : "N", "L" : "S" }}
for d in directions:
    facing = turns[facing][d[0]]
    mag = int(d[1:])
    if facing == "E":
        x += mag
    elif facing == "W":
        x -= mag
    elif facing == "N":
        y += mag
    elif facing == "S":
        y -= mag

print(abs(x) + abs(y))

x = 0
y = 0
visited_locs = {(0, 0)}
facing = "N"
turns = { "N" : { "R" : "E", "L" : "W" }, "S" : { "R" : "W", "L" : "E" }, "E" : { "R" : "S", "L" : "N" }, "W" : { "R" : "N", "L" : "S" }}
done = False
for d in directions:
    if done:
        break
    facing = turns[facing][d[0]]
    mag = int(d[1:])
    while mag > 0:
        if facing == "E":
            x += 1
        elif facing == "W":
            x -= 1
        elif facing == "N":
            y += 1
        elif facing == "S":
            y -= 1
        mag -= 1
        if (x, y) in visited_locs:
            print(abs(x) + abs(y))
            done = True
            break
        else:
            visited_locs.add((x, y))
