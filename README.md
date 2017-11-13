# Pyhton Hi-Lo card counting program

# Purpose
This is a simple Hi-Lo black jack card counting program written in python.
# Benifits
It's modular to it can be easily intergrated into other programs, look at the example program for an example program.
# How to use
It's quite straight forward.<br/>
step 1. Import the module ```from CardCounting import cardCounting```<br/>
step 2. Create an instance ```instance = cardCounting()```<br/>
step 3. Input the card you want ```counting.addCount(input(number))```<br/>
step 4. Input the remaining decks ``` counting.setNumOfDecks(input(number))```<br/>
step 5. Calculate the true count ```counting.calcTrueCount()```<br/>
step 6. Display information however you like:

    print("Current Count:",counting.getCount())
    print("Current number of decks: ",counting.getNumOfDecks())
    print("True count value:", counting.getTrueCount())
# Additional notes
All the information I got for card counting was from https://www.blackjackapprenticeship.com/resources/how-to-count-cards/ go there to find out more.

