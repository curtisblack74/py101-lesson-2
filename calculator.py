# X Ask the user for the first number.
# X Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json

#Open the JSON file for reading
with open('calculator_messages.json','r') as file:
    data = json.load(file)

#Now 'data' contains the contents of the JSON file as a Python disctionary or list

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def calculator():
    prompt("What language do you speak? English, Spanish, or French?")
    language = input()

    prompt(data[language]["welcome_message"])
    

    prompt(data[language]["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(data[language]["invalid_number"])
        number1 = input()

    prompt(data[language]["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(data[language]["invalid_number"])
        number2 = input()

    prompt(data[language]["operation"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(data[language]["invalid_operation"])
        operation = input()

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    prompt(data[language]["output"].format(output=output))
    response = input()

    if response == 'Yes':
        calculator()
    else:
        exit

calculator()


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