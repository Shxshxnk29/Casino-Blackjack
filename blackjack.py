#  Shashank Navale
#  Professor Zhou
#  COP 3502C Project 1 - Blackjack
#  3 June 2023

import p1_random as p1  # imports the provided random module


def main():
    global player_card, card_title  # sets player_card and card_title as global variables
    rng = p1.P1Random()  # creates a rng variable of the P1 random module
    game_counter = 1
    hand = 0
    menu_option = 1
    player_wins = 0
    tie_games = 0
    dealer_wins = 0
    percentage_player_wins = 0
    print("START GAME #" + str(game_counter) + "\n")
    # code above sets up the necessary variables and prints out the "start game #" statement

    while menu_option != 4:  # only runs sequence when menu_option is not equal to 4
        if menu_option == 1:  # only runs sequence if menu_option is equal to 1
            player_card = rng.next_int(13) + 1

            if player_card == 1:
                card_title = "ACE"
            elif player_card == 11:
                card_title = "JACK"
                player_card = 10
            elif player_card == 12:
                card_title = "QUEEN"
                player_card = 10
            elif player_card == 13:
                card_title = "KING"
                player_card = 10
            else:
                card_title = player_card

            hand += player_card
            print("Your card is a " + str(card_title) + "!")
            print("Your hand is: " + str(hand) + "\n")

            '''above code sequence generates a random card for the player and stores it in player_card and also
            calculates the player hand throughout each game, while also printing the current card and hand'''

        if hand == 21:  # sequence runs if hand is equal to 21 exactly
            print("BLACKJACK! You win!\n")
            player_wins += 1
            game_counter += 1
            player_card = rng.next_int(13) + 1

            if player_card == 1:
                card_title = "ACE"
            elif player_card == 11:
                card_title = "JACK"
                player_card = 10
            elif player_card == 12:
                card_title = "QUEEN"
                player_card = 10
            elif player_card == 13:
                card_title = "KING"
                player_card = 10
            else:
                card_title = player_card
            #  above sequence labels the face cards with its respective titles

            hand = 0
            hand += player_card

            menu_option = 1
            print("START GAME #" + str(game_counter) + "\n")
            print("Your card is a " + str(card_title) + "!")
            print("Your hand is: " + str(hand) + "\n")

            '''above code sequence runs after a game is won by the player by BLACKJACK, it adds 1 to the player_wins
            and game_counter to indicate game has been won and completed, and then it continues to the next game'''

        if hand > 21:  # sequence runs only when hand is greater than 21
            print("You exceeded 21! You lose.\n")
            dealer_wins += 1
            game_counter += 1
            player_card = rng.next_int(13) + 1

            if player_card == 1:
                card_title = "ACE"
            elif player_card == 11:
                card_title = "JACK"
                player_card = 10
            elif player_card == 12:
                card_title = "QUEEN"
                player_card = 10
            elif player_card == 13:
                card_title = "KING"
                player_card = 10
            else:
                card_title = player_card
            #  above sequence labels face cards with its respective titles
            hand = 0
            hand += player_card
            menu_option = 1
            print("START GAME #" + str(game_counter) + "\n")
            print("Your card is a " + str(card_title) + "!")
            print("Your hand is: " + str(hand) + "\n")
            '''Let's the player know that they have lost the round due to going over 21, adds +1 to the necessary
            variables, and the continues to the next round of the game'''

        print("1. Get another card \n2. Hold hand\n3. Print statistics\n4. Exit\n")  # prints the options menu
        menu_option = int(input("Choose an option: "))  # stores user input into the menu_option variable
        while menu_option < 1 or menu_option > 4:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.\n")
            print("1. Get another card \n2. Hold hand\n3. Print statistics\n4. Exit\n")
            menu_option = int(input("Choose an option: "))
        # above code sequence checks to ensure user input for menu_option is only within 1 and 4

        print()

        if menu_option == 2:  # sequence runs when user inputs 2
            dealer_card = rng.next_int(11) + 16
            print("Dealer's hand: " + str(dealer_card))
            print("Your hand is: " + str(hand))
            # above code sequence generates a card for the dealer and prints the dealer and player card values

            if (dealer_card <= 21) and (dealer_card > hand):
                print("Dealer wins!\n")
                dealer_wins += 1
                hand = 0
                game_counter += 1
                print("START GAME #" + str(game_counter) + "\n")
                menu_option = 1
                '''above code sequence runs when dealer's hand is greater than player hand but both less than 21
                it then lets player know that the dealer won, adds +1 to and resets necessary variables, and starts the 
                next game'''

            if dealer_card > 21 >= hand:
                print("You win!\n")
                player_wins += 1
                hand = 0
                game_counter += 1
                print("START GAME #" + str(game_counter) + "\n")
                menu_option = 1
                '''above code sequence runs when player's hand is greater than dealer hand, lets player know they won
                and adds +1 / resets necessary variables, and then starts the next round of the game'''

            if dealer_card == hand:  # code sequence runs when dealer hand equals player hand
                print("It's a tie! No one wins!\n")
                tie_games += 1
                hand = 0
                game_counter += 1
                print("START GAME #" + str(game_counter) + "\n")
                menu_option = 1
                '''above code sequence lets player know the game has been tied, adds +1 /resets to necessary variables
                and starts the next game'''

        if menu_option == 3:  # code sequence runs when user inputs option 3 for game statistics
            game_counter -= 1  # fixes the game counter
            percentage_player_wins = (player_wins / game_counter) * 100  # calculates the player win percentage as float
            print("Number of Player wins: " + str(player_wins))
            print("Number of Dealer wins: " + str(dealer_wins))
            print("Number of tie games: " + str(tie_games))
            print("Total # of games played is: " + str(game_counter))
            print("Percentage of Player wins: " + str(percentage_player_wins) + "%\n")
            menu_option = 3
            # above code sequence prints out the necessary statistics when user inputs option 2


main()  # runs the main function
