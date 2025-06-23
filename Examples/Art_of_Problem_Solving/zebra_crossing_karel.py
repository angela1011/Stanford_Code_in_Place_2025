"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    put_beeper()
    turn_left()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_blocked() and facing_north():
            turn_right()
            move()
            turn_right()
            put_beeper()
        if front_is_blocked() and facing_south():
            turn_left()
            if front_is_clear():
                move()
                move()
                move()
                move()
                turn_left()
                put_beeper()
        
            
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one!
    """
    
    # pass  # Delete this line and write your code here! :)

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
