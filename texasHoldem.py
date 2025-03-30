# Python

from random import *

# create deck of cards using multidimensional list
cards = []

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for rank in ranks:
    for suit in suits:
        cards += [[rank,suit]]
      
# test/ length should be 52 cards with 52 cards printed 
print(len(cards))
print("****")
print(cards)
print("****")

#player cards 2
player = [[],[]]

for i in range(len(player)):
    ranCard = choice(cards)
    player[i] = ranCard
    for j in cards:
        if (ranCard == j):
            cards.remove(ranCard)
          
# test/ should print player 2 cards and the length should be 50 cards
print(player)
print("****")
print(len(cards))
print("****")

#table cards 5
table = [[],[],[],[],[]]
for m in range(len(table)):
    ranCard2 = choice(cards)
    table[m] = ranCard2
    for n in cards:
        if (ranCard2 == n):
            cards.remove(ranCard2)

# test/ should print table 5 cards and the length shhould be 45
print(table)
print("****")
print(len(cards))
print(cards)
