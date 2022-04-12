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
debugmode = False
starterchosen = False
location = "Pallet Town"
destination = "null"




# Pokémon stat calculation
def statcalculate(chosenpokemon, chosenlevel):
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
def damagecalculate(chosenpokemon, chosenlevel, targetpokemon, targetlevel):
    global attackdamage, crit
    crit = False
    statcalculate(chosenpokemon, chosenlevel)
    attackdamage = 0.2 * battleatk
    round(attackdamage)
    if random.randint(0, 100) < 16:
        attackdamage = attackdamage * 2
        crit = True



def attack(firstpokemon, firstpokemonlevel, firstpokemonhp, secondpokemon, secondpokemonlevel, secondpokemonhp):
    type_message(firstpokemon + " used " + pokemonlib[firstpokemon]["move"] + "!")
    damagecalculate(firstpokemon, firstpokemonlevel, secondpokemon, secondpokemonlevel)
    secondpokemonhp = secondpokemonhp - attackdamage
    time.sleep(0.5)
    if crit == True:
        type_message("A critical hit!")
        time.sleep(0.5)



        
def faintcheck():
    if opponentpokemonhp <= 0:
        print("")
        if battletype == "trainer":
            type_message("Opponent's " + opponentpokemon + " has fainted!")
        if battletype == "wild":
            type_message("Wild " + opponentpokemon + " has fainted!")
        battleoutcome = "win"
        battlefinish()
    if selectedpokemonhp <= 0:
        print("")
        type_message(selectedpokemon + " has fainted")
        battleoutcome = "lose"
        battlefinish()




# Encounter text at the start of the battle
def trainerencounter():
    global attacked, selectedpokemonspd, opponentpokemonspd
    attacked = False
    print('''

        ''')
    type_message(title + " " + opponent + " wants to battle!")
    time.sleep(0.5)
    type_message("Go, " + selectedpokemon + "!")
    time.sleep(0.5)
    type_message("Pokémon Trainer " + rival + " sent out " + opponentpokemon + "!")
    time.sleep(0.5)
    statcalculate(selectedpokemon, selectedpokemonlevel)
    selectedpokemonhp = battlehp
    originalselectedpokemonhp = battlehp
    selectedpokemonspd = battlespd
    print(selectedpokemon + " (Lv. " + str(selectedpokemonlevel) + ")" + ": " + str(selectedpokemonhp) + "/" + str(originalselectedpokemonhp) + "HP")
    statcalculate(opponentpokemon, opponentpokemonlevel)
    opponentpokemonhp = battlehp
    originalopponentpokemonhp = battlehp
    opponentpokemonspd = battlespd
    print(opponentpokemon + " (Lv. " + str(opponentpokemonlevel) + ")" + ": " + str(opponentpokemonhp) + "/" + str(originalopponentpokemonhp) + "HP")
    fightscreen()




# Fight screen menu
def fightscreen():
    global attacked
    if attacked == True:
        print(selectedpokemon + " (Lv. " + str(selectedpokemonlevel) + ")" + ": " + str(selectedpokemonhp) + "/" + str(originalselectedpokemonhp) + "HP")
        print(opponentpokemon + " (Lv. " + str(opponentpokemonlevel) + ")" + ": " + str(opponentpokemonhp) + "/" + str(originalopponentpokemonhp) + "HP")
    print('''What will you do?
    (1) Fight
    (2) Pokémon
    (3) Run''')
    fightinput = input(">>> ")
    if fightinput == "1":
        attacked = True
        if selectedpokemonspd > opponentpokemonspd:
            attack(selectedpokemon, selectedpokemonlevel, selectedpokemonhp, opponentpokemon, opponentpokemonlevel, opponentpokemonhp)
            opponentpokemonhp = secondpokemonhp
            faintcheck()
            attack(opponentpokemon, opponentpokemonlevel, opponentpokemonhp, selectedpokemon, selectedpokemonlevel, selectedpokemonhp)
            selectedpokemonhp = secondpokemonhp
            faintcheck()
            fightscreen()
        if selectedpokemonspd < opponentpokemonspd:
            attack(opponentpokemon, opponentpokemonlevel, opponentpokemonhp, selectedpokemon, selectedpokemonlevel, selectedpokemonhp)
            faintcheck()
            selectedpokemonhp = secondpokemonhp
            attack(selectedpokemon, selectedpokemonlevel, selectedpokemonhp, opponentpokemon, opponentpokemonlevel, opponentpokemonhp)
            opponentpokemonhp = secondpokemonhp
            faintcheck()
            fightscreen()
        else:
            if random.randint(1, 2) < 1:
                attack(selectedpokemon, selectedpokemonlevel, selectedpokemonhp, opponentpokemon, opponentpokemonlevel, opponentpokemonhp)
                faintcheck()
                attack(opponentpokemon, opponentpokemonlevel, opponentpokemonhp, selectedpokemon, selectedpokemonlevel, selectedpokemonhp)
                faintcheck()
                fightscreen()
            else:
                attack(opponentpokemon, opponentpokemonlevel, opponentpokemonhp, selectedpokemon, selectedpokemonlevel, selectedpokemonhp)
                faintcheck()
                attack(selectedpokemon, selectedpokemonlevel, selectedpokemonhp, opponentpokemon, opponentpokemonlevel, opponentpokemonhp)
                faintcheck()
                fightscreen()
    if fightinput == "2":
        statcalculate(selectedpokemon, pokemonhp, pokemonlevel)
        print("Selected Pokémon:")
        print(selectedpokemon + ", the " + pokemonlib[selectedpokemon]["species"] + " Pokémon")
        print("")
        returntobattle = input("Press start to return to battle")
        print("")
        fightscreen()
    if fightinput == "3":
        if battletype == "wild":
            type_message("Are you sure (y/n)")
            runconfirm = input(">>> ")
            if runconfirm == "y":
                type_message("You ran away.")
                time.sleep(0.5)
                print('''

                ''')
                run()
            if runconfirm == "n":
                print("")
                fighscreen()
            if battletype == "trainer":
                print("You cannot run from a trainer battle!")
                print("")
                fightscreen()

def battlefinish():
    if battleoutcome == "win":
        type_message("You defeated " + title + " " + opponent + "!")
    




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
            print("")
            textspeedmenu()
        else:
            textspeed = 0.05
            type_message("Text speed has been set to slow.")
            print("")
            textspeedmenu()
    if textspeedinput == "2":
        if textspeed == 0.025:
            type_message("Text speed is already set to normal.")
            print("")
            textspeedmenu()
        else:
            textspeed = 0.025
            type_message("Text speed has been set to normal.")
            print("")
            textspeedmenu()
    if textspeedinput == "3":
        if textspeed == 0.001:
            type_message("Text speed is already set to fast.")
            print("")
            textspeedmenu()
        else:
            textspeed = 0.001
            type_message("Text speed has been set to fast.")
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
            print("")
            debugmodemenu()
        else:
            debugmode = True
            type_message("Debug Mode has been turned on.")
            print("")
            debugmodemenu()
    if debugmodeinput == "2":
        if debugmode == True:
            debugmode = False
            type_message("Debug Mode has been turned off.")
            print("")
            debugmodemenu()
        else:
            type_message("Debug Mode is already turned off.")
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
    finish_intro = input("PRESS ENTER TO CONTINUE")
    print('''

    ''')
    house()




# Player's house
def house():
    print('''Location: Home, Pallet Town
(1) Talk to Mum
(2) Exit
    ''')
    houseinput()

def houseinput():
    houseoptioninput = input(">>> ")
    if houseoptioninput == "1":
        if starterchosen == True:
            type_message("Mum:")
            type_message("\"Hi " + name + ". It looks like you need a rest.\"")
            time.sleep(0.5)
            type_message("Your Pokémon have been healed!")
            time.sleep(0.5)
            houseinput()
        else:
            type_message("Mum:")
            type_message("\"Hi " + name + ", our new neighbour Professor Oak is looking for you.\"")
            time.sleep(0.5)
            houseinput()
    if houseoptioninput == "2":
        print('''

        ''')
        pallettown()
    else:
        houseinput()




# Rival's house
def rivalhouse():
    print('''Location: ''' + rival + '''\'s House, Pallet Town
(1) Talk to ''' + rival + '''\'s Mum
(2) Exit
    ''')
    rivalhouseinput()

def rivalhouseinput():
    rivalhouseoptioninput = input(">>> ")
    if rivalhouseoptioninput == "1":
        if starterchosen == True:
            type_message(rival + "'s Mum:")
            type_message("\"Hey " + name + ". How is your's and " + rival + "'s adventure going!\"")
            time.sleep(0.5)
            rivalhouseinput()
        else:
            type_message(rival + "'s Mum:")
            type_message("\"Hey " + name + ", welcome new neighbour!. " + rival + " is outside.\"")
            time.sleep(0.5)
            rivalhouseinput()
    if rivalhouseoptioninput == "2":
        print('''

        ''')
        pallettown()
    else:
        rivalhouseinput()




# Pallet Town
def pallettown():
    print('''Location: Pallet Town
(1) ''' + name + '''\'s House
(2) ''' + rival + '''\'s House
(3) Professor Oak's Lab
(4) Route 1
    ''')
    pallettowninput()

def pallettowninput():
    pallettownoptioninput = input(">>> ")
    if pallettownoptioninput == "1":
        print('''

        ''')
        house()
    if pallettownoptioninput == "2":
        print('''

        ''')
        rivalhouse()
    if pallettownoptioninput == "3":
        if starterchosen == True:
            print('''

            ''')
            lab()
        else:
            print('''

            ''')
            emptylab()
    if pallettownoptioninput == "4":
        if starterchosen == True:
            print('''

            ''')
            route1()
        else:
            print('''

            ''')
            oakroute1()




# Professor Oak stops you from going in the tall grass
def oakroute1():
    print('''Location: Route 1
    ''')
    type_message("Professor Oak:")
    type_message("\"Hey! Wait! Don't go out!\"")
    time.sleep(0.5)
    type_message("...")
    time.sleep(0.5)
    type_message("\"It's unsafe! Wild Pokémon live in tall grass!\"")
    time.sleep(0.5)
    type_message("\"You need your own Pokémon for your protection.\"")
    time.sleep(0.5)
    type_message("\"I know! Here, come with me!\"")
    time.sleep(0.5)
    type_message("...")
    time.sleep(0.5)
    print("")
    gotolab = input("PRESS ENTER TO CONTINUE")
    print('''

    ''')
    starterselect()




# Introduction to the starter Pokémon
def starterselect():
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

def starterinput():
    type_message("Please choose a Pokémon.")
    starterselect = input(">>> ")
    global debugmode, selectedpokemon, rivalpokemon
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
    starterchosen = True
    type_message("Selected Pokémon: " + selectedpokemon)
    time.sleep(0.5)
    type_message("Are you sure you want to select this Pokémon? (y/n)")
    starterconfirm = input(">>> ")
    if starterconfirm == "y":
        global selectedpokemonlevel, rivalpokemonlevel
        selectedpokemonlevel, rivalpokemonlevel = 5, 5
        if selectedpokemon == "??????????":
            selectedpokemonlevel = 100
        type_message("You recieved " + selectedpokemon + "!")
        type_message("Professor Oak:")
        type_message("\"Good choice, " + name + ". " + selectedpokemon + " will be a great partner.\"")
        rivalscene()
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
    global rivalbattle, opponent, title, opponentpokemon, opponentpokemonlevel, battletype, pokemonhp, opponenthp
    battle = "rivalbattle"
    opponent = rival
    title = "Pokémon Trainer"
    opponentpokemon = rivalpokemon
    opponentpokemonlevel = rivalpokemonlevel
    battletype = "trainer"
    trainerencounter()
    if battleoutcome == "win":
        type_message(rival + ":")
        type_message("\"No way you beat me...\"")
        time.sleep(0.5)
        type_message(rival + " has left the lab.")
        type_message(0.5)
        type_messave("Professor Oak:")
        type_message("\"Well done " + name + "! Sorry about the attitude of my great grandson though.\"")
        time.sleep(0.5)
        type_message("\"Hopefully his Pokémon journey will change that for him.\"")
    if battleoutcome == "lose":
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
    print('''

    ''')
    pallettown()




# Route 1
def route1():
    if location == "Pallet Town":
        locationfunc = pallettown()
        destinationfunc = viridiancity()
        destination = "Viridian City"
    if location == "Viridian City":
        locationfunc = viridiancity()
        destinationfunc = pallettown()
        destination = "Pallet Town"
    if location == "Pallet Town":
        print('''Location: Route 1
(1) Walk through tall grass to ''' + destination + '''
(2) Back to ''' + location
        )
        route1input()

def route1input():
    route1optioninput = input(">>> ")
    if route1optioninput == "1":
        if random.randint(0,3) > 1:
            wildpokemon = ["Rattata", "Pidgey"]
            wildencounter()
            print('''

            ''')
            type_message("You walked to " + destination + " safely.")
            time.sleep(0.5)
            destinationfunc
        else:
            type_message("You walked to " + destination + " safely.")
            time.sleep(0.5)
            destinationfunc()
    if route1optioninput == "2":
        type_message("You walked back to " + location + ".")
        time.sleep(0.5)
        locationfunc()
    else:
        route1input()




titlescreen()
