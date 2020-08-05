#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys


#Player information and their statistics at the start
class player:
    def __init__(self):
        self.name = ''
        self.points = 0
myPlayer = player()

#Menu function - this will handle player's first inputs in the game.
def menu():
    print("#------Welcome to Global Citizen.------#")
    print("(-----------------Play-----------------)")
    print("(-----------------Help-----------------)")
    print("(-----------------Exit-----------------)")
    choice =  input("Tell me what you wanna do: ")
    if choice.lower() == ("play"):
        play()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        escape()
    while choice.lower() not in ['play','help','exit']:
        print("Command unrecognized. Try again?")
        choice =  input("Tell me what you wanna do: ")
        if choice.lower() == ("play"):
            play()
        elif choice.lower() == ("help"):
            help()
        elif choice.lower() == ("exit"):
            sys.exit()  

#Defining the game functions:
def play():
    print("")
    
#Defining the help menu
def help():
    print("#-----------------Help-----------------#")
    print("Hello player. Welcome to Global Citizen.")
    print("Global Citizen is a game where you will")
    print("experience and learn about the ramifications")
    print("of the plastic use towards the environment.")
    print("To play the game, you'll be provided with")
    print("options and you can type the keyword to do")
    print("the particular action you want to do in the")
    print("situation provided.")
    print("Type menu to return to menu, type exit to exit")
    print("the program.")
    choice =  input("Tell me what you wanna do: ")
    if choice.lower() == ("menu"):
        menu()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['menu','exit']:
        print("Command unrecognized. Try again?")
        choice =  input("Tell me what you wanna do: ")
        if choice.lower() == ("menu"):
            menu()
        elif choice.lower() == ("exit"):
            sys.exit()      
#Runs menu function
menu()