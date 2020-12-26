class Cup:
    def __init__(self, val, right = None):
        self.value = val
        self.right = right

start = "327465189"
current = Cup(int(start[0]))
prev = current
value_to_cup = { 3 : current }
for x in start[1:]:
    new_cup = Cup(int(x), current)
    value_to_cup[int(x)] = new_cup
    prev.right = new_cup
    prev = new_cup

for i in range(100):
    removed_head = current.right
    removed_vals = [removed_head.value, removed_head.right.value, removed_head.right.right.value]
    current.right = current.right.right.right.right
    destination_label = current.value - 1
    if destination_label == 0:
        destination_label = 9
    while destination_label in removed_vals:
        destination_label -= 1
        if destination_label == 0:
            destination_label = 9
    destination_cup = value_to_cup[destination_label]
    removed_head.right.right.right = destination_cup.right
    destination_cup.right = removed_head
    current = current.right
    

current = value_to_cup[1]
part1 = ""
for i in range(8):
    current = current.right
    part1 += str(current.value)
print(part1)

current = Cup(int(start[0]))
prev = current
value_to_cup = { current.value : current }
for x in start[1:]:
    new_cup = Cup(int(x), current)
    value_to_cup[int(x)] = new_cup
    prev.right = new_cup
    prev = new_cup
for x in range(10, 1000000+1):
    new_cup = Cup(x, current)
    value_to_cup[x] = new_cup
    prev.right = new_cup
    prev = new_cup
    
for i in range(10000000):
    removed_head = current.right
    removed_vals = [removed_head.value, removed_head.right.value, removed_head.right.right.value]
    current.right = current.right.right.right.right
    destination_label = current.value - 1
    if destination_label == 0:
        destination_label = 1e6
    while destination_label in removed_vals:
        destination_label -= 1
        if destination_label == 0:
            destination_label = 1e6
    destination_cup = value_to_cup[destination_label]
    removed_head.right.right.right = destination_cup.right
    destination_cup.right = removed_head
    current = current.right
    
part2 = value_to_cup[1].right.value * value_to_cup[1].right.right.value
print(str(part2))
