from deck import *
from graphics import *
from playingcard import *

class Poker:
    def __init__(self,playerHand=[],otherHand=[],deckDown=[],imList=[],winningHand=[]):
        self.deck = Deck()
        self.playerHand = playerHand
        self.otherHand = otherHand
        self.deckDown = deckDown
        self.imList = imList
        self.winningHand = winningHand

    #do the initial deal to both of the players
    def initDeal(self, gwin, dealer, xposD,yposD,xposP,yposP):
        for i in range(2):
            #dealer is a boolean that tells whether dealer or user starts
            if (dealer):
                self.otherHand.append(self.deck.dealCard())
                self.playerHand.append(self.deck.dealCard())
            else:
                self.playerHand.append(self.deck.dealCard())
                self.otherHand.append(self.deck.dealCard())
        
        #simulates the middle row of cards for holdem
        self.deck.burnCard()
        for i in range(3):
            self.deckDown.append(self.deck().dealCard())
        for i in range(2):
            self.deck().burnCard()
            self.deckDown.append(self.deck.dealCard())

        #show the dealers cards face down
        imD = Image(Point(xposD, yposD), "playingcards/b2fv.gif")
        imD.draw(gwin)
        imD2 = Image(Point(xposD + 20, yposD), "playingcards/b2fv.gif")
        imD2.draw(gwin)
        self.imList.append(imD)
        self.imList.append(imD2)

        #show the users cards face up
        self.playerCard1 = self.playerHand.pop(0)
        self.playerCard2 = self.playerHand.pop(0)

        suit1 = self.playerCard1.getSuit()
        rank1 = self.playerCard1.getRank()
        im = Image(Point(xposP, yposP), "playingcards/" + suit1 + str(rank1) + ".gif")
        im.draw(gwin)

        suit2 = self.playerCard2.getSuit()
        rank2 = self.playerCard2.getRank()
        im1 = Image(Point(xposP + 30, yposP), "playingcards/" + suit2 + str(rank2) + ".gif")
        im1.draw(gwin)

        self.imList.append(im)
        self.imList.append(im1)


    #shows the middle cards on the game board
    def DisplayMiddleCards(self,gwin,xpos,ypos,num):
        #show the first 3 cards
        if (num == 1):
            self.card1 = self.deckDown.pop(0)
            self.card2 = self.deckDown.pop(0)
            self.card3 = self.deckDown.pop(0)

            suit1 = self.card1.getSuit()
            rank1 = self.card1.getRank()
            im = Image(Point(xpos, ypos), "playingcards/" + suit1 + str(rank1) + ".gif")
            im.draw(gwin)

            xpos = xpos + 30
            suit1 = self.card2.getSuit()
            rank1 = self.card2.getRank()
            im2 = Image(Point(xpos, ypos), "playingcards/" + suit1 + str(rank1) + ".gif")
            im2.draw(gwin)

            xpos = xpos + 30
            suit1 = self.card3.getSuit()
            rank1 = self.card3.getRank()
            im3 = Image(Point(xpos, ypos), "playingcards/" + suit1 + str(rank1) + ".gif")
            im3.draw(gwin)

            self.imList.append(im)
            self.imList.append(im2)
            self.imList.append(im3)

        #show the 4th card
        elif (num == 2):
            self.card4 = self.deckDown.pop(0)
            suit = self.card4.getSuit()
            rank = self.card4.getRank()
            im4 = Image(Point(xpos, ypos), "playingcards/" + suit + str(rank) + ".gif")
            im4.draw(gwin)
            self.imList.append(im4)

        #show the last card
        else:
            self.card5 = self.deckDown.pop(0)
            suit = self.card5.getSuit()
            rank = self.card5.getRank()
            im5 = Image(Point(xpos, ypos), "playingcards/" + suit + str(rank) + ".gif")
            im5.draw(gwin)
            self.imList.append(im5)

    def royalFlush(self):
        i = 8

    def fourOfKind(self):
        #set true if dealer also has 4 of a kind
        dealWin = False
        temp1 = self.otherHand[0]
        temp4 = self.otherHand[3]
        #doesn't work need a search here
        count1 = self.otherHand.count(temp1)
        count2 = self.otherHand.count(temp4)
        #checks dealer's hand
        if (count1 == 4):
            for i in range(5):
                self.winningHand.append(self.otherHand[i])
            dealWin = True
        elif (count1 < 4 and count2 == 4):
            dealWin = True

        #checks player's hand
        temp1 = self.playerHand[0]
        temp4 = self.playerHand[3]
        count1 = self.playerHand.count(temp1)
        count2 = self.playerHand.count(temp4)
        #Top ranked card is 4 of a kind
        if (count1 == 4):
            #check for who has a higher 4 of a kind
            if (dealWin):
                for i in range(5):
                    cardP = self.playerHand[i]
                    cardD = self.otherHand[i]
                    if (cardP.value() > cardD.value()):
                        self.winningHand.clear()
                        for i in range(5):
                            self.winningHand.append(self.playerHand[i])
                        return "player"
                    elif (cardP.value() < cardD.value()):
                        return "dealer"
                return "tie"
            #only player had 4 of a kind
            else:
                for i in range(5):
                    self.winningHand.append(self.playerHand[i])
                return "player"

        elif (count1 < 4 and count2 == 4):
            if (dealWin):
                for i in range(5):
                    cardP = self.playerHand[i]
                    cardD = self.otherHand[i]
                    if (cardP.value() > cardD.value()):
                        for i in range(4):
                            self.winningHand.append(self.playerHand[i])
                        self.winningHand.append(self.playerHand[0])
                        return "player"
                    elif (cardP.value() < cardD.value()):
                        return "dealer"
            else:
                t=0

        elif (count1 < 4 and count2 < 4 and dealWin == True):
            return "dealer"
        
        return "n"
            

    def highCard(self):
        for i in range(5):
            cardP = self.playerHand[i]
            cardD = self.otherHand[i]
            if (cardP.value() > cardD.value()):
                for i in range(5):
                    self.winningHand.append(self.playerHand[i])
                return "player"
            elif (cardP.value() < cardD.value()):
                for i in range(5):
                    self.winningHand.append(self.otherHand[i])
                return "dealer"
        #in tie just show user their best 5 cards
        for i in range(5):
            self.winningHand.append(self.playerHand[i])
        return "tie"
        
    def higherHand(self):
        found = True
        self.orderCardRank()
        if found:
            name = self.royalFlush()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False
        
        if found:
            name = self.straightFlush()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False
        
        if found:
            name = self.fourOfKind()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.fullHouse()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.flush()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.straight()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.threeOfKind()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.twoPair()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False

        if found:
            name = self.pair()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name
                found = False
        
        if found:
            return self.highCard()
            

    def displayWin(self,gwin,xpos,ypos):
        for card in self.winningHand:
            suit = card.getSuit()
            rank = card.getRank()
            im = Image(Point(xpos,ypos), "playingcards/" + suit + str(rank) + ".gif")
            im.draw(gwin)
            self.imList.append(im)
            xpos = xpos + 30

    def orderCardRank(self):
        self.playerHand.append(self.playerCard1)
        self.playerHand.append(self.playerCard2)
        self.playerHand.append(self.card1)
        self.playerHand.append(self.card2)
        self.playerHand.append(self.card3)
        self.playerHand.append(self.card4)
        self.playerHand.append(self.card5)
        #Sorts based off of poker value
        self.playerHand.sort(key= lambda x: x.value())

        self.otherCard1 = self.otherHand[0]
        self.otherCard2 = self.otherHand[1]

        self.otherHand.append(self.card1)
        self.otherHand.append(self.card2)
        self.otherHand.append(self.card3)
        self.otherHand.append(self.card4)
        self.otherHand.append(self.card5)

        self.otherHand.sort(key= lambda x: x.value())
        

