label YouSee:
    "You look around your surroundings; trying to find something that can stop the dog from looking like it wants to make you its new chewtoy."

    call DiceRoll from _call_DiceRoll_4
    $ _rollOutcome = d20

    # if IntWis >= _rollOutcome:

    $ didYouLook = True
    jump PlayerMove
