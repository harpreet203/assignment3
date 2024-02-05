numbers = input("Enter a list of numbers separated by spaces: ")

num = [float(num) for num in numbers.split()]

if num:
    smallest_number = min(num)
    largest_number = max(num)

    print("The smallest number is:", smallest_number)
    print("The largest number is:", largest_number)
else:
    print("The list is empty. Please enter some numbers.")