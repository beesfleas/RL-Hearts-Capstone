import numpy as np
from Cards import Card, Hand, Deck

class Trick:
    def __init__(self, startOrder):
        self.startOrder = startOrder
        self.cards = np.full((4, 2), -1, dtype=np.int8)
        self.trump_suit = None
        self.card_count = 0
    
    def add_card(self, card):
        if self.card_count == 0:
            self.trump_suit = card.card[0]
        if self.card_count < 4:
            self.cards[self.card_count] = card.card
            self.card_count += 1
        else:
            print('Too many cards played in this trick')
    
    def getPoints(self):
        hearts_mask = self.cards[:, 0] == 2
        queen_of_spades_mask = (self.cards[:, 0] == 3) & (self.cards[:, 1] == 11)
        points = np.sum(hearts_mask) + 13 * np.sum(queen_of_spades_mask)
        return points  
    
    def determine_winner(self):
        trumpMask = self.cards[:, 0] == self.trump_suit
        winner = np.argmax(self.cards[self.cards[:, 1] * trumpMask])
        return (winner + self.startOrder) % 4

class Round:
    def __init__(self):
        self.tricksPlayed = 0
        self.points = np.zeros(4, dtype=np.int8)
        self.heartsBroken = False
        deck = Deck()
        deck.shuffle()
        self.hands = [self.deck.deal_hand() for _ in range(4)]

        self.startingPlayer = 0
        for i, hand in enumerate(self.hands):
            if (hand.cards[:, 0] == 0).any() and (hand.cards[:, 1] == 2).any():
                self.startingPlayer = i
                break
        self.currentTrick = Trick(self.startingPlayer)
        self.currentPlayer = self.startingPlayer

    def getTurn(self, card):
        self.currentPlayer += 1
        self.currentTrick.add_card(card)

    def newTrick(self):
        winner = self.currentTrick.determine_winner()
        points = self.currentTrick.getPoints()

        self.points[winner] += points
        self.currentTrick = Trick(winner)
        self.currentPlayer = winner
        self.tricksPlayed += 1



    

