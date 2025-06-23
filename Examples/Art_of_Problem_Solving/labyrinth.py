"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        move_to_wall()
        turn_left()
        move_to_wall()
        turn_left()
        move_to_wall()
        turn_right()
        move_to_wall()
        turn_left()
    turn_around()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()
    move_to_wall()


    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one!
    """
    
    pass  # Delete this line and write your code here! :)

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
