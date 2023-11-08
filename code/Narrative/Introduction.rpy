label Intro: 
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BGwoods

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show CHcain

    # These display lines of dialogue.

    "You find yourself awake, nestled between the crowds of trees. They sway with joy as they watch you rise, for their saviour has finally come."

    "You looked around and found a large claymore beside you. The blade shines in the dark forest, like a lantern to guide you in the darkness."

    "You grab the blade; the familiar weight comforts you in the unknown land. You tucked the blade under your cape, and rose from the ground."

    call DiceRoll
    $ _rollOutcome = d20

    if IntWis <= _rollOutcome:
        "Passive Wisdom Roll: [_rollOutcome] success"
        
        "You sense a shiver on the bush before you. At a closer inspection, you find something that does not belong in the sea of leaves."
        
        "A small tuff of fur hides in the cover of the bushes, and emits a silent growl. The air thins and awaits your decision."

        menu surpriseAttack:
            "{i}({b}STR{/b}: roll) are decisions that require a strength check. To pass, you will need to roll a number {b}under{/b} your Charisma/Strength stat: [ChrStr].{/i}"
            "({b}STR{/b}: roll under [ChrStr]) Make the first attack":
                jump SurpriseAttack
            "Don't do anything":
                jump DoNotSee
            
    else:
        "Passive Wisdom Roll: [_rollOutcome] fail"
        jump DoNotSee

    return

label DoNotSee:
        "You look around, trying to find out where you have landed. However, an orb speeds towards you and you can feel a sharp piercing wound on your leg."

        "You looked down and found your leg being caught by a white tuff of fur. A small white dog has you at its jaws and biting as hard as it could on you. Weakling."

        call DiceRoll
        $ _damageRoll = d4
        $ PlayerHP -= _damageRoll

        "You take [_damageRoll] damage and have [PlayerHP] HP left"

        "You easily shook the dog off, and the dog regains its balance then barks at you, baring its small baby teeth. It has disgraced you and dared to lay a hand on you."

        "Finish it."

        jump PlayerMove

        return

label SurpriseAttack:
    call CainAttackRoll

    if ChrStr >= _rollOutcome:
        "You slowly approached the tuff, and slashed at the fluff. The tuff quickly dodged your attack, but not fast enough that it avoided your blade."
        "The dog takes the hit and receives [_damageRoll]; the dog has [EnemyHP] HP left."
        "How unfortunate. It must suffer now for its disobedience."
    else:
        "You slowly approached the tuff, but the tuff noticed your advances and exited the bush."
        "The white dog barks at you, and bares its small teeth at you. Hostility will not be tolerated."
    
    jump PlayerMove

    return


