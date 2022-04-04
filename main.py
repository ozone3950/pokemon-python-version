
import time
from pokemon import pokemonlib
import random

# The "type_message" function
textspeed = 0.025
messagedelay = 0.5
def type_message(message):
    for char in message:
        print(char, end="")
        time.sleep(textspeed)
    print()
    time.sleep(messagedelay)

# Starting perameters
debugmode = True
starterchosen = False




# Pokémon stat calculation
def statcalculate(chosenpokemon, chosenhp, chosenlevel):
    global battlehp, battleatk, battledef, battlespd
    battlehp = 0.01 * (2 * pokemonlib[chosenpokemon]["hp"] * chosenlevel) + chosenlevel + 10
    battlehp = round(battlehp)
    battleatk = 0.01 * (2 * pokemonlib[chosenpokemon]["hp"] * chosenlevel) + chosenlevel + 10
    battleatk = round(battleatk)
    battledef = 0.01 * (2 * pokemonlib[chosenpokemon]["hp"] * chosenlevel) + chosenlevel + 10
    battledef = round(battledef)
    battlespd = 0.01 * (2 * pokemonlib[chosenpokemon]["hp"] * chosenlevel) + chosenlevel + 10
    battlespd = round(battlespd)




# Attack damage calculation
def pokemonattack(chosenpokemon, chosenhp, chosenlevel):
    statcalculate(chosenpokemon, chosenhp, chosenlevel)
    attackdamage = 0.2 * chosenpokemon[atk]
    if random.randint(0, 100) < 16:
        attackdamage = attackdamage * 2    




# Encounter text at the start of the battle
def encounter():
    print('''

        ''')
    type_message(title + " " + opponent + " wants to battle!")
    time.sleep(0.5)
    type_message("Go, " + selectedpokemon + "!")
    time.sleep(0.5)
    type_message("Pokémon Trainer " + rival + " sent out " + opponentpokemon + "!")
    statcalculate(selectedpokemon, pokemonhp, pokemonlevel)
    print(selectedpokemon + ": " + str(battlehp) + "/" + str(battlehp) + "HP")
    statcalculate(opponentpokemon, opponenthp, opponentpokemonlevel)
    print(opponentpokemon + ": " + str(battlehp) + "/" + str(battlehp) + "HP")
    fightscreen()




# Fight screen menu
def fightscreen():
    print('''What will you do?
    (1) Fight
    (2) Pokémon
    (3) Run''')
    fightinput = input(">>> ")
    if fightinput == "1":
        type_
    if fightinput == "2":
        statcalculate(selectedpokemon, pokemonhp, pokemonlevel)
        type_message("Pokédex scanning...")
        time.sleep(0.5)
        print("Your Pokémon:")
        print(selectedpokemon + ", the " + pokemonlib[selectedpokemon]["species"] + " Pokémon")
        print("Level: " + str(pokemonlevel))
        print("Evolution Level: " + pokemonlib[selectedpokemon]["evolvl"])
        print("Type: " + pokemonlib[selectedpokemon]["type"])
        print("HP: " + battlehp)
        print("Attack: " + battleatk)
        print("Defence: " + battledef)
        print("Speed: " + battlespd)
        print("Move: " + pokemonlib[selectedpokemon]["move"])
        print("")
        statcalculate(opponentpokemon, opponenthp, opponentpokemonlevel)
        print("Opponent's Pokémon:")
        print(opponentpokemon + ", the " + pokemonlib[opponentpokemon]["species"] + " Pokémon")
        print("Level: ", opponentpokemonlevel)
        print("Evolution Level: " + pokemonlib[opponentpokemon]["evolvl"])
        print("Type: " + pokemonlib[opponentpokemon]["type"])
        print("HP: " + battlehp)
        print("Attack: " + battleatk)
        print("Defence: " + battledef)
        print("Speed: " + battlespd)
        print("Move: " + pokemonlib[opponentpokemon]["move"])
        print("")
        returntobattle = input("Press start to return to battle")
        fightscreen()
    if fightinput == "3":
            if runconfirm == "y":
                if battletype == "wild":
                    type_message("Are you sure (y/n)")
                    runconfirm = input(">>> ")
                    if runconfirm == "y":
                        type_message("You ran away.")
                        time.sleep(0.5)
                        print("")
                        run()
                    if runconfirm == "n":
                        print("")
                        fighscreen()
                if battletype == "trainer":
                    print("You cannot run from a trainer battle!")
                    print("")
                    fightscreen()




# Titlescreen
def titlescreen():
    print('''Pokémon Python Version
    ''')
    start = input("PRESS START")
    menu()

def menu():
    print('''(1) New Game
(2) Options
(3) Return
    ''')
    startmenu()




# Menus
def startmenu():
    startmenuinput = input(">>> ")
    if startmenuinput == "1":
        print('''

        ''')
        intro()
    if startmenuinput == "2":
        print('''(1) Text Speed
(2) Debug Mode
(3) Return
        ''')
        optionsmenu()
    if startmenuinput == "3":
        print("")
        titlescreen()
        
    else:
        ('''Invalid option.
        ''')
        startmenu()
            
def optionsmenu():
    optionsmenuinput = input(">>> ")
    if optionsmenuinput == "1":
        print('''(1) Slow
(2) Normal
(3) Fast
(4) Return
        ''')
        textspeedmenu()
    if optionsmenuinput == "2":
        print('''(1) On
(2) Off
(3) Return
        ''')
        debugmodemenu()
    if optionsmenuinput == "3":
        print("")
        menu()
    else:
        print('''Invalid option.
        ''')
        optionsmenu()

def textspeedmenu():
    global textspeed
    textspeedinput = input(">>> ")
    if textspeedinput == "1":
        if textspeed == 0.05:
            type_message("Text speed is already set to slow.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
        else:
            textspeed = 0.05
            type_message("Text speed has been set to slow.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
    if textspeedinput == "2":
        if textspeed == 0.025:
            type_message("Text speed is already set to normal.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
        else:
            textspeed = 0.025
            type_message("Text speed has been set to normal.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
    if textspeedinput == "3":
        if textspeed == 0.001:
            type_message("Text speed is already set to fast.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
        else:
            textspeed = 0.001
            type_message("Text speed has been set to fast.")
            time.sleep(0.5)
            print("")
            textspeedmenu()
    if textspeedinput == "4":
        print("")
        menu()
    else:
        ('''Invalid option.
        ''')
        textspeedmenu()

def debugmodemenu():
    global debugmode
    debugmodeinput = input(">>> ")
    if debugmodeinput == "1":
        if debugmode == True:
            type_message("Debug Mode is already turned on.")
            time.sleep(0.5)
            print("")
            debugmodemenu()
        else:
            debugmode = True
            type_message("Debug Mode has been turned on.")
            time.sleep(0.5)
            print("")
            debugmodemenu()
    if debugmodeinput == "2":
        if debugmode == True:
            debugmode = False
            type_message("Debug Mode has been turned off.")
            time.sleep(0.5)
            print("")
            debugmodemenu()
        else:
            type_message("Debug Mode is already turned off.")
            time.sleep(0.5)
            print("")
            debugmodemenu()
    if debugmodeinput == "3":
        print("")
        menu()
    else:
        ('''Invalid option.
        ''')
        debugmodemenu()




# Introduction to the game
def intro():
    type_message("Professor Oak:")
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
    if name == "":
        name = "Python"
    type_message("\"Right! So your name is " + name + "!\"")
    time.sleep(0.5)
    type_message("\"This is my great grandson. He's been your rival since you were a baby.\"")
    time.sleep(0.5)
    type_message("\"…Erm, what is his name again?\"")
    global rival
    rival = input(">>> ")
    if rival == "":
        rival = "Fred"
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
    house()




def house():
    print('''Location: Home, Pallet Town
(1) Exit
    ''')
    houseinput()

def houseinput():
    global starterchosen
    houseinput = input(">>> ")
    if houseinput == "1":
        if starterchosen == False:
            starterselect()
        else:
            pallettown()
    else:
        houseinput()




# Introduction to the starter Pokémon
def starterselect():
    print('''

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
    print('''
(1) Bulbasaur, the Seed Pokémon
(2) Charmander, the Lizard Pokémon
(3) Squirtle, the Tiny Turtle Pokémon
    ''')
    starterinput()




# Starter selection menu
def starterinput():
    global debugmode
    type_message("Please choose a Pokémon.")
    starterselect = input(">>> ")
    global selectedpokemon, rivalpokemon
    if starterselect == "1":
        selectedpokemon = "Bulbasaur"
        
        rivalpokemon = "Charmander"
    if starterselect == "2":
        selectedpokemon = "Charmander"
        rivalpokemon = "Squirtle"
    if starterselect == "3":
        selectedpokemon = "Squirtle"
        rivalpokemon = "Bulbasaur"
    if debugmode == True:
        if starterselect == "debug123":
            selectedpokemon = "??????????"
            rivalpokemon = "Squirtle"
    else:
        starterinput()
    starterchosen = True
    type_message("Selected Pokémon: " + selectedpokemon)
    time.sleep(0.5)
    type_message("Are you sure you want to select this Pokémon? (y/n)")
    starterconfirm = input(">>> ")
    if starterconfirm == "y":
        global pokemonlevel, rivalpokemonlevel
        pokemonlevel, rivalpokemonlevel = 5, 5
        if selectedpokemon == "??????????":
            pokemonlevel = 100
        type_message("You recieved " + selectedpokemon + "!")
        type_message("Professor Oak:")
        type_message("\"Good choice, " + name + ". " + selectedpokemon + " will be a great partner.\"")
        rivalscene()
        return
    if starterconfirm == "n":
        starterinput()
    else:
        starterinput()




# Rival walking in scene
def rivalscene():
    type_message(rival + ":")
    type_message("\"Hey gramps, I'm here for that Pokémon that you were talking about.\"")
    time.sleep(0.5)
    type_message("\"Wait, how come " + name + " got a Pokémon before me?\"")
    time.sleep(0.5)
    type_message("Professor Oak:")
    type_message("\"Well " + rival + ", " + name + " showed up on time.\"")
    time.sleep(0.5)
    type_message(rival + ":")
    type_message("\"In that case, I have the chance to get the type advantage!\"")
    time.sleep(0.5)
    type_message(rival + " recieved " + rivalpokemon + "!")
    time.sleep(0.5)
    type_message(rival + ":")
    type_message("\"Now we're both here we may as well battle.\"")
    time.sleep(0.5)
    rivalbattle()




# First rival battle
def rivalbattle():
    global opponent, title, opponentpokemon, opponentpokemonlevel, battletype, pokemonhp, opponenthp
    opponent = rival
    title = "Pokémon Trainer"
    opponentpokemon = rivalpokemon
    opponentpokemonlevel = rivalpokemonlevel
    battletype = "trainer"
    pokemonhp = 0
    opponenthp = 0
    encounter()
    if battle == "win":
        type_message(rival + ":")
        type_message("\"No way you beat me...\"")
        time.sleep(0.5)
        type_message(rival + " has left the lab.")
        type_message(0.5)
        type_messave("Professor Oak:")
        type_message("\"Well done " + name + "! Sorry about the attitude of my great grandson though.\"")
        time.sleep(0.5)
        type_message("\"Hopefully his Pokémon journey will change that for him.\"")
    if battle == "lose":
        type_message(rival + ":")
        type_message("\"Haha, that was easy, see you around, " + name + ".\"")
        time.sleep(0.5)
        type_message(rival + " has left the lab.")
        type_message("Professor Oak:")
        type_message("\"Sorry about that " + name + ". Please don't mind the attitude of my great grandson though.\"")
        timel.sleep(0.5)
        type_message("\"Hopefully his Pokémon journey will change that for him.\"")
    time.sleep(0.5)
    type_message("...")
    time.sleep(0.5)
    print("")
    exitlab = input("PRESS ENTER TO CONTINUE")
    pallettown()

def pallettown():
    print('''
Location: Pallet Town
(1) ''' + name + '''\'s House
(2) ''' + rival + '''\'s House
(3) Professor Oak's Lab
(4) Route 1
    ''')

def pallettowninput():
    pallettowninput = input(">>> ")
    if pallettowninput == "1":
        print('''

        ''')
        house()
    if pallettowninput == "2":
        rivalhouse()
    if pallettowninput == "3":
        lab()
    if pallettowninput == "4":
        route101()




titlescreen()
