import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class Player:
    def __init__(self, cards):
        self.cards = cards

    def show_hand(self):
        for i in self.cards:
            print(i.number, i.suit)


class Game:
    def __init__(self):
        self.cards = [Card(i, j) for i in ["Heart", "Spade", "Diamond", "Clubs"] for j in range(7, 15)]
        self.players = list()

    def show(self):
        for i in self.cards:
            print(i.number, i.suit)

    def shuffle(self):
        random.shuffle(self.cards)

    def spread_cards(self):
        p1 = list()
        p2 = list()
        p3 = list()
        p4 = list()
        while self.cards:
            p1.append(self.cards.pop())
            p2.append(self.cards.pop())
            p3.append(self.cards.pop())
            p4.append(self.cards.pop())
        self.players = [Player(i) for i in [p1, p2, p3, p4]]
