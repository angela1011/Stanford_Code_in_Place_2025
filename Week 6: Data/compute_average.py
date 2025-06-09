def main():
    number_list = load_numbers_from_file("numbers.txt")
    if number_list:
        average = sum(number_list) / len(number_list)
        print(f"Average: {average}")
    else:
        print("The file is empty. Cannot compute average.")

    # number_list = int(number_list)
    # for i in range(len(number_list)):
        # all_num = number_list[0] + number_list[i]
        # print(number_list[i])
    # list = []
    # for i in range(len(number_list)):
    #     list.append(i)
    #     list.append(i)
    # print(list)

    # TODO: your code here


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                numbers.append(float(cleaned_line))
    
    return numbers


if __name__ == '__main__':
    main()
