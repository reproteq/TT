#!/usr/bin/python
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
###############
# BANNER #
###############
def ban():
    print W + " +---------------------+"+ W
    print W + " | " +R," _______________" + W + "   | "
    print W + " | " +R,"|__    ___    __|"+ W + "  | " 
    print W + " | " +R,"   |  |   |  |   "+ W + "  | "
    print W + " | " +R,"   |__|   |__|   "+ W + "  | "
    print W + " |                     | "
    print W + " +---------------------+"+ W
    print  W + " |"+O +" Python source code"+ W + "  |"
    print W + " +---------------------+"+ W   
    print  W + " |"+R +" T"+ R + "T"+ G +" v1.0 2017-05-08 "+ W + " |"
    print W + " +---------------------+"+ W

    return

ban()
