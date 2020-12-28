utility = open("input.txt").readlines()
pairs_utils = dict()
for u in utility:
    u_split = u.strip("\n.").split(" ")
    first_person = u_split[0]
    happy = int(u_split[3])
    happy *= -1 if u_split[2] == "lose" else 1
    second_person = u_split[-1]
    pairs_utils[(first_person, second_person)] = happy

people = sorted(list(set([pair[0] for pair in pairs_utils.keys()])))
def get_max_utility():
    max_utility = -1e10
    import itertools
    for arrangement in itertools.permutations(people):
        arr = list(arrangement)
        arr += [arr[0]]
        utility = 0
        for i in range(len(arrangement)):
            utility += pairs_utils[(arr[i], arr[i+1])] + pairs_utils[(arr[i + 1], arr[i])]
        max_utility = utility if utility > max_utility else max_utility
    print(max_utility)

get_max_utility()

for person in people:
    pairs_utils[("me", person)] = 0
    pairs_utils[(person, "me")] = 0
people.append("me")

get_max_utility()