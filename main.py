#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys

#Player information and their statistics at the start


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
            escape()   

#Defining the game functions:
def play():
    print("game!!!")

def help():
    print("Help documentation")

def escape():
    sys.exit()

#Runs menu function
menu()