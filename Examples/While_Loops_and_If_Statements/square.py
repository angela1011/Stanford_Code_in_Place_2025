"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    for i in range(4):
        move()
        turn_left()
        put_beeper()

    """
    Makes Karel place beepers in a square (4 beepers total) and end in the same position Karel starts in.
    """
def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
