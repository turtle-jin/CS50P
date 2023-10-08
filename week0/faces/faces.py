def convert(str):
    new_str = str.replace(":)", "🙂")
    new_str = new_str.replace(":(", "🙁")
    print(new_str)


def main():
    user_input = input()
    convert(user_input)


main()



