label PlayerMove:
    while EnemyHP > 0:
        menu playerMove:
            "Your move, Little One."
            "({b}STR{/b}: roll under [ChrStr]) Attack":
                jump AttackEnemy

    "The dog is dead."
    "{b}{i}Kill: slashed the dog to death.{/i}{/b}"
    return

label AttackEnemy:
    "You attack the dog."
    
    call CainAttackRoll
    call BarkCalls

    if ChrStr >= _rollOutcome:
        "The dog takes the hit and loses [_damageRoll]! the dog has [EnemyHP] HP left."
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

    jump PlayerMove
    return


