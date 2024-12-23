import numpy as np

class Card:
    def __init__(self, suit, rank):
        self.card = np.array([suit, rank], dtype=np.int8)
    
    def __str__(self):
        if np.array_equal(self.card, np.array([-1, -1], dtype=np.int8)):
            return "X" 
        suits = ["♣", "♢", "♡", "♠"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        return f"{ranks[self.card[1]]}{suits[self.card[0]]}"

class Hand:
    def __init__(self, cards):
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
