import math
import random 
from ai import call_gpt

def main():
    BD = input("When is your birthday?: ")
    if BD == "1011":
        print("Congratulation! We're the same!")
    else:
        print("Okay. I got it.")

if __name__ == "__main__":
    main()
