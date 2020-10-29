## Author: Feras
## Description: A program that finds repeated values in a list

def repeated(myList):
    for i in myList:
        if myList.count(i) > 1:
            return i
print("The repeated number is: ", repeated([1,2, 45, 67, 45]))

