import json

with open('tree.txt', 'r') as f:
    tree = f.read()

with open('pairs.txt') as f:
    pairs = json.load(f)


def find_nodes_comman_parent(p1, p2):
    if p1 == p2:
        return p1
    elif p1 > p2:
        return find_nodes_comman_parent((p1 - 1) // 2, p2)
    elif p1 < p2:
        return find_nodes_comman_parent(p1, (p2 - 1) // 2)


solved = [tree[find_nodes_comman_parent(pair[0], pair[1])] for pair in pairs]

print(''.join(solved))
