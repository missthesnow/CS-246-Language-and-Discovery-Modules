##program02.py - Command Line Calculator

repeat = 'Y'
print('Calculator is now accepting input.\n')
 
while repeat == 'Y':
 
    '''Ask user for input'''
    num1 = float(input('Enter a number: '))
    operator = input('''What mathematical operator would you like to use:
                        + for addition,
                        - for subtraction,
                        * for multiplication,
                        / for division,
                        % for modulus and
                        ** for the power operator
                        ''')
 
    num2 = float(input('Enter the second number: '))
 
 
    '''Determine which operator needs to be applied'''
    if operator == '+':
        answer = num1 + num2
        print(f'{num1} + {num2} = {answer}')
 
    elif operator == '-':
        answer = num1 - num2
        print(f'{num1} - {num2} = {answer}')
 
    elif operator == '*':
        answer = num1 * num2
        print(f'{num1} * {num2} = {answer}')
 
    elif operator == '/':
        answer = num1 / num2
        print(f'{num1} ÷ {num2} = {answer}')
 
    elif operator == '%':
        answer = num1 % num2
        print(f'The remainder of {num1} ÷ {num2} is {answer}')
 
    elif operator == '**':
        answer = num1 ** num2
        print(f'{num1} to the power of {num2} = {answer}')
 
    else:
        print('You have entered an invalid operator')
 
    '''Ask the user to try another calculation'''
    y_or_n = input('Do you want to do another calculation? (Y/N)')
    repeat = y_or_n.upper()
 
    if repeat != 'Y':
        print('The program will now end.')