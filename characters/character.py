from random import randint

class Character:
    def __init__(self, name, is_alive, hp, damage,mana,real_name):
        self.name = name

        self.is_alive = is_alive
        self.hp = int(hp)
        self.damage = damage
        self.mana = int(mana)
        self.real_name = real_name

    def get_details_lines(self):
        lines = [
            f"Name:   {str(self.name):<12}",
            f"Status: {str(self.is_alive):<12}",
            f"HP:     {str(self.hp):<12}❤️",
            f"Damage: {str(self.damage):<12}",
            f"Mana:   {str(self.mana):<12}❄️",
            "--------------------"
        ]
        return lines

    def show_single_table(self):
        """Displays character stats in a formatted box"""
        width = 30
        # Top border
        print("+" + "-" * (width - 2) + "+")

        # Header with character name
        header = f" {self.name.upper()} STATS "
        print(f"|{header.center(width - 2)}|")

        # Separator
        print("+" + "-" * (width - 2) + "+")

        # Data rows
        stats = [
            ("Status", self.is_alive),
            ("HP", self.hp),
            ("Damage", self.damage),
            ("Mana", self.mana)
        ]

        for label, value in stats:
            # Formatting label to left and value to right
            row = f" {label:<10} : {str(value):>10} "
            print(f"|{row.center(width - 2)}|")

        # Bottom border
        print("+" + "-" * (width - 2) + "+")
        print()

    def normal_attack(self,target):   #the main attack of charcter
        print(f"{self.name} is trying to attack {target.name}.")
        try:
           target.take_damage(self.damage, self.name)
           self.mana = self.mana + 2
           print("+[2] mana")
           return True

        except (KeyError, AttributeError):
           print(f"error!, {target} is not a valid target. Pls try again.")
           return False

        except Exception as e :
            print(e)
            return False

    def take_damage(self, damage, attacker):
        try:

            if self.hp <= 0:      #cheak hp to know if the char is already dead or not
             self.hp = 0
             print(f"💀 {self.name} is now dead.")
            else:
             self.hp = self.hp - damage
             print(f"{self.name} had been attacked by {attacker}.")
             print(f"{self.name} has {self.hp} HP left.")
             if self.hp <= 0 :
                 print(f"{self.name} has been killed by {attacker}💀.")

        except AttributeError:
            print("error!, Pls try again.")

        except Exception as e :
            print(e)



    def healing(self):
        if self.mana >= 5:   # make sure mana is enough
            try:
                self.mana = self.mana - 5
                print(f"{self.name} is healing❤️‍🩹.")
                ran_hp = randint(5, 12)
                print(f"{self.name} got +[{ran_hp}] hp!")
                self.hp = self.hp+ ran_hp
                return True
            except (KeyError, AttributeError):
                print(f"error!, Pls try again.")
                return False
            except Exception as e :
                print(e)
                return False
        else:
            rec_mana = 5 - self.mana
            print(f"still need {self.mana} mana! ")
            return False




