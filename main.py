#Global Citizen by Manh Quyen Vu
#Version 0.8

#Importing library
import sys
import cmd
import os
import time
from adventurelib import *

#defining print_slow
#print_slow slower text for a nice slow typing effect for words
#original source: https://stackoverflow.com/questions/20302331/typing-effect-in-python
def print_slow(str):
    for char in str:
        time.sleep(.0420)
        sys.stdout.write(char)
        sys.stdout.flush()

#Mood lists:
lmood_happy = ['happy','good','alright','fun','cheer','overjoy','great']
lmood_neutral = ['ok','fine','meh']
lmood_sad = ['sad','unhappy','tired','upset','uncomfortable']

#Player information and their statistics at the start
p_score = 0
p_karma = 0

#adventurelib.py setup

#items
#make bag into inventory for easier calling
inventory = Bag()
#when user put inventory as command they'll see their inventory
@when('inventory')
def show_inventory():
    print_slow('You currently have:')
    if not inventory:
        print_slow('nothing')
        return
    for item in inventory:
        print(f'* {item}') #code from adventurelib.py's documentation


#stick at shed
stick = Item('a Wooden Y-shaped Stick')
#red wrapper on tree
red_wrapper = Item('a piece of Red Wrapper')
#bundle of plastic bottles
bundle_trash = Item('a bundle of Plastic Bottles')
#mama nature
mama_nature = Item('a mystical figure.')
#bell to scare the bird
bell = Item('a Small Loud Bell')


#define "rooms" for the game

r_field = Room("""
You're a new Papatoetoe High School
student. You're walking around for some
fresh air, and you want to explore the
back of the school.
Let's check out the shed first!
(shed)
    """) #starting point (in the middle of the field)

r_shed = Room("""
This is the shed, where the staff
stores their items. And there are 
European bee hives! 
What would you like to do now?
(look around the shed/keep exploring)
    """) #walk left (west)

r_garden = Room("""
It's pretty clean right now, with 
flowers and plants growing. 
Suddenly, there was a piece of 
plastic wrapper flew by, and
got on top to a tree. 
What would you like to do?
(use stick/leave trash)
    """) #walk straight and right (east)

r_stream = Room("""
This is the Puhinui stream. This 
is where the eels live, however, 
there's a lot of trash under the
water. Many eels are small dispite
their age. Many tin cans are
rusting, as well as the visible
oil patches on top of the water. 
Should you fish out the few 
plastic bottles that you 
can reach?
(fish them out/leave the trash)
    """) #walk straight further right (east)

r_stream_middle = Room("""
Well... someone stopped you 
in the middle of the stream.
She doesn't look like a 
staff at school, and she's 
radiating mystical energy. 
And... she... has a green beard?
And she has a bouquet of fern,
manuka and so many other flowers
on her head... Also she... has a
bird nest on top of her head!
She suddenly asked you "Well well,
did you pick up the trash along the 
way before you got here?"
What is your response?
(yes/i did or no/i didn't)
    """
    ) #mama nature


r_stream_end = Room("""
This is the end of the stream.
There are old trees all around.
Many are purposefully cut down
because of their parasitic nature.
You think to yourself... Is this
the end? 
Then you realized... a bird is
about to eat a tiny piece from a
plastic bottle! You have to do something,
quick! 
(scare the bird/ignore the bird)
    """) #end of stream / end of the game

current_room = r_field #default current room is at field

#commands for player for start command

#rooms

#each time play leave trash/pick trash up they'll turn on the condition .solved
#for each room. unless they pick trash up they won't get any points. they might
#need to get items from one room to progress another room.

#field
@when('field')
@when('go to field')
@when('go to the field')
def field():
    #set current_room as global variable
    global current_room
    if current_room is not r_garden:
        print_slow("You can't access the field now.\n")
    #change current room to field
    current_room = r_field
    print_slow("You're now arrived at the field.\n")

    #show room description
    print(current_room)

#------------------------shed---------------------------#

#defining the shed
@when('shed')
@when('go to shed')
@when('go to the shed')
def shed():
    #set current_room as a global variable
    global current_room 
    if current_room is not r_field and r_garden:
        print_slow("You can't access the shed unless you're in the field or\nthe garden.")
        return
    #change current room to shed
    current_room = r_shed
    print_slow("So you walked... to the shed.\n")

    #show the room description to tell player more about the "room"
    print(current_room)

#define npc, items and conditions of the room
Room.have_stick = False #other "rooms" dont have stick
r_shed.have_stick = True #but shed has stick
r_shed.solved = False #shed hasn't solved yet
r_shed.looked = False #shed hasn't looked yet

#look around the shed
@when('look around shed')
@when('look around the shed')
def look_shed():
    if r_shed.looked == False:
        if current_room.have_stick:
            print_slow("So, you walked around the shed. Then,\nyou saw a stick that shaped like a Y.\nMaybe you'll need this soon.\nTake the item? (take stick/leave stick)")
            r_shed.looked = True #player had looked at the shed, permitting them to proceed
        else:
            print_slow("You're not at the shed!") #player hasn't looked at shed


#take stick or not
@when('take stick')
def take_stick():
    if r_shed.looked == True: #they can only take stick if they looked at shed
        global current_room
        if current_room is not r_shed:
            print_slow("You're currently somewhere else outside of the\nshed area.\n")
        global stick
        for stick in inventory:
            print_slow("You already have the stick!\n")
            return
        if current_room.have_stick:
            inventory.add(stick)
            global p_score
            p_score += 20
            global p_karma
            p_karma += 10
            r_shed.solved = True #player acquired the stick, which means the area is solved.
            print_slow("You just picked up the stick.\n")
            print_slow("You also gained 20 points.\n")
            print_slow("Where do you want to go now?\n")
            print_slow("(go to the garden)\n")
    if r_shed.looked == False:
        print_slow("You're not looking around the shed!\n")
        current_room = r_shed

#leave the stick
@when('leave stick')
def leave_stick():
    if current_room.have_stick:
        print_slow("You left the stick on the ground.\n")
        print_slow("Where do you want to go now?\n")
        print("(go to garden)")
    else:
        print_slow("You're not at the shed!\n")

#leave the shed and go to the garden
@when('keep going')
def ignore_shed():
    print_slow("So you walk... to the garden!\n")
    global current_room
    current_room=r_stream
    print(current_room)

#-----------------------garden-----------------------------#

#defining the garden
@when('keep exploring')
@when('garden')
@when('go to garden')
@when('go to the garden')
def garden():
#set current_room as a global variable
    global current_room
    if current_room is not r_shed:
        print_slow("You can't come to the garden unless you've\nvisited the shed.\n")
        return
    #change current room to garden
    current_room = r_garden
    print_slow("So you walked on... to the garden.\n")

    #show the room description to tell player more about the "room"
    print(current_room)

#define npc, items and conditions of the room
Room.have_red_wrapper = False
r_garden.have_red_wrapper = True #room has wrapper
r_garden.solved = False #trash is collected
r_garden.solvedb = False #trash is not collected but player has already passed

#use stick function
@when('use stick')
@when('get wrapper down')
def get_wrapper():
    if current_room.have_red_wrapper:
        if r_garden.solved == False:
            for stick in inventory:
                inventory.discard(stick)
                inventory.add(red_wrapper)
                print_slow("You got the stick, and you brought it down.\nHowever, the stick snapped in half when you\ntried to get it down.\n")
                print_slow("You lost the Wooden Stick!\n")
                print_slow("You got the plastic red wrapper.\n")
                print_slow("Where do you want to go?\n")
                print_slow("(go to the stream)\n")
                global p_score
                p_score += 50
                global p_karma
                p_karma += 40
                r_garden.solved = True
                break
            else:
                print_slow("You don't have the stick to get it off.\nSeems like you're out of options... oh wait,\nyou can go back to the field and revisit\nthe shed!\nWhat will you do?\n")
                print_slow("\n(go back to the field/keep going)\n")
        else:
            print_slow("There's no wrapper on the tree anymore.\n")
    else:
        print_slow("You aren't at the garden.\n")

#leave function
@when('leave trash')
@when('ignore the wrapper')
def ignore_wrapper():
    if current_room.have_red_wrapper:
        if r_garden.solvedb == False:
            print_slow("You ignored the trash. It's an option, but still,\nthat plastic wrapper is glistening on top\nthat tree, seemingly laughing at you.\n What do you want to go now?\n")
            print_slow("(go to the stream)\n")
            r_garden.solvedb = True
    else:
        print_slow("You aren't at the garden.\n")

#----------------------stream----------------------------#

#defining the stream
@when('stream')
@when('to the stream')
@when('go to stream')
@when('go to the stream')
@when('keep going')
def stream():

#set current_room as a global variable
    global current_room 
#check to see if player is at the the garden or not
    if current_room is not r_garden:
        print_slow("Hmm... You can't come to the stream\nbecause you're not in the garden.\n")
        return

    #change current room to stream
    current_room = r_stream
    print_slow("So you walked to... the stream.\n")

    #show the room description to tell player more about the "room"
    print(current_room)

#define npc, items and conditions of the room
Room.have_bundle_trash = False
r_stream.have_bundle_trash = True #must have trash
r_stream.solved = False #trash is collected
r_stream.solvedb = False #trash is not collected but player has already passed

#defining r_streams actions - fish out the trash
@when('fish them out')
@when('fish the trash out')
@when('fish them out')
def fish_trash():
    if current_room.have_bundle_trash:
        if r_stream.solved == False:
            print_slow("You tried to fish as much as you can...\nand you got a bundle of plastic\nbottles!\n")
            print_slow("You got a bundle of trash!\n")
            print_slow("You got 250 points!\n")
            print_slow("Where do you want to go?\n")
            print_slow("(keep going on the path of the stream)\n")
            inventory.add(bundle_trash)
            global p_score
            p_score += 250
            global p_karma
            p_karma += 240
            r_stream.solved = True
    else:
        print_slow("You aren't around the stream!\nWhere do you want to go?\n(keep going on the path of the stream)")

#defining r_streams actions - ignore the trash
@when('leave the trash')
@when('leave the trash on stream')
def leave_stream():
    if current_room.have_bundle_trash:
        if r_stream.solvedb == False:
            print_slow("The bottles float, and float 'til it was stopped by\nthe plants growing by the side.\nWhere do you want to go now?\n")
            print_slow("(keep going on the path of the stream)\n")
            r_stream.solvedb = True
    else:
        print_slow("\nYou're not at the stream!\nWhere do you want to go?\n(keep going on the path of the stream)")

#---------------------middle of the stream------------------------#

#defining the middle of the stream
#defining the stream
@when('keep going on the path of the stream')
@when('keep going on path of stream')
@when('keep going on path')
def stream_mid():

#set current_room as a global variable
    global current_room 
#check to see if player is at the field or not
    if current_room is not r_stream:
        print_slow("Hmm... You can't do that now because you're not in the stream.\n")
        return

    #change current room to stream
    current_room = r_stream_middle
    print_slow("So you walked on... to the middle of the stream.\nHowever...")

    #show the room description to tell player more about the "room"
    print(current_room)

#define npc, items and conditions of the room
Room.have_mama_nature = False
r_stream_middle.have_mama_nature = True #must have mama_nature npc
r_stream_middle.solved = False
r_stream_middle.solvedb = False

#defining r_stream_middles actions - yes

#these functions check for puzzles that were solved, in other words the trash that
#player collected. the more they get, the more points they get
#if player lies and say no when they do have trash they'll get less amount of points
#this is done by checking whether or not room_solved condition is True -> if it is
#then the code knows that player has the trash of that room
#alternatively, if room_solvedb is True then player hasn't picked trash up from that
#particular place.
#same with the ans_no function, however if player does have trash in their bag then
#they get penalized for lying (-20/30 points even when they collected both trash)

@when('yes')
@when('yes i did')
@when('i did')
def ans_yes():
    if current_room.have_mama_nature:
        if r_stream_middle.solved == False: #1/2 trash collected
            if r_garden.solved == True and r_stream.solvedb == True: #solved the wrapper
                inventory.discard(red_wrapper)
                print_slow('She seems unimpressed. Maybe if you collected the bundle\nof trash she would be more impressed.\nShe gave you a small bell anyways.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 50 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                global p_score
                p_score += 50
                global p_karma
                p_karma += 30
                r_stream_middle.solvedb = True
                

            elif r_garden.solvedb == True and r_stream.solved == True: #1/2 trash collected
                inventory.discard(bundle_trash)
                print_slow('She seems unimpressed. Maybe if you collected the red\nwrapper she would be more impressed.\nShe gave you a small bell anyways.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 50 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                p_score += 50
                p_karma += 30
                r_stream_middle.solvedb = True
                

            elif r_garden.solved == True and r_stream.solved == True: #both collected
                inventory.discard(bundle_trash)
                inventory.discard(red_wrapper)
                print_slow('She seems impressed. She gave you a bell and a hug!\nAnd just like that, she disappeared into thin\nair.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 100 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                p_score += 100
                p_karma += 80
                r_stream_middle.solved = True
                

            else: #nothing is found
                print_slow("She sensed that you lied.\nShe didn't give you anything.\n")
                r_stream_middle.solvedb = True
                p_karma -= 20

    if r_stream_middle.solved == True:
        print_slow("\n...Hmmmm... she isn't here anymore.\n")

#defining r_stream_middles actions - no
@when('no')
@when('no i didnt')
@when("i didnt")
def ans_no():
    if current_room.have_mama_nature:
        if r_stream_middle.solvedb == False: #1/2 trash collected
            if r_garden.solved == True and r_stream.solvedb == True: #solved the wrapper
                inventory.discard(red_wrapper)
                print_slow('She knew you lied, but she still expected better.\nShe looked at the wrapper in disappointment.\nShe gave you a small bell anyways.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 30 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                global p_score
                p_score += 30
                p_karma += 20
                r_stream_middle.solvedb = True
                

            elif r_garden.solvedb == True and r_stream.solved == True: #1/2 trash collected
                inventory.discard(bundle_trash)
                print_slow('She knew you lied, but she still expected better.\nShe looked at the bundle of bottles in disappointment.\nShe gave you a small bell anyways.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 30 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                p_score += 30
                p_karma += 20
                r_stream_middle.solvedb = True
                

            elif r_garden.solved == False and r_stream.solved == False: #both collected
                inventory.discard(bundle_trash)
                inventory.discard(red_wrapper)
                print_slow('She seems impressed, however disappointed.\nShe wanted you to say the truth, yet you lied.\nAnd just like that, she disappeared into thin\nair.')
                print_slow('You got a small bell!\n')
                print_slow('You got another 70 points.\n')
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                inventory.add(bell)
                p_score += 70
                p_karma += 50
                r_stream_middle.solvedb = True
                

            else: #nothing is found
                print_slow("""\n"Thought so," she said.\nAnd she gave you nothing.\n""")
                print_slow("You lost -50 points\n")
                print_slow("Where do you want to go?\n")
                print_slow("(go to the end of the stream)\n")
                p_score -= 50
                p_karma -= 70
                r_stream_middle.solvedb = True

    if r_stream_middle.solvedb == True:
        print_slow("\nShe's no longer here.\n")


#--------------------end of stream/game-----------------------------#

#defining the end of the stream - the end of the game
@when('the end of the stream')
@when('go to the end of the stream')
def end_stream():
#set current_room as a global variable
    global current_room 
#check to see if player is at the middle of the stream or not
    if current_room is not r_stream_middle:
        print("hmm... You can't come to that place now because\n you're not in the middle of the stream.\n")
        return

    #change current room to end of stream
    current_room = r_stream_end
    print_slow("So you walked to... the end of the stream.\n")

    #show the room description to tell player more about the "room"
    print(current_room)

#define npc, items and conditions of the room
Room.have_bird = False
r_stream_end.have_bird = True
r_stream_end.solved = False
r_stream_end.solvedb = False

#save the bird
@when('save the bird')
@when('save bird')
@when('ring the bell')
@when('scare the bird')
def ring_bell():
    if current_room.have_bird:
        if r_stream_end.solved == False:
            for bell in inventory:
                print_slow('You used the bell from the mysterious lady.\nSurprisingly, the bell made a loud sound\nand the bird flew away.\n')
                print_slow('You lost The Small Bell!\n')
                inventory.discard(bell)
                print_slow('You got 300 points!')
                print_slow("Well... that's all! To check your\nstats, put check stats into the\nconsole. To return back to menu,\nput menu in the console.\nTo exit, put exit.\n")
                print_slow("(menu/check stats/exit)")
                global p_score
                p_score += 300
                global p_karma
                p_karma += 300
                r_stream_end.solved = True
                break
        else:
            print_slow("You don't have the bell! Hmmmmm,\nmaybe you can scream at it!\n")
            print_slow('Well, you screamed at the bird\n... it flew away. Phew!\n')
            print_slow("You got 250 points... You felt\nlike you could've done better.\n")
            print_slow("Well... that's all! To check your\nstats, put check stats into the\nconsole. To return back to menu,\nput menu in the console.\nTo exit, put exit.\n")
            print_slow("(menu/check stats/exit)")
            p_score += 250
            p_karma += 250
            r_stream_end.solved = True

#ignore the bird... you evil devil!
@when('ignore the bird')
@when('ignore it')
@when('leave the bird')
def ignore_bird():
    if current_room.have_bird:
        if r_stream_end.solvedb == False:
            print_slow('...Did you just... ignored the bird?\nWell...\n')
            print_slow("Poof! A girl appeared out of thin air\nand took the trash away. She pet\nthe bird after doing so.")
            print_slow("Wait a minute...\nIs that... Greta Thunburg?!?\n")
            print_slow("She looked at you, disappointed, just\nlike the mysterious woman.\n")
            print_slow("Then just like that... Poof! She\ndisappeared.\n")
            print_slow('You lost 350 points!')
            print_slow('You lost 200 karmas!')
            print_slow("Well... that's all! To check your\nstats, put check stats into the\nconsole. To return back to menu,\nput menu in the console.")
            print_slow("(menu/check stats/exit)")
            p_score -= 350
            p_karma -= 200
            r_stream_end.solvedb = True

#----------------------------------------------------------#

#defining checking stats/more detailed check score function
#check score
@when("score")
@when("check score")
@when("points")
@when("check points")
@when('check stats')
@when('stats')
@when('check stat')
@when('stat')
@when('statistics')
@when('statistic')
def check_stats():
    if p_score <= 20: #got the stick
        print_slow("Your score is " + str(p_score) + ".\nTo gain more, you can try\nto do more for the environment!\n")
    elif p_score == 70: #after using stick + getting the wrapper LG :#
        print_slow("Your score is " + str(p_score) + ".\nYou're on the right track!\n") 
    elif p_score == 170: #after show the man the trash you've been collected
        print_slow("Your score is " + str(p_score) + ".\nYou've shown Mama Nature that you truly\ncare!\n")
    elif p_score == 320: #after you fish out the bundle of trash
        print_slow("Your score is " + str(p_score) + ".\nMan, you're on a rollll today!\n")
    elif p_score == 420:
        print_slow("Your score is " + str(p_score) + ".\nMan, amazing!\n")
    elif p_score == 620: #saved the bird
        print_slow("Your score is " + str(p_score) + ".\nYou truly cared about the environment\nand the small habitants of it,\nincluding us!\n")
    else: #if p_score isnt programmed
        print_slow("Your score is " + str(p_score) + ".\n")
    
    #check karma
    if p_karma <= 0:
        print_slow("You're on neutral/bad karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 10: #got the stick
        print_slow("You're on neutral karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 50:
        print_slow("You're on neutral/bad karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 170:
        print_slow("You're on neutral/bad karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 200:
        print_slow("You're on neutral/OK karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 270:
        print_slow("You're on neutral/good karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 290:
        print_slow("You're on neutral/good karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 310:
        print_slow("You're on neutral/fairly good karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 320:
        print_slow("You're on neutral/fairly good karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 340:
        print_slow("You're on neutral/fairly good karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma == 370:
        print_slow("You're on neutral/great karma.\nYour karma is " + str(p_karma) + ".\n")
    elif p_karma >= 670:
        print_slow("You're on amazing karma.\nYour karma is " + str(p_karma) + ".\n")
    else:
        print_slow("Your score is " + str(p_karma) + ".\n")

    #check the amount of trash collected
    if r_shed.solved == True:
        print_slow("You have picked the stick up.\n")
    elif r_shed.solved == False:
        print_slow("You haven't picked the stick up.\n")
    if r_garden.solved == True:
        print_slow("You have picked the red wrapper up\nfrom the tree.\n")
    elif r_garden.solvedb == True:
        print_slow("You haven't picked up the wrapper.\n")
    if r_stream.solved == True:
        print_slow("You have collected the bundle of trash.\n")
    elif r_stream.solvedb == True:
        print_slow("You haven't picked up the bundle of trash.\n")
    if r_stream_middle.solved == True:
        print_slow("You impressed the mysterious lady.\n")
    elif r_stream_middle.solvedb == True:
        print_slow("You disappointed the mysterious lady.\n")
    if r_stream_end.solved == True:
        print_slow("You saved the bird.\n")
    elif r_stream_end.solvedb == True:
        print_slow("You didn't save the bird\nGreta did.\n")

#come back to menu at any stages
@when('menu')
@when('go back menu')
@when('go back to menu')
def go_back_menu():
    menu()

#exiting the game
@when('help')
@when('show help')
def help_in_game():
    help()

#exiting the game
@when('exit')
@when('escape')
def exit_game():
    os.system('cls')
    sys.exit()

#-------------done with adventurelib.py setup------------------#
#Defining the game functions:
#Menu function - this will handle player's first inputs in the game.
def menu():
    print("#------Welcome to Global Citizen.------#")
    print("(-----------------Play-----------------)")
    print("(-----------------Help-----------------)")
    print("(-----------------Exit-----------------)")
    print("What would you like to do?")
    choice =  input("> ")
    if choice.lower() == ("play"):
        basicinfo()
    elif choice.lower() == ("help"):
        help()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['play','help','score','exit']: #while loop loops back to the question when there's no valid answer
        print_slow("Command unrecognized. Try again?\n")
        print_slow("What would you like to do?\n")
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
    situation provided.\n
    The options that are allowed are usually in brackets\n
    like this (menu/exit)\n
    Type menu to return to menu, type exit to exit \n
    the program.\n
    """)
    print_slow("What would you like to do?\n(menu/exit)\n")
    choice =  input("> ")
    if choice.lower() == ("menu"):
        os.system('cls')
        menu()
    elif choice.lower() == ("exit"):
        sys.exit()
    while choice.lower() not in ['menu','exit']:
        print_slow("Command unrecognized. Try again?\n")
        print_slow("What would you like to do?\n")
        choice =  input("> ")
        if choice.lower() == ("menu"):
            menu()
        elif choice.lower() == ("exit"):
            sys.exit() 


#defining the age function

def pageInput(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print_slow("That's not a number!\n")
            continue
        else:
            return userInput 
        break 

#defining the generic questions function - this function runs w/o any validation except for age 
def p_question():
    print_slow("Well, what do you want to change?\n")
    print_slow("Select what you want to change (name, age or mood):... \n")
    p_change = input("> ")
    if p_change.lower() == ("name"):
        p_name = input("So, what's your name? ")
        os.system('cls')
    if p_change.lower() == ("age"):
        print_slow ("So, what's your age this time? ")
        p_age = p_ageInput()
        os.system('cls')
    if p_change.lower() == ("mood"):
        p_mood = input("How are you feeling now? ")
        os.system('cls')
    print_slow("Alright then, let's move on.\n")     

#stage 1: gathering data from user before starting the game.
def basicinfo():
    os.system('cls')
    print_slow("Hello friend! What is your name?\n")
    print_slow("My name is...: \n")
    p_name = input("> ") # asking for name

    print_slow("Well how are you, " + p_name + "?\n")
    print_slow("I feel...: \n")
    p_mood = input("> ") #asking user for their mood

    if p_mood.lower() in lmood_happy: #good mood
        print_slow("Wow, you're happy today huh? That's great!\n")
    elif p_mood.lower in lmood_neutral: #neutral mood
        print_slow("Well, well, well, your day could've gone a bit better don't you think, " + p_name + "?\n")
    elif p_mood.lower() in lmood_sad: #sad mood
        print_slow("Aww, don't worry, tomorrow will definitely go better than today!\n")
    elif p_mood.lower() == ("sick"): #feeling not well
        print_slow("Please stay at home, wear a mask, don't go outside and wash your hand regularly!\n")

    else: #adding custom mood as the mood wasn't defined in the list/editing the list
        print_slow("Well, interesting! It seems like whatever you're feeling is not in the array.\nDo you want to add your mood into the list of moods?\n") #add mood item into the list of moods
        print_slow("(Yes/No):\n")
        p_addmood = input("> ")

        if p_addmood.lower() == ("yes"):

          #asking player what mood they're in
            print_slow("Cheerio! What type of mood are you in?\n")
            print_slow("My mood is (Happy, sad or neutral)...: \n")
            p_tolist = input("> ")

            #checks if the mood is happy
            if p_tolist.lower() == ("happy"):
                print_slow("I see that you're happy. That's good!\n")
                lmood_happy.append(p_mood)
                print_slow("The current happy mood list is:\n")
                print(lmood_happy)

            #checks if the mood is sad
            if p_tolist.lower() == ("sad"):
                print_slow("I see that you're a bit sad. Hope you feel better!\n")
                lmood_sad.append(p_mood)
                print_slow("The current sad mood list is:\n")
                print(lmood_sad)

            #checks if the mood is neutral
            if p_tolist.lower() == ("neutral"):
                print_slow("I see that you're just fine. I see.\n")
                lmood_neutral.append(p_mood)
                print_slow("The current neutral mood list is:\n")
                print(lmood_neutral) 

            #while loop to ensure players input neutral/sad/happy 
            while p_tolist.lower() not in ['happy','sad','neutral']:
                print_slow("It seemed like you didn't put in the correct choice (happy/sad/neutral).\n")
                print_slow("So, what type of mood are you feeling? (happy/sad/neutral)... \n")
                p_tolist =  input("> ")

                #checks if the mood is happy
                if p_tolist.lower() == ("happy"):
                    print_slow("I see that you're happy. That's good!\n")
                    lmood_happy.append(p_mood)
                    print_slow("The current happy mood list is:\n")
                    print(lmood_happy)

            #checks if the mood is sad
                if p_tolist.lower() == ("sad"):
                    print_slow("I see that you're a bit sad. Hope you feel better!\n")
                    lmood_sad.append(p_mood)
                    print_slow("The current sad mood list is:\n")
                    print(lmood_sad)

            #checks if the mood is neutral
                if p_tolist.lower() == ("neutral"):
                    print_slow("I see that you're just fine. I see.\n")
                    lmood_neutral.append(p_mood)
                    print_slow("The current neutral mood list is:\n")
                    print(lmood_neutral) 
    
        #if user says no              
        if p_addmood.lower() == ("no"):
            print_slow("Oh that's fine then! You can continue on...\n")

        #while loop to loop back if user didn't put (Yes/No)
        while p_addmood.lower() not in ['yes','no']:
            print_slow("It seemed like you didn't put in the correct choice ((Yes/No)).\n")
            print_slow("Do you still want to add the mood? ((Yes/No))... \n")
            p_addmood =  input("> ")

            #if user says yes
            if p_addmood.lower() == ("yes"):
                print_slow("What mood is this, " + p_name + "? (happy, neutral, sad) \n")
                print_slow("My mood is (Happy, sad or neutral)...: \n")
                p_tolist = input("> ")

                #checks if the mood is happy
                if p_tolist.lower() == ("happy"):
                    print_slow("I see that you're happy. That's good!\n")
                    lmood_happy.append(p_mood)
                    print_slow("The current happy mood list is:\n")
                    print(lmood_happy)

            #checks if the mood is sad
                if p_tolist.lower() == ("sad"):
                    print_slow("I see that you're a bit sad. Hope you feel better!\n")
                    lmood_sad.append(p_mood)
                    print_slow("The current sad mood list is:\n")
                    print(lmood_sad)

            #checks if the mood is neutral
                if p_tolist.lower() == ("neutral"):
                    print_slow("I see that you're just fine. I see.\n")
                    lmood_neutral.append(p_mood)
                    print_slow("The current neutral mood list is:\n")
                    print(lmood_neutral) 
                    
                #if user say something else the third time
                if p_tolist.lower() not in ['happy','sad','neutral']:
                    print_slow("We'll move on then.\n")
                                    
            #if user says no              
            if p_addmood.lower() == ("no"):
                print_slow("Oh that's fine then! You can continue on...\n")      
            
    #ask for age
    print_slow("How old are you?")
    print("")
    p_age = pageInput("> ")
    if p_age == 13: #check what year level the user is in
        print_slow("Oh, you're probably in Year 9 then.\n")
    elif p_age == 14:
        print_slow("Oh, you're possibly in Year 10 then.\n") 
    elif p_age == 15:
        print_slow("Oh, you may be are in Year 11 then.\n")  
    elif p_age == 16:
        print_slow("Oh, you're probably in Year 12.\n")
    else:
        print_slow("I see. You are over 17!\n") #over 17

    #asking users to check their information
    print_slow("Are these details correct?\n") 
    print_slow("Your name is " + p_name + ".\nYou are currently " + str(p_age) + " year old.\nAnd you're feeling " + p_mood + " today.\n") #convert int to str (integer to string)
    print_slow("(Yes/No): \n")
    p_confirm = input("> ")

    #run once when user gives a valid answer
    if p_confirm.lower() == ("yes"):
        print_slow("Alright then! We shall continue on!\n")
    if p_confirm.lower() == ("no"):
        p_question()
        print("")

    #while loop loops back to the question when there's no valid answer
    while p_confirm.lower() not in ['yes','no']:
        print_slow("It seemed like you didn't put in the correct choice ((Yes/No)).\n")
        print_slow("Do you still want to change your details? ((Yes/No))... \n")
        p_confirm =  input("> ")
        if p_confirm.lower() == ("yes"):
            print_slow("Well, what do you want to change?\n")
            print_slow("Select what you want to change (name, age or mood):... \n")
            p_change = input("> ")
            if p_change.lower() == ("name"):
                p_name = input("So, what's your name?\n")
                print("")
            if p_change.lower() == ("age"):
                p_age = pageInput("So, how old are you really?\n")
                print("")
            if p_change.lower() == ("mood"):
                p_mood = ("How are you feeling now?\n")     
                print("") 
            if p_confirm.lower() == ("no"):
                print_slow("Alright then! We shall continue on!\n")

    #asking player to start the game
    print_slow("So, " + p_name + ", would you like to play a game?\n ")
    print_slow("(Yes/No): \n")
    p_play = input("> ")
    #while loop loops back to the question when there's no valid answer
    while p_play.lower() not in ['yes','no']:
        print_slow("You didn't say yes or no.\n")
        print_slow("Do you want to play the game or no?\n")
        p_play = input("> ")
        if p_play.lower() == ("yes"):
            g_play()       
    if p_play.lower() == ("no"):
        print_slow("The game will return you back to the menu now.\n You can try the game later.\n")
        menu()

    #run once when user gives a valid answer
    if p_play.lower() == ("yes"):
        print_slow("Alright then! We shall continue on!\n ")
        os.system('cls')
        g_play()
    if p_play.lower() == ("no"):
        print_slow("The game will return you back to the menu now.\n You can try the game later.\n ")
        os.system('cls')
        menu()
        

#defining the play function
def g_play():
    print(r_field)
    start()

#Runs menu function
menu()
start()