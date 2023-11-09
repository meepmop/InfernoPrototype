label YouSee:
    "You look around your surroundings; trying to find something that can stop the dog from 
    looking like it wants to make you its new chewtoy."

    call DiceRoll from _call_DiceRoll_4
    $ _rollOutcome = d20

    if IntWis >= _rollOutcome:
        "Wisdom Roll: [_rollOutcome] success"
        "You look around the premises. A small stick lays near you and you could also spot 
        the whispers of rushing water. You turned towards the noise, and found a river beyond 
        the curtain of the woods."
        "You grab the stick and determine that, with your strength, you could throw the stick 
        towards the river."
        "You turn back and find the dog still growling at you, but its eyes are trained at the stick 
        that you have picked up. The dog may look hostile towards you, but you could see behind 
        the fluff that its tail is wagging."
        $ doYouSeeRiver = True
    else: 
        "Wisdom Roll: [_rollOutcome] fail"
        "You looked around and found a very large stick. It doesn’t look like the dog could bite it, 
        as you doubt yourself if you could lift it yourself."
        $ doYouHaveBigStick = True
    $ didYouLook = True
    jump PlayerMove

label DogToRiver:   # Kill End
    "You wiggle the stick in front of the dog, and the dog follows the movement of the stick. 
    While you have the dog entranced, you lift the stick and throw it towards the rushing river."
    "The dog bolts towards the direction of the stick and you lost sight of the dog. You hear a loud splash, 
    and hurry towards the sound."
    "When you reached the river, you do not see the dog but only a stick that quickly flows away from you. 
    There’s only the sound of the rushing river to fill the dead woods."
   
    "{b}{i}Kill: killed the dog using nature.{/b}{/i}"
    return

label StickAtDog:
    call DiceRoll
    $ _damageRoll = d4
    $ EnemyHP -=_damageRoll
    if EnemyHP <= 0 :
        $ EnemyHP = 0

    "You threw the stick at the dog, and the dog received [_damageRoll]. 
    the dog has [EnemyHP] HP left. You could tell that this made it angry."

    $ isDogAngry = True
    $ didYouLook = False
    $ doYouSeeRiver = False

    jump EnemyAttack


label LargeStickAtDog: # Kill end
    call LargeStickGamble

    if _largeSuccess:
        "Due to the large size of the stick, the dog got crushed by the stick and 
        you could not see a hint of white underneath the log. In the silence, you 
        could hear the woods cheer at the act of your destruction."
        "{b}{i}Kill: the dog is crushed under the large stick.{/b}{/i}"
    else:
        jump LargeStickFailure 
    return

label LargeStickFailure:
    $ PlayerHP -= _damageRoll
    "You try to pick up the stick, but you feel a crack in your body when you try to lift it. 
    Something broke inside you, and it was the fault of your hubris."
    "You take [_damageRoll] damage from the stick, and have [PlayerHP] HP left"

    jump EnemyAttack
    
label FetchBoy:
    "You threw the stick towards the woods, and the dog runs towards the direction of the thrown stick."
    return