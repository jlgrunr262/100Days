print("Welcome to the Love Calculator")
name1 = input("What is your name? ")
name2 = input("what is your lovers name? ")

combinedNames = (name1 + name2).lower()
#caluculating the first digit
t = combinedNames.count("t")
r = combinedNames.count("r")
u = combinedNames.count("u")
e = combinedNames.count("e")
firstDigit = t + r + u + e

l = combinedNames.count("l")
o = combinedNames.count("o")
v = combinedNames.count("v")
e = combinedNames.count("e")
secondDigit = l + o + v + e

score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"your score is {score} and you are off the charts in a bad way.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score} and you should start banging each other.") 
else:
    print(f"Your score is {score}, you should just be fuck buddies")