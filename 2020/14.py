program = open("input.txt").readlines()
memory = dict()
mask = ""

for command in program:
    if "mask" in command:
        mask = command[7:].replace("\n", "")
    else:
        address = command.split("[")[1].split("]")[0]
        value = str(format(int(command.split(" ")[-1]), "036b"))
        masked = "".join([v if mask[i] == "X" else mask[i] for i, v in enumerate(value)])
        memory[address] = masked 

print(sum([int(x, 2) for x in memory.values()]))

memory = dict()
mask = ""
n_x = 0

for command in program:
    if "mask" in command:
        mask = command[7:].replace("\n", "")
    else:
        address = str(format(int(command.split("[")[1].split("]")[0]), "036b"))
        value = int(command.split(" ")[-1])
        addresses = set("0")
        for index, bit in enumerate(mask):
            if bit == "1":
                new_addresses = {addr + "1" for addr in addresses}
                addresses = new_addresses
            elif bit == "X":
                new_addresses = {addr + "0" for addr in addresses}.union({addr + "1" for addr in addresses})
                addresses = new_addresses
            else:
                new_addresses = {addr + address[index] for addr in addresses}
                addresses = new_addresses
        for addr in addresses:
            memory[addr] = value
            
print(sum(memory.values()))
