boss_hp_max = 51
boss_atk = 9
hero_hp_max = 50
hero_mana_initial = 500

# Name : [Cost, Damage, Healing, (Effect, Duration)]
spells = {
    "Magic Missile" : [53, 4, 0, None],
    "Drain" : [73, 2, 2, None],
    "Shield" : [113, 0, 0, ("Shield", 6)],
    "Poison" : [173, 0, 0, ("Poison", 6)],
    "Recharge" : [229, 0, 0, ("Recharge", 5)]
}

# Name : [Armor, Boss Damage, Mana Gain]
effects = {
    "Shield" : [7, 0, 0],
    "Poison" : [0, 3, 0],
    "Recharge" : [0, 0, 101]
}

# Effect : Duration
active_effects_initial = {"Shield" : 0, "Poison" : 0, "Recharge" : 0}

class Battle:

    def __init__(self, hero_hp = hero_hp_max, mana = hero_mana_initial, boss_hp = boss_hp_max, active_effects = active_effects_initial, hero_turn = True, spent_mana = 0, depth = 0):
        self.hero_hp = hero_hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.active_effects = active_effects
        self.hero_turn = hero_turn
        self.spent_mana = spent_mana
        self.depth = depth

    def step(self):
        self.successor_states = []
        hero_armor = 0
        hero_damage = 0
        hero_mana_gain = 0
        next_battle_effects = {key : max(0, value - 1) for key, value in self.active_effects.items()}
        for effect, duration in self.active_effects.items():
            if duration > 0:
                hero_armor += effects[effect][0]
                hero_damage += effects[effect][1]
                hero_mana_gain += effects[effect][2]
        if self.boss_hp <= hero_damage:
            self.successor_states = [Battle(self.hero_hp, self.mana, self.boss_hp - hero_damage, self.active_effects, "Start of hero turn" if self.hero_turn else "Start of Boss Turn", self.spent_mana, self.depth + 0.5)]
        elif self.hero_turn:
            for spell in spells.values():
                if spell[0] <= self.mana:
                    if (spell[3] is not None) and next_battle_effects[spell[3][0]] <= 0:
                        next_battle_effects[spell[3][0]] = spell[3][1]
                    self.successor_states.append(Battle(self.hero_hp + spell[2], self.mana - spell[0] + hero_mana_gain, self.boss_hp - hero_damage - spell[1], next_battle_effects, not self.hero_turn, self.spent_mana + spell[0], self.depth + 1))
                next_battle_effects = {key : max(0, value - 1) for key, value in self.active_effects.items()}
        else:
            self.successor_states = [Battle(self.hero_hp - boss_atk + hero_armor, self.mana + hero_mana_gain, self.boss_hp - hero_damage, next_battle_effects, not self.hero_turn, self.spent_mana, self.depth + 1)]

    def gen_and_prune(self, best_so_far):
        self.step()
        unpruned_branches = []
        updated_min = best_so_far
        for successor in self.successor_states:
            if successor.spent_mana > updated_min or successor.hero_hp <= 0: 
                continue
            if successor.boss_hp <= 0:
                updated_min = min(updated_min, successor.spent_mana)
                continue
            unpruned_branches.append(successor)
        return unpruned_branches, updated_min

battle_states = [Battle()]
min_spent_mana = float("inf")
while len(battle_states) > 0:
    next_battle_states = []
    for state in battle_states:
        succ_states, succ_best = state.gen_and_prune(min_spent_mana)
        next_battle_states += succ_states
        min_spent_mana = min(succ_best, min_spent_mana)
    battle_states = next_battle_states

print(min_spent_mana)

battle_states = [Battle()]
min_spent_mana = float("inf")
while len(battle_states) > 0:
    next_battle_states = []
    for state in battle_states:
        if state.hero_turn:
            state.hero_hp -= 1
        if state.hero_hp <= 0:
            continue
        succ_states, succ_best = state.gen_and_prune(min_spent_mana)
        next_battle_states += succ_states
        min_spent_mana = min(succ_best, min_spent_mana)
    battle_states = next_battle_states

print(min_spent_mana)