import random
import numpy as np

class Card:
    def __init__(self, suit, rank):
        self.card = np.array([suit, rank], dtype=np.int8)
    
    def __str__(self):
        if np.array_equal(self.card, np.array([-1, -1], dtype=np.int8)):
            return "X" 
        suits = ["♣", "♢", "♡", "♠"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{ranks[self.card[1]]}{suits[self.card[0]]}"

class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = np.full((13, 2), -1, dtype=np.int8)
        else:
            self.cards = cards
    
    def play_card(self, index):
        played_card = self.cards[index]
        self.cards[index] = np.array([-1, -1], dtype=np.int8)
        return Card(played_card[0], played_card[1])
    
    def __str__(self):
        return ', '.join([str(Card(int(self.cards[i][0]), int(self.cards[i][1]))) for i in range(13)])

class Deck:
    def __init__(self):
        self.cards = np.column_stack((np.repeat(np.arange(4, dtype=np.int8), 13), 
                                      np.tile(np.arange(13, dtype=np.int8), 4)))
    
    def shuffle(self):
        np.random.shuffle(self.cards)
    
    def deal_hand(self):
        if len(self.cards) < 13:
            print("No cards left to deal.")
            return None 
        hand_cards = np.array(self.cards[:13], dtype=np.int8)
        self.cards = self.cards[13:] 
        return Hand(hand_cards) 

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

        deck = Deck()
        deck.shuffle()
        self.hands = [self.deck.deal_hand() for _ in range(4)]

        self.startingPlayer = 0
        for i, hand in enumerate(self.hands):
            if (hand.cards[:, 0] == 0).any() and (hand.cards[:, 1] == 2).any():
                self.startingPlayer = i
                break
        self.currentTrick = Trick(self.startingPlayer)
        self
    
