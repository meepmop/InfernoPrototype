# initialization of flags
# Calm Dog flags
default isDogShh = False
## Snake Route
default didYouHiss = False
default areYouASnake = False
# Fetch Dog flags
default didYouLook = False

label PlayerMove:
    if EnemyHP > 0:
        menu playerMove:
            "Your move, Little One."
            # basic attack
            "({b}STR{/b}: roll under [ChrStr]) Attack":
                jump AttackEnemy
            # Calm Dog Sequence
            "({b}CHR{/b}: roll over [ChrStr]) Try to calm the dog" if not isDogShh:
                jump ShhDog
            ## Snake Route
            "Fool the dog into thinking you're a snake" if didYouHiss:
                jump SnakeFool
            "Run towards the dog, while flapping your cape and hissing" if areYouASnake:
                jump ChaseDog
            # Fetch Sequence
            "({b}WIS{/b}: roll under [IntWis]) Find something that can help" if not didYouLook:
                $ didYouLook = True
                jump YouSee

    "You took your sword, and dealt the killing blow on the small beast. The large blade pierces the small body; the dog lies limp on the ground surrounded in a pool of blood"
    "A deserving end for a worthless creature."
    "{b}{i}Kill: slashed the dog to death.{/i}{/b}"
    return

label AttackEnemy:
    # Player's turn
    "You attack the dog."
    
    call CainAttackRoll
    call BarkCalls

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
    call DogAttackRoll
    call BarkCalls

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



