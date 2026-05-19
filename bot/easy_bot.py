from random import choice


def easy_bot(bot_char):
    if bot_char.mana > 14 and bot_char.real_name == "wolly":
        options = ["E", "Q", "F", "W", "R", "W"]
        return choice(options)
    elif bot_char.mana >= 6 and  bot_char.real_name == "wolly":
        options = ["E", "Q", "W", "R", "W"]
        return choice(options)
    elif  bot_char.mana > 10 and bot_char.real_name == "meow_meow":
        options = ["E", "Q", "F", "W", "R", "W"]
        return choice(options)
    elif bot_char.mana >= 5 and bot_char.real_name == "meow_meow":
        options = ["E", "Q", "W", "R", "W"]
        return choice(options)
    else:
        options = ["Q", "W", "W"]
        return choice(options)

















