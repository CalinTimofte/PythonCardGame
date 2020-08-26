import random


class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number


class Player:
    def __init__(self, cards):
        self.cards = cards


class Game:
    def __init__(self):
        self.cards = [Card(i, j) for i in ["Heart", "Spade", "Diamond", "Clubs"] for j in range(7, 15)]
        self.players = list()
