# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# define are used for things that do not change in the same way that variables do

define c = Character("Cain")
define d = Character("Dog")
# The game starts here.

# player stats
# default is used for establishing variables that will change in the future
default PlayerHP = 20
default ChrStr = 15
default IntWis = 10

# enemy stats
default EnemyHP = 10

label start:
    #default rolls
    $ _previousBark = None
    
    # places the player into the intro sequence
    jump Intro

    # turns off the game
    return
