

def main ():
    time = input("What time is it? ")
    n = convert(time)
    if n >= 7.00 and n <= 8.00:
        print("breakfast time")
    elif n >= 12.00 and n <= 13.00:
        print("lunch time")
    elif n >= 18.00 and n <= 19.00:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    min_to_hr = int(minute) / 60
    return float(hour) + float(min_to_hr)


if __name__ == "__main__":
    main()
