label ForestMusic:
    play music "audio/Music/Forest.mp3" volume 0.5
    return

label CombatMusic:
    play music "audio/Music/Combat.mp3" volume 0.5 if_changed
    return

label KillMusic:
    stop music fadeout 1.0
    play SFX "audio/SFX/Conclusions/Kill.wav" volume 0.5
    return

label ToleranceMusic:
    stop music fadeout 1.0
    play SFX "audio/SFX/Conclusions/Tolerance.wav" volume 0.5
    return

label ConversionMusic:
    stop music fadeout 1.0 
    play SFX "audio/SFX/Conclusions/Tolerance.wav" volume 0.5
    return