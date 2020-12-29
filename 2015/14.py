puzzle = open("input.txt").readlines()
reindeer = dict()
for p in puzzle:
    split_p = p.split(" ")
    reindeer[split_p[0]] = (int(split_p[3]), int(split_p[6]), int(split_p[13]))

def winner_distance(race_time):
    winning_distance = 0
    winners = set()
    for name, r in reindeer.items():
        n_cycles = int(race_time / (r[1] + r[2]))
        extra_run_time = min(race_time - n_cycles * (r[1] + r[2]), r[1])
        distance = (n_cycles * r[1] + extra_run_time) * r[0]
        if winning_distance == distance:
            winners.add(name)
        elif winning_distance < distance:
            winners = set([name])
            winning_distance = distance
    return winners, winning_distance

print(winner_distance(2503))

def winning_score(race_time):
    scores = dict()
    for name in reindeer.keys():
        scores[name] = 0
    for i in range(1, race_time+1):
        winners, _ = winner_distance(i)
        for winner in winners:
            scores[winner] = scores[winner] + 1
    print([f"{k}, {v}" for k, v in scores.items() if v == max(scores.values())])

winning_score(2503)