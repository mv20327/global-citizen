#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys
import cmd
import os

#Mood lists:
lmood_happy = ['happy','good','alright','fun','cheer','overjoy','great']
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
        basicinfo()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['play','help','exit']: #while loop loops back to the question when there's no valid answer
        print("Command unrecognized. Try again?")
        choice =  input("Tell me what you wanna do: ")
        if choice.lower() == ("play"):
            basicinfo()
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
    elif p_mood.lower in lmood_neutral:
        print("Well, well, well, your day could've gone a bit better don't you think, " + p_name + "?")
    elif p_mood.lower in lmood_sad:
        print("Aww, don't worry, tomorrow will definitely go better than today!")
    elif p_mood.lower == ("sick"):
        print("Please stay at home, wear a mask, don't go outside and wash your hand regularly!")
    else:
        print("Well, interesting! It seems like whatever you're feeling is not recognized. Do you want to add your mood into the list of moods?") #add mood item into the list of moods
        p_addmood = input("Yes/No: ")
        if p_addmood.lower() == ("yes"):
          #asking player what mood they're in
          print("Cheerio! What type of mood are you in?")
          p_tolist = input("My mood is (Happy, sad or neutral)...: ")
          #checks if the mood is happy
          if p_tolist.lower == ("happy"):
            print("I see that you're happy. That's good!")
            lmood_happy.append(p_mood)
            print("The current happy mood list is:")
            print(lmood_happy)
          #checks if the mood is sad
          if p_tolist.lower == ("sad"):
            print("I see that you're a bit sad. Hope you feel better!")
            lmood_sad.append(p_mood)
            print("The current sad mood list is:")
            print(lmood_sad)
          #checks if the mood is neutral
          if p_tolist.lower == ("neutral"):
            print("I see that you're just fine. I see.")
            lmood_neutral.append(p_mood)
            print("The current neutral mood list is:")
            print(lmood_neutral)          
    print("How old are you, " + p_name + "?") #ask for age
    while True: #checks whether or not age is a number or not
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
    elif p_age == 14:
      print("Oh, you're possibly in Year 10 then.")    
    elif p_age == 15:
      print("Oh, you may be are in Year 11 then.")     
    elif p_age == 16:
      print("Oh, you're probably in Year 12.")
    else:
      print("I see.")


#defining the play function
def g_play():

  print("You're a student at Papatoetoe High. You're walking around the school field to get some fresh air. Suddenly, you saw a piece of trash.")


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