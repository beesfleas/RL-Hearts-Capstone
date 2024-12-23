from Cards import Card, Hand, Deck

deck = Deck()
deck.shuffle()
hands = []

for i in range(4):
    hand = deck.deal_hand()
    print(f"Hand {i+1}: {hand}")
    hands.append(hand)

hand = deck.deal_hand()


hands[0].play_card(0)  
hands[1].play_card(4) 
hands[2].play_card(7) 
hands[3].play_card(12)  

for i in range(4):
    print(f"Hand {i+1}: {hands[i]}")

print(hand)