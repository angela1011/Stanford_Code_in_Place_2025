from karel.stanfordkarel import *

def main():
    put_beeper()
    turn_left()
    while front_is_clear(): 
        while front_is_clear(): 
            move()
            if front_is_clear(): 
                move()
                put_beeper()  
        turn_around()
        move_to_wall()
        turn_left()
        if front_is_clear() and beepers_present(): 
            move()
            turn_left()
            move()
            put_beeper()  
        if front_is_clear() and no_beepers_present():
            move()
            turn_left()
            put_beeper()  
    if front_is_blocked():
        turn_around()
        move_to_wall()
        turn_around()
            
        # if front_is_blocked() and facing_north():
        #     turn_right()
        #     if front_is_blocked():
        #         turn_right()
        #         move_to_wall()
        #         turn_left()
        #     if front_is_clear() and no_beepers_present():
        #         move()
        #         put_beeper()
        #         turn_right()
        #     else:
        #         move()
        #         turn_right()
        #         if front_is_clear():
        #             move()
        #             put_beeper()

    #     if front_is_blocked() and facing_east():
    #         turn_right()
    #     if front_is_blocked() and facing_west():
    #         turn_around()
    #     if front_is_blocked() and facing_south():
    #         turn_left()
    #         if front_is_clear():
    #             move()
    #             put_beeper()
    #             turn_left()
    #         else:
    #             turn_around()
    #             move_to_wall()
    # if front_is_blocked() and facing_west():
    #     turn_around()
    # if front_is_blocked() and facing_east():
    #     turn_around()
    #     move_to_wall()
                
    pass
                

#     if beepers_present():
#         checkerboard()
    
def checkerboard():
    while front_is_clear():
        draw_line()
        reset()
    draw_line()
    reset()
    
def draw_line():
    turn_left()
    move()
    while front_is_clear():
        put_beeper()     
        move()



def jump():
    if front_is_clear():  
        turn_left()
        move()
        if front_is_clear():
            move()
            put_beeper()
        else:
            draw_line()

def reset():
    turn_right()
    if front_is_clear():
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
    else:
        turn_right()
        while front_is_clear():
            move()
        turn_right()
        move_to_wall()
        turn_around()
        

# def main():
#     while front_is_clear():
#         put_beeper()
#         move()
#         while front_is_clear():
#             move()
#         if front_is_blocked():
#             turn_left()
#             move()
#             turn_left()
#         if beepers_present():
#             spread_one()
#         else:
#             turn_left()
#             move()
#     pass

# def spread_one():
#     while beepers_present():
#         turn_left()
#         move()
#         move()
#         turn_right()

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

# from karel.stanfordkarel import *

# def main():
#     fill_one_row()
#     while left_is_clear():
#         go_to_next_row()
#         fill_one_row()

# def fill_one_row():
#     if no_beepers_present():
#         put_beeper()
#     while front_is_clear():
#         move()
#         if front_is_clear():
#             move()
#             put_beeper()

# def go_to_next_row():
#     if facing_east():
#         turn_left()
#         if front_is_clear():
#             move()
#             turn_left()
#     else:
#         turn_right()
#         if front_is_clear():
#             move()
#             turn_right()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()