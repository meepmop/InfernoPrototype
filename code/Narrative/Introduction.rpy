label Intro:
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
            "{i}[STR] are decisions that require a strength check. To pass, you will need to roll a number {b}under{/b} your Charisma/Strength stat: [ChrStr].{/i}"
            "[STR] Make the first attack":
                jump SurpriseAttack
            "Don't do anything":
                jump DoNotSee
            
    else:
        "Passive Wisdom Roll: [_rollOutcome] fail"
        jump DoNotSee

    # This ends the game.

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

        return

label SurpriseAttack:
    call DiceRoll
    $ _rollOutcome = d20
    $ _damageRoll = d6

    if StrChr >= _rollOutcome:
        "Attack Roll: [_rollOutcome] success"

        "You slowly approached the tuff, and slashed at the fluff. The tuff quickly dodged your attack, but not fast enough that it avoided your blade."

        $ EnemyHP -= _damageRoll

        "The dog takes the hit and receives [_damageRoll]; the dog has [EnemyHP] HP left."
        "How unfortunate. It must suffer now for its disobedience."
    else:
        "Attack Roll: [_rollOutcome] fail"
        "You slowly approached the tuff, but the tuff noticed your advances and exited the bush."
        "The white dog barks at you, and bares its small teeth at you. Hostility will not be tolerated."

    return


