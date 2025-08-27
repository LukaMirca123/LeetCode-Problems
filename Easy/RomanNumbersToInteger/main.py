# Input Roman number transform into integer number 

import re

def IsInputNumberValid (romanNumber):
    if re.fullmatch(r"[IVXLCDM]+",romanNumber):
        return True
    return False

def TransformRomanToInteger(romanNumber):
    
    integerNumberValue = 0
    previousDigitValue = 0

    values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    for digit in reversed(romanNumber):
        valueOfDigit = values[digit]

        if valueOfDigit < previousDigitValue:
            integerNumberValue -= valueOfDigit
        else:
            integerNumberValue += valueOfDigit
        
        previousDigitValue = valueOfDigit
    
    return integerNumberValue


while True:
    romanNumber = input("Enter Roman number: ").upper()

    if not IsInputNumberValid(romanNumber):
        print("\nInvalid number. Use only symbols like: I,V,X,L,C,D,M")
        continue
    
    integerNumber = TransformRomanToInteger(romanNumber)

    print("Roman Number: " + romanNumber + "  ->  " + "Integer Number: " + str(integerNumber))


    

