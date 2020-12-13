notes = open("input.txt").readlines()
earliest_depart = int(notes[0])
ids_in_service = [int(x) for x in notes[1].replace("\n", "").split(",") if x.isnumeric()]
found = False
depart_time = earliest_depart
while not found:
    for bus in ids_in_service:
        if depart_time % bus == 0:
            print(bus * (depart_time - earliest_depart))
            found = True
            break
    depart_time += 1
    
modulo_conditions = dict()
bus_ids = notes[1].replace("\n", "").split(",")
for index, bus_id in enumerate(bus_ids):
    if bus_id.isnumeric():
        modulo_conditions[int(bus_id)] = index

print(modulo_conditions)
sorted_ids = list(modulo_conditions.keys())
sorted_ids.sort()
t = max(sorted_ids) - modulo_conditions[max(sorted_ids)]
increment = max(sorted_ids)

# i just used wolfram alpha for part 2 lol
