boss_hp_max = 104
boss_atk = 8
boss_armor = 1
hero_hp_max = 100
weapons, armor, rings = open("input.txt").read().split("\n\n")

def get_shop(shop):
    items = dict()
    for item in shop.split("\n")[1:]:
        item_info = item.split()
        items[" ".join(item_info[:-3])] = [int(x) for x in item_info[-3:]]
    return items

wpns = get_shop(weapons)
armr = get_shop(armor)
ring = get_shop(rings)

def fight(hero_hp, hero_atk, hero_arm, boss_hp, hero_turn = True):
    if hero_hp <= 0 or boss_hp <= 0:
        return boss_hp <= 0
    if hero_turn:
        return fight(hero_hp, hero_atk, hero_arm, boss_hp - max(1, hero_atk - boss_armor), not hero_turn)
    else:
        return fight(hero_hp - max(1, boss_atk - hero_arm), hero_atk, hero_arm, boss_hp, not hero_turn)

wpns_choices = sorted(wpns.keys(), key = lambda wpn: wpns[wpn][0])
armr_choices = sorted(armr.keys(), key = lambda arm: armr[arm][0])
ring_choices = sorted(ring.keys(), key = lambda rng: ring[rng][0])

winning_cost = 1e6
for wpn in wpns_choices:
    wpn_cost, wpn_dmg, _ = wpns[wpn]
    if wpn_cost > winning_cost:
        break
    for buy_armor in [False, True]:
        if not buy_armor:
            for n_rings in [0, 1, 2]:
                if n_rings == 0:
                    if fight(hero_hp_max, wpn_dmg, 0, boss_hp_max):
                        winning_cost = wpn_cost
                        break
                else:
                    if n_rings == 1:
                        for ring_purchase in ring_choices:
                            ring_cost, ring_damage, ring_armor = ring[ring_purchase]
                            if wpn_cost + ring_cost > winning_cost:
                                break
                            if fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor, boss_hp_max):
                                winning_cost = wpn_cost + ring_cost
                    else:
                        for ring_p_1 in ring_choices:
                            ring_cost, ring_damage, ring_armor = ring[ring_p_1]
                            if wpn_cost + ring_cost > winning_cost:
                                break
                            for ring_p_2 in ring_choices:
                                if ring_p_2 == ring_p_1:
                                    continue
                                ring_cost += ring[ring_p_2][0]
                                ring_damage += ring[ring_p_2][1]
                                ring_armor += ring[ring_p_2][2]
                                if wpn_cost + ring_cost > winning_cost:
                                    break
                                if fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor, boss_hp_max):
                                    winning_cost = wpn_cost + ring_cost
        else:
            for armor_choice in armr_choices:
                arm_cost, _, arm_prot = armr[armor_choice]
                if arm_cost + wpn_cost + arm_cost > winning_cost:
                    break
                for n_rings in [0, 1, 2]:
                    if n_rings == 0:
                        if fight(hero_hp_max, wpn_dmg, arm_prot, boss_hp_max):
                            winning_cost = wpn_cost + arm_cost
                            break
                    else:
                        if n_rings == 1:
                            for ring_purchase in ring_choices:
                                ring_cost, ring_damage, ring_armor = ring[ring_purchase]
                                if wpn_cost + ring_cost + arm_cost > winning_cost:
                                    break
                                if fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor + arm_prot, boss_hp_max):
                                    winning_cost = wpn_cost + ring_cost + arm_cost
                        else:
                            for ring_p_1 in ring_choices:
                                ring_cost, ring_damage, ring_armor = ring[ring_p_1]
                                if wpn_cost + ring_cost + arm_cost > winning_cost:
                                    break
                                for ring_p_2 in ring_choices:
                                    if ring_p_2 == ring_p_1:
                                        continue
                                    ring_cost += ring[ring_p_2][0]
                                    ring_damage += ring[ring_p_2][1]
                                    ring_armor += ring[ring_p_2][2]
                                    if wpn_cost + ring_cost + arm_cost > winning_cost:
                                        break
                                    if fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor + arm_prot, boss_hp_max):
                                        winning_cost = wpn_cost + ring_cost + arm_cost

print(winning_cost)

wpns_choices.reverse()
armr_choices.reverse()
ring_choices.reverse()

losing_cost = 0
for wpn in wpns_choices:
    wpn_cost, wpn_dmg, _ = wpns[wpn]
    for buy_armor in [True, False]:
        if not buy_armor:
            for n_rings in [2, 1, 0]:
                if n_rings == 0:
                    if wpn_cost < losing_cost:
                        break
                    if not fight(hero_hp_max, wpn_dmg, 0, boss_hp_max):
                        losing_cost = wpn_cost
                        break
                else:
                    if n_rings == 1:
                        for ring_purchase in ring_choices:
                            ring_cost, ring_damage, ring_armor = ring[ring_purchase]
                            if wpn_cost + ring_cost < losing_cost:
                                break
                            if not fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor, boss_hp_max):
                                losing_cost = wpn_cost + ring_cost
                    else:
                        for ring_p_1 in ring_choices:
                            ring_cost, ring_damage, ring_armor = ring[ring_p_1]
                            if wpn_cost + ring_cost < losing_cost:
                                break
                            for ring_p_2 in ring_choices:
                                if ring_p_2 == ring_p_1:
                                    continue
                                ring_cost += ring[ring_p_2][0]
                                ring_damage += ring[ring_p_2][1]
                                ring_armor += ring[ring_p_2][2]
                                if wpn_cost + ring_cost < losing_cost:
                                    break
                                if not fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor, boss_hp_max):
                                    losing_cost = wpn_cost + ring_cost
        else:
            for armor_choice in armr_choices:
                arm_cost, _, arm_prot = armr[armor_choice]
                if arm_cost + wpn_cost + arm_cost < losing_cost:
                    break
                for n_rings in [2, 1, 0]:
                    if n_rings == 0:
                        if not fight(hero_hp_max, wpn_dmg, arm_prot, boss_hp_max):
                            losing_cost = wpn_cost + arm_cost
                            break
                    else:
                        if n_rings == 1:
                            for ring_purchase in ring_choices:
                                ring_cost, ring_damage, ring_armor = ring[ring_purchase]
                                if wpn_cost + ring_cost + arm_cost < losing_cost:
                                    break
                                if not fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor + arm_prot, boss_hp_max):
                                    losing_cost = wpn_cost + ring_cost + arm_cost
                        else:
                            for ring_p_1 in ring_choices:
                                ring_cost, ring_damage, ring_armor = ring[ring_p_1]
                                if wpn_cost + ring_cost + arm_cost < losing_cost:
                                    break
                                for ring_p_2 in ring_choices:
                                    if ring_p_2 == ring_p_1:
                                        continue
                                    ring_cost += ring[ring_p_2][0]
                                    ring_damage += ring[ring_p_2][1]
                                    ring_armor += ring[ring_p_2][2]
                                    if wpn_cost + ring_cost + arm_cost < losing_cost:
                                        break
                                    if not fight(hero_hp_max, wpn_dmg + ring_damage, ring_armor + arm_prot, boss_hp_max):
                                        losing_cost = wpn_cost + ring_cost + arm_cost

print(losing_cost)