# --- IMAGES ---
# declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# --

# --- CHARACTERS ---
# declare characters used by this game.

# character narration
define un_narr = Character('')
define ej_narr = Character('', color="#ff00ff")
define rs_narr = Character('', color="#00ff00")
    
# character conversation
define ej_conv = Character('Eijiro') 
define rs_conv = Character('Ritsu')
# --

# The game starts here.
label start:

    # starting scene == black
    un_narr "We're going to test how this engine works."

    # scene shifts to school 
    
    # shows eijiro_annoyed
    ej_conv "Why would we even try to take this test, anyway?"
    ej_conv "It's not that you didn't do this before."
    
    # shows ritsu_happy beside him
    rs_conv "It's okay, Eijiro!"
    rs_conv "The developer will give us some incentives after this work. Am I right, dev?"
    
    un_narr "No."
    
    # shift ritsu -> ritsu_mad
    rs_conv "WHY IN THE HELL WON'T YOU GIVE SOME INSENTIVES??!! DID YOU KNOW IT'S TIRING TO JUST STAND IN HERE AND DO NOTHING???!!!"
    
    # shift eijiro -> eijiro_drop
    ej_conv "It's really impressive that you shifted your expression so quickly."
    
    # shift ritsu -> ritsu_pout
    rs_conv "Well, at least I don't have a boring personality like someone out there."
    
    # shift eijiro -> eijiro_

    return