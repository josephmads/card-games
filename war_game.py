# The card game "War"

# Rules:
# 1. Deal entire Deck between the two players.
# 2. Each player places flips top card face up.
# 3. PLayer with the highest card wins both cards and returns card to the 
# bottom of their deck.
# 4. If players flip cards of the same value it starts a war. Each player 
# places three more cards face down and flips a fourth card face up. 
# 5. PLayer with the highest card wins all the cards and returns them to the 
# bottom of their deck.
# 6. If players tie again the war is repeated until one player flips a higher
# value card.
# 7. The player who collects all 52 cards wins the game.

import cards as c
from time import sleep

def card_flip(hand1, hand2):
    """Gameplay function.

    Args:
        hand1 (Hand): Player 1's hand
        hand2 (Hand): PLayer 2's hand

    Returns:
        Hand: winning player adds all cards to their hand.
    """
    war_hand = c.Hand()

    flip1 = hand1.pop_card(0)
    flip2 = hand2.pop_card(0)
    print(f"Player 1 flips: {flip1}")
    print(f"Player 2 flips: {flip2}")
    sleep(1)

    if flip1 > flip2:
        print("Player 1 wins the hand!")      
        return hand1.add_card(flip1), hand1.add_card(flip2)

    elif flip1 < flip2:
        print("Player 2 wins the hand!")      
        return hand2.add_card(flip1), hand2.add_card(flip2)

    elif flip1 == flip2:
        print("\nA war has started!")
        war = True

        while war == True:
            war_hand.add_card(flip1), war_hand.add_card(flip2)
            input("Hit Enter to play 4 more cards each...")
            print("1... 2... 3... FLIP!")
            hand1.move_cards(war_hand, 3)
            hand2.move_cards(war_hand, 3)

            flip1 = hand1.pop_card(0)
            flip2 = hand2.pop_card(0)
            print(f"Player 1 flips: {flip1}")
            print(f"Player 2 flips: {flip2}")

            if flip1 > flip2:
                print("Player 1 wins this war!")
                war = False
                war_hand.add_card(flip1), war_hand.add_card(flip2)
                counter = war_hand.count_hand()
                return war_hand.move_cards(hand1, counter)

            elif flip1 < flip2:
                print("Player 2 wins this war!")
                war = False
                war_hand.add_card(flip1), war_hand.add_card(flip2)
                counter = war_hand.count_hand()
                return war_hand.move_cards(hand2, counter)

            elif flip1 == flip2:
                print("The war continues...")
                continue

def final_four(hand1, hand2):
    """Gameplay function for when a player has less than 4 cards left.

    Args:
        hand1 (Hand): Player 1's hand
        hand2 (Hand): PLayer 2's hand

    Returns:
        Hand: winning player adds all cards to their hand.
    """
    war_hand = c.Hand()

    flip1 = hand1.pop_card(0)
    flip2 = hand2.pop_card(0)
    print(f"Player 1 flips: {flip1}")
    print(f"Player 2 flips: {flip2}")
    sleep(1)

    if flip1 > flip2:
        print("Player 1 wins the hand!")      
        return hand1.add_card(flip1), hand1.add_card(flip2)

    elif flip1 < flip2:
        print("Player 2 wins the hand!")      
        return hand2.add_card(flip1), hand2.add_card(flip2)

    elif flip1 == flip2:
        print("\nA war has started!")
        war = True

        while war == True:
            war_hand.add_card(flip1), war_hand.add_card(flip2)
            input("Hit Enter to play 1 more card each...")

            flip1 = hand1.pop_card(0)
            flip2 = hand2.pop_card(0)
            print(f"Player 1 flips: {flip1}")
            print(f"Player 2 flips: {flip2}")

            if flip1 > flip2:
                print("Player 1 wins this war!")
                war = False
                war_hand.add_card(flip1), war_hand.add_card(flip2)
                counter = war_hand.count_hand()
                return war_hand.move_cards(hand1, counter)

            elif flip1 < flip2:
                print("Player 2 wins this war!")
                war = False
                war_hand.add_card(flip1), war_hand.add_card(flip2)
                counter = war_hand.count_hand()
                return war_hand.move_cards(hand2, counter)

            elif flip1 == flip2:
                print("The war continues...")
                continue

def main():
    """Main program function. Starts the game of War."""
    
    deck = c.DeckAH()
    deck.shuffle()

    player1 = c.Hand()
    player2 = c.Hand()

    deck.move_cards(player1, 26)
    deck.move_cards(player2, 26)

    score1 = player1.count_hand()
    score2 = player2.count_hand()

    game = True

    print("""
     .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. |
    | | _____  _____ | || |      __      | || |  _______     | |
    | ||_   _||_   _|| || |     /  \     | || | |_   __ \    | |
    | |  | | /\ | |  | || |    / /\ \    | || |   | |__) |   | |
    | |  | |/  \| |  | || |   / ____ \   | || |   |  __ /    | |
    | |  |   /\   |  | || | _/ /    \ \_ | || |  _| |  \ \_  | |
    | |  |__/  \__|  | || ||____|  |____|| || | |____| |___| | |
    | |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------' 

                            THE CARD GAME
    """)

    sleep(3)

    while game == True:
        input("\nHit Enter to flip a card...")

        if score1 and score2 > 4:
            card_flip(player1, player2)
        else:
            final_four(player1, player2)

        score1 = player1.count_hand()
        score2 = player2.count_hand()
        if score1 == 52:
            game = False
            print("Player 1 wins!")
        elif score2 == 52:
            game = False
            print("Player 2 wins!")
        else:
            pass
        sleep(1)
        print(f"\nSCORE\nPlayer 1: {score1} | Player 2: {score2}")

if __name__ == "__main__":     
    main()
