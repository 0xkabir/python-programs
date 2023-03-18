# Write a function that takes a list of strings as input and returns the longest string.

string_list = list()
while True:
    string = input("Enter a string, press enter to finish: ")
    if string == '':
        break
    string_list.append(string)

def longest_string(string_list):
    longest = ""
    for string in string_list:
        if len(string) > len(longest):
            longest = string
    return longest

print(longest_string(string_list))