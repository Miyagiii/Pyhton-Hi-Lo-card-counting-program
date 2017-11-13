#Coded by TheSpaceCowboy
#Github: https://www.github.com/thespacecowboy42534
#Date: 13/11/17

#
# Actual Module
# Note: Based of this information: https://www.blackjackapprenticeship.com/resources/how-to-count-cards/
#

class cardCounting: # Creates the class cardCounting
    
    def __init__(self): # Intializes the clas
        self.trueCount = 0 # True count for displaying and using the true count for calculations
        self.count = 0 # Count for storing the current count of the game
        self.numOfDecks = 0 # Number of decks remaining
        
    def calcTrueCount(self): # Calculate the true count of the current game
        self.trueCount = self.count/self.numOfDecks # To calculate the true count of the game you divide the current count with the amount of decks remaining, this is used if multiple decks are being used in a game
        
    def getTrueCount(self):  # Basic getter
        return self.trueCount
    
    def setNumOfDecks(self,numOfDecks : int): # Basic setter
        self.numOfDecks = numOfDecks
        
    def getNumOfDecks(self): # Basic getter
        return self.numOfDecks
    
    def addCount(self, card): # Used for adding the count to the game
        if(card == "J" or card == "Q" or card == "K" or card == "A" or int(card) == 10): # If the card is a high card -1 from the current count also doubles as a filter for strings
            self.count -= 1
            return
        if(int(card) >=2 and int(card) <=6): # If it isn't a high card or a string and is between 2 and 6 its an advantage to player
            self.count += 1
        elif( int(card) >=7 and int(card) <= 9): # 7 to 9 are neutral cards and favour no one
            self.count +=0
    def getCount(self): # Basic getter
        return self.count
        
