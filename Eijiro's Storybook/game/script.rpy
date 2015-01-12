# --- IMAGES ---
# (images credits to Uncle Mugen[background] and Tokudaya[CGs])

# DIRPATH TO CG
define cgpath = "assets/image/cg/"

# EIJIRO
define ejpath = cgpath + "eijiro/eijiro_"
image ej annoy = ejpath + "annoyed.png"
image ej drop  = ejpath + "drop.png"
image ej sarca = ejpath + "sarcastic.png"
image ej shock = ejpath + "shocked.png"

# RITSU
define rspath = cgpath + "ritsu/ritsu_"
image rs aloof = rspath + "aloof.png"
image rs confi = rspath + "confident.png"
image rs happy = rspath + "happy.png"
image rs angry = rspath + "mad.png"
image rs smug  = rspath + "smug.png"

# DIRPATH TO BG
define bgpath = "assets/image/bg/"

# EMPTY SCENE
define black = bgpath + "black.jpg"

# SCHOOL SETTING DIRAPATH
define skpath = bgpath + "school/"

# - corridor
image sk coriday  = skpath + "corridor/morning.jpg" 
## --


# --- CONVERSATIONS AND NARRATIONS ---
# declare characters used by this game.

# character narration
define un_narr = Character('')
define ej_narr = Character('', color="#ff00ff")
define rs_narr = Character('', color="#00ff00")
    
# character conversation
define ej_conv = Character('Eijiro') 
define rs_conv = Character('Ritsu')
## --


# --- MODIFIED CG POSITIONS ---
init: 
    $ cleft  = Position(xpos=0.15, xanchor=0.0, ypos=0.0, yanchor=0.0)
    $ cright = Position(xpos=0.60, xanchor=0.0, ypos=0.0, yanchor=0.0)
## --

# --- ANIMATIONS AND TRANSITIONS ---
transform right_to_center:
    xalign 0.83 yalign 0.0
    linear 1.0 xalign 0.5
    
transform center_to_left:
    xalign 0.5 yalign 0.0
    linear 1.0 xalign 0.15
## --

# --- GAME START ---
# The game starts here.
label start:

    # starting scene == black
    scene black
    un_narr "We're going to test how this engine works."

    # scene shifts to school corridor
    scene sk coriday
    with fade 
    
    # shows eijiro_annoyed.
    show ej annoy
    with dissolve
    ej_conv "Why would we even try to take this test, anyway?"
    ej_conv "It's not that you didn't do this before...{w} or did you really not try this one?"
    
    # shows ritsu_happy beside him.
    show ej annoy at center_to_left
    with None
    show rs happy at cright
    with dissolve
    rs_conv "It's okay, Eijiro!"
    rs_conv "The developer will give us some incentives after this work. Am I right, dev?"
    
    un_narr "No."
    
    # shift ritsu -> ritsu_mad.
    show rs angry
    rs_conv "I shall sue you with child abuse."
    
    # shift eijiro -> eijiro_drop.
    show ej drop
    ej_conv "It's really impressive that you shifted your side so quickly."
    
    # shift ritsu -> ritsu_aloof.
    show rs aloof
    rs_conv "Well, at least I don't have a boring personality like someone out there."
    
    # shift eijiro -> eijiro_sarcastic.
    show ej sarca
    ej_conv "Sorry if I'm too boring for a crazy kid like you."
    
    # shift ritsu -> ritsu_happy.
    show rs happy 
    rs_conv "Thanks for the compliment."
    # shift ritsu -> ritsu_confident.
    show rs confi
    rs_conv "Oh, or maybe you're not exaggerating too much."
    
    # shift eijiro -> eijiro_shocked.
    # note: italic text for mind-emphasis
    show ej shock
    ej_conv "{i}She really accepted it? And she even wants more?!{/i}"
    
    # shift ritsu -> ritsu_smug (just to shut her mouth lol)
    show rs smug
    
    un_narr "Okay, okay. This is just a test run, so don't make your dialogues too long, a'ight?"
    
    # shift eijiro -> eijiro_drop.
    show ej drop
    ej_conv "Aren't you the one who's typing this whole script?"
    
    un_narr "No. I'm just an innocent narrator in this skit."
    
    # shift eijiro -> eijiro_shocked.
    show ej shock
    ej_conv "THIS IS A SKIT??!!!"
    
    # shift ritsu -> ritsu_happy.
    show rs happy at right_to_center
    rs_conv "Well, everyone. This story will get released soon, so please stay tuned!"
    # shift ritsu -> ritsu_smug
    show rs smug
    rs_conv "Or you can pressure the developer to make it sooner. Huehuehuehue..."
    
    # shift eijiro -> eijiro_drop.
    show ej drop
    ej_conv "She'll be dead if you do that, y'know."
             
    return