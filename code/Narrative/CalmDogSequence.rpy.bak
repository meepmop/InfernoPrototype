label ShhDog:
    if didYouHiss == True:
        "You clear your throat and try to calm the dog again. Hoping it does not sound like a hiss again."
    else:
        "You lower yourself and slightly raise your hands in a calming manner."

    call DiceRoll from _call_DiceRoll_3
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
            "You try to channel your best calming voice, but you got too focussed on turning your voice 
            into the pinnacle of calmness, that your “Shh” sounds like a snake’s hiss. You’re not built for this."
            "The dog sounds surprised at your hiss, and slightly backs away with a growl."
        else:
            "You try to “Shh” the dog again, but it still comes out like a hiss. The dog is still wary of you."
        $ didYouHiss = True
        jump EnemyAttack
################################################################################
## Failing the roll choices 
################################################################################
label SnakeFool:
    "You puffed up your chest, and straighten your posture. Both of your hands grabbed 
    your cape and lifted your arms, to flap your cape like a viper!"
    "The dog cowers at your size, and gives a weak bark. The dog is smarter than it looks, 
    as it does not fully buy your act."
    "You need more flair to convince the beast that you are its bane! You flap the cape and hiss at the dog."
    
    c "Hiss! Hiss!"
    
    "The dog tucks his head down and backs away, but still maintains its confidence. 
    You could hear its voice betrays it, as its mildly gruff barks becomes squeaks."
    # snake lock route
    $ areYouASnake = True
    # no more shh
    $ isDogShh = True
    jump PlayerMove

label ChaseDog: # Tolerance end
    call DogLeaves
    "You hone in at the dog, and ready yourself for a dash. However, as you attempt to 
    make a step towards the dog, you see it dash inside the bushes."
    "You run up to the bush, and find the dog has left the premises."
    "Remember its face, Little One. We will find it again, and make it pay for its mockery."
    "{b}Tolerance{/b}: Dog Runs Away"
    return

label HissLocation:
    "You waved large ripples on your cape, like a vicious monster, and gave a loud hiss. 
    The dog barks at you and tenses at your posturing."
    "The dog is planning something. Make sure you make the first move."
    $ areYouABigSnake = True
    jump PlayerMove

label BiteDog:  # Tolerance and kill end
    "You tackle the dog, and the dog was caught by surprise. 
    With the small dog in your arms, you take a large bite at the dog."
    "You couldn’t bite hard, due to its hair that stops you from going deeper in. 
    However, it seemed powerful enough as the dog yowls in pain and faints."
    call DogDeath
    "In your hands, the dog falls limp, but you could feel its panicked breaths from the movement of its stomach."

    menu ToKillOrNot:
        "In your hands, the dog falls limp, but you could feel its panicked breaths from the movement of its stomach."
        "End the dog":
            "You take the small head of the dog, and twist it. You could hear a sharp crack and the breathing stops."
            "A small death, for a small nuisance."
            "{b}{i}Kill: killed the dog through a twist.{/b}{/i}"
            return
        "Set the dog down and leave":
            "You set the dog down; you could see the dog peek out with one eye and closes, 
            as you placed the dog on the floor"
            "You move away and try to find your way around the forest, with a new found talent of being venomous."
            "{b}{i}Tolerance: You poisoned the dog?{/b}{/i}"
            return

################################################################################
## Succeeding the roll choices
################################################################################
label ApproachDog:
    "You slowly approach the dog, but the dog tightens up at your advances 
    and lets out a warning bark."
    "You decided that it was not the best action and backed away."

    $ didYouApproachTheDog = True
    jump EnemyAttack
label LowerYourself:
    "You carefully lowered your body to its height, being aware of your descent to not 
    scare the dog. Due to the small size of the dog, you had to lay on your belly to 
    be the size of the dog."
    "The dog perks his ears and tail up at your new size. 
    It stopped barking and looks at you as it tilts its head."

    $ areYouADogToo = True
    jump PlayerMove
label LayDown:
    "No. Don’t do it."
    "You slowly twist you body, so you are lying on your back and 
    look at the dog through upside down eyes."
    "The dog jumped at your changed of movement, but slowly approaches you and sniff at you."
    
    $ areYouLyingDown = True
    jump PlayerMove

label SniffHand:    # conversion and kill end
    "The dog jumps as you lift your hand to the dog. 
    However, the dog warily approaches your hand and gives a delicate sniff at your hand."
    "You could see that your hand dwarfs the dog, 
    and you can easily grab it with a quick motion. You can end this quick."

    menu BashTheDogOrSniff:
        "You could see that your hand dwarfs the dog, and you can easily grab it with a quick motion. You can end this quick."
        # Kill end
        "Grab the dog and bash its head to the ground":
            "You wait for the right moment to strike. As the dog nears your palm, 
            you grab the dog with your hand, and bashed the small creature against the ground."
            call DogDeath
            "You could not sense any motion from the dog, as it lies crushed on the ground 
            like a swatted bug."
            "{b}{i}Kill: swat the dog.{/i}{/b}"
            return
        # Conversion end
        "Do not move":
            "You do not do anything and wait for the dog to sniff your hand. 
            The dog sniffs your hand, and you can feel its soft wet nose against your rough hands."
            "It licks at your fingers. You do your best to keep your hands still, 
            but it is difficult to fight the tickle of the fluff."
            "You carefully twist your hand, and the dog softly headbutts your hand. The dog rubs its 
            small head against your hand, and you reciprocate the gesture with a pat."
            "You could feel your heart fill with joy, as the soft fur embraces your hand. 
            In your joy, you could feel something poison inside you."
            "We are disappointed at you."
            "{b}{i}Conversion: Befriend through traditional means.{/i}{/b}"
            return

label BarkBark:
    "You try to mimic the small barks the dog gives, but it comes out a 
    bit too gruff for your taste."
    "What are you doing?! This is not befitting you!"
    "You hope that your barks did not sound too gruff, and the dog responds 
    to you with a bark. A good response as the dog does not attempt to attack you. 
    You bark at the dog, and it barks as well, to form a one-sided conversation from 
    both sides."
    "Stop this playing and kill it. Don’t degrade yourself anymore for it."
    "The dog goes around you, and sniffs your butt, then comes back towards your 
    face and turns around to show its own. The tail lifts up, and you could see 
    speckles of brown on its bottom – you can tell that is not soil as it gives out a 
    pungent smell."
    "Don’t. you. dare."

    $ didYouBark = True

    jump PlayerMove

label DogAssWhiff:  # conversion end
    "You pray to no God that can answer you back, as you took a deep breath of the dog’s butt.
    It takes your whole body to prevent yourself from puking at the white fluff."
    "You manage to hold the position as long as you could, and God has placed mercy upon you 
    as the dog turns away and gave you a lively bark. The dog runs around you in circles, 
    and it has seemed that you have gained a new friend."
    "No friend is worth the cost of your pride, Little One…"
    "{b}{i}Conversion: You sniffed a dog’s ass.{/i}{/b}"
    return