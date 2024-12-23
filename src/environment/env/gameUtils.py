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
        self.cards = np.column_stack((np.repeat(np.arange(4), 13), np.tile(np.arange(13), 4) ))
    def shuffle(self):
        random.shuffle(self.cards) 
    
    def deal_hand(self):
        if len(self.cards) < 13:
            print("No cards left to deal.")
            return None 
        hand_cards = np.array(self.cards[:13]) 
        self.cards = self.cards[13:] 
        return Hand(hand_cards) 



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
    def __init__(self): 
        self.currentTrick = None
        self.tricksPlayed = 0
        self.currentPlayer = -1

