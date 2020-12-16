import itertools
distances = open("input.txt").readlines()

cities = set([distance.split(" ")[0] for distance in distances]).union(set([distance.split(" ")[2] for distance in distances]))

def get_distance(city1, city2):
    for distance in distances:
        if city1 in distance and city2 in distance:
            return int(distance.split(" ")[-1])

min_distance = float("inf")
max_distance = 0
for permutation in itertools.permutations(cities):
    distance = 0
    for i in range(len(permutation)-1):
        distance += get_distance(permutation[i], permutation[i+1])
    if distance < min_distance:
        min_distance = distance
    if distance > max_distance:
        max_distance = distance

print(min_distance, max_distance)
