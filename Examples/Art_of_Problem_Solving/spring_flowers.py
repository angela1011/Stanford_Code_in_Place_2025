"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    move()
    for i in range(2):
        while front_is_blocked():
            turn_left()
            move()
            turn_right()
        put_beeper()
        turn_left()
        move()
        turn_right()
        put_beeper()
        move()
        put_beeper()
        turn_right()
        move()
        put_beeper()
        move_to_wall()
        turn_left()
        move_to_wall()

    

    

    """
    Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
    Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
    """
    
    pass  # Delete this line and write your code here! :)

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
