# Write a function that takes a list of numbers as input and returns the sum of the numbers.

num_list = []
while True:
    number = input('Enter a number, press enter to finish: ')
    if number.isdigit():
        num_list.append(int(number))
    elif number == '':
        break
    else:
        print("Not a number")

def list_sum(number_list):
    return sum(number_list)

print(list_sum(num_list))