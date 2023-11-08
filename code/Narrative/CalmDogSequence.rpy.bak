label ShhDog:
    if didYouHiss == True:
        "You clear your throat and try to calm the dog again. Hoping it does not sound like a hiss again."
    else:
        "You lower yourself and slightly raise your hands in a calming manner."

    call DiceRoll
    $ _rollOutcome = d20

    if ChrStr <= _rollOutcome:
        "Charisma Roll: [_rollOutcome] success"
        "You quietened your voice and softly calmed the dog."
        "You can see that the dog’s posture relaxes a bit, but it still keeps its stance; some of its aggression has faded away due to your actions."
        # success in shh
        $ isDogShh = True
        # remove all the other paths that makes you look like snake
        $ didYouHiss = False
        $ areYouASnake = False
        jump PlayerMove
    else:
        "Charisma Roll: [_rollOutcome] fail"
        if didYouHiss == False:
            "You try to channel your best calming voice, but you got too focussed on turning your voice into the pinnacle of calmness, 
            that your “Shh” sounds like a snake’s hiss. You’re not built for this."
            "The dog sounds surprised at your hiss, and slightly backs away with a growl."
        else:
            "You try to “Shh” the dog again, but it still comes out like a hiss. The dog is still wary of you."
        $ didYouHiss = True
        jump EnemyAttack

label SnakeFool:
    "You puffed up your chest, and straighten your posture. Both of your hands grabbed your cape and lifted your arms, to flap your cape like a viper!"
    "The dog cowers at your size, and gives a weak bark. The dog is smarter than it looks, as it does not fully buy your act."
    "You need more flair to convince the beast that you are its bane! You flap the cape and hiss at the dog."
    c "Hiss! Hiss!"
    "The dog tucks his head down and backs away, but still maintains its confidence. You could hear its voice betrays it, as its mildly gruff barks becomes squeaks."
    # snake lock route
    $ areYouASnake = True
    # no more shh
    $ isDogShh = True
    jump PlayerMove

label ChaseDog:
    "You hone in at the dog, and ready yourself for a dash. However, as you attempt to make a step towards the dog, you see it dash inside the bushes."
    "You run up to the bush, and find the dog has left the premises."
    "Remember its face, Little One. We will find it again, and make it pay for its mockery."
    "{b}Tolerance Spare{/b}: Dog Runs Away"
    return

