import random
import numpy as np

class Card:
    def __init__(self, suit, rank):
        self.card = np.array([suit, rank]) 
    
    def __str__(self):
        if np.array_equal(self.card, np.array([-1, -1])):
            return "X" 
        suits = ["♣", "♢", "♡", "♠"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        return f"{ranks[self.card[1]]}{suits[self.card[0]]}"


class Hand:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = np.full((13, 2), -1) 
        else:
            self.cards = cards 
    
    def play_card(self, index):
        played_card = self.cards[index]
        self.cards[index] = np.array([-1, -1])
        return Card(played_card[0], played_card[1])
    
    def __str__(self):
        return ', '.join([str(Card(int(self.cards[i][0]), int(self.cards[i][1]))) for i in range(13)])


class Deck:
    def __init__(self):
        # Initialize the deck as a list of 52 cards, each represented by a [suit, rank] numpy array
        self.cards = [np.array([suit, rank]) for suit in range(4) for rank in range(13)] 
    
    def shuffle(self):
        random.shuffle(self.cards)  # Shuffle the deck
    
    def deal_hand(self):
        if len(self.cards) < 13:
            print("No cards left to deal.")
            return None 
        hand_cards = np.array(self.cards[:13])  # First 13 cards as a 13x2 numpy array
        self.cards = self.cards[13:]  # Remove dealt cards from the deck
        return Hand(hand_cards)  # Return the hand

