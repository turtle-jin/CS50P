


amount_due = 50

while amount_due != 0:
    print(f"Amount Due: {amount_due}")
    prompt = int(input("Insert Coin: "))

    if prompt == 5 or prompt == 10 or prompt == 25:
        amount_due -= prompt

    if amount_due <= 0:
        print(f"Change Owed: {-1 * amount_due}")
        break

