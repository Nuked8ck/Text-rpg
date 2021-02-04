import random 
from time import sleep

#heroes
class fighter(object):
    hp = 1
    armor = 100
    strength = 10
    magic = 1
    
#enemies
class orc(object):
    name = "Orc"
    hp = 100
    armor = 75
    strength = 10

class giantRat(object):
    name = "Giant Rat"
    hp = 75
    armor = 25
    strength = 6

class thief(object):
    name = "Thief"
    hp = 90
    armor = 50
    strength = 5

def gameOver(character):
    if character.hp < 1:
        print("You ran out of hp...")
        print("Your character falls over and die")
        print("Thank you for playing the game")
        exit()

def intro():
    print("Welcome to the world of textia!")
    nameCha = input("Please enter the name for your character: ")
    start = input("Please click on '1' to start the adventure!!")
    if start == "1":
          character = fighter
          print("Nice to meet you", nameCha, "!! You will be playing as a fighter!... These are your stats!")
          print("Hit points: ", character.hp)
          print("Armor: ", character.armor)
          print("Strength: ", character.strength)
          print("Magic: ", character.magic)
          return character

def enemySelect(orc, giantRat, thief):
    enemyList = [orc, giantRat, thief]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["Potion", "Sword", "Shield"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def battlestate():
    print("You are being attacked!")
    enemy = enemySelect(orc, giantRat, thief)
    print(enemy.name, "has appeared!!")
    while enemy.hp > 0 :
        choice = input("1. Attack\n2 Magic\n3 inventory\n4 FLEE!")

        if choice == "1":
            print("You swing your sword at the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.hp = enemy.hp - character.strength
                print("The attack hit!!, enemy health is now ", enemy.hp)

                if enemy.hp > 0:
                    character.hp = character.hp - (enemy.strength/character.armor)
                    print ("The", enemy.name, "the enemy has hit you! leaving you with", character.hp, "hp")
                    gameOver(character)

                else:
                    if enemy.name == "Orc":
                        enemy.hp == 100

                    elif enemy.name == "Giant Rat":
                        enemy.hp == 75

                    elif enemy.name == "Thief":
                        enemy.hp == 90

                    print("You have defeated the", enemy.name)
                    print("The", enemy.name,"dropped something!!")
                    lootDrop = loot()
                    print("you got a", lootDrop)
                    break
            

            else:
                print("Your attack missed")
                print("The", enemy.name, "hits you for full damage")
                character.hp = character.hp - enemy.strength
                print("You now", character.hp,"hp")
                gameOver(character)


                
        elif choice == "2":
            print("You cast your spell at the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.hp = enemy.hp - character.magic
                print("The attack hit!!, enemy health is now ", enemy.hp)
                gameOver(character)

                if enemy.hp > 0:
                    character.hp = character.hp - (enemy.strength/character.armor)
                    print ("The", enemy.name, "the enemy has hit you! leaving you with", character.hp, "hp")
                    gameOver(character)

                else:
                    if enemy.name == "Orc":
                        enemy.hp == 100

                    elif enemy.name == "Giant Rat":
                        enemy.hp == 75

                    elif enemy.name == "Thief":
                        enemy.hp == 90

                    print("You have defeated the", enemy.name)
                    print("The", enemy.name,"dropped something!!")
                    lootDrop = loot()
                    print("you got a", lootDrop)
                    break
            

            else:
                print("Your attack missed")
                print("The", enemy.name, "hits you for full damage")
                character.hp = character.hp - enemy.strength
                print("You now", character.hp,"hp")
                gameOver(character)
        


        elif choice == "3":
            print("Your inventory is empty")
    
        elif choice == "4":
            print("You try to flee the battle")
            fleechance = random.randint(1,10)
            if fleechance > 4:
                print("You fled successfully!")
                break
            else:
                print("You fell over as you tried to flee")
                print("The enemy hits you for full damage")
                character.hp = character.hp - enemy.strength
                print("You now have", character.hp, "hp")
                gameOver(character)

        else:
            print("Sorry, but you can only choose the other 4 options")
        
character = intro()
battlestate()
