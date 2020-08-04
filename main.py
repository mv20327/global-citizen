#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys


def menu():
    print("Welcome to the game.")
    print("Pick an option. You can use numbers or words.")
    choice =  input("Tell me what you wanna do: ")
    if choice.lower() == ("play"):
        play()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        escape()

def play():
    print("game!!!")

def help():
    print("Help documentation")

def escape():
    sys.exit()

menu()