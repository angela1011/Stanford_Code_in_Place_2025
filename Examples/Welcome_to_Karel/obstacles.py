"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    move()
    goin()
    move()
    move()
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    pass  # Delete this line and write your code here! :)

def goin():
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        put_beeper()
        turn_left()



def turn_right():
    turn_left()
    turn_left()
    turn_left()        
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
