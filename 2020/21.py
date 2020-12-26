puzzle_input = open("input.txt").readlines()
translate_allergen = dict()
untranslated_allergens = set()
foods_and_allergens = []
for line in puzzle_input:
    ingredients, allergens = line.split(" (")
    ingredients_list = ingredients.split(" ")
    allergens = allergens.replace("contains ", "").replace(",", "").replace(")", "").replace("\n", "").split(" ")
    foods_and_allergens.append([ingredients_list, allergens])
    for allergen in allergens:
        if allergen not in untranslated_allergens:
            translate_allergen[allergen] = set(ingredients_list)
        else:
            translate_allergen[allergen] = set(list(ingredients_list)).intersection(translate_allergen[allergen])
    untranslated_allergens = untranslated_allergens.union(set(allergens))

while len(untranslated_allergens) > 0:
    for item in foods_and_allergens:
        ingredients = item[0]
        allergens = item[1]
        for allergen in allergens:
            if allergen not in untranslated_allergens:
                unknown_ingredients = [ingredient for ingredient in ingredients if ingredient != list(translate_allergen[allergen])[0]]
                this_untranslated_allergens = [a for a in allergens if a != allergen]
                if len(this_untranslated_allergens) > 0:
                    for a in this_untranslated_allergens:
                        translate_allergen[a] = set(unknown_ingredients).intersection(translate_allergen[a])
                        if len(translate_allergen[a]) == 1:
                            untranslated_allergens.remove(a)
                            for b, value in translate_allergen.items():
                                value.remove(a)
    change = True
    while change:
        change = False
        newly_translated = []
        for key, value in translate_allergen.items():
            if key not in untranslated_allergens:
                continue
            if len(value) == 1:
                change = True
                untranslated_allergens.remove(key)
                newly_translated.append(list(value)[0])
        for ingredient in newly_translated:
            for key, value in translate_allergen.items():
                if len(value) > 1:
                    translate_allergen[key].discard(ingredient)
    
translated_allergens = [list(value)[0] for key, value in translate_allergen.items()]
print(sum([sum([1 for ingredient in ingredients_list[0] if ingredient not in translated_allergens]) for ingredients_list in foods_and_allergens]))
print(",".join([list(value)[0] for key, value in sorted(translate_allergen.items())]))
