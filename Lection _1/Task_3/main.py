x=float(input("x="))
y=float(input("y="))
action = input("Enter action(+, -, *, /)")

match action:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)