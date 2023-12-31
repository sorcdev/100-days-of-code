'''
Calculator program
'''
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    from art import logo
    print(logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")

    should_continue = True

    while should_continue:
        next_num = float(input("What's the next number? ")) 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, next_num)

        print(f"{num1} {operation_symbol} {next_num} = {answer}")

        continue_or_new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
        
        if continue_or_new == 'y':
            num1 = answer
            operation_symbol = input("Pick another operation: ")
        else:
            calculator()

calculator()

