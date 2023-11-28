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

# Character getting hurt
transform Stagger:
    linear 0.1 xoffset 20
    linear 0.1 xoffset -20
    linear 0.1 xoffset 0

transform LowerDown:
    xalign 0.0
    yalign 1.0
    linear 1.0 ypos 1.25

################################################################################
# Character Appearance Calls
################################################################################
# Cain
################################################################################
# Cain on the Left
label CainLeftIntro:
    show CHcain at left with dissolve
    return

label CainLeft:
    show CHcain at Left
    return

label CainDeath:
    hide CHcain with easeoutbottom
    return

label CainHurt:
    show CHcain at Stagger
    call DamageSound
    return

label CainLowerDown:
    show CHcain at LowerDown
    return


################################################################################
# Dog
################################################################################

# Dog on the Right
label DogRight:
    show CHDog at Right with easeinbottom
    return

# Dog Death
label DogDeath:
    hide CHDog with easeoutbottom
    return

# Dog Leaves the scene
label DogLeaves:
    hide CHDog with easeoutright
    return

label DogComesBack:
    show CHDog at Right with easeinright
    return

label DogHurt:
    show CHDog at Stagger
    call DamageSound
    return