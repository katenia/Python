#random used to select which enemy you face and what loot they drop
import random

#importing what I need for walk through woods (zigzag program pg72)
import time, sys


#stuff is the overall inventory, loot is what they can drop, enemies are what you may face in the woods
stuff = {'hearty durian': 1, 'big hearty truffle': 1, 'endura shroom': 1, 'rushroom': 1, 'hearty radish': 1, 'endura carrot': 1, 'acorn': 1, 'farosh scale': 1, 'hyrule bass': 1, 'energetic rhino beetle': 1, 'keese wing': 1, 'wood': 1, "traveler's sword": 1, "forest dweller's sword": 1, 'royal halberd': 1}
loot = ['hearty durian', 'big hearty truffle', 'endura shroom', 'rushroom', 'hearty radish', 'endura carrot', 'acorn', 'farosh scale', 'hyrule bass', 'energetic rhino beetle', 'keese wing', 'wood', 'traveler sword', 'forest dweller sword', 'royal halberd', 'ruby', 'diamond']
enemies = ['chuchu', 'keese', 'forest octorok', 'bokoblin', 'moblin', 'lizalfos', 'lynel', 'guardian', 'yiga footsoldier', 'stone talus', 'stone pebblit']


#this is what is used to print the overall inventory of the game
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total = item_total + v
    print('Total number of items:' + str(item_total))

#This code is called to display the inventory after a kill
#It is optional for the user
def optionalDisplay(stuff):
    while True:
        print ('Would you like to view your inventory?')
        print ('yes/no')
        answer= input()
        if answer.lower() in ["yes", "y"]:
            displayInventory(stuff)
            break
        elif answer.lower() in ["no", "n"]:
            break
        else:
            continue

#Introduction to the game. Game kickoff
print ('Welcome to generic knockoff Zelda!')
print ('The one with no graphics and stolen trademark names....')
print ('You have started this game with a few items in your inventory.')
displayInventory (stuff)


#Code to add killed item/dropped spoils to dictonary(stuff)
def addTOinventory (spoils):
    for item in spoils:
        if item in stuff:
            stuff[item] += 1
        else:
            stuff[item] = 1

#the part of the code that makes you face an enemy
def enemieEncounter ():
    enemy = random.choice(enemies)
    print (' ')
    print ('You run into a ' + enemy)
    while True:
       print (' ')
       print ('Do you kill the ' + enemy + ' or let it live?')
       print ('kill/leave')
       kill= input()
       if kill.lower() in ["kill", "k"]:
            dropped = random.choices(loot, k=4)
            print ('The ' + enemy + ' dropped:')
            print (', '.join(dropped))
            print (' ')
            addTOinventory (dropped)
            print ('Adding items to your current inventory')
            print (' ')
            optionalDisplay (stuff)
            break
       elif kill.lower() in ["leave", "l"]:
            break
       else:
            continue

#walk through woods (just fun screen movement-no purpose)
def woodWalk():
    indent = 0
    indentIncreasing = True
    while True: 
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.05)

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent -1
            if indent == 0:
                break


#Gives you the option to return to the woods and face an enemy or exit the game
def woodsORexit ():
    while True:
       print (' ')
       print ('Do you want to walk through the woods or exit?')
       print ('woods/exit')
       stop= input()
       if stop.lower() in ["woods", "w"]:
            woodWalk ()
            enemieEncounter ()
       elif stop.lower() in ["exit", "e"]:
            break
       else:
            continue

woodsORexit ()
