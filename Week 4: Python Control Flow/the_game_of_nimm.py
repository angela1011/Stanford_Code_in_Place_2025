# def main():
#     # print("The Ancient Game of Nimm")  
#     stone_num = 20
#     print(f"There are {stone_num} stones left.")

#     user1_input = int(input("Player 1 would you like to remove 1 or 2 stones? "))
#     if user1_input > 2:
#         input_is_invalid = user1_input 
#         user1_input = int(input("Please enter 1 or 2: "))
#     left = int(stone_num) - user1_input
    
#     while left > 0:
#         print()
#         print(f"There are {left} stones left.")
#         user2_input = int(input("Player 2 would you like to remove 1 or 2 stones? "))
#         if user2_input > 2:
#             input_is_invalid = user2_input 
#             user1_input = int(input("Please enter 1 or 2: "))
#         left = left - user2_input
#         if left > 0:
#             print()
#             print(f"There are {left} stones left.")
#         else:
#             print("Player 2 wins!")
#         if left > 0:
#             user1_input = int(input("Player 1 would you like to remove 1 or 2 stones? "))
#             if user1_input > 2:
#                 input_is_invalid = user1_input 
#                 user1_input = int(input("Please enter 1 or 2: "))
#             left = left - user1_input
#             if left == 0:
#                 print("Player 1 wins!")


# if __name__ == '__main__':
#     main()

def main():
    stones = 20
    current_player = 1

    while stones > 0:
        print(f"There are {stones} stones left.")
        move = int(input(f"Player {current_player} would you like to remove 1 or 2 stones?  "))

        # Validate input
        while move not in [1, 2] or move > stones:
            move = int(input("Please enter 1 or 2:  "))

        stones -= move

        if stones == 0:
            # The player who just played loses, so the other wins
            winner = 2 if current_player == 1 else 1
            print(f"\nPlayer {winner} wins!")
            break

        # Switch player
        current_player = 2 if current_player == 1 else 1
        print()  # Add an empty line between turns


if __name__ == '__main__':
    main()

