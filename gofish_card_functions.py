from itertools import combinations

import basic_card_functions as bcf


def find_pairs(hand):
    pairs = []
    combs = combinations(hand, 2)
    for comb in list(combs):
        if bcf.same_value(comb[0], comb[1]):
            pairs.append((comb[0], comb[1]))
    return (pairs)


def print_pairs(pairs):
    if len(pairs) > 0:
        print('Mogelijke paren:')
        for pair in pairs:
            print('{} & {}'.format(pair[0], pair[1]))
    else:
        print('Geen mogelijke acties, raap een kaart')
