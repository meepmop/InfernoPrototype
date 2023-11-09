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

label StickAtDog:   # Kill end
    if doYouHaveBigStick:
        call LargeStickGamble

        if _largeSuccess:
            "Due to the large size of the stick, the dog got crushed by the stick and 
            you could not see a hint of white underneath the log. In the silence, you 
            could hear the woods cheer at the act of your destruction."
            "{b}{i}Kill: the dog is crushed under the large stick.{/b}{/i}"
        else:
            jump LargeStickFailure 
    else: 
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
    
    return

label LargeStickFailure:
    $ PlayerHP -= _damageRoll
    "You try to pick up the stick, but you feel a crack in your body when you try to lift it. 
    Something broke inside you, and it was the fault of your hubris."
    "You take [_damageRoll] damage from the stick, and have [PlayerHP] HP left"

    jump EnemyAttack
    
label FetchBoy:
    if doYouHaveBigStick:
        call LargeStickGamble
        
        if _largeSuccess:
            "You threw the stick towards the woods, and the dog runs towards the direction of the thrown stick."
            "You don’t believe that the dog will be able to bring the large stick back. 
            However, after a few minutes, you could see that a small tuff of white emerge 
            from the bushes."
            "The small dog drags the large stick out of the bush, and slowly brings you the large stick back."
        else:
            jump LargeStickFailure
    else:
        "You threw the stick towards the woods, and the dog runs towards the direction of the thrown stick."
        "The dog fetches the stick and brings it back, with a wagging tail."
    
    $ didDogBringBackStick = True
    jump PlayerMove

label TugOfWar:
    "You attempt to grab the stick away from the dog, but its bite is tightened on the wood. As you try to pull the stick 
    away from the dog, you could see the dog’s tail vigorously wag at your attempts."
    "You could feel the dog pull at the stick, as you try to pull the stick away from it. It does not want to relent the stick to you."
    "Don’t let the dog win this stick. Claim what is rightfully yours!"
    menu TugOfWarDecision:
        "Don’t let the dog win this stick. Claim what is rightfully yours!"
        "Let the dog win and have the stick":
            "You pull away from the stick, and let the dog have the stick. The dog wags his tail faster at this victory, 
            and starts taking the stick to hit your leg with it."
            "Its attacks did not hurt, and the dog looks rather cute with the stick in its mouth. The dog releases the stick after 
            it had its fun in swatting you, sat up proudly, and smiled at you with its fluffy tail dancing behind it."
            "The dog walks away and barks at you when you watch it move away. It quickly approaches you and bites at your cape, pulling it 
            towards the direction of its journey. You follow the dog, as it leashes you with your cape."
            "This is an embarrassment, Little One, for you have become the dog’s pet."
            "{b}{i}Conversion: Become Beta{/i}{/b}"
            return
        "Win this tug of war":
            "Due to the strength of the dog, you easily won the war by lifting the stick with the dog on it. The dog did not release 
            the stick when you clearly have defeated the dog in the show of power."
            "You lowered the dog on a stick down, and the dog released the stick then growled at you. 
            It did not like you winning, and looks angry due to its wounded pride."
            
            $ didDogBringBackStick = False

            jump EnemyAttack
