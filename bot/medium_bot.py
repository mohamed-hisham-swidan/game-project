from bot.easy_bot import easy_bot
"""
|w:       Normal Attack🐾10/7            |
|E:  special_attack_1 (costs 5/6 mana) (damage 15/12)  |
|F: special_attack_2 (costs 10/14 mana )(damage 25/22 )|
|Q:        (gain mana❄️)                 |
|R:     healing (costs 5 mana)❤️‍🩹         |
"""


def medium_bot(other_turn_char,bot_char):
        if other_turn_char.hp <= bot_char.damage:
            return "W"
        elif bot_char.mana >= 5 and  other_turn_char.hp <= bot_char.damage+5 and bot_char.real_name == "meow_meow":
            return "E"
        elif bot_char.mana >= 6 and  other_turn_char.hp <= bot_char.damage+5 and bot_char.real_name == "wolly":
            return "E"
        elif bot_char.mana >= 10 and other_turn_char.hp <= bot_char.damage + 15 and bot_char.real_name == "meow_meow":
            return "F"
        elif bot_char.mana >= 14 and other_turn_char.hp <= bot_char.damage + 15 and bot_char.real_name == "wolly":
            return "F"
        elif bot_char.hp <= bot_char.damage + 15 and  bot_char.mana >= 5:
            return "R"
        elif bot_char.mana < 3:
            return "Q"
        else:
            return easy_bot(bot_char)
