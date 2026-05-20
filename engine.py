import json
from time import sleep
from random import choice, randint  # ADD THIS LINE
from characters.cat_girl import Cat_girl
from characters.wolf_man import Wolf_man
from bot.easy_bot import easy_bot
from bot.medium_bot import medium_bot
from data_manager import update_stats



def show_leaderboard():
    file_path = "data/game_stats.json"
    try:
        with open(file_path, "r") as f:
            stats = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No stats available yet.")
        return

    # Prepare leaderboard: sort by number of wins (descending)
    leaderboard = sorted(
        stats.items(),
        key=lambda item: item[1].get("wins", 0),
        reverse=True
    )

    print("\n" + "="*30)
    print("        Leaderboard")
    print("="*30)
    print(f"{'Player':<15}{'Wins':<8}{'Games':<8}{'Win Rate':<8}")
    print("-"*30)
    for player, data in leaderboard:
        wins = data.get("wins", 0)
        games = data.get("games_played", 0)
        win_rate = f"{(wins/games*100):.1f}%" if games > 0 else "N/A"
        print(f"{player:<15}{wins:<8}{games:<8}{win_rate:<8}")
    print("="*30 + "\n")
    # test








def choose_character(name):  # ask user for char he want to play with
    print(" [1] meow-meow🐈‍⬛ the cat mid hp high damage special technique: claw attack🦞")
    sleep(.3)
    print(" [2] wolly🐺 the wolf high hp mid damage special technique: bite attack😮")
    sleep(.3)
    print("-" * 20)
    print()

    while True:
        user_choice = input(f"{name} choose your character>> ...  ").strip()
        if user_choice == "1":
            print(f"{name}  successfully choose [meow_meow🐈‍⬛]")
            return Cat_girl(f"{name}'s Cat", True, 60, 10, 5, "meow_meow")
        elif user_choice == "2":
            print(f"{name} you successfully choose [wolly🐺]")
            return Wolf_man(f"{name}'s Wolf", True, 80, 7, 5,"wolly")
        else:
            print("invalid choice!, you have to choose [1-2]")


def bot_choice():  # randomly set bot choice
    meow_meow = Cat_girl("bot's cat", True, 60, 10, 5, "meow_meow")
    wolly = Wolf_man("bot's wolf", True, 80, 7, 5, "wolly")

    # but them in a dictionary to easy access them
    characters = {
        "meow-meow": meow_meow,
        "wolly": wolly}

    selected_char = choice(list(characters.values()))  # Store the result

    if selected_char == meow_meow:
        print("the bot successfully choose [meow_meow🐈‍⬛]")
    else:
        print("the bot successfully choose [wolly🐺]")

    return selected_char  # Return the character


def switch_turns(current_player,player1, player2, char1, char2):
    try:
        if current_player == player1 :
            return player2, char2, char1
        elif current_player == player2 :
            return player1, char1, char2
        else:
            print("error in switch turns function")
            return None, None, None
    except Exception as e:
        print(f"error in switch turns function: {e}")



def show_battlefield(char1, char2): # print two char statu table
    lines1 = char1.get_details_lines()
    lines2 = char2.get_details_lines()

    print(f"{'YOUR STATS':<25} | {'OPPONENT STATS':<25}")
    print("=" * 50)

    for l1, l2 in zip(lines1, lines2):
        print(f"{l1:<25} | {l2:<25}")
    print()

def game_logic(user_choice,current_turn_char,other_turn_char):
    is_done = False
    if user_choice == "Q":
        is_done = current_turn_char.mana_recovery()
        sleep(1)
    elif user_choice == "W":
        is_done = current_turn_char.normal_attack(other_turn_char)
        sleep(1)
    elif user_choice == "E":
        is_done = current_turn_char.special_attack_1(other_turn_char)
        sleep(1)
    elif user_choice == "F":
        is_done = current_turn_char.special_attack_2(other_turn_char)
        sleep(1)
    elif user_choice == "R":
        is_done = current_turn_char.healing()
        sleep(1.75)
    elif user_choice == "/KILL":
        other_turn_char.take_damage(other_turn_char.hp, current_turn_char.name)
        is_done = True
    else:
        print("invalid choice! you have to choose from the options above")
        is_done = False
    return is_done





def start_game_bot(player_name, bot_name, player_char, bot_char):

    ran_num = randint(1, 2)
    if ran_num == 1:
        current_turn_char, current_turn_player = player_char, player_name
        other_turn_char, other_turn_player = bot_char, bot_name
    else:
        current_turn_char, current_turn_player = bot_char, bot_name
        other_turn_char, other_turn_player = player_char, player_name

    while True:
        if player_char.hp <= 0:
            sleep(1)
            print(f"{bot_name} won the game!🎉")
            update_stats(player_name, won=False)
            break
        elif bot_char.hp <= 0:
            sleep(1)
            print(f"{player_name} won the game!🎉")
            update_stats(player_name, won=True)
            break
        print()
        sleep(1)
        print(f"🔥 {current_turn_player}, it is your turn!")
        if current_turn_player == bot_name:
            sleep(1)
            print("the bot is thinking...")
            sleep(2.5)
            if bot_name == "easy_bot" :
              bot_move = easy_bot()
            elif bot_name == "medium_bot" :
              bot_move = medium_bot(other_turn_char, bot_char)


            is_done = game_logic(bot_move, current_turn_char, other_turn_char)
        else:
            show_battlefield(current_turn_char, other_turn_char)
            sleep(1.5)
            current_turn_char.show_options()
            print()
            user_choice = input(">>").upper()
            print()
            is_done = game_logic(user_choice, current_turn_char, other_turn_char)
        if is_done:
            current_turn_player, current_turn_char, other_turn_char = switch_turns(current_turn_player, player_name, bot_name, player_char, bot_char)
        else:
            continue


def start_game_friend(player1, player2, char1, char2): #start the main game
    ran_num = randint(1, 2)
    if ran_num == 1:
        current_turn_char, current_turn_player = char1, player1
        other_turn_char, other_turn_player = char2, player2
    else:
        current_turn_char, current_turn_player = char2, player2
        other_turn_char, other_turn_player = char1, player1

    while True:
        if char1.hp <= 0:
            sleep(1)
            print(f"player {player2} won the game!🎉")
            update_stats(player2, won=True)
            update_stats(player1, won=False)


            break
        elif char2.hp <= 0:
            sleep(1)
            print(f"player {player1} won the game!🎉")
            update_stats(player1, won=True)
            update_stats(player2, won=False)
            break
        print()
        sleep(1)
        print(f"🔥 {current_turn_player}, it is your turn!")
        show_battlefield(current_turn_char, other_turn_char)  # print two char statu table
        sleep(1.5)
        current_turn_char.show_options()
        print()
        user_choice = input(">>").upper()
        print()
        is_done = game_logic(user_choice, current_turn_char, other_turn_char)
        if is_done:
            current_turn_player, current_turn_char, other_turn_char = switch_turns(current_turn_player, player1, player2, char1, char2)
        else:
            continue




