label DiceRoll:
    $ d3 = renpy.random.randint(1,3)
    $ d4 = renpy.random.randint(1,4)
    $ d6 = renpy.random.randint(1,6)
    $ d20 = renpy.random.randint(1,20)
    return

label CainAttackRoll:
    call DiceRoll
    $ _rollOutcome = d20
    $ _damageRoll = d6

    if ChrStr >= _rollOutcome:
        "Attack Roll: [_rollOutcome] success"
        $ EnemyHP -=_damageRoll
        if EnemyHP <= 0:
            $ EnemyHP = 0
    else:
        "Attack Roll: [_rollOutcome] fail"
    return

label BarkCalls:
    call DiceRoll
    $ _bark = d3
    if _previousBark == None:
        $ _previousBark = _bark
    elif _previousBark == _bark:
        jump BarkCalls
    else:
        $ _previousBark = _bark
    return