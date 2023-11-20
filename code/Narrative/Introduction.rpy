# initialization of Flags
default wasDogSpotted = False   # did you spot the dog?

label Intro: 
    "Trigger Warning: Based on the player's choices, this demo may contain animal death and animal cruelty. This demo may be disturbing to players and players' discretion advised."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    call ForestMusic from _call_ForestMusic
    scene BGwoods with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    call CainLeftIntro from _call_CainLeftIntro

    # These display lines of dialogue.

    "You find yourself awake, nestled between the crowds of trees. They sway with joy as they watch you rise, for their saviour has finally come."

    "You looked around and found a large claymore beside you. The blade shines in the dark forest, like a lantern to guide you in the darkness."

    "You grab the blade; the familiar weight comforts you in the unknown land. You tucked the blade under your cape, and rose from the ground."

    # roll the dice to see if the player passes or not
    call DiceRoll from _call_DiceRoll_5
    $ _rollOutcome = d20

    # if the player rolls under the IntWis stat, they pass and see the dog
    if IntWis <= _rollOutcome:
        "Passive Wisdom Roll: [_rollOutcome] success"
        
        "You sense a shiver on the bush before you. At a closer inspection, you find something that does not belong in the sea of leaves."

        # Dog portraits come up
        call DogRight from _call_DogRight
        # Dog was spotted
        $ wasDogSpotted = True
        
        "A small tuff of fur hides in the cover of the bushes, and emits a silent growl. The air thins and awaits your decision."

        # the player can make an attack on the dog or choose to not do anything
        menu surpriseAttack:
            "{i}({b}STR{/b}: roll) are decisions that require a strength check. To pass, you will need to roll a number {b}under{/b} your Charisma/Strength stat: [ChrStr].{/i}"
            # attack dog
            "({b}STR{/b}: roll under [ChrStr]) Make the first attack":
                jump SurpriseAttack
            # don't attack dog
            "Don't do anything":
                jump DoNotSee

    # if player don't see shit        
    else:
        "Passive Wisdom Roll: [_rollOutcome] fail"
        jump DoNotSee

    return

# what happens when players don't see anything
label DoNotSee:
        "You look around, trying to find out where you have landed. However, an orb speeds towards you and you can feel a sharp piercing wound on your leg."

        if wasDogSpotted == False:
            call DogRight from _call_DogRight_1

        "You looked down and found your leg being caught by a white tuff of fur. A small white dog has you at its jaws and biting as hard as it could on you. Weakling."

        # roll the dice to see how much damage the player gets
        call DiceRoll from _call_DiceRoll_6
        $ _damageRoll = d4
        # damage deduction from player's max hp
        $ PlayerHP -= _damageRoll

        call CainHurt
        "You take [_damageRoll] damage and have [PlayerHP] HP left"

        "You easily shook the dog off, and the dog regains its balance then barks at you, baring its small baby teeth. It has disgraced you and dared to lay a hand on you."

        "Finish it."

        # start battle
        jump PlayerMove

        return

# making the attack on the dog if they player sees it
label SurpriseAttack:
    # call the attack roll from the player to determine the success and the damage on the enemy
    call CainAttackRoll from _call_CainAttackRoll_1

    if ChrStr >= _rollOutcome:
        "You slowly approached the tuff, and slashed at the fluff. The tuff quickly dodged your attack, but not fast enough that it avoided your blade."
        call DogHurt
        "The dog takes the hit and receives [_damageRoll]; the dog has [EnemyHP] HP left."
        "How unfortunate. It must suffer now for its disobedience."
    else:
        "You slowly approached the tuff, but the tuff noticed your advances and exited the bush."
        "The white dog barks at you, and bares its small teeth at you. Hostility will not be tolerated."
    
    # start combat
    jump PlayerMove

    return


