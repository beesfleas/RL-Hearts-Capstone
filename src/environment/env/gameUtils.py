from cardUtils import Card, Hand, Deck
import random
import numpy as np

class Trick:
    def __init__(self, startOrder):
        self.startOrder = startOrder
        self.cards = np.full((4, 2), -1)
        self.trump_suit = None
        self.card_count = 0
    
    def add_card(self, card):
        if self.card_count == 0:
            self.trump_suit = card.card[0]
        if self.card_count < 4:
            self.cards[self.card_count] = card.card
            self.card_count += 1
        else:
            print('too much tricked')
    
    def get_cards(self):
        return self.cards
    
    def determine_winner(self):
        trumpMask = self.cards[:, 0] == self.trump_suit
        winner = np.argmax(self.cards[self.cards[:, 1] * trumpMask])
        return (winner+self.startOrder) % 4

class Table:
    
