def get_ip_and_hypernet(string):
    if "[" not in string:
        return [string], []
    left = string.index("[")
    right = string.index("]")
    ip_segs = [string[:left]]
    hypernet_segs = [string[(left+1):right]]
    remaining_ips, remaining_hypernets = get_ip_and_hypernet(string[(right+1):])
    return ip_segs + remaining_ips, hypernet_segs + remaining_hypernets


def has_abba(string):
    if len(string) < 4:
        return False
    for i, char in enumerate(string[:-3]):
        if char == string[i+3] and char != string[i+1] and string[i+1] == string[i+2]:
            return True
    return False

def support_TLS(string):
    ips, hypernets = get_ip_and_hypernet(string)
    return any([has_abba(ip) for ip in ips]) and not any([has_abba(hyp) for hyp in hypernets])

print(sum([support_TLS(ip.strip()) for ip in open("input.txt").readlines()]))

def get_abas(ips):
    abas = set()
    for ip in ips:
        for i, char in enumerate(ip[:-2]):
            if char == ip[i+2] and char != ip[i+1]:
                abas.add(ip[i:(i+3)])
    return abas

def has_bab(hypernets, abas):
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        for hypernet in hypernets:
            if bab in hypernet:
                return True
    return False

def support_SSL(string):
    ips, hypernets = get_ip_and_hypernet(string)
    abas = get_abas(ips)
    return has_bab(hypernets, abas)

print(sum([support_SSL(ip.strip()) for ip in open("input.txt").readlines()]))