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
        self.winningHand.clear()
        rank1 = 0
        rank2 = 0
        """ dealHand = []
        dealerWon = False
        suit1 = 0
        suit2 = 0
        #checks top 5 cards of CPU to see if we have royal flush there
        for i in range(4):
            rank1 = self.otherHand[i].getRank()
            suit1 = self.otherHand[i].getSuit()
            rank2 = self.otherHand[i+1].getRank()
            suit2 = self.otherHand[i+1].getSuit()
            if (rank1 == 1):
                if (rank2 == 13):
                    if (suit1 == suit2):
                        dealHand.append(self.otherHand[i])
                    else:
                        break            
                else:
                    break
            elif (rank1 >= 10):
                if (rank1 == rank2 + 1):
                    if (suit1 == suit2):
                        dealHand.append(self.otherHand[i])
                    else:
                        break
                else:
                    break
            else:
                break
        if (rank1 == 11 and rank2 == 10 and suit1 == suit2):
            dealerWon = True
        
        #checks top 5 cards of user to see if we have royal flush there
        for i in range(4):
            rank1 = self.playerHand[i].getRank()
            suit1 = self.playerHand[i].getSuit()
            rank2 = self.playerHand[i+1].getRank()
            suit2 = self.playerHand[i+1].getSuit()
            if (rank1 == 1):
                if (rank2 == 13):
                    if (suit1 == suit2):
                        self.winningHand.append(self.playerHand[i])
                    else:
                        break            
                else:
                    break
            elif (rank1 >= 10):
                if (rank1 == rank2 + 1):
                    if (suit1 == suit2):
                        self.winningHand.append(self.playerHand[i])
                    else:
                        break
                else:
                    break
            else:
                break
        #player wins, dealer loses
        if (rank1 == 11 and rank2 == 10 and suit1 == suit2 and dealerWon == False):
            return "player"
        #both have royal flush
        elif (rank1 == 11 and rank2 == 10 and suit1 == suit2 and dealerWon):
            return "tie"
        #only the dealer has won
        elif(dealerWon):
            self.winningHand.clear()
            for i in range(5):
                self.winningHand.append(dealHand[i])
        #niether won in initial check
        else: """
        #calls the flush method because it will set the winning hand as a royal flush if one exists 
        name = self.flush()
        if (self.winningHand[0].getRank() == 1 and self.winningHand[1].getRank() == 13):
            for i in range(3):
                rank1 = self.winningHand[i+1].getRank()
                rank2 = self.winningHand[i+2].getRank()
                if (rank1 != rank2 + 1):
                    return "n"
        else:
            return "n"

        return name

    def straightFlush(self):
        self.winningHand.clear()
        rank1 = 0
        rank2 = 0
        ind1 = 0
        ind2 = 0
        playerFlush = []
        otherFlush = []
        dealerStraight = []
        player = False
        h = 0
        s = 0
        d = 0
        c = 0
        h2 = 0
        s2 = 0
        d2 = 0
        c2 = 0
        for i in range(7):
            suitP = self.playerHand[i].getSuit()
            suitD = self.otherHand[i].getSuit()
            #running variables to check if one hits 5 
            if (suitP == "s"):
                s = s + 1
            elif (suitP == "h"):
                h = h + 1
            elif (suitP == "d"):
                d = d + 1
            else:
                c = c + 1

            if (suitD == "s"):
                s2 = s2 + 1
            elif (suitD == "h"):
                h2 = h2 + 1
            elif (suitD == "d"):
                d2 = d2 + 1
            else:
                c2 = c2 + 1
        #player flush
        if (h >= 5 or s >= 5 or d >= 5 or c >= 5):
            if (h >= 5):
                for i in range(7):
                    if (self.playerHand[i].getSuit() == "h"):
                        playerFlush.append(self.playerHand[i])
            elif (s >= 5):
                for i in range(7):
                    if (self.playerHand[i].getSuit() == "s"):
                        playerFlush.append(self.playerHand[i])
            elif (d >= 5):
                for i in range(7):
                    if (self.playerHand[i].getSuit() == "d"):
                        playerFlush.append(self.playerHand[i])
            elif (c >= 5):
                for i in range(7):
                    if (self.playerHand[i].getSuit() == "c"):
                        playerFlush.append(self.playerHand[i])
            #check if the flush cards contains a straight
            for i in range(len(playerFlush) - 1):
                rank1 = playerFlush[i].getRank()
                rank2 = playerFlush[i+1].getRank()
                if (rank1 == rank2 + 1 and ind1 < 5):
                    ind1 = ind1 + 1
                    self.winningHand.append(playerFlush[i])
                elif (ind1 == 5):
                    break
                else:
                    ind1 = 0
                    self.winningHand.clear()
            
            #both have a flush
            if (h2 >= 5 or s2 >= 5 or d2 >= 5 or c2 >= 5):
                if (h2 >= 5):
                    for i in range(7):
                        if (self.otherHand[i].getSuit() == "h"):
                            otherFlush.append(self.otherHand[i])
                elif (s2 >= 5):
                    for i in range(7):
                        if (self.otherHand[i].getSuit() == "s"):
                            otherFlush.append(self.otherHand[i])                          
                elif (d2 >= 5):
                    for i in range(7):
                        if (self.otherHand[i].getSuit() == "d"):
                            otherFlush.append(self.otherHand[i])
                elif (c2 >= 5):
                    for i in range(7):
                        if (self.otherHand[i].getSuit() == "c"):
                            otherFlush.append(self.otherHand[i])
                #again check if contains a straight
                for i in range(len(otherFlush) - 1):
                    rank1 = otherFlush[i].getRank()
                    rank2 = otherFlush[i+1].getRank()
                    if(rank1 == rank2 + 1 and ind2 < 5):
                        ind2 = ind2 + 1
                        dealerStraight.append(otherFlush[i])
                    elif (ind2 == 5):
                        break
                    else:
                        ind2 = 0
                        dealerStraight.clear()

                if (ind1 == 5):
                    if (ind2 != 5):
                        return "player"
                    else:
                        #both players have it, so check the top card
                        if (self.winningHand[0].getRank() > dealerStraight[0].getRank):
                            return "player"
                        elif (self.winningHand[0].getRank() < dealerStraight[0].getRank):
                            self.winningHand.clear()
                            for i in range(5):
                                self.winningHand.append(dealerStraight[i])
                            return "dealer"
                        else:
                            return "tie"
                elif (ind1 != 5 and ind2 == 5):
                    self.winningHand.clear()
                    for i in range(5):
                        self.winningHand.append(dealerStraight[i])
                else:
                    return "n"

            #just player has a flush    
            else:
                if (ind1 == 5):
                    return "player"
                else:
                    return "n"
                
        #other hand flush
        elif (h2 >= 5 or s2 >= 5 or d2 >= 5 or c2 >= 5):
            #adds the right suit
            if (h2 >= 5):
                for i in range(7):
                    if (self.otherHand[i].getSuit() == "h"):
                        otherFlush.append(self.otherHand[i])
            elif (s2 >= 5):
                for i in range(7):
                    if (self.otherHand[i].getSuit() == "s"):
                        otherFlush.append(self.otherHand[i])
            elif (d2 >= 5):
                for i in range(7):
                    if (self.otherHand[i].getSuit() == "d"):
                        otherFlush.append(self.otherHand[i])
            elif (c2 >= 5):
                for i in range(7):
                    if (self.otherHand[i].getSuit() == "c"):
                        otherFlush.append(self.otherHand[i])

            #again check if contains a straight
            for i in range(len(otherFlush) - 1):
                rank1 = otherFlush[i].getRank()
                rank2 = otherFlush[i+1].getRank()
                if(rank1 == rank2 + 1 and ind2 < 5):
                    ind2 = ind2 + 1
                    self.winningHand.append(otherFlush[i])
                if (ind2 == 5):
                    break
                else:
                    ind2 = 0
                    self.winningHand.clear()

            if (ind2 == 5):
                return "dealer"
            else:
                return "n"

        else:
            return "n"

    def fourOfKind(self):
        self.winningHand.clear()
        #set true if dealer also has 4 of a kind
        dealWin = False
        index = 0
        #if person has 4 of a kind, either the first card and/or the 4th card will be the match
        temp1 = self.otherHand[0].getRank()
        temp2 = self.otherHand[3].getRank()
        #checks player's hand
        temp3 = self.playerHand[0].getRank()
        temp4 = self.playerHand[3].getRank()
        
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        #find the count values
        for i in range(7):
            cardP = self.playerHand[i].getRank()
            cardD = self.otherHand[i].getRank()
            if (cardD == temp1 ):
                count1 = count1 + 1
            elif (cardD == temp2):
                count2 = count2 + 1

            if (cardP == temp3):
                count3 = count3 + 1
            elif (cardP == temp4):
                count4 = count4 + 1

        #checks dealer's hand
        if (count1 == 4):
            for i in range(5):
                self.winningHand.append(self.otherHand[i])
            dealWin = True
        elif (count1 < 4 and count2 == 4):
            dealWin = True
            for i in range(4):
                cardRank = self.otherHand[i].getRank()
                if (cardRank == temp2):
                    index = i
                    break
            for i in range(4):
                self.winningHand.append(self.otherHand[index+i])
            self.winningHand.append(self.otherHand[0])

        #Top ranked card is 4 of a kind
        if (count3 == 4):
            #check for who has a higher 4 of a kind
            if (dealWin):
                for i in range(5):
                    cardP = self.playerHand[i]
                    cardD = self.winningHand[i]
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
        #need to find the 4 of a kind
        elif (count3 < 4 and count4 == 4):
            #gets the index of the first match
            for i in range(4):
                cardRank = self.playerHand[i].getRank()
                if (cardRank == temp4):
                    index = i
                    break

            if (dealWin):
                for i in range(4):
                    cardP = self.playerHand[i+index]
                    cardD = self.winningHand[i]
                    if (cardP.value() > cardD.value()):
                        self.winningHand.clear()
                        for i in range(4):
                            self.winningHand.append(self.playerHand[i+index])
                        #5th card is highest card tiebreaker
                        self.winningHand.append(self.playerHand[0])
                        return "player"
                    elif (cardP.value() < cardD.value()):
                        return "dealer"
                cardP = self.playerHand[0]
                cardD = self.winningHand[5]
                if (cardP.value() > cardD.value()):
                    self.winningHand.clear()
                    for i in range(4):
                        self.winningHand.append(self.playerHand[i+index])
                    #5th card is highest card tiebreaker
                    self.winningHand.append(self.playerHand[0])
                    return "player"
                elif (cardP.value() < cardD.value()):
                    return "dealer"
                return "tie"
            #dealer does not have 4 of a kind
            else:
                for i in range(4):
                    self.winningHand.append(self.playerHand[i+index])
                self.winningHand.append(self.playerHand[0])
        #dealer is only one who won
        elif (count3 < 4 and count4 < 4 and dealWin == True):
            return "dealer"
        #niether won continue to search hands
        return "n"

    def flush(self):
        self.winningHand.clear()
        #variables needed
        p = 5
        otherFlush = []
        player = False
        h = 0
        s = 0
        d = 0
        c = 0
        h2 = 0
        s2 = 0
        d2 = 0
        c2 = 0
        for i in range(7):
            suitP = self.playerHand[i].getSuit()
            suitD = self.otherHand[i].getSuit()
            #running variables to check if one hits 5 
            if (suitP == "s"):
                s = s + 1
            elif (suitP == "h"):
                h = h + 1
            elif (suitP == "d"):
                d = d + 1
            else:
                c = c + 1

            if (suitD == "s"):
                s2 = s2 + 1
            elif (suitD == "h"):
                h2 = h2 + 1
            elif (suitD == "d"):
                d2 = d2 + 1
            else:
                c2 = c2 + 1
        #player flush
        if (h >= 5 or s >= 5 or d >= 5 or c >= 5):
            if (h >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.playerHand[i].getSuit() == "h"):
                        self.winningHand.append(self.playerHand[i])
                        p = p - 1
            elif (s >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.playerHand[i].getSuit() == "s"):
                        self.winningHand.append(self.playerHand[i])
                        p = p - 1
            elif (d >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.playerHand[i].getSuit() == "d"):
                        self.winningHand.append(self.playerHand[i])
                        p = p - 1
            elif (c >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.playerHand[i].getSuit() == "c"):
                        self.winningHand.append(self.playerHand[i])
                        p = p - 1
            
            if (h2 >= 5 or s2 >= 5 or d2 >= 5 or c2 >= 5):
                #check who has higher
                if (h2 >= 5):
                    for i in range(7):
                        if (p == 0): 
                            break
                        elif (self.otherHand[i].getSuit() == "h"):
                            otherFlush.append(self.otherHand[i])
                            p = p - 1
                elif (s2 >= 5):
                    for i in range(7):
                        if (p == 0): 
                            break
                        elif (self.otherHand[i].getSuit() == "s"):
                            otherFlush.append(self.otherHand[i])
                            p = p - 1
                elif (d2 >= 5):
                    for i in range(7):
                        if (p == 0): 
                            break
                        elif (self.otherHand[i].getSuit() == "d"):
                            otherFlush.append(self.otherHand[i])
                            p = p - 1
                elif (c2 >= 5):
                    for i in range(7):
                        if (p == 0): 
                            break
                        elif (self.otherHand[i].getSuit() == "c"):
                            otherFlush.append(self.otherHand[i])
                            p = p - 1
                for i in range(5):
                    cardP = self.winningHand[i]
                    cardD = otherFlush[i]
                    if (cardP.value() > cardD.value()):
                        return "player"
                    elif (cardP.value() < cardD.value()):
                        self.winningHand.clear()
                        for i in range(5):
                            self.winningHand.append(otherFlush[i])
                        return "dealer"
                return "tie"
            else:
                return "player"
                
        #other hand flush
        elif (h2 >= 5 or s2 >= 5 or d2 >= 5 or c2 >= 5):
            if (h2 >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.otherHand[i].getSuit() == "h"):
                        self.winningHand.append(self.otherHand[i])
                        p = p - 1
            elif (s2 >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.otherHand[i].getSuit() == "s"):
                        self.winningHand.append(self.otherHand[i])
                        p = p - 1
            elif (d2 >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.otherHand[i].getSuit() == "d"):
                        self.winningHand.append(self.otherHand[i])
                        p = p - 1
            elif (c2 >= 5):
                for i in range(7):
                    if (p == 0): 
                        break
                    elif (self.otherHand[i].getSuit() == "c"):
                        self.winningHand.append(self.otherHand[i])
                        p = p - 1
            return "dealer"

        else:
            return "n"

    def threeOfKind(self):
        self.winningHand.clear()
        playerWon = False
        dealerWon = False
        dHand = []
        rank1 = self.playerHand[0].getRank()
        for i in range(5):
            rank2 = self.playerHand[i+1].getRank()
            if (rank1 == rank2):
                rank3 = self.playerHand[i + 2].getRank()
                if (rank2 == rank3):
                    playerWon = True
                    self.winningHand.append(self.playerHand[i])
                    self.winningHand.append(self.playerHand[i+1])
                    self.winningHand.append(self.playerHand[i+2])
                    k = 0
                    while (len(self.winningHand) < 5):
                        if (self.playerHand[k].getRank() != rank2):
                            self.winningHand.append(self.playerHand[k])
                        k = k + 1
                else:
                    break
            else:
                rank1 = rank2
        
        rank1 = self.otherHand[0].getRank()
        for i in range(6):
            rank2 = self.otherHand[i+1].getRank()
            if (rank1 == rank2):
                rank3 = self.otherHand[i + 2].getRank()
                if (rank2 == rank3):
                    dealerWon = True
                    dHand.append(self.otherHand[i])
                    dHand.append(self.otherHand[i+1])
                    dHand.append(self.otherHand[i+2])
                    k = 0
                    while (len(dHand) < 5):
                        if (self.otherHand[k].getRank() != rank2):
                            dHand.append(self.otherHand[k])
                        k = k + 1
                else:
                    break
            else:
                rank1 = rank2
        
        if (playerWon and dealerWon == False):
            return "player"
        elif (dealerWon and playerWon == False):
            return "dealer"
        elif (playerWon and dealerWon):
            for i in range(5):
                rank1 = self.winningHand[i]
                rank2 = dHand[i]
                if (rank1 > rank2):
                    return "player"
                elif (rank1 < rank2):
                    self.winningHand.clear()
                    for i in range(5):
                        self.winningHand.append(dHand[i])
                    return "dealer"
            return "tie"

        else:
            return "n"
        

    def pair(self):
        self.winningHand.clear()
        playerWon = False
        dealerWon = False
        dHand = []
        rank1 = self.playerHand[0].getRank()
        for i in range(6):
            rank2 = self.playerHand[i+1].getRank()
            if (rank1 == rank2):
                playerWon = True
                self.winningHand.append(self.playerHand[i])
                self.winningHand.append(self.playerHand[i+1])
                k = 0
                while (len(self.winningHand) < 5):
                    if (self.playerHand[k].getRank() != rank2):
                        self.winningHand.append(self.playerHand[k])
                    k = k + 1
            else:
                rank1 = rank2
        
        rank3 = self.otherHand[0].getRank()
        for i in range(6):
            rank4 = self.otherHand[i+1].getRank()
            if (rank3 == rank4):
                dealerWon = True
                dHand.append(self.otherHand[i])
                dHand.append(self.otherHand[i+1])
                k = 0
                while (len(dHand) < 5):
                    if (self.otherHand[k].getRank() != rank4):
                        dHand.append(self.otherHand[k])
                    k = k + 1
            else:
                rank3 = rank4
        
        if (playerWon and dealerWon == False):
            return "player"
        elif (dealerWon and playerWon == False):
            return "dealer"
        elif (playerWon and dealerWon):
            for i in range(5):
                rank1 = self.winningHand[i]
                rank2 = dHand[i]
                if (rank1 > rank2):
                    return "player"
                elif (rank1 < rank2):
                    self.winningHand.clear()
                    for i in range(5):
                        self.winningHand.append(dHand[i])
                    return "dealer"
            return "tie"

        else:
            return "n"

    def highCard(self):
        self.winningHand.clear()
        #loop through the top 5 ranked cards and see if one hand has a card thats higher
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
                return name, "Royal Flush"
                found = False
        
        if found:
            name = self.straightFlush()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Straight Flush"
                found = False
        
        if found:
            name = self.fourOfKind()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Four of a Kind"
                found = False

        if found:
            name = self.fullHouse()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Full House"
                found = False

        if found:
            name = self.flush()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Flush"
                found = False

        if found:
            name = self.straight()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Straight"
                found = False

        if found:
            name = self.threeOfKind()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Three of a Kind"
                found = False

        if found:
            name = self.twoPair()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "Two Pair"
                found = False

        if found:
            name = self.pair()
            if (name == "player" or name == "dealer" or name == "tie"):
                return name, "One Pair"
                found = False
        
        if found:
            return self.highCard(), "High Card"
            
    #displays to the user what the winning hand was
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
        

