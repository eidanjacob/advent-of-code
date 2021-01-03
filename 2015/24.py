import math
weights = [int(w.strip()) for w in open("input.txt").readlines()]
weights.reverse()
group_weight = sum(weights)/3

def find_group(available_weights, max_length, target_sum):
    if max_length == 0:
        return None
    best_group = None
    for i, w in enumerate(available_weights):
        if w < target_sum:
            sub_group = find_group(available_weights[(i + 1):], max_length - 1, target_sum - w)
            if sub_group is not None:
                sub_group.append(w)
                if best_group is None:
                    best_group = sub_group
                else:
                    if len(best_group) == len(sub_group):
                        best_group = best_group if math.prod(best_group) < math.prod(sub_group) else sub_group
                    else:
                        best_group = best_group if len(best_group) < len(sub_group) else sub_group
                max_length = len(best_group)
        elif w == target_sum:
            return [w]
    return best_group

g = find_group(weights, int(len(weights)/3) + 1, group_weight)
print(math.prod(g))

group_weight = sum(weights)/4
g = find_group(weights, int(len(weights)/4) + 1, group_weight)
print(math.prod(g))