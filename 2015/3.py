changes = {"^" : [0, 1], ">": [1, 0], "<": [-1, 0], "v": [0, -1]}

with open("./input.txt") as f:
    houses = set()
    current_location = [0, 0]
    houses.add(" ".join([str(i) for i in current_location]))
    for direction in f.read():
        change = changes[direction]
        current_location = [current_location[i] + change[i] for i in range(2)]
        houses.add(" ".join([str(i) for i in current_location]))
    print(len(houses))


with open("./input.txt") as f:
    houses = set()
    current_location = [0, 0]
    robo_location = [0, 0]
    houses.add(" ".join([str(i) for i in current_location]))
    current_mover = "santa"
    for direction in f.read():
        change = changes[direction]
        if current_mover == "santa":
            current_location = [current_location[i] + change[i] for i in range(2)]
            houses.add(" ".join([str(i) for i in current_location]))
            current_mover = "robo"
        else:
            robo_location = [robo_location[i] + change[i] for i in range(2)]
            houses.add(" ".join([str(i) for i in robo_location]))
            current_mover = "santa"
    print(len(houses))
