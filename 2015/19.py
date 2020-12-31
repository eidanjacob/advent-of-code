rxns, chem = open("input.txt").read().split("\n\n")
cal_products = set()
replacements = set()
for rxn in rxns.split("\n"):
    reactant, product = rxn.strip().split(" => ")
    replacements.add((reactant, product))

for reactant, product  in replacements:
    for i in range(len(chem)-len(reactant)+1):
        if chem[i:(i+len(reactant))] == reactant:
            cal_products.add(chem[:i] + product + chem[(i+len(reactant)):])

print(len(cal_products))

def rev_synth_dfs(chemical, depth):
    if chemical == "e":
        return True, depth
    for reactant, product in replacements:
        for i in range(len(chemical)-len(product)+1):
            if chemical[i:(i+len(product))] == product:
                next_chemical = chemical[:i] + reactant + chemical[(i + len(product)):]
                works, steps = rev_synth_dfs(next_chemical, depth + 1)
                if works:
                    return True, steps
    return False, depth

print(rev_synth_dfs(chem.strip(), 0))