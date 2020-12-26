decks = open("input.txt").read().split("\n\n")
player_1, player_2 = [[int(d) for d in deck.split("\n") if d.isnumeric()] for deck in decks]

while(len(player_1) > 0 and len(player_2) > 0):
    p1 = player_1.pop(0)
    p2 = player_2.pop(0)
    if p1 > p2:
        player_1.append(p1)
        player_1.append(p2)
    if p2 > p1:
        player_2.append(p2)
        player_2.append(p1)

def score(winner):
    return sum([i * winner[-1 * i] for i in range(1, len(winner)+1)])

print(score(player_1) if len(player_2) == 0 else score(player_2))

def recursive_combat(me, crab):
    previous_rounds = set()
    me_copy = me.copy()
    crab_copy = crab.copy()
    while len(me_copy) > 0 and len(crab_copy) > 0:
        if str((me_copy, crab_copy)) in previous_rounds:
            return me, crab, True
        previous_rounds.add(str((me_copy, crab_copy)))
        me_first = me_copy.pop(0)
        crab_first = crab_copy.pop(0)
        if len(me_copy) < me_first or len(crab_copy) < crab_first:
            if me_first > crab_first:
                me_copy.append(me_first)
                me_copy.append(crab_first)
            if me_first < crab_first:
                crab_copy.append(crab_first)
                crab_copy.append(me_first)
        else:
            sub_me, sub_crab, my_win = recursive_combat(me_copy[:me_first], crab_copy[:crab_first])
            if my_win:
                me_copy.append(me_first)
                me_copy.append(crab_first)
            else:
                crab_copy.append(crab_first)
                crab_copy.append(me_first)
    return me_copy, crab_copy, len(crab_copy) == 0

player_1, player_2 = [[int(d) for d in deck.split("\n") if d.isnumeric()] for deck in decks]
me, crab, result = recursive_combat(player_1, player_2)
print(score(me) if result else score(crab))
