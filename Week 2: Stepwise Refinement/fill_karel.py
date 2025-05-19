from karel.stanfordkarel import *

def main():    
    while front_is_clear():
        reset_to_next_row()
    # while front_is_clear():  
    #     put_beeper()
    #     move()
    # put_beeper()
    pass


def reset_to_next_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()    
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    
    if front_is_blocked():
        for i in range(1):
            turn_right()
            last()
    else:
        move()
        turn_right()

# def last():
#     while front_is_blocked():
#         turn_right()
#         move()
#         move()
#         move()
def last():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
