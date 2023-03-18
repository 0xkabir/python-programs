# Write a function that takes a number as input and returns True if the number is prime and False otherwise.

number = int(input("Enter a number to check prime: "))

def check_prime(number):
    return "This is not a prime number" if any(number%i == 0 for i in range(2, number)) else "This is a prime number" 

print(check_prime(number))