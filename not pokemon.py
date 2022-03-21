import time

# Remember to use https://fsymbols.com/draw/

# The "Type Message" function
letter_delay = 0.025
message_delay = 0.5
def type_message(message):
    for char in message:
        print(char, end="")
        time.sleep(letter_delay)
    print()
    time.sleep(message_delay)




# Introduction to the game
def intro():
    type_message("Phone dialing...")
    type_message("PROF OAK:")
    type_message("*coughs* Oh- Hello there! Welcome to the world of Pokémon!")
    time.sleep(0.5)
    type_message("My name is Oak! People call me the Pokémon Professor!")
    time.sleep(0.5)
    type_message("This world is inhabited by creatures called Pokémon!")
    time.sleep(0.5)
    type_message("For some people, Pokémon are pets. Other use them for fights.")
    time.sleep(0.5)
    type_message("Myself… I study Pokémon as a profession.")
    time.sleep(0.5)
    type_message("First, what is your name?")
    name = input(">>> ")
    type_message("Right! So your name is " + name + "!")
    time.sleep(0.5)
    type_message("This is my great grandson. He's been your rival since you were a baby.")
    time.sleep(0.5)
    type_message("…Erm, what is his name again?")
    rival = input(">>> ")
    type_message("That's right! I remember now! His name is " + rival + "!")
    time.sleep(0.5)
    type_message("I'm getting too old for this...")
    time.sleep(0.5)
    type_message("I mean- " + name + "! Your very own Pokémon legend is about to unfold!")
    time.sleep(0.5)
    type_message("A world of dreams and adventures with Pokémon awaits! Let's go!")


def home_start():
    type_message("Location: Home")
    time.sleep(0.5)
    type_message("Options:")
    type_message("(1) Read Oak's note.")
    type_message("(2) Exit home.")
    home_start = input(">>> ")
    if home_start == "1":
        type_message("")


# Titlescreen
def titlescreen():
    print('''
      ___     _                        ___      _   _              __   __          _
     | _ \___| |_____ _ __  ___ _ _   | _ \_  _| |_| |_  ___ _ _   \ \ / /__ _ _ __(_)___ _ _
     |  _/ _ \ / / -_) '  \/ _ \ ' \  |  _/ || |  _| ' \/ _ \ ' \   \ V / -_) '_(_-< / _ \ ' \\
     |_| \___/_\_\___|_|_|_\___/_||_| |_|  \_, |\__|_||_\___/_||_|   \_/\___|_| /__/_\___/_||_|
                                           |__/
    
                                        PRESS START''')
    start = input("")
    if start == "":
        print('''

[==================================================================================================]
        ''')
        intro()
    else:
        print('''

[==================================================================================================]
        ''')
        titlescreen()


# Runs the first part of the game
titlescreen()
