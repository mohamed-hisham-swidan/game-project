from characters.character import Character
from random import randint

class Wolf_man(Character):
    def __init__(self, name, is_alive, hp, damage,mana,real_name):
        super().__init__(name, is_alive, hp, damage,mana,real_name)

    def mana_recovery(self):  #method used for recover mana
        try:
            print(f"{self.name} is barking🐶.")
            ran_mana = randint(3, 8)
            print(f"you got +[{ran_mana}] mana❄️")
            self.mana = self.mana + ran_mana
            return True
        except (KeyError, AttributeError):
            print(f"error!, Pls try again.")
            return False
        except Exception as e:
            print(e)
            return False


    def special_attack_1(self, target):    #special attack
        if self.mana >= 6:        #make sure mana is enough
            print(f"{self.name} is trying to use bite attack on {target.name}.")
            try:
                target.take_damage(self.damage + 8, self.name)
                self.mana = self.mana - 6
                return True
            except (KeyError, AttributeError):
                print(f"error!, Pls try again.")
                return False
            except Exception as e:
                print(e)
                return False

        else:
            rec_mana = 6 - self.mana
            print(f"still need {rec_mana} mana! ")
            return False


    def special_attack_2(self, target):
        if self.mana >= 14:  # make sure mana is enough
            print(f"{self.name} is trying to use die bite attack on {target.name}.")
            try:
                target.take_damage(self.damage + 15, self.name)
                self.mana = self.mana - 14
                return True
            except (KeyError, AttributeError):
                print(f"error!, {target} is not a valid target. Pls try again.")
                return False
            except Exception as e:
                print(e)
                return  False
        else:
            rec_mana = 14 - self.mana
            print(f"still need {rec_mana} mana! ")
            return False

    def show_options(self):
        print("|w:       Normal Attack🐾          |")
        print("|E:   bite Attack (costs 6  mana)  |")
        print("|F:die_bite Attack (costs 14 mana) |")
        print("|Q:        bark🐶 (gain mana❄️)      |")
        print("|R:     healing (costs 5 mana)❤️‍🩹   |")
