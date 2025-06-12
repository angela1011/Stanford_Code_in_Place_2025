"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    if front_is_blocked():
        turn_left()
        move_to_wall()
    if front_is_blocked():
        turn_right()
        move_to_wall()  
    if front_is_blocked():
        turn_right()
        move_to_wall()  
        turn_left()
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
