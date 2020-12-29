vols = sorted([int(x.strip()) for x in open("input.txt").readlines()])

def n_combos(volumes, target):
    if target == 0:
        return 1
    if len(volumes) == 0:
        return 0
    if target < volumes[0]:
        return 0
    if target == volumes[0]:
        return 1
    return sum([n_combos(volumes[(i+1):], target-volumes[0]) for i in range(len(volumes))])

print(sum([n_combos(vols[i:], 150) for i in range(len(vols))]))

def n_min_combos(volumes, target, depth, known_min_depth = None):
    if known_min_depth is not None:
        if depth > known_min_depth:
            return 0, depth
    if target == 0:
        return 1, depth
    if len(volumes) == 0:
        return 0, depth
    if target < volumes[0]:
        return 0, depth
    if target == volumes[0]:
        return 1, depth
    total_combos = 0
    for i in range(len(volumes)):
        n_combo, best_depth = n_min_combos(volumes[(i+1):], target-volumes[0], depth + 1, known_min_depth)
        if known_min_depth is None or best_depth < known_min_depth and n_combo > 0:
            known_min_depth = best_depth
            total_combos = n_combo
        else:
            total_combos += n_combo
    return total_combos, known_min_depth

minimal_size = len(vols)
total_combos = 0
for i in range(len(vols)):
    n_combo, depth = n_min_combos(vols[i:], 150, 1, minimal_size)
    if depth < minimal_size and n_combo > 0:
        minimal_size = depth
        total_combos = n_combo
    else:
        total_combos += n_combo

print(total_combos, minimal_size)