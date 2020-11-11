from playingcard import *
from random import *


class Deck:

    def __init__(self):
        #starts of with an empty list of cards
        self.cardList = []
        #loops through each suit 13 times to create a deck of cards
        for i  in range(13):
            card = PlayingCard(i+1,"s")
            self.cardList.append(card)

            card = PlayingCard(i+1,"d")
            self.cardList.append(card)

            card = PlayingCard(i+1,"h")
            self.cardList.append(card)

            card = PlayingCard(i+1,"c")
            self.cardList.append(card)
        #shuffles the deck
        self.shuffle()
    
    def shuffle(self):
        shuffle(self.cardList)
    #deals the first card in the list
    def dealCard(self):
        return self.cardList.pop(0)
    #returns how many cards left in the deck
    def cardsLeft(self):
        return len(self.cardList)
    #burns the top card
    def burnCard(self):
        self.cardList.pop(0)

