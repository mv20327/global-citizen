#Global Citizen by Manh Quyen Vu
#Version 0.1

#Importing library
import sys
import cmd
import os
import time
from adventurelib import *

#print_slow slower text for a nice slow typing effect for words
#original source: https://stackoverflow.com/questions/20302331/typing-effect-in-python
def print_slow(str):
    for char in str:
        time.sleep(.0421)
        sys.stdout.write(char)
        sys.stdout.flush()

#Mood lists:
lmood_happy = ['happy','good','alright','fun','cheer','overjoy','great']
lmood_neutral = ['ok','fine','meh']
lmood_sad = ['sad','unhappy','tired','upset','uncomfortable']

#Player information and their statistics at the start
p_score = 0

#adventurelib.py setup
#directions of the game - add new directions
Room.add_direction('straight', 'right')
Room.add_direction('left', 'stream')

#items
#make bag into inventory for easier calling
inventory = Bag()
#when user put inventory as command they'll see their inventory
@when('inventory')
def show_inventory():
    print('You currently have:')
    if not inventory:
        print('nothing')
        return
    for item in inventory:
        print(f'* {item}') #code from adventurelib.py's documentation

#stick at shed
stick = Item('a wooden Y shaped stick', 'stick')

#plastic bottle at garden +50points
plastic_trash1 = Item('red plastic bottle','plastic bottle')
plastic_trash1.color = 'red'

#item attribs - red plastic bottle
@when('look at ITEM')
def look(item):
    obj = inventory.find(item)
    if not item:
        print(f"You do not have  {item}.")
    else:
        print(f"It's a sort of {obj.colour}-ish colour.")

#define "rooms" for the game

r_field = Room("""
You're a new Papatoetoe High School
student. You're walking around for some
fresh air, and you want to explore the
back of the school.
Where would you like to go now? 
(shed/garden/stream)
    """) #starting point (in the middle of the field)

r_shed = Room("""
This is where the staff stores their items.
And there are European bee hives! 
What would you like to do now?
(look around the shed/keep exploring)
    """) #walk left (west)

r_garden = Room("""
This is the school's garden. It's pretty 
clean right now, with a flowers and plants 
growing. Suddenly, there was a piece of 
trash flew by, and got on top to a tree.
What would you like to do?
(use stick/leave trash)
    """) #walk straight and right (east)

r_stream = Room("""
This is the Puhinui stream. This is where
the eels live, however, there's a lot of 
trash under the water. Many eels are 
small dispite their age. Many tin cans are
rusting, as well as the visible oil patches 
on top of the water. Should you fish out the
few plastic bottles that you can reach?
(fish out with stick/leave)
    """) #walk straight further right (east)

r_stream_end = Room("""
This is the end of the stream. There are 
old trees all around. Many are purposefully
cut down because of their parasitic nature.
You think to yourself... Is this the end?
Then you realized... a bird is about to
eat a piece of plastic trash! You have to
do something, quick! 
(scare the bird/ignore the bird)
    """) #end of stream / end of the game

current_room = r_field #current room is at field

#directions of the rooms
r_field.straight = r_shed
r_field.right = r_garden
r_field.left = r_stream
r_field.stream = r_stream_end

#@when statements to move b/w rooms and a function to display what the player is seeing
@when('straight', direction='straight')
@when('right', direction='right')
@when('left', direction='left')
@when('stream', direction='stream')
def walk(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        print(f'You go {direction}.')
        look()

#commands for player for start command

#rooms
#defining the garden
@when('garden')
def garden():
#set current_room as a global variable
    global current_room 
#check to see if player is at the field or not
    if current_room is not r_field:
        print("Hmm... You're not on the field.")
        return

    #change current room to shed
    current_room = r_garden
    say("""
        So you walked on... to the garden. 
        """
        )

    #show the room description to tell player more about the "room"
    print(current_room)

#defining the shed
@when('shed')
def shed():
#set current_room as a global variable
    global current_room 
#check to see if player is at the field or not
    if current_room is not r_field:
        print("Hmm... You're not on the field.")
        return

    #change current room to shed
    current_room = r_shed
    say("""
        So you walked on... to the shed. 
        """
        )

    #show the room description to tell player more about the "room"
    print(current_room)

#shed
#looking around the shed
Room.have_stick = False #other "rooms" dont have stick
r_shed.have_stick = True #but shed has stick

@when('look around the shed')
def look_shed():
    print(
        "So, you walked around the shed. Then," +
        "you saw a stick that shaped like an Y."
        "Maybe you'll need this soon." +
        "Take the item? (take stick/leave stick)"
        )

#take stick or not
@when('take stick')
def take_stick():
    if current_room.have_stick:
        inventory.add(stick)
        p_score + 20
        say("""
            A stick has been added into your inventory!
        """)
        print("20 points are added to your score.")
    else:
        print("You're not at the shed!")

@when('leave stick')
def leave_stick():
    if current_room.have_stick:
        say("""
            You left the stick on the ground.
        """)
    else:
        print("You're not at the shed!")

#leave the shed and go to the garden
@when('keep exploring')
def leave_shed():
    print("So you walk on... to the garden!")
    current_room=r_garden
    print(current_room)

#defining the stream
@when('stream')
def stream():
#set current_room as a global variable
    global current_room 
#check to see if player is at the field or not
    if current_room is not r_field:
        print("Hmm... You're not on the field.")
        return

    #change current room to stream
    current_room = r_stream
    say("""
        So you walked on... to the stream. 
        """
        )

    #show the room description to tell player more about the "room"
    print(current_room)

#defining the end of the stream - the end of the game
@when('the end of the stream')
def end_stream():
#set current_room as a global variable
    global current_room 
#check to see if player is at the field or not
    if current_room is not r_stream_end:
        print("Hmm... You're not on the field.")
        return

    #change current room to end of stream
    current_room = r_stream_end
    say("""
        So you walked on... to the shed. 
        """
        )

    #show the room description to tell player more about the "room"
    print(current_room)

#room attribs

#check if room has trash to pick up or not
Room.have_trash = True
shed.have_trash = False

#check if room has npc or not
Room.have_npc = False
stream.have_npc = False

#actions
#pick trash up
@when("take TRASH")
def take(trash):
    if current_room.have_trash:
        print(f"You picked up the {trash}. You have +50 points.")
        p_score + 50
    else:
        print("Tough. There's no trash to pick.")

#show NPC trash
@when("show ITEM to NPC")
def show(item, npc):
    if current_room.have_npc:
        print(f"You've shown the man that you picked up the trash. ")
    else:
        print("Tough. There's NPC to talk to.")


#Defining the game functions:

#Menu function - this will handle player's first inputs in the game.
def menu():
    print("#------Welcome to Global Citizen.------#")
    print("(-----------------Play-----------------)")
    print("(-----------------Help-----------------)")
    print("(-------------Check Score--------------)")
    print("(-----------------Exit-----------------)")
    print("What would you like to do?")
    choice =  input("> ")
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
        print("What would you like to do?")
        choice =  input("> ")
        if choice.lower() == ("play"):
            basicinfo()
        elif choice.lower() == ("help"):
            help()
        elif choice.lower() == ("exit"):
            sys.exit()  

#Defining the help menu
def help():
    os.system('cls') #since players are **PROBABLY** using windows, to clear the console on cmd/idle, the program must use cls instead of clear
    print("#-----------------Help-----------------#")
    say("""Hello player. Welcome to Global Citizen.\n
    Global Citizen is a game where you will \n
    experience and learn about the ramifications \n
    of the plastic use towards the environment. \n
    To play the game, you'll be provided with \n
    options and you can type the keyword to do \n
    the particular action you want to do in the \n
    situation provided. \n
    Type menu to return to menu, type exit to exit \n
    the program.""")
    print_slow("What would you like to do? (menu/exit)")
    print("")
    choice =  input("> ")
    if choice.lower() == ("menu"):
        os.system('cls')
        menu()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['menu','exit']:
        print_slow("Command unrecognized. Try again?")
        print("")
        print_slow("What would you like to do?")
        choice =  input("> ")
        if choice.lower() == ("menu"):
            menu()
        elif choice.lower() == ("exit"):
            sys.exit() 

#defining the checking score function
def score():
    os.system('cls')
    print_slow("Your score is " + str(p_score) + ". To gain more, you can try\nto do more for the environment!")
    print_slow("What do you want to do now? (menu, play, help, or exit)... ")
    choice =  input("> ")
    if choice.lower() == ("menu"):
        menu()
    elif choice.lower() == ("play"):
        basicinfo()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        sys.exit()  
    while choice.lower() not in ['play','help','score','exit']: #while loop loops back to the question when there's no valid answer
        print_slow("It seemed like you didn't put in any defined choice.")
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

def pageInput(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print_slow("That's not a number!")
            continue
        else:
            return userInput 
        break 

#defining the generic questions function - this function runs w/o any validation except for age 
def p_question():
    print_slow("Well, what do you want to change?")
    p_change = input("Select what you want to change (name, age or mood):... ")
    if p_change.lower() == ("name"):
        p_name = input("So, what's your name? ")
    if p_change.lower() == ("age"):
        print_slow ("So, what's your age this time? ")
        p_age = p_ageInput()
    if p_change.lower() == ("mood"):
        p_mood = ("How are you feeling now? ")
    print_slow("Alright then, let's move on.")     

#stage 1: gathering data from user before starting the game.
def basicinfo():
    os.system('cls')
    print_slow("Hello friend! What is your name?")
    print("")
    print_slow("My name is...: ")
    print("")
    p_name = input("> ") # asking for name

    print_slow("Well how are you, " + p_name + "?")
    print("")
    print_slow("I feel...: ")
    print("")
    p_mood = input("> ") #asking user for their mood

    if p_mood.lower() in lmood_happy: #good mood
        print_slow("Wow, you're happy today huh? That's great!")
        print("")
    elif p_mood.lower in lmood_neutral: #neutral mood
        print_slow("Well, well, well, your day could've gone a bit better don't you think, " + p_name + "?")
        print("")
    elif p_mood.lower() in lmood_sad: #sad mood
        print_slow("Aww, don't worry, tomorrow will definitely go better than today!")
        print("")
    elif p_mood.lower() == ("sick"): #feeling not well
        print_slow("Please stay at home, wear a mask, don't go outside and wash your hand regularly!")
        print("")

    else: #adding custom mood as the mood wasn't defined in the list/editing the list
        print_slow("Well, interesting! It seems like whatever you're feeling is not in the array.\nDo you want to add your mood into the list of moods?") #add mood item into the list of moods
        print("")
        print_slow("Yes/No:")
        print("")
        p_addmood = input("> ")

        if p_addmood.lower() == ("yes"):

          #asking player what mood they're in
            print_slow("Cheerio! What type of mood are you in?")
            print("")
            print_slow("My mood is (Happy, sad or neutral)...: ")
            print("")
            p_tolist = input("> ")

            #checks if the mood is happy
            if p_tolist.lower() == ("happy"):
                print_slow("I see that you're happy. That's good!")
                print("")
                lmood_happy.append(p_mood)
                print("")
                print_slow("The current happy mood list is:")
                print("")
                print(lmood_happy)

            #checks if the mood is sad
            if p_tolist.lower() == ("sad"):
                print_slow("I see that you're a bit sad. Hope you feel better!")
                print("")
                lmood_sad.append(p_mood)
                print("")
                print_slow("The current sad mood list is:")
                print("")
                print(lmood_sad)

            #checks if the mood is neutral
            if p_tolist.lower() == ("neutral"):
                print_slow("I see that you're just fine. I see.")
                print("")
                lmood_neutral.append(p_mood)
                print("")
                print_slow("The current neutral mood list is:")
                print("")
                print(lmood_neutral) 

            #while loop to ensure players input neutral/sad/happy 
            while p_tolist.lower() not in ['happy','sad','neutral']:
                print_slow("It seemed like you didn't put in the correct choice (happy/sad/neutral).")
                print("")
                print_slow("So, what type of mood are you feeling? (happy/sad/neutral)... ")
                print("")
                p_tolist =  input("> ")

                #checks if the mood is happy
                if p_tolist.lower() == ("happy"):
                    print_slow("I see that you're happy. That's good!")
                    print("")
                    lmood_happy.append(p_mood)
                    print("")
                    print_slow("The current happy mood list is:")
                    print("")
                    print(lmood_happy)

            #checks if the mood is sad
                if p_tolist.lower() == ("sad"):
                    print_slow("I see that you're a bit sad. Hope you feel better!")
                    print("")
                    lmood_sad.append(p_mood)
                    print("")
                    print_slow("The current sad mood list is:")
                    print("")
                    print(lmood_sad)

            #checks if the mood is neutral
                if p_tolist.lower() == ("neutral"):
                    print_slow("I see that you're just fine. I see.")
                    print("")
                    lmood_neutral.append(p_mood)
                    print("")
                    print_slow("The current neutral mood list is:")
                    print("")
                    print(lmood_neutral) 
    
        #if user says no              
        if p_addmood.lower() == ("no"):
            print("")
            print_slow("Oh that's fine then! You can continue on...")

        #while loop to loop back if user didn't put yes/no
        while p_addmood.lower() not in ['yes','no']:
            print_slow("It seemed like you didn't put in the correct choice (yes/no).")
            print("")
            print_slow("Do you still want to add the mood? (Yes/No)... ")
            print("")
            p_addmood =  input("> ")

            #if user says yes
            if p_addmood.lower() == ("yes"):
                print_slow("What mood is this, " + p_name + "? (happy, neutral, sad) ")
                print("")
                print_slow("My mood is (Happy, sad or neutral)...: ")
                print("")
                p_tolist = input("> ")

                #checks if the mood is happy
                if p_tolist.lower() == ("happy"):
                    print_slow("I see that you're happy. That's good!")
                    print("")
                    lmood_happy.append(p_mood)
                    print("")
                    print_slow("The current happy mood list is:")
                    print("")
                    print(lmood_happy)

            #checks if the mood is sad
                if p_tolist.lower() == ("sad"):
                    print_slow("I see that you're a bit sad. Hope you feel better!")
                    print("")
                    lmood_sad.append(p_mood)
                    print("")
                    print_slow("The current sad mood list is:")
                    print("")
                    print(lmood_sad)

            #checks if the mood is neutral
                if p_tolist.lower() == ("neutral"):
                    print_slow("I see that you're just fine. I see.")
                    print("")
                    lmood_neutral.append(p_mood)
                    print("")
                    print_slow("The current neutral mood list is:")
                    print("")
                    print(lmood_neutral) 
                    
                #if user say something else the third time
                if p_tolist.lower() not in ['happy','sad','neutral']:
                    print("")
                    print_slow("We'll move on then.")
                                    
            #if user says no              
            if p_addmood.lower() == ("no"):
                print_slow("Oh that's fine then! You can continue on...")      
                print("") 
            
    #ask for age
    print_slow("How old are you?")
    print("")
    p_age = pageInput("> ")
    if p_age == 13: #check what year level the user is in
        print_slow("Oh, you're probably in Year 9 then.")
        print("")
    elif p_age == 14:
        print_slow("Oh, you're possibly in Year 10 then.") 
        print("")   
    elif p_age == 15:
        print_slow("Oh, you may be are in Year 11 then.")  
        print("")   
    elif p_age == 16:
        print_slow("Oh, you're probably in Year 12.")
        print("")
    else:
        print_slow("I see. You are over 17!") #over 17
        print("") 

    #asking users to check their information
    os.system('cls')
    print_slow("Are these details correct?") 
    print("")
    print_slow("Your name is " + p_name + ". You are currently " + str(p_age) + " year\nold. And you're feeling " + p_mood + " today.") #convert int to str (integer to string)
    print("")
    print_slow("Yes/No: ")
    print("")
    p_confirm = input("> ")

    #run once when user gives a valid answer
    if p_confirm.lower() == ("yes"):
        print_slow("Alright then! We shall continue on!")
        print("")
    if p_confirm.lower() == ("no"):
        p_question()
        print("")

    #while loop loops back to the question when there's no valid answer
    while p_confirm.lower() not in ['yes','no']:
        print_slow("It seemed like you didn't put in the correct choice (yes/no).")
        print("")
        print_slow("Do you still want to change your details? (Yes/No)... ")
        print("")
        p_confirm =  input("> ")
        if p_confirm.lower() == ("yes"):
            print_slow("Well, what do you want to change?")
            print("")
            p_change = input("Select what you want to change (name, age or mood):... ")
            print("")
            if p_change.lower() == ("name"):
                p_name = input("So, what's your name? ")
                print("")
            if p_change.lower() == ("age"):
                p_age = pageInput("So, how old are you really? ")
                print("")
            if p_change.lower() == ("mood"):
                p_mood = ("How are you feeling now? ")     
                print("") 
            if p_confirm.lower() == ("no"):
                print_slow("Alright then! We shall continue on!")
                print("")

    #asking player to start the game
    print_slow("So, " + p_name + ", would you like to play a game?")
    print("")
    print_slow("Yes/No: ")
    print("")
    p_play = input("> ")
    print("")
    #while loop loops back to the question when there's no valid answer
    while p_play.lower() not in ['yes','no']:
        print_slow("You didn't say yes or no.")
        print("")
        print_slow("Do you want to play the game or no?")
        print("")
        p_play = input("> ")
        if p_play.lower() == ("yes"):
            g_play()       
    if p_play.lower() == ("no"):
        print_slow("The game will return you back to the menu now.\n You can try the game later.")
        print("")
        menu()

    #run once when user gives a valid answer
    if p_play.lower() == ("yes"):
        print_slow("Alright then! We shall continue on!")
        print("")
        g_play()
    if p_play.lower() == ("no"):
        print_slow("The game will return you back to the menu now.\n You can try the game later.")
        print("")
        menu()
#defining the play function
def g_play():
    print(r_field)
    start()

#Runs menu function
menu()