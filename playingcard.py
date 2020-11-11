from random import *
class PlayingCard:

    #defines the variables
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        
        
    #returns the rank of the card
    def getRank(self):
        return self.rank
    #returns the suit of the card
    def getSuit(self):
        if self.suit == "s":
            self.card = "Spades"
        elif self.suit == "d":
            self.card = "Diamonds"
        elif self.suit == "c":
            self.card = "Clubs"
        else:
            self.card = "Hearts"
            
        return self.suit
    #returns the blackjack value of the card
    def value(self):
        if 11 <= self.rank <= 13:
            return 10
        elif self.rank == 1:
            return 11
        else:
            return self.rank
        
    #turns the card into a string name that has a friendly output
    def __str__(self):
        numNames = ["0","Ace","Two","Three","Four","Five","Six","Seven","Eight",
                    "Nine","Ten","Jack","Queen","King"]
        CardNum = numNames[self.rank]
        CardName = CardNum + " of " + self.card
        return CardName


def main():
    card= PlayingCard(randrange(0,14),"d")
    print(card.getSuit())
    print(card.getRank())
    print(card.value())
    print(card.__str__())


if __name__ == "__main__": 
    main()
