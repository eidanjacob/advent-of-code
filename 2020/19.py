rules_messages = open("input.txt").readlines()
separator = [i for i, line in enumerate(rules_messages) if line == "\n"][0]

rules_list = [r.replace("\n", "") for r in rules_messages[:separator]]
rules = dict()
for rule in rules_list:
    rule_split = rule.split(": ")
    rule_id = int(rule_split[0])
    if rule_split[1][0] == "\"":
        rules[rule_id] = rule_split[1][1]
    else:
        rules[rule_id] = [[int(n) for n in nested_rule.split(" ")] for nested_rule in rule_split[1].split(" | ")]

messages = [m.replace("\n", "") for m in rules_messages[(separator+1):]]
atoms = {key for key, value in rules.items() if str(value) == value}

def matches_rule(message, stack):
    if len(message) < len(stack):
        return False
    elif len(stack) == 0 or len(message) == 0:
        return len(stack) == 0 and len(message) == 0

    rule = stack.pop()
    if rule in atoms:
        if message[0] == rules[rule]:
            return matches_rule(message[1:], stack.copy())
    else:
        for subrule in rules[rule]:
            if matches_rule(message, stack + list(reversed(subrule))):
                return True
    return False

print(sum([matches_rule(m, [0]) for m in messages]))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
                   
print(sum([matches_rule(m, [0]) for m in messages]))
