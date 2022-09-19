# Modeling cards, deck of cards, shuffling, and dealing.
# Based on code example from Think Python, 2nd Edition, Chapter 18.


import random


class Card:
    """Models a standard playing card."""
    
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    value_names = {1: "Ace", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 
                   7 : "7", 8 : "8", 9 : "9", 10 : "10", 11 : "Jack", 
                   12 : "Queen", 13 : "King"}

    def __init__(self, suit=0, value=2) -> None:
        self.suit = suit
        self.value = value

    def __str__(self) -> str:
        return "%s of %s" % (Card.value_names[self.value], 
                             Card.suit_names[self.suit])
    
    def __lt__(self, other):
        """Compares this card to other.   

        Returns: boolean
        """
        t1 = self.value, self.suit
        t2 = other.value, other.suit
        return t1 < t2

    def __eq__(self, other):
        """Checks whether self and other have the same value and suit.

        returns: boolean
        """
        return self.suit == other.suit and self.value == other.value

class CardAH(Card):
    """Models standard playing cards where Aces are high card. """

    Card.value_names = {2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 
                   7 : "7", 8 : "8", 9 : "9", 10 : "10", 11 : "Jack", 
                   12 : "Queen", 13 : "King", 14 : "Ace"}

    def __lt__(self, other):
        """Compares this card to other.   

        Returns: boolean
        """
        t1 = self.value
        t2 = other.value
        return t1 < t2
    
    def __eq__(self, other):
        """Checks whether self and other have the same value.

        returns: boolean
        """
        return self.value == other.value

class Deck:
    """Models a deck of cards."""

    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for value in range(1,14):
                card = Card(suit, value)
                self.cards.append(card)

    def __str__(self) -> str:
        """Returns a string representation of the deck."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
        
    def add_card(self, card):
        """Adds a card to the deck.

        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck or raises exception if it is not there.
        
        card: Card
        """
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card(0))

class DeckAH(Deck):
    """Models a deck of cards where Aces are high card."""

    def __init__(self) -> None:
        self.cards = []
        for suit in range(4):
            for value in range(2,15):
                card = CardAH(suit, value)
                self.cards.append(card)


class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    
    def count_hand(self):
        """Counts number of cards in Hand.

        Returns:
            int: card count
        """
        counter = 0
        for card in self.cards:
            counter +=1
        return counter


if __name__ == "__main__":


    print(CardAH.value_names)
    # card1 = CardAcesHigh(1, 14)
    
    # card2 = CardAcesHigh(1, 13)

    # print(card1, card2)
    # print(card1 > card2)
    
    # deck = Deck()
    # # deck.shuffle()
    # print(deck)

    # hand1 = Hand("Player 1")
    # hand2 = Hand()

    # hand1.add_card
    # deck.move_cards(hand1, 5)
    # deck.move_cards(hand2, 5)
    # hand1.sort()
    # hand2.sort()
    # print(f"Hand1:\n{hand1}\n\n"
    #     f"Hand2:\n{hand2}\n")
    # breakpoint()
    # hand1.move_cards(hand2, )
    
    # print(f"Hand1:\n{hand1}\n\n"
    #     f"Hand2:\n{hand2}\n")