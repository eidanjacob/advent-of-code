reqs = dict()
with open("./input.txt") as f:
    for line in f:
        s = line.replace(".", "").replace(",","").replace("bags", "bag")
        contain_split = s.split("contain")
        containing_bag = contain_split[0][:-5]
        contained_bags = dict()
        contained = contain_split[1]
        while contained != "\n" and contained != " no other bag\n":
            n = int(contained[1])
            contained = contained[2:]
            digits_index = [x.isdigit() for x in contained]
            next_num = len(contained) if not any(digits_index) else digits_index.index(True)
            contained_bags[contained[1:(next_num-5)]] = n
            contained = contained[next_num-1:]
        reqs[containing_bag] = contained_bags

can_contain_gold = dict()

def can_contain_shiny_gold(bag):
    if bag in can_contain_gold.keys():
        return can_contain_gold[bag]
    else:
        contained_bags_contain_shiny_gold = any([contained_bag == "shiny gold" or can_contain_shiny_gold(contained_bag) for contained_bag in reqs[bag].keys()])
        can_contain_gold[bag] = contained_bags_contain_shiny_gold
        return contained_bags_contain_shiny_gold

print(sum([int(can_contain_shiny_gold(bag)) for bag in reqs.keys()]))

def bags_inside(bag):
    contents = reqs[bag]
    if len(contents.keys()) == 0:
        return 1
    else:
        return 1 + sum([value * bags_inside(key) for key, value in contents.items()])

print(bags_inside("shiny gold"))
