

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (s_length(s) and two_letters(s) and num_check(s) and char_check(s))

def two_letters(str):
    return str[:2].isalpha()


def s_length(str):
    return 2 <= len(str) <= 6


def num_check(str):
    for char in str:
        if char.isdigit():
            i = str.index(char)
            if not str[i:].isdigit() or char == "0":
                return False
            break
    return True


def char_check(str):
    for char in str:
        if not (char.isalpha() or char.isdigit()):
            print("non letter and not num found in str!!")
            return False

    return True


main()