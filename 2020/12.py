actions = open("input.txt").readlines()

turn = {"E" : { "L" : "N", "R" : "S"},
        "N" : { "L" : "W", "R" : "E"},
        "W" : { "L" : "S", "R" : "N"},
        "S" : { "L" : "E", "R" : "W"}}

current_direction = "E"
current_x = 0
current_y = 0

for action in actions:
    a = action[0]
    m = int(action[1:])
    if a == "F":
        a = current_direction
    if a == "E":
        current_x += m
    elif a == "W":
        current_x -= m
    elif a == "S":
        current_y -= m
    elif a == "N":
        current_y += m
    else:
        while m > 0:
            current_direction = turn[current_direction][a]
            m -= 90

print(abs(current_x)+abs(current_y))

def rotate_left(waypt):
    return -1 * waypt[1], waypt[0]

def rotate_right(waypt):
    return waypt[1], -1 * waypt[0]

ship_x = 0
ship_y = 0
waypt_x = 10
waypt_y = 1

for action in actions:
    a = action[0]
    m = int(action[1:])
    if a == "N":
        waypt_y += m
    elif a == "S":
        waypt_y -= m
    elif a == "W":
        waypt_x -= m
    elif a == "E":
        waypt_x += m
    elif a == "L":
        while m > 0:
            waypt_x, waypt_y = rotate_left([waypt_x, waypt_y])
            m -= 90
    elif a == "R":
        while m > 0:
            waypt_x, waypt_y = rotate_right([waypt_x, waypt_y])
            m -= 90
    elif a == "F":
        ship_x += m * waypt_x
        ship_y += m * waypt_y

print(abs(ship_x) + abs(ship_y))
