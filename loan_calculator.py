#Create a mortgage/car loan calculator
#Inputs: loan amount, annual percentage rate (APR), and loan duration
#Outputs: Monthly payment assuming interest is compounded monthly

def prompt(message):
    print(f"==> {message}")

while True:
    prompt("Welcome to the loan calculator:")
    prompt("Please enter the loan amount:")
    loan_amount = input()

    if ',' in loan_amount:
        loan_amount = loan_amount.replace(',','')

    try:
        loan_amount = float(loan_amount)
    except ValueError:
        loan_amount = float(loan_amount[1:])

    prompt("Please enter the annual percentage rate for the loan:")
    annual_percentage_rate = input()

    try:
        annual_percentage_rate = float(annual_percentage_rate)
    except ValueError:
        annual_percentage_rate = float(annual_percentage_rate[:-1])

    monthly_percentage_rate = (annual_percentage_rate / 100) / 12

    prompt("Please enter the loan duration in months:")
    monthly_loan_duration = int(input())

    monthly_payment = float(loan_amount *
                            (monthly_percentage_rate /
                            (1 - (1 + monthly_percentage_rate)
                            ** -monthly_loan_duration)))

    prompt(f"Your monthly payment is ${monthly_payment:,.2f}")
    prompt("Would you like to do another loan calculation?")
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break

'''
START
X GET loan_amount (float) from user
X GET annual_percentage_rate (percent) from user
X GET monthly_loan_duration from user

X SET monthly_percentage_rate = annual_percentage_rate / 12
X SET monthly_loan_duration = annual_loan_duration * 12
SET monthly_payment = loan_amount * (monthly_percentage_rate / (1 - (1 + monthly_percentage_rate) ** (-loan_duration))
SET output = "Your monthly payment is 
PRINT(f/"Your monthly payment is {monthly_payment}"
'''