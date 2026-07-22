def get_number(result):
        if result is not None:
            number_1 = result
        else:
            number_1 = int(input("What's the first number? "))

        calculation = validate_operation(input("+\n-\n*\n-\nPick an operation: "))
        number_2 = int(input("What's the next number? "))
        return number_1, number_2, calculation

def validate_operation(operation):
    done = False
    while not done:
        if operation not in operations:
            operation = input("Invalid operation. Try again.")
        else:
            done = True
    return operation

def calculate(previous_result):
    num1, num2, operation = get_number(previous_result)
    raw_output = operations[operation](num1,num2)

    if isinstance(raw_output, tuple):
        result = raw_output[0]
        num2 = raw_output[1]
    else:
        result = raw_output

    print(f"{num1} {operation} {num2} = {result}")
    return result

def calculator():

    outcome = calculate(None)

    should_continue = True
    while should_continue:
        decision = input("Type 'y' to continue calculating, or type 'n' to begin new calculation, or type 'q' to quit")
        if decision == 'y':
            outcome = calculate(outcome)
        elif decision == 'n':   
            outcome = calculate(None)
        elif decision == 'q':
            should_continue = False
        else:
            print("Invalid decision. Please try again.")

    print("Goodbye ^^")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    while True:
        try:
            result = a / b
            return result, b
        except ZeroDivisionError:
            print("You cannot divide by zero!")
            b = int(input("Input a valid number."))


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator()