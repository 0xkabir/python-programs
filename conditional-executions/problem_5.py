# Write a program that prompts the user to enter a number and then checks if it is divisible by 5.

number = int(input("Enter a number: "))
print("The number is divisible by 5." if number%5 == 0 else "The number is not divisible by 5.")