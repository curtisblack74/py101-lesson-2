# X Ask the user for the first number.
# X Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt('What operation would you like to perform?\n'
       '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ["1", "2", "3", "4"]:
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is {output}")

#another version
'''def prompt(message):
    print(f"==> {message}")

def is_valid_number(value):
    while True:
        try:
            value = int(value)
            return value
        except ValueError:
            prompt('Invalid input. Please enter an integer: ')
            value = input()

def is_valid_operator(value):
    while True:
        try:
            value = int(value)
            if 1 <= value <= 4:
                return value
            else:
                prompt('Invalid input. Please select the operation to perform:\n'
                    '1) addition 2) subtraction 3) multiplication 4) division')
                value = input()
   
        except ValueError:
            prompt('Invalid input. Please select the operation to perform:\n'
                    '1) addition 2) subtraction 3) multiplication 4) division')
            value = input()

prompt('Welcome to Calculator!')

prompt('Please enter the first number: ')
number1 = input()
number1 = is_valid_number(number1)

prompt('Please enter the second number: ')
number2 = input()
number2 = is_valid_number(number2)

prompt('Please select the operation to performn:\n'
      '1) addition 2) subtraction 3) multiplication 4) division')
operation = input()
operation = is_valid_operator(operation)


match operation:
    case 1:
        output = number1 + number2
    case 2:
        output = number1 - number2
    case 3:
        output = number1 * number2
    case 4:
        output = number1 / number2

prompt(f"The output is {output}.")
'''