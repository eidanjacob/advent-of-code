sues = open("input.txt").readlines()
sues_dict = dict()
for sue in sues:
    sue_info = sue.replace(",", ":").split(": ")
    sues_dict[sue_info[0]] = {sue_info[i] : int(sue_info[i+1]) for i in range(1, len(sue_info)-1, 2)}

my_sue = {"children" : 3, "cats" : 7, "samoyeds" : 2, "pomeranians" : 3, "akitas" : 0, "vizslas" : 0, "goldfish" : 5, "trees" : 3, "cars" : 2, "perfumes" : 1}
for key, value in sues_dict.items():
    if all(value[search_key] == search_value for search_key, search_value in my_sue.items() if search_key in value.keys()):
        print(key)

[my_sue.pop(x) for x in ["cats", "trees", "pomeranians", "goldfish"]]
my_sue_gt = {"cats" : 7, "trees" : 3}
my_sue_lt = {"pomeranians" : 3, "goldfish" : 5}
for key, value in sues_dict.items():
    if all([value[search_key] == search_value for search_key, search_value in my_sue.items() if search_key in value.keys()]) \
    and all([value[search_key] > search_value for search_key, search_value in my_sue_gt.items() if search_key in value.keys()]) \
    and all([value[search_key] < search_value for search_key, search_value in my_sue_lt.items() if search_key in value.keys()]):
        print(key)