def remove_duplicates(numbers):

    unique_numbers = []
    seen = set()
    for num in numbers:
        if num not in seen:
            unique_numbers.append(num)
            seen.add(num)
    return unique_numbers

default_list = [4, 2, 5, 2, 3, 4, 1, 5, 6]

print("Default list:", default_list)
my_list = remove_duplicates(default_list)
print("The list with unique elements only: ")
print(my_list)

use_custom = input("\nWould you like to enter your own list? (yes/no): ").strip().lower()
if use_custom == 'yes':
    user_input = input("Enter numbers separated by spaces: ")
    try:
        user_list = list(map(int, user_input.split()))
        my_list = remove_duplicates(user_list)
        print("The list with unique elements only: ")
        print(my_list)
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")