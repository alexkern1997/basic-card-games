import basic_card_functions as bcf
import gofish_card_functions as gcf

if __name__ == "__main__":

    def print_hand(hand):
        i = 1
        for card in hand:
            print("{}. {}".format(i, card))
            i += 1


    print('Welkom bij Go fish')
    print('Je speelt dit spel tegen de computer')
    print('De menselijke speler begint')

    card_deck = bcf.build_deck()
    bcf.shuffle_deck(card_deck)
    hands = bcf.deal_hand(card_deck, 7, 2)

    game_finished = False

    while game_finished != True:

        print_hand(hands[0])
        pairs = gcf.find_pairs(hands[0])
        print('Mogelijke paren')
        for pair in pairs:
            print(pair)
        game_finished = True
