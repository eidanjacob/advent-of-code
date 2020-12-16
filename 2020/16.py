def read_input():
    with open("input.txt") as f:
        valid_values = dict()
        line = f.readline()
        while line != "\n":
            field_name = line.split(": ")[0]
            ranges = line.split(": ")[1].split(" or ")
            first_range = [int(n) for n in ranges[0].split("-")]
            second_range = [int(n) for n in ranges[1].split("-")]
            valid_values[field_name] = [first_range, second_range]
            line = f.readline()
        line = f.readline()
        ticket = f.readline().replace("\n", "").split(",")
        f.readlines(2)
        nearby_tickets = [ticket.replace("\n", "").split(",") for ticket in f.readlines()]

        return valid_values, ticket, nearby_tickets

valid_values, my_ticket, nearby_tickets = read_input()

sum_invalid_vals = 0
valid_tickets = []
for ticket in nearby_tickets:
    valid = True
    for num in ticket:
        n = int(num)
        if not any([any([value_range[0] <= n <= value_range[1] for value_range in item]) for item in valid_values.values()]):
            sum_invalid_vals += n
            valid = False
    if valid:
        valid_tickets.append(ticket)
print(sum_invalid_vals)

field_indices = {field : set() for field in valid_values.keys()}
for field, ranges in valid_values.items():
    for index in range(len(nearby_tickets[0])):
        possible_index = True
        for ticket in valid_tickets:
            if not any([value_range[0] <= int(ticket[index]) <= value_range[1] for value_range in ranges]):
                possible_index = False
                break
        if possible_index:
            field_indices[field].add(index)

candidates = [sum([1 for field, indices in field_indices.items() if i in indices]) for i in range(len(valid_tickets[0]))]
prod_departure_fields = 1
for i in range(len(valid_tickets[0])):
    field, index = [(field, indices) for field, indices in field_indices.items() if len(indices) == 1][0]
    index = index.pop()
    for other_set in field_indices.values():
        other_set.discard(index)
    if "departure" in field[0:10]:
        prod_departure_fields *= int(my_ticket[index])

print(prod_departure_fields)
