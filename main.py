#!/usr/bin/python
# IMPORT MODULES
###################
import sys, os 
DN = open('./debug.log', 'w')
ERRLOG = open(os.devnull, 'w')
OUTLOG = open(os.devnull, 'w')
#############
# COLORS #
#############
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
######################
# LOGO BAN TT
######################
import tt
######################

######################
# DEF MAIN     
#####################
def main_menu():
    print (W+' +---------------------+'+W)
    print (W+' |'+ O +'     MAIN MENU       '+ W+'|'+W)
    print (W+' +---------------------+'+W)
    print (W+' |'+GR + ' ['+ G +'A'+ GR +']' + B +"  Menu A         " +W + "|")
    print (W+' |'+GR + ' ['+ G +'E'+ GR +']' + B +"  Exit           " +W + "|")
    print (W+' +---------------------+'+W)
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
######################
# DEF EXECUTE MENU
#####################
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return
######################
# DEF MENU A ATTACK
#####################
def menuA():
    print (W+'Menu A'+W)

    print (GR + ' ['+ G +'B'+ GR +']' + B +"  Back "+W)
    print (GR + ' ['+ G +'E'+ GR +']' + B +"  Exit "+W)
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
######################
# DEF BACK MENU
#####################
def back():
    menu_actions['main_menu']()
######################
# DEF EXIT MENU
#####################
def exit():
    sys.exit()
 

######################
# MENU DEFINITIONS
#####################
menu_actions = {
    'main_menu': main_menu,
    'a': menuA,
    'b': back,
    'e': exit,
}
 
######################
# MAIN PROGRAM 
#####################
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
