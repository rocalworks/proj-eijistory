# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define un_narr = Character('');
define ej_narr = Character('', color="#ff00ff")
define ej_conv = Character('Eijiro') 


# The game starts here.
label start:

    # starting scene == black
    un_narr "This is a Ren'Py test. Seriously."

    # scene shifts to school 
    
    ej_conv "Why would we even try to take this test, anyway?"
    
    

    return