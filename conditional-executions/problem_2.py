# Write a program that prompts the user to enter their age and tells them whether they are a child, teenager, or adult.

age = int(input("Enter your age: "))
if age < 0:
    print("This is an invalid age.")
elif age <= 12:
    print("You're a Child.")
elif age > 12 and age < 18:
    print("You're a Teenager.")
else:
    print("You're an adult.")