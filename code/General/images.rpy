# defined backgrounds
################################################################################
image BGwoods = "BG_Limbo_Forest.png"
################################################################################
# defined images
################################################################################
image CHcain = "Side_Cain.png"
image CHDog = "Side_Dog.png"
################################################################################
# positions of characters
################################################################################
# Character at Left side of the screen
transform Left:
    xalign 0.0
    yalign 1.0

# Character at Right side of the screen
transform Right:
    xalign 1.0
    yalign 1.0
################################################################################
# Character Appearance Calls
################################################################################
# Cain on the Left
label CainLeft:
    show CHcain at Left
    return

# Dog on the Right
label DogRight:
    show CHDog at Right 
    return
