#Write a code to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

from typing import List


def FindIndexOfMinimunLenghtString(strings : List[str]):
    indexOfMinLenString = 0
    
    for i in range(1,len(strings)):
        if len(strings[indexOfMinLenString]) > len(strings[i]):
            indexOfMinLenString = i

    return indexOfMinLenString
    

def function(strings : List[str]):
    if not strings:
        return ""
    
    commonPrefix = ""
   
    indexOfMinLenString = FindIndexOfMinimunLenghtString(strings)
    
    for i in range(len(strings[indexOfMinLenString])):
        charExistInAll = True
        for j in range(len(strings)):
            if strings[indexOfMinLenString][i] != strings[j][i]:
                charExistInAll = False
                break
        
        if charExistInAll:
            commonPrefix += strings[indexOfMinLenString][i]
        else:
            break

    return commonPrefix


strings = ["Fireworker", "Fired", "Firecracker"]

print(function(strings))

            

    

    
    
    
