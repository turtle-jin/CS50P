

expression = input("Expression: ")

x,operator,z = expression.split(" ")


match operator:
    case "+":
        print(float(x) + float(z))
    case "-":
        print(float(x) - float(z))
    case "*":
        print(round(float(x) * float(z), 1))
    case "/":
        print(round(float(x) / float(z), 1))