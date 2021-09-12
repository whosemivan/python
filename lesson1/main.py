import math
import random

# print('Hello World!')

# print(math.cos(1));

# randomNumber = random.randint(1, 10)
# print(randomNumber)


# user = input('Как вас зовут? ')
# age = input('Сколько Вам лет?')

# print(f'Hello, {user}! Вам {age} лет!')

firstNumber = input('Введите любое число: ')
secondNumber = input('Введите любое число: ')

if firstNumber.isdigit() and secondNumber.isdigit():
	summ = int(firstNumber) + int(secondNumber)
	print(f'Сумма: {summ}')
else:
	try:
		float(firstNumber)
		summ = float(firstNumber) + float(secondNumber)
		print(f'Сумма: {summ}')
	except ValueError:
		print('Ну вас же попросили, введите любое число!')


numbers = [5, 7, 2, 90]

def findMaxElement(arr):
	currentMax = arr[0]
	for element in arr:
		if element > currentMax:
			currentMax = element
	return currentMax
    
print(findMaxElement(numbers))