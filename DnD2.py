# DND2.py

class Character:
    def __init__(self):
        self.strength = True

class Monster:
    def __init__(self):
        self.monsterStrength = True

player_name = []
player_strength = []
num_characters = int(input("Please enter the number of characters you wish to have: "))

for i in range(num_characters):
    name = input("Please enter a name: ")
    player_name.append(name)
    name = Character()
    char_strength = int(input("Please enter " + player_name[i] + "'s" + " strength: "))
    player_strength.append(char_strength)
    name.strength = char_strength

monster_list = []
monster_name = input("Please enter the monsters Name: ")
monster_list.append(monster_name)
monster_name = Monster()
monster_strength = int(input("please enter the monsters strength: "))
monster_name.monsterStrength = monster_strength   


for i in range(num_characters):
    print(player_name[i], "is fighting", monster_list[0])
    if player_strength[i] < monster_name.monsterStrength:
        print(monster_list[0], "wins")
        monster_name.monsterStrength = monster_name.monsterStrength - player_strength[i]
        print("Monsters strength: ", monster_name.monsterStrength)
    else:
        print(player_name[i], "wins!!!")
        break

    




