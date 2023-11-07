# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Cain")
define d = Character("Dog")
# The game starts here.

label start:

    # stat initialization

    # player stats
    $ PlayerHP = 20
    $ Wisdom = 10

    # enemy stats
    $ EnemyHP = 10

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BGwoods

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show CHcain

    jump Intro

    return
