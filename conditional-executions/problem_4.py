# Write a program that prompts the user to enter their grade and tells them whether they have passed or failed.

grade = int(input("Enter your grade: "))

if grade >= 40:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed.")