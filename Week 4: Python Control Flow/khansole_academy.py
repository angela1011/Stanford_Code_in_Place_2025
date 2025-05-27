import random

def main():
    print("Khansole Academy")
    # TODO: your code here
    num1 = random.randint(10, 99) 
    num2 = random.randint(10, 99) 
    answer = int(num1)+int(num2)
    print(f"What is {num1} + {num2}?")
    Ans = input("Your answer: ")
    Ans = int(Ans)
    if answer == Ans:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {answer}")
    
    
if __name__ == '__main__':
    main()
