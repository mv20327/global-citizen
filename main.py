#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys
import cmd
import os

#Mood lists:
lmood_happy = ['happy','good','alright','fun','cheer','overjoy']
lmood_neutral = ['ok','fine','meh']
lmood_sad = ['sad','unhappy','tired','upset','uncomfortable']


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
#stage 1: gathering data from user before starting the game.
def basicinfo():
    print("Hello friend! What is your name?")
    p_name = input("My name is...: ")
    print("Well how are you, " + p_name + "?")
    p_mood = input("I feel...: ")
    if p_mood.lower in lmood_happy:
        print("Wow, you're happy today huh? That's great!")
    if p_mood.lower in lmood_neutral:
        print("Well, well, well, your day could've gone a bit better don't you think, " + pname + "?")
    if p_mood.lower in lmood_sad:
        print("Aww, don't worry, tomorrow will definitely go better than today!")
    if p_mood.lower == ("sick"):
        print("Please stay at home, wear a mask, don't go outside and wash your hand regularly!")
    else:
        print("Well, interesting!")
        
    print("How old are you, " + p_name + "?")
    while True:
        try:
            p_age = int((input(("I am...: "))))
        except ValueError:
            print("That's not a number!")
            break       
        else:
            if p_age >= 17:
                print("Oh, you're probably a Year 13 or out of school then.")             
            break
        if p_age == 13:
            print("Oh, you're probably in Year 9 then.")
        if p_age == 14:
            print("Oh, you're possibly in Year 10 then.")    
        if p_age == 15:
            print("Oh, you may be are in Year 11 then.")     
        if p_age == 16:
            print("Oh, you're probably in Year 12.")
        else:
            print("I see.")
    print("So, " + p_name + "who is " + p_age + "year old, would you like to play a game?")
    
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