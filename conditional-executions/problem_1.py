# Write a program that checks if a number entered by the user is positive, negative, or zero.
number = float(input("Enter a number: "))
if number>0:
    print("This is a positive number.")
elif number < 0:
    print("This is a negative number.")
else:
    print("The number is zero.")