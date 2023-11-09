# initialization of flags
################################################################################
# Attack flags
################################################################################
default isDogAngry = False              # di you make the dog angry?
################################################################################
# Calm Dog flags 
################################################################################
default isDogShh = False                # did you successfully shh the dog?
## Snake Route #################################################################
default didYouHiss = False              # did you accidentally hiss at the dog?
default areYouASnake = False            # did you go along being a snake?
default areYouABigSnake = False         # did you just admit you are a snake and start becoming one?
## One of Us route #############################################################
default didYouApproachTheDog = False    # did you try to approach the dog?
default areYouADogToo = False           # did you lower yourself and make the dog question you?
default areYouLyingDown= False          # are you lying down?
default didYouBark = False              # did you just bark at the dog?
################################################################################
# Fetch Dog flags 
################################################################################
default didYouLook = False              # did you try to look around to find something that can help you out?
default doYouHaveBigStick = False       # do you have a big stick?
default doYouSeeRiver = False           # do you see a river?
default didDogBringBackStick = False    # did the dog bring back the stick you threw?
################################################################################

label PlayerMove:
    if EnemyHP > 0:
        menu playerMove:
            "Your move, Little One."
            # basic attack
            "({b}STR{/b}: roll under [ChrStr]) Attack":
                jump AttackEnemy
            ################################################################################
            # Calm Dog Sequence
            "({b}CHR{/b}: roll over [ChrStr]) Try to calm the dog" if not isDogShh:
                jump ShhDog
            ################################################################################
            ## Failed roll: Snake Route
            "Fool the dog into thinking you're a snake" if didYouHiss:
                jump SnakeFool
            "Run towards the dog, while flapping your cape and hissing" if areYouASnake:
                jump ChaseDog
            "Continue flapping and hissing" if areYouASnake and not areYouABigSnake:
                jump HissLocation
            "Bite the dog" if areYouABigSnake:
                jump BiteDog
            ################################################################################
            ## Success roll : One of us One of us
            "Slowly approach dog" if isDogShh and not didYouApproachTheDog and not areYouLyingDown:
                jump ApproachDog
            "Lower yourself to the dog's height" if isDogShh and not areYouADogToo:
                jump LowerYourself
            "Lay on your back and show your belly like a dog" if areYouADogToo and not areYouLyingDown:
                jump LayDown
            "Let the dog sniff your hand" if areYouLyingDown:
                jump SniffHand
            "Bark at the dog" if areYouLyingDown and not didYouBark:
                jump BarkBark
            "Sniff the dog's butt" if didYouBark:
                jump DogAssWhiff
            ################################################################################
            # Fetch Sequence
            "({b}WIS{/b}: roll under [IntWis]) Find something that can help" if not didYouLook:
                jump YouSee
            "Lure the dog with the stick and throw the stick in the river" if didYouLook and doYouSeeRiver:
                jump DogToRiver
            "Throw the stick at the dog" if didYouLook and not doYouHaveBigStick:
                jump StickAtDog
            "({b}STR{/b}: roll under [ChrStr]) Throw the stick at the dog" if didYouLook and not doYouSeeRiver:
                jump StickAtDog
            "Throw the stick into the forest" if didYouLook and not doYouHaveBigStick:
                jump FetchBoy
            "({b}STR{/b}: roll under [ChrStr]) Throw the stick into the forest" if didYouLook and doYouHaveBigStick:
                jump FetchBoy

    "You took your sword, and dealt the killing blow on the small beast. The large blade pierces 
    the small body; the dog lies limp on the ground surrounded in a pool of blood"
    "A deserving end for a worthless creature."
    "{b}{i}Kill: slashed the dog to death.{/i}{/b}"
    return

################################################################################
## Attack Sequence
################################################################################
label AttackEnemy:
    # Player's turn
    "You attack the dog."
    
    call CainAttackRoll from _call_CainAttackRoll
    call BarkCalls from _call_BarkCalls

    if ChrStr >= _rollOutcome:
        "The dog takes the hit and loses [_damageRoll]! the dog has [EnemyHP] HP left."
        if EnemyHP > 0:
            if _bark == 1:
                "Keep going, Little One."
            elif _bark == 2:
                "We are cheering for you!"
            else:
                "No mercy."
    else:
        "The attack misses."
        if _bark == 1:
            "Once more."
        elif _bark == 2:
            "Careful, Little One."
        else:
            "Focus."
    
    # if enemy is still alive, they will do their attack
    if EnemyHP > 0:
        jump EnemyAttack
    
    # if enemy is dead, go back to PlayerMove
    jump PlayerMove
    return

label EnemyAttack:
    # Dog's turn
    "The dog tries to bite you."
    call DogAttackRoll from _call_DogAttackRoll
    call BarkCalls from _call_BarkCalls_1

    if _didEnemyLandAttack:
        if _bark == 1:
            "How dare it."
        elif _bark == 2:
            "It will regret that."
        else:
            "Stay strong."
    else:
        if _bark == 1:
            "Expected."
        elif _bark == 2:
            "Worthless."
        else:
            "Waste of time."
    
    jump PlayerMove
    return



