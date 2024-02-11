print("Welome to the carnival. To ride this ride you have to be over 120cm tall.")
height = int(input("How tall are you in centimeters?\n "))
if height < 120:
    print("Sorry, your are too short to ride safely.")
age = int(input("How old are you?\n "))
if age <12:
    bill = 5
    print("Child tickets are $5.\n")
elif age <18:
    bill = 7
    print("Youth tickets are $7.\n")
elif age >= 45 and age <= 55:
    print("You get the mid-life discount so ride for free.\n")
    bill = 0
else:
    bill = 12
    print("Adult tickets are $12.\n")

#using the upper() suffix will insure the answer is always upper case, so the use can do upper or lower
wantsPhoto = input("Do you want a photo, Y or N: \n").upper()
if wantsPhoto == "Y":
    bill += 3
# Two different print fomrats
print ("\nEnjoy the ride. You owe us ${}.".format(bill))
print(f"\nJust to be clear, you pay ${bill} cash money.")

