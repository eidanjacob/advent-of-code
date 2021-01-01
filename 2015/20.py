present_n = 29000000

houses = [0 for i in (range(int(present_n/10) + 1))]
for elf in range(1, len(houses)+1):
    for i in range(elf, len(houses), elf):
        houses[i] += elf * 10

satisfies = [house > present_n for house in houses]
print(satisfies.index(True))

houses = [0 for i in (range(int(present_n/10) + 1))]
for elf in range(1, len(houses)+1):
    for i in range(elf, min(len(houses), 51*elf), elf):
        houses[i] += elf * 11

satisfies = [house > present_n for house in houses]
print(satisfies.index(True))