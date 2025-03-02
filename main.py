import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?:   "))

    decision = True
    while decision:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation:  ")
        num2 = float(input("What's the next number?:   "))

        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if again == "y":
            num1 = answer
        else:
            decision = False
            print("\n" * 20)
            calculator()


calculator()
