ingredients = open("input.txt").readlines()
props = dict()
for i in range(len(ingredients)):
    ing_name, ing_props = ingredients[i].split(": ")
    props[i] = [int(x) for x in ing_props.replace(",", "").split(" ")[1::2]]

def recipe_val(tsps):
    v = 1
    for i in range(4):
        v *= max(0, sum([props[j][i]*tsps[j] for j in range(len(props.keys()))]))
    return v

best_val = 0
best_val_2 = 0

best_val = 0
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            rec_val = recipe_val([a, b, c, 100-a-b-c])
            if sum([props[j][4] * [a, b, c, 100-a-b-c][j] for j in range(4)]) == 500:
                best_val_2 = max(rec_val, best_val_2)
            best_val = max(best_val, rec_val)

print(best_val, best_val_2)