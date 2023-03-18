# Write a function that takes two strings as input and returns the concatenation of the two strings.

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

def string_concat(string1, string2):
    return " ".join([string1, string2])

print(string_concat(string1, string2))
