print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'r at a crossroad. Where do you want to go? Type "left" or "right".\n').lower()
if choice1 =="left":
    choice2=input('\nYou\'ve come to a lake.There is an Iceland in the middle of the lake. Type "wait" to wait for a boat.Type "swim" to swim across.\n')
    if choice2 =="wait":
        choice3=input("\nYou arrive at the Island and unharmed.There is house with 3 doors. One red ,one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 =="red":
            print("It's room full of fire. GAME OVER..")
        elif choice3 =="yellow":
            print("\nYou found the treasure. YOU WIN!!!")
        elif choice3 =="blue":
            print("You enter a room of beast. GAME OVER..")
        else:
            print("You choose a door that doesn't exist. GAME OVER..")
    else:
        print("You got attacked by an angry trout. Game over..")
else:
    print("You fell into a hole. Game over..")