#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys
import cmd
import os
import adventurelib
from adventurelib import say

#Mood lists:
lmood_happy = ['happy','good','alright','fun','cheer','overjoy','great']
lmood_neutral = ['ok','fine','meh']
lmood_sad = ['sad','unhappy','tired','upset','uncomfortable']


#Player information and their statistics at the start
p_score = 0
#Menu function - this will handle player's first inputs in the game.
def menu():
    print("#------Welcome to Global Citizen.------#")
    print("(-----------------Play-----------------)")
    print("(-----------------Help-----------------)")
    print("(-------------Check Score--------------)")
    print("(-----------------Exit-----------------)")
    choice =  input("Tell me what you wanna do: ")
    if choice.lower() == ("play"):
        basicinfo()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() ==("score"):
        score()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['play','help','score','exit']: #while loop loops back to the question when there's no valid answer
        print("Command unrecognized. Try again?")
        choice =  input("Tell me what you wanna do: ")
        if choice.lower() == ("play"):
            basicinfo()
        elif choice.lower() == ("help"):
            help()
        elif choice.lower() == ("exit"):
            sys.exit()  

#Defining the game functions:

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

#defining the checking score function
def score():
    print("Your score is " + str(p_score) + ". To gain more, you can try to do more for the environment!")
    print("What do you want to do now? (menu, play, help, or exit)... ")
    choice =  input("Tell me what you wanna do: ")
    if choice.lower() == ("menu"):
        menu()
    elif choice.lower() == ("play"):
        basicinfo()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        sys.exit()  
    while choice.lower() not in ['play','help','score','exit']: #while loop loops back to the question when there's no valid answer
        print("It seemed like you didn't put in any defined choice.")
        choice =  input("Tell me what you wanna do (menu, play, help, or exit): ")
        if choice.lower() == ("menu"):
            menu()
        elif choice.lower() == ("play"):
            basicinfo()
        elif choice.lower() == ("help"):
            help()
        elif choice.lower() == ("exit"):
            sys.exit()  

#defining the age function

def p_ageInput():
    while True:
        try:
            pageInput = int(input("What is your age?"))       
        except ValueError:
            print("That's not a number!")
            continue
    else:
        return pageInput
        

#defining the generic questions function - this function runs w/o any validation except for age 
def p_question():
    print("Well, what do you want to change?")
    p_change = input("Select what you want to change (name, age or mood):... ")
    if p_change.lower() == ("name"):
        p_name = input("So, what's your name? ")
    if p_change.lower() == ("age"):
        print ("So, what's your age this time? ")
        p_age = p_ageInput()
    if p_change.lower() == ("mood"):
        p_mood = ("How are you feeling now? ")
    print("Alright then, let's move on.")     

#stage 1: gathering data from user before starting the game.
def basicinfo():
    print("Hello friend! What is your name?")
    p_name = input("My name is...: ") # asking for name

    print("Well how are you, " + p_name + "?")
    p_mood = input("I feel...: ") #asking user for their mood

    if p_mood.lower() in lmood_happy: #good mood
        print("Wow, you're happy today huh? That's great!")
    elif p_mood.lower in lmood_neutral: #neutral mood
        print("Well, well, well, your day could've gone a bit better don't you think, " + p_name + "?")
    elif p_mood.lower() in lmood_sad: #sad mood
        print("Aww, don't worry, tomorrow will definitely go better than today!")
    elif p_mood.lower() == ("sick"): #feeling not well
        print("Please stay at home, wear a mask, don't go outside and wash your hand regularly!")

    else: #adding custom mood as the mood wasn't defined in the list/editing the list
        print("Well, interesting! It seems like whatever you're feeling is not in the array. Do you want to add your mood into the list of moods?") #add mood item into the list of moods
        p_addmood = input("Yes/No: ")
        if p_addmood.lower() == ("yes"):
          #asking player what mood they're in
            print("Cheerio! What type of mood are you in?")
            p_tolist = input("My mood is (Happy, sad or neutral)...: ")
            #checks if the mood is happy
            if p_tolist.lower() == ("happy"):
                print("I see that you're happy. That's good!")
                lmood_happy.append(p_mood)
                print("The current happy mood list is:")
                print(lmood_happy)
            #checks if the mood is sad
            if p_tolist.lower() == ("sad"):
                print("I see that you're a bit sad. Hope you feel better!")
                lmood_sad.append(p_mood)
                print("The current sad mood list is:")
                print(lmood_sad)
            #checks if the mood is neutral
            if p_tolist.lower() == ("neutral"):
                print("I see that you're just fine. I see.")
                lmood_neutral.append(p_mood)
                print("The current neutral mood list is:")
                print(lmood_neutral) 

        #if user says no              
        if p_addmood.lower() == ("no"):
            print("Oh that's fine then! You can continue on...")

        #while loop to loop back if user didn't put yes/no
        while p_addmood.lower() not in ['yes','no']:
            print("It seemed like you didn't put in the correct choice (yes/no).")
            p_addmood =  input("Do you still want to change your details? (Yes/No)... ")
            if p_addmood.lower() == ("yes"):
                print("What mood is this, " + p_name + "? (happy, neutral, sad) ")
                p_tolist = input("My mood is (Happy, sad or neutral)...: ")
                #checks if the mood is happy
                if p_tolist.lower() == ("happy"):
                    print("I see that you're happy. That's good!")
                    lmood_happy.append(p_mood)
                    print("The current happy mood list is:")
                    print(lmood_happy)
            #checks if the mood is sad
                if p_tolist.lower() == ("sad"):
                    print("I see that you're a bit sad. Hope you feel better!")
                    lmood_sad.append(p_mood)
                    print("The current sad mood list is:")
                    print(lmood_sad)
            #checks if the mood is neutral
                if p_tolist.lower() == ("neutral"):
                    print("I see that you're just fine. I see.")
                    lmood_neutral.append(p_mood)
                    print("The current neutral mood list is:")
                    print(lmood_neutral) 
            #if user says no              
            if p_addmood.lower() == ("no"):
                print("Oh that's fine then! You can continue on...")       

    print("How old are you, " + p_name + "?") 
    #ask for age
    p_age = p_ageInput()
    if p_age == 13: #check what year level the user is in
        print("Oh, you're probably in Year 9 then.")
    elif p_age == 14:
        print("Oh, you're possibly in Year 10 then.")    
    elif p_age == 15:
        print("Oh, you may be are in Year 11 then.")     
    elif p_age == 16:
        print("Oh, you're probably in Year 12.")
    else:
        print("I see. You are over 17!") #over 17

    #asking users to check their information
    print("Are these details correct?") 
    print("Your name is " + p_name + ". You are currently " + str(p_age) + " year old. And you're feeling " + p_mood + " today.") #convert int to str (integer to string)
    p_confirm = input("Yes/No: ")
    #run once when user gives a valid answer
    if p_confirm.lower() == ("yes"):
        print("Alright then! We shall continue on!")
    if p_confirm.lower() == ("no"):
        p_question()

    #while loop loops back to the question when there's no valid answer
    while p_confirm.lower() not in ['yes','no']:
        print("It seemed like you didn't put in the correct choice (yes/no).")
        p_confirm =  input("Do you still want to change your details? (Yes/No)... ")
        if p_confirm.lower() == ("yes"):
            print("Well, what do you want to change?")
            p_change = input("Select what you want to change (name, age or mood):... ")
        if p_change.lower() == ("name"):
            p_name = input("So, what's your name? ")
        if p_change.lower() == ("age"):
            print ("So, what's your age this time? ")
            p_age = p_ageInput()
        if p_change.lower() == ("mood"):
            p_mood = ("How are you feeling now? ")      
        if p_confirm.lower() == ("no"):
            print("Alright then! We shall continue on!")

    #asking player to start the game
    print("So, " + p_name + " who is " + str(p_age) + " year old, would you like to play a game?")
    p_play = input("Yes(Y)/No(N): ")
    #while loop loops back to the question when there's no valid answer
    while p_play.lower() not in ['yes','no']:
        print("You didn't say yes or no.")
        if p_play.lower() == ("yes"):
            g_play_stage1()       
    if p_play.lower() == ("no"):
        print("The game will return you back to the menu now. You can try the game later.")

    #run once when user gives a valid answer
    if p_play.lower() == ("yes"):
        print("Alright then! We shall continue on!")
        g_play_stage1()
    if p_play.lower() == ("no"):
        print("The game will return you back to the menu now. You can try the game later.")

#defining the play function
def g_play_stage1():
    say("You're a student at Papatoetoe High. You're walking around the school field to get some fresh air. Suddenly, you see a piece of plastic trash.")
    p_choice1 = input("Are you going to leave the trash or pick it up? (leave/pick): ")
    if p_choice1.lower() == ("pick"):
        print("You're a very responsible student huh? +50 points for you!")
    if p_choice1.lower() == ("leave"):
        print("")


#Runs menu function
menu()