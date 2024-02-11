# names = nameString.split(", ")
'''This lesson skipped how to enter the names as a string and then convert them to a list. 
I did some searching and found the syntax to do it, so I have completed the code
so it works up front'''

import random

nameList = input("Enter all the dinner guests separated by a comma and space\n")
diners = nameList.split(", ")
print("The following people are dining with us: \n" + "\t" + nameList)

numItems = len(diners)
randomChoice = random.randint(0, numItems - 1)

payee = diners[randomChoice]

print(payee + " is paying tonight")

