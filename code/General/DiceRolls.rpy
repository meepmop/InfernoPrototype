# the available dices
label DiceRoll:
    $ d3 = renpy.random.randint(1,3)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d10 = renpy.random.randint(1,10)
    $ d20 = renpy.random.randint(1,20)
    return

# the player's attack rolls
label CainAttackRoll:
    # take the dice and roll it to determine the _rollOutcome and _damageRoll
    call DiceRoll from _call_DiceRoll
    $ _rollOutcome = d20
    $ _damageRoll = d6

    if ChrStr >= _rollOutcome:
        "Attack Roll: [_rollOutcome] success"
        $ EnemyHP -=_damageRoll
        # if EnemyHp is lower than 0, make it 0
        if EnemyHP <= 0:
            $ EnemyHP = 0
    else:
        "Attack Roll: [_rollOutcome] fail"
    return

# Dog attack rolls
label DogAttackRoll:
    call DiceRoll from _call_DiceRoll_1
    $ _rollOutcome = d20
    $ _damageRoll = d4
    $ _didEnemyLandAttack = False

    if DexCon >= _rollOutcome:
        $ PlayerHP -= _damageRoll
        # if PlayerHp is lower than 0, make it 0
        if PlayerHP <= 0:
            $ PlayerHP = 0
        "The attack lands! You take [_damageRoll] damage and have [PlayerHP] HP left"
        $ _didEnemyLandAttack = True
    else:
        "The dog misses."
    return

# barks for the player based on if they manage to hit or miss and if the dog manages to hit or miss
label BarkCalls:
    call DiceRoll from _call_DiceRoll_2
    $ _bark = d3
    if _previousBark == None:
        $ _previousBark = _bark
    elif _previousBark == _bark:
        jump BarkCalls
    else:
        $ _previousBark = _bark
    return

# large stick rolls for large stick causes
label LargeStickGamble:
    call DiceRoll from _call_DiceRoll_7
    $ _rollOutcome = d20
    $ _damageRoll = d10

    if ChrStr >= _rollOutcome:
        "Strength Roll: [_rollOutcome] success"
        $ _largeSuccess = True

    else:
        "Strength Roll: [_rollOutcome] fail"
        $ _largeSuccess = False
    return