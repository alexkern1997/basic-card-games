from random import randint, shuffle


def build_deck():
    card_deck = []
    for suit in ['Hearts', 'Spades', 'Diamonds', 'Spades']:

        for i in range(1, 11):
            card_deck.append('{} of {}'.format(i, suit))

        card_deck.append('Jack of {}'.format(suit))
        card_deck.append('Queen of {}'.format(suit))
        card_deck.append('King of {}'.format(suit))
    return (card_deck)


def get_suit(card):
    suit = card.split(' ')[2]
    return (suit)


def get_value(card):
    value = card.split(' ')[0]
    return (value)


def same_value(card1, card2, *cards):
    if get_value(card1) == get_value(card2):
        for card in cards:
            if get_value(card) != get_value(card1):
                return False
        return True
    else:
        return False


def same_suit(card1, card2, *cards):
    if get_suit(card1) == get_suit(card2):
        for card in cards:
            if get_suit(card) != get_suit(card1):
                return False
        return True
    else:
        return False


def deal_top_card(card_deck):
    if len(card_deck) > 0:
        card = card_deck.pop(0)
        return (card)
    else:
        print('Card deck is empty')


def get_random_card(card_deck):
    if len(card_deck) > 0:
        i = randint(0, len(card_deck))
        card = card_deck.pop(i)
        return (card)
    else:
        print('Card deck is empty')


def shuffle_deck(card_deck):
    shuffle(card_deck)


def deal_hand(card_deck, n_cards, n_hands):
    hands = []
    for i in range(0, n_hands):
        hand = []
        for i in range(0, n_cards):
            hand.append(deal_top_card(card_deck))
        hands.append(hand)
    return (hands)
