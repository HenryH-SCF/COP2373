# Henry Huitema

import random
import re

class Deck():
    def __init__(self, n_decks = 1):
        self.card_list = [num + suit
                          for suit in "\u2665\u2666\u2663\u2660"
                          for num in "A23456789TJQK"
                          for deck in range(n_decks)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    def deal(self):
        if len(self.card_list) <1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print("Reshuffling!")

        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)

        return new_card

    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()

def dealHand(deck, hand):
    # Take a Deck object (deck) and list (hand), deal from deck until hand has five cards, then return hand
    while len(hand) < 5:
        hand.append(deck.deal())

    return hand

def removeCards(hand):
    regexPattern = r"\d"
    # Uses regex to create a list of all digits found in the user's input
    cardsRemoved = re.findall(regexPattern, input("Please input the positions of the cards you'd like to"
                                                  " discard. (1-5) "))
    # Converts the raw output of re.findall from a list of strings to a list of integers
    for i in range(len(cardsRemoved)):
        cardsRemoved[i] = int(cardsRemoved[i])

    # Rearranges the user-supplied cards to descending order, from last to first. This is done
    # because removing a card displaces all the cards to its right in the list. By removing the
    # rightmost selections first, this displacement becomes a non-issue.
    cardsRemoved.sort(reverse=True)
    for position in cardsRemoved:
        if position <= len(hand):
            del hand[position-1]

def main():
    dk = Deck(1)
    current_hand = []
    # Initial deal
    dealHand(dk, current_hand)
    for card in current_hand:
        print(card, end = ' ')
    # Prompt user to discard cards
    removeCards(current_hand)
    # Deal cards back to the user until their hand has five cards again
    dealHand(dk, current_hand)
    for card in current_hand:
        print(card, end = ' ')

if __name__ == "__main__":
    main()