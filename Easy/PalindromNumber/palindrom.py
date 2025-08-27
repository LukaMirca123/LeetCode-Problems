# Program that checks if the input number is a palindrome and prints a message.

def CountDigits (number):
    countOfDigits = 0

    while number > 0:
        number //= 10
        countOfDigits += 1

    return countOfDigits

def RemoveLastAndFirstDigit (number,countOfDigits):
    number %= 10**(countOfDigits - 1)
    number //= 10
    return number

def IsNumberPalindrom (number):
    
    countOfDigits = CountDigits(number)

    while countOfDigits > 1:
        if (number % 10) != (number // 10**(countOfDigits - 1)):
            return False
        
        number = RemoveLastAndFirstDigit(number,countOfDigits)

        countOfDigits -= 2

    return True

while True:
    x = int(input("Enter a number:"))

    if IsNumberPalindrom(x):
        print("A number is Palindrom.")
    else:
        print("A number isn't Palindrom.")