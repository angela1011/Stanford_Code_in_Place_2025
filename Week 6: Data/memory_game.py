# import random

# NUM_PAIRS = 3

# def main():
#     """
#     You should write your code here. Make sure to delete 
#     the 'pass' line before starting to write your own code.
#     """
#     truth_list = []
#     for i in range(NUM_PAIRS):
#         truth_list.append(i)
#         truth_list.append(i)
#     # print(truth_list)

#     random.shuffle(truth_list)
#     # print(truth_list)

#     if:
#         Print("No match. Try again.")
#         input("Enter")
#     else:
#         Print("Match!")


# def get_valid_index():
#     print("You entered the same index twice. Try again.")
#     print("Invalid index. Try again.")
#     print("Not a number. Try again.")
#     print("This number has already been matched. Try again.")

# def clear_terminal():
#     for i in range(20):
#       print('\n')

# if __name__ == '__main__':
#     main()
import random
import os

# ------------------------
# Utility Functions
# ------------------------

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_index(displayed, prompt, exclude_index=None):
    """Get a valid index from the user with validation."""
    while True:
        index_input = input(prompt)
        if not index_input.isdigit():
            print("Not a number. Try again.")
            continue

        index = int(index_input)

        if index < 0 or index >= len(displayed):
            print("Invalid index. Try again.")
            continue

        if displayed[index] != '*':
            print("This number has already been matched. Try again.")
            continue

        if exclude_index is not None and index == exclude_index:
            print("You entered the same index twice. Try again.")
            continue

        return index

# ------------------------
# Game Setup
# ------------------------

NUM_PAIRS = 3  # You can change this number as needed

# Milestone #1: Create the truth list
truth_list = []
for i in range(NUM_PAIRS):
    truth_list.append(i)
    truth_list.append(i)

# Milestone #2: Shuffle the list
random.shuffle(truth_list)

# Milestone #3: Create displayed list
displayed_list = ['*'] * len(truth_list)

# ------------------------
# Game Loop
# ------------------------

while '*' in displayed_list:
    clear_terminal()
    print(displayed_list)

    # Milestone #4: Get two valid indices
    idx1 = get_valid_index(displayed_list, "Enter an index: ")
    idx2 = get_valid_index(displayed_list, "Enter an index: ", exclude_index=idx1)

    # Milestone #5: Check correct
    if truth_list[idx1] == truth_list[idx2]:
        displayed_list[idx1] = truth_list[idx1]
        displayed_list[idx2] = truth_list[idx2]
        print("Match!")
    else:
        print(f"Value at index {idx1} is {truth_list[idx1]}")
        print(f"Value at index {idx2} is {truth_list[idx2]}")
        print("No match. Try again.")
        input("Press Enter to continue...")

# Milestone #6: End Game
clear_terminal()
print(displayed_list)
print("Congratulations! You won!")

