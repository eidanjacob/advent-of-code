ops_master = [o.strip() for o in open("input.txt").readlines()]

ops = ops_master.copy()
bots = dict()
while len(ops) > 0: 
    next_ops = []
    for op in ops:
        if "value" in op:
            value = int(op.split(" ")[1])
            bot = op.split(" to ")[1]
            if bot in bots.keys(): 
                bots[bot].append(value)
            else:
                bots[bot] = [value]
            continue
        else:
            source_bot = op.split(" gives ")[0]
            low = " ".join(op.split(" ")[5:7])
            high = " ".join(op.split(" ")[-2:])
            if source_bot in bots.keys():
                if len(bots[source_bot]) == 2:
                    if low in bots.keys():
                        bots[low].append(min(bots[source_bot]))
                    else:
                        bots[low] = [min(bots[source_bot])]
                    if high in bots.keys():
                        bots[high].append(max(bots[source_bot]))
                    else:
                        bots[high] = [max(bots[source_bot])]
                    continue
        next_ops.append(op)
    ops = next_ops

print([bot for bot, chips in bots.items() if 61 in chips and 17 in chips])
print(bots["output 0"][0] * bots["output 1"][0] * bots["output 2"][0])