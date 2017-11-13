#Coded by TheSpaceCowboy
#Github: https://www.github.com/thespacecowboy42534
#Date: 13/11/17

#
# This is an example of how the module works
#

#Imports
from CardCounting import cardCounting # Importing the actual card counting class

counting = cardCounting() # Creates an instance of the card counting class

while True: # Repeats this code forever
    while True: # Error handling
        try:
            test = input("input Card: ") # Input the card you would like
            counting.addCount(test) # Add it to the running count
        except ValueError:
            continue
        if(int(test)<= 0 or int(test) >=11):
            continue
        else:
            break
    while True: # Error handling
        try:
            test = int(input("input number of decks remaining")) # Input the number of decks remaining
            counting.setNumOfDecks(test) # Set the current number of decks remianing
        except ZeroDivisionError:
            continue
        if(test<= 0):
            continue
        else:
            break
        
    
    counting.calcTrueCount() # Calculate the true count
    print("Current Count:",counting.getCount()) # Display the running count
    print("Current number of decks: ",counting.getNumOfDecks()) # Display number of decks remaining
    print("True count value:", counting.getTrueCount()) # Display true count
