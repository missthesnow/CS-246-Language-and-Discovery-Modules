##program01.py - Dice Roller
 
import random
 
try:
    minDiceValue = int(input('Enter the minimum value of the die: '))
    maxDiceValue = int(input('Enter the maximum value of the die: '))
except:
    print('One of the values you have entered is invalid. The dice roller will return to the default values of 1-6')
    minDiceValue = 1
    maxDiceValue = 6
 
again = True
 
while again:
    sides = int 
    sides = maxDiceValue - minDiceValue + 1
    print('You have rolled a ')
    print(sides)
    print('sided die. The result is: ')
    print(random.randint(minDiceValue, maxDiceValue))
 
    another_roll = input('Do you want to roll the die again? (y/n)')
 
    if another_roll.lower() == 'yes' or another_roll.lower() == 'y':
        continue
    else:
        break