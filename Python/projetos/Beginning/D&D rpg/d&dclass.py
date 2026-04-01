import time   
import random 

def rpg_class():
    print("==========D&D RPG SYSTEM==========")
    time.sleep(2)
    print("Welcome to my D&D rpg system")
    time.sleep(2)
    print("You need to choose your class and your weapon")
    time.sleep(2)
    print("After that you will need to fight some enemies")
    time.sleep(1)

    print("=======1 - Rogue==========")
    print("=======2 - Mage===========")
    print("=======3 - Sorcerer=======")
    print("=======4 - Paladin========")
    dnd_class = int(input("\nChoose a class to start the game: "))
    print("=========================================================")
    time.sleep(1)

    if dnd_class == 1:
        print("You are a Rogue!")
    elif dnd_class == 2:
        print("You are a Mage!")
    elif dnd_class == 3:
        print("You are a Sorcerer!")   
    elif dnd_class == 4:
        print("You are a Paladin!") 

def dnd_races():
    print("============================================")
    print("Now you will need to choose your race")
    print("1 - Human")
    print("2 - Elf")
    print("3 - Dwarf")
    print("4 - Dragonborn")
    print("5 - Half-Orc")
    print("============================================")
    races = int(input("Choose a race please: "))

    if races == 1:
        print("You are a Human!")
    elif races == 2:
        print("You are an Elf")
    elif races == 3:
        print("You are a Dwarf")
    elif races == 4:
        print("You are a Dragonborn")
    elif races == 5:
        print("You are a Half-Orc")

def combat():
    
    def attack():
        return random.randint(5, 15)
    
    player_health = 50
    enemy_health = 45

    print("\n==========FIGHT YOUR ENEMY!!==========")
    
    while player_health > 0 and enemy_health > 0:
        input("\nPress ENTER to attack...")

        player_damage = attack()
        enemy_health -= player_damage
        print(f"You dealt {player_damage} damage!")
        print(f"Enemy HP: {max(enemy_health, 0)}")
        time.sleep(1.5)

        if enemy_health <= 0:
            print("===========YOU WON THE GAME!!===================")
            print("You have defeated your enemy, congratulations!")
            print("================================================")
            break

   
        enemy_damage = attack()
        player_health -= enemy_damage
        print(f"You have taken {enemy_damage} damage!")
        print(f"Your HP: {max(player_health, 0)}")

        if player_health <= 0:
            print("===========YOU LOST THE GAME!!===================")
            print("Game Over!")
            print("================================================")
            break

rpg_class()
dnd_races()
combat()