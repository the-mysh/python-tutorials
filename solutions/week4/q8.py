import sys
import random

hand_size = 5
num_hands = int(sys.argv[1])
# We will assume that n is small enough (<= 10) such that we will not
# run out of cards

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

cards = []
# Each card is represented by a pair (list of length 2) of a value and
# a suit. We will build up the full list by looping over all the suits
# and values, and recording each combination.
for suit in suits:
    for value in values:
        cards.append([value, suit])

# Now we shuffle
random.shuffle(cards)


# Finally, we deal by giving each person the next five cards in sequence
for i in range(num_hands):
    print("Hand {}: ".format(i), end="")
    # recall the end keyword is used to prevent print from moving to a
    # new line
    for i in range(hand_size):
        card = cards.pop(0) # remove a card from top of the deck
        # Cards are lists of the form [value, suit]
        value = card[0]
        suit = card[1]
        print("{} of {}, ".format(value, suit), end="")

    print("") # move onto next line
