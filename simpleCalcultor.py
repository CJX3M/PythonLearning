print("Simple Calculator!")
firstNumber = input("First number? ")
operation = input("Operation? ")
secondNumber = input("SecondNumber? ")

if not firstNumber.isnumeric() or not secondNumber.isnumeric():
    print("Please input a number")
    exit()

resultOperation = ''
result = 0
firstNumber = int(firstNumber)
secondNumber = int(secondNumber)

if operation == '+':
    resultOperation = 'Sum'
    result = firstNumber + secondNumber
elif operation == '-':
    resultOperation = 'Difference'
    result = firstNumber - secondNumber
elif operation == '*':
    resultOperation = 'Product'
    result = firstNumber * secondNumber
elif operation == '/':
    resultOperation = 'Quotient'
    result = firstNumber / secondNumber
elif operation == '%':
    resultOperation = 'Modulus'
    result = firstNumber % secondNumber
elif operation == '**':
    resultOperation = 'Exponent'
    result = firstNumber ** secondNumber
else:
    print("Operation not recognized")
    exit()
print(f'{resultOperation} of {firstNumber} {operation} {secondNumber} equals {result}')