import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        suits = ["♣", "♢", "♡", "♠"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{ranks[self.rank]}{suits[self.suit]}"


class nullCard(Card):
    def __init__(self):
        self.suit = -1
        self.rank = -1 
    
    def __str__(self):
        return "X" 

class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
        else:
            self.cards = cards
    
    def play_card(self, index):
        played_card = self.cards[index]
        self.cards[index] = nullCard()
        return played_card
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(13)] 
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_hand(self):
        if len(self.cards) < 13:
            print("no cards left")
            return None 
        hand_cards = self.cards[:13]
        self.cards = self.cards[13:] 
        return Hand(hand_cards)