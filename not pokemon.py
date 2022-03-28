import time


# The "Type Message" function
letter_delay = 0.025
message_delay = 0.5
def type_message(message):
    for char in message:
        print(char, end="")
        time.sleep(letter_delay)
    print()
    time.sleep(message_delay)

hp = 16


# Titlescreen
def titlescreen():
    print('''
      ___     _                        ___      _   _              __   __          _
     | _ \___| |_____ _ __  ___ _ _   | _ \_  _| |_| |_  ___ _ _   \ \ / /__ _ _ __(_)___ _ _
     |  _/ _ \ / / -_) '  \/ _ \ ' \  |  _/ || |  _| ' \/ _ \ ' \   \ V / -_) '_(_-< / _ \ ' \\
     |_| \___/_\_\___|_|_|_\___/_||_| |_|  \_, |\__|_||_\___/_||_|   \_/\___|_| /__/_\___/_||_|
                                           |__/
    
                                        PRESS ENTER''')
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
    intro()



# Introduction to the game
def intro():
    type_message("Proffessor Oak:")
    type_message("*coughs* \"Oh- Hello there! Welcome to the world of Pokémon!\"")
    time.sleep(0.5)
    type_message("\"My name is Oak! People call me the Pokémon Professor!\"")
    time.sleep(0.5)
    type_message("\"This world is inhabited by creatures called Pokémon!\"")
    time.sleep(0.5)
    type_message("\"For some people, Pokémon are pets. Other use them for fights.\"")
    time.sleep(0.5)
    type_message("\"Myself… I study Pokémon as a profession.\"")
    time.sleep(0.5)
    type_message("\"First, what is your name?\"")
    global name
    name = input(">>> ")
    type_message("\"Right! So your name is " + name + "!\"")
    time.sleep(0.5)
    type_message("\"This is my great grandson. He's been your rival since you were a baby.\"")
    time.sleep(0.5)
    type_message("\"…Erm, what is his name again?\"")
    global rival
    rival = input(">>> ")
    type_message("\"That's right! I remember now! His name is " + rival + "!\"")
    time.sleep(0.5)
    type_message("\"I'm getting too old for this...\"")
    time.sleep(0.5)
    type_message("\"I mean- " + name + "! Your very own Pokémon legend is about to unfold!\"")
    time.sleep(0.5)
    type_message("\"A world of dreams and adventures with Pokémon awaits! Let's go!\"")
    time.sleep(0.5)
    print("")
    type_message("PRESS ENTER TO CONTINUE")
    finish_intro = input("")
    if finish_intro == "":
        starter()
    else:
        starter()




# Introduction to the starter Pokémon
def starter():
    print('''
[==================================================================================================]
        ''')
    type_message("Professor Oak:")
    type_message("\"Hello again, " + name + ". You are ready to receive your first Pokémon.\"")
    time.sleep(0.5)
    type_message("\"Please follow me this way.\"")
    time.sleep(0.5)
    type_message("...")
    time.sleep(0.5)
    type_message("\"" + name + ", these Pokémon are extremely rare. Please make your choice carefully.\"")
    time.sleep(0.5)
    print("")
    type_message("(1) Bulbasaur, the Seed Pokémon.")
    time.sleep(0.5)
    type_message("(2) Torchic, the Chick Pokémon.")
    time.sleep(0.5)
    type_message("(3) Froakie, the Bubble Frog Pokémon.")
    time.sleep(0.5)
    print("")
    starterinput()
    
    
    
    
# Starter selection menu
def starterinput():
    type_message("Please choose a Pokémon.")
    starterselect = input(">>> ")
    global pokemon
    global rivalpokemon
    if starterselect == "1":
        pokemon = "Bulbasaur"
        rivalpokemon = "Torchic"
    if starterselect == "2":
        pokemon = "Torchic"
        rivalpokemon = "Froakie"
    if starterselect == "3":
        pokemon = "Froakie"
        rivalpokemon = "Bulbasaur"
    type_message("Selected Pokémon: " + pokemon)
    time.sleep(0.5)
    type_message("Are you sure you want to select this Pokémon? (y/n)")
    starterconfirm = input(">>> ")
    if starterconfirm == "y":
        type_message("You recieved " + pokemon + "!")
        type_message("Proffessor Oak:")
        type_message("\"Good choice, " + name + ". " + pokemon + " will be a great partner.\"")
        rivalscene()
        return
    if starterconfirm == "n":
        starterinput()
        return
    else:
        starterinput()
        return
    
    
    
            
def rivalscene():
    type_message(rival + ":")
    type_message("\"Hey gramps, I'm here for that Pokémon that you were talking about.\"")
    time.sleep(0.5)
    type_message("\"Wait, how come " + name + " got a Pokémon before me?\"")
    time.sleep(0.5)
    type_message("Proffesor Oak:")
    type_message("\"Well " + rival + ", " + name + " showed up on time.\"")
    time.sleep(0.5)
    type_message("\"In that case, I have the chance to get the type advantage!\"")
    time.sleep(0.5) 
    type_message(rival + " recieved " + rivalpokemon + "!")
    time.sleep(0.5)
    type_message(rival + ":")
    type_message("\"Now we're both here we may as well battle.\"")
    time.sleep(0.5)
    rivalbattle()
    
    
    
    
def rivalbattle():
    print('''
[==================================================================================================]
        ''')
    type_message("Pokémon Trainer " + rival + " wants to battle!")
    time.sleep(0.5)
    type_message("Go, " + pokemon + "!")
    time.sleep(0.5)
    type_message("Pokémon Trainer " + rival + " sent out " + rivalpokemon + "!")
    print("")
    type_message(pokemon + ": " + str(hp) + "/" + str(hp) + "HP")
    type_message(rivalpokemon + ": " + str(hp) + "/" + str(hp) + "HP")
    type_message("What will you do?")
    type_message("(1) Fight")
    type_message("(2) Item")
    type_message("(3) Pokémon")
    type_message("(4) Run")
    rivalfightinput = input(">>> ")
    
    
    
    
titlescreen()
