def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    # print("Welcome to the Spanish Vocabulary Quiz!\n")

    correct_count = 0

    for english, spanish in translations.items():
        answer = input(f"What is the Spanish translation for {english}? ")
        # answer = input("Your answer: ").strip().lower()
        if answer == spanish:
            print("That is correct!\n")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.\n")

    print(f"You got {correct_count}/{len(translations)} words correct, come study again soon!")

    pass  # Delete this line and write your code here! :)



if __name__ == '__main__':
    main()
