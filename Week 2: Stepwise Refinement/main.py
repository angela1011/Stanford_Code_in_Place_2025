from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    turn_right()
    put_beeper()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    turn_left()
    put_beeper()
    for i in range(4):
        move()
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    turn_right()
    put_beeper()
    for i in range(4):
        move()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    turn_left()
    put_beeper()

    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    pass

def turn_right():
    # defines turn_right as 3x turn_left
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()