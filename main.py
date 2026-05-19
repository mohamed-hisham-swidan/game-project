from engine import *
from menus.menus import main_menu, game_mode_menu, bot_mode_menu



def main():
 player1_name = ""
 player2_name = ""
 while True :
    main_menu()
    main_menu_choice = input("enter your choice: ")  #ask user if he want to start game or exit
    if main_menu_choice == "1":
        game_mode_menu()
        game_tir_choice = input("enter your choice: ")

        if game_tir_choice == "1":                            # ask user about game tir
            while player1_name == "" or player2_name == "":
                player1_name = input("enter your name🧒: ").strip()
                player2_name = input("enter your friend name👦: ").strip()   #ask users for username and chars
            print("lodding...")
            sleep(1)
            player1_char = choose_character(player1_name)
            player2_char = choose_character(player2_name)
            print(f"{player1_name} you choose {player1_char.name} \n{player2_name} you choose {player2_char.name}")
            print()
            sleep(2)
            start_game_friend(player1_name, player2_name, player1_char, player2_char)
            chars = (player1_char, player2_char)
        elif game_tir_choice == "2":
            print("lodding...")
            sleep(2)
            while True:
                bot_mode_menu()
                bot_mode_choice = input("enter your choice: ")
                if bot_mode_choice == "1":
                    bot_name = "easy_bot"
                    break
                elif bot_mode_choice == "2":
                    bot_name = "medium_bot"
                    break
                elif bot_mode_choice == "3":
                    print("sorry sir, hard mode is not available yet, please choose another mode.")
                    continue
                else:
                    print("Invalid choice. Please try again.")

            player1_name = input("enter your name🧒: ")
            player1_char = choose_character(player1_name)
            bot_char = bot_choice()
            sleep(2)
            start_game_bot(player1_name, bot_name, player1_char, bot_char)



        else:
            print("Invalid choice. Please try again.")

    elif main_menu_choice == "2":
        show_leaderboard()
        sleep(2)



    elif main_menu_choice == "3":
        print("Exiting the game...")
        sleep(1)
        break


    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

