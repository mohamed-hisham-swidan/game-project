from characters.character import Character
from random import randint


class Cat_girl(Character):
    def __init__(self, name,is_alive,hp, damage,mana,real_name):
        super().__init__(name, is_alive,hp,damage,mana,real_name)

    def mana_recovery(self):
        try:
            print(f"{self.name} is meowing🐱.")
            ran_mana = randint(2, 7)
            print(f"you got +[{ran_mana}] mana️️️️❄️")
            self.mana = self.mana + ran_mana
            return True
        except (KeyError, AttributeError):
            print(f"error!, Pls try again.")
            return False
        except Exception as e:
            print(e)
            return False


    def special_attack_1(self, target):
        if self.mana >= 5:      #make sure mana is enough
            print(f"{self.name} is trying to use claw attack on {target.name}.")
            try:
                target.take_damage(self.damage + 5, self.name)
                self.mana = self.mana - 5
                return True
            except (KeyError, AttributeError):
                print(f"error!, {target} is not a valid target. Pls try again.")
                return False
            except Exception as e:
                print(e)
                return False
        else:
            rec_mana = 5 - self.mana
            print(f"still need {rec_mana} mana! ")
            return False


    def special_attack_2(self, target):
        if self.mana >= 10:             #make sure mana is enough
            print(f"{self.name} is trying to use die claw attack on {target.name}.")
            try:
                target.take_damage(self.damage + 15, self.name)
                self.mana = self.mana - 10
                return True

            except (KeyError, AttributeError):
                print(f"error!, {target} is not a valid target. Pls try again.")
                return False
            except Exception as e:
                print(e)
                return False
        else:
            rec_mana = 10 - self.mana
            print(f"still need {rec_mana} mana! ")
            return False



    def show_options(self):
        print("|w:       Normal Attack🐾          |")
        print("|E:    law Attack (costs 5 mana)   |")
        print("|F:Die Claw Attack (costs 10 mana) |")
        print("|Q:        Meow🐈(gain mana❄️)     |")
        print("|R:     healing (costs 5 mana)❤️‍🩹   |")



