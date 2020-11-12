from deck import *
from graphics import *
from playingcard import *

class Poker:
    def __init__(self,playerHand=[],otherHand=[],deckDown=[],imList=[]):
        self.deck = Deck()
        self.playerHand = playerHand
        self.otherHand = otherHand
        self.deckDown = deckDown
        self.imList = imList

    #do the initial deal to all of the players
    def initDeal(self, gwin, dealer, xposD,yposD,xposP,yposP):
        for i in range(2):
            #dealer is a boolean that tells whether dealer or user starts
            if (dealer):
                self.otherHand.append(self.deck.dealCard())
                self.playerHand.append(self.deck.dealCard())
            else:
                self.playerHand.append(self.deck.dealCard())
                self.otherHand.append(self.deck.dealCard())
        
        self.deck.burnCard()
        for i in range(3):
            self.deckDown.append(self.deck().dealCard())
        for i in range(2):
            self.deck().burnCard()
            self.deckDown.append(self.deck.dealCard())

        imD = Image(Point(xposD, yposD), "playingcards/b2fv.gif")
        imD.draw(gwin)
        imP = Image(Point(xposP, yposP), "playingcards/b2fv.gif")
        imP.draw(gwin)
        self.imList.append(imD)
        self.imList.append(imP)
            


