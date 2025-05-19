from karel.stanfordkarel import *

def main():
    put_beeper()
    move_to_wall()
    put_beeper()
    for i in range(2):
        turn_left()
        move_to_wall()
        put_beeper()
    turn_left()
    move_to_wall()
    turn_left()
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear() :
        move()

# don't change this code
if __name__ == '__main__':
    main()
    
'''
front_is_clear()
beepers_present()
beepers_in_bag()
left_is_clear()
right_is_clear()
facing_north()
facing_south()
facing_east()
facing_west()

front_is_blocked()
no_beepers_present()
no_beepers_in_bag()
left_is_blocked()
right_is_blocked()
not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()
'''
