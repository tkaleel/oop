import time, os, random

ranks = ["Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]
suits = ["Clubs" "Hearts" "Diamonds" "Spades"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " +suit, value])
    value = value + 1

print(deck)