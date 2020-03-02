from random import shuffle, randrange
from itertools import combinations
import time

print('Welcome to the game Players!')


class Card:

    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def show(self):
        print('{} of {}'.format(self.value, self.suit))

    def same_value(self, card):
        return self.value == card.value

    def same_suit(self, card):
        return self.suit == card.suit


class Deck:

    def __init__(self, shuffle=False):
        self.cards = []
        self.build()
        if shuffle:
            self.shuffle()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def show_deck(self):
        for card in self.cards:
            card.show()

    def deck_empty(self):
        return len(self.cards) == 0

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self, random=False):
        if not random:
            return self.cards.pop()
        else:
            return self.cards.pop(randrange(len(self.cards)))


class Player:

    def __init__(self, name, computer):
        self.name = name
        self.computer = computer
        self.hand = []
        self.score = 0

    def draw_hand(self, n=1):
        for i in range(n):
            self.hand.append(gofish.deck.draw_card())
        self.show_hand()

    def show_hand(self):
        if not self.computer:
            print('Dit zijn de kaarten van {}'.format(self.name))
            for card in self.hand:
                card.show()
        else:
            print('{} heeft {} kaarten vast.'.format(self.name, len(self.hand)))

    def remove_pairs(self):
        pairs = []
        j = 1
        while 0 < j <= len(self.hand):
            card1 = self.hand.pop(len(self.hand) - j)
            card2 = self.has_card(card1, question=False)
            if card2:
                pairs.append([card1, card2])
                self.score += 1
            else:
                self.hand.append(card1)
            j += 1
        return pairs

    def ask_user_input(self):
        self.show_hand()
        if not self.computer:
            print('Kies een van de kaarten in je hand om uit te vragen.')
            while True:
                try:
                    user_input = int(input('Kies een kaart tussen 1 & {}:\n\n'.format(len(self.hand))))
                except ValueError:
                    print('Geen valide input, probeer nogmaals')
                    continue
                else:
                    if 1 <= user_input <= len(self.hand):
                        break
                    else:
                        print('Geen valide input, probeer nogmaals')
                        continue
            return self.hand.pop(user_input - 1)
        else:
            return self.hand.pop(randrange(len(self.hand)))

    def has_card(self, card, question=True):
        for i in range(len(self.hand)):
            if card.same_value(self.hand[i]) and not card.same_suit(self.hand[i]):
                return self.hand.pop(i)
        if question:
            print('{}: GO FISH!'.format(self.name))


class Table:

    def __init__(self):
        self.tafel_nummer = 1
        self.table = []

    def add_pair(self, pair):
        self.table.append(pair)

    def print_table(self, n=5):
        i = 1
        if len(self.table) > 0:
            print('Er liggen {} paren op tafel:'.format(len(self.table)))
            i = len(self.table) - n + 1
            for pair in self.table[-n:]:
                print('Paar {}:'.format(i))
                pair[0].show()
                pair[1].show()
                i += 1
        else:
            print('De tafel is leeg')


class Gofish:

    def __init__(self):
        self.deck = Deck(shuffle=True)
        self.players = []
        self.table = Table()
        self.n_players = 2

    def create_players(self):
        computer = True
        for name in ['Alex', 'Paul']:
            self.players.append(Player(name, computer))
        for player in self.players:
            player.draw_hand(14)
        for player in self.players:
            pairs = player.remove_pairs()
            for pair in pairs:
                self.table.add_pair(pair)
            player.show_hand()

    def game_status_check(self):
        return self.deck and self.players[0].hand and self.players[1].hand

    def show_hands(self):
        for player in self.players:
            player.show_hand()

    def setup_game(self):
        self.create_players()
        self.table.print_table()

    def play(self):
        self.setup_game()
        time.sleep(2)
        turn = 0
        while self.game_status_check():
            print('\nBeurt {}, {}:{} - {}:{} '.format(turn, self.players[0].name, self.players[0].score,
                                                      self.players[1].name, self.players[1].score))
            while True:
                # self.table.print_table()
                current_player = turn % 2
                other_player = (abs(current_player - 1)) % 2
                current_player = self.players[current_player]
                other_player = self.players[other_player]
                print('Het is de beurt van {}'.format(current_player.name))
                card = current_player.ask_user_input()
                print('{} vraagt om de volgende kaart: {}'.format(current_player.name, card.value))
                card_2 = other_player.has_card(card)
                if card_2:
                    self.table.add_pair([card, card_2])
                    self.table.print_table()
                    current_player.score += 1
                    if not self.game_status_check():
                        break
                else:
                    current_player.hand.append(card)
                    print('{} pakt een kaart van de stapel.'.format(current_player.name))
                    current_player.draw_hand()
                    pairs = current_player.remove_pairs()
                    if not pairs or not self.game_status_check():
                        break
                    else:
                        print('{} kan alsnog een paar opleggen en mag nogmaals spelen.'.format(current_player.name))
                        for pair in pairs:
                            self.table.add_pair(pair)
                            self.table.print_table()
                time.sleep(2)
            turn += 1
        print('\nHet spel is afgelopen!')
        if not self.deck:
            print('Het pakje kaarten is namelijk op!')
        elif not self.players[0].hand:
            print('{} heeft namelijk geen kaarten meer!'.format(self.players[0].name))
        else:
            print('{} heeft namelijk geen kaarten meer!'.format(self.players[1].name))
        self.print_score()

    def print_score(self):
        print('\n Final Score')
        print('{}:{} - {}:{} '.format(self.players[0].name, self.players[0].score, self.players[1].name,
                                      self.players[1].score))
        if self.players[0].score > self.players[1].score:
            print('{} heeft gewonnen!'.format(self.players[0].name))
        elif self.players[0].score == self.players[1].score:
            print('Er is gelijk gespeeld!'.format(self.players[0].name))
        else:
            print('{} heeft gewonnen!'.format(self.players[1].name))


print('Let\'s play a game!')
gofish = Gofish()
gofish.play()
