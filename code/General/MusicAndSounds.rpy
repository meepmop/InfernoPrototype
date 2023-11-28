label ForestMusic:
    play music "audio/Music/Forest.mp3" volume 0.5
    return

label CombatMusic:
    play music "audio/Music/Combat.mp3" volume 0.5 if_changed
    return

label KillMusic:
    stop music fadeout 1.0
    play sound "audio/SFX/Conclusions/Kill.wav" volume 0.5
    return

label ToleranceMusic:
    stop music fadeout 1.0
    play sound "audio/SFX/Conclusions/Tolerance.wav" volume 0.5
    return

label ConversionMusic:
    stop music fadeout 1.0 
    play sound "audio/SFX/Conclusions/Tolerance.wav" volume 0.5
    return

label AttackSound:
    play sound "audio/SFX/Battle/Attack2.ogg" volume 0.75
    return

label DamageSound:
    play sound "audio/SFX/Battle/Blow1.ogg" volume 0.75
    return

label EvadeSound:
    play sound "audio/SFX/Battle/Evasion1.ogg" volume 0.75
    return
