def get_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            else:
                print(f"Error: the value is not within permitted range ({low}..{high})")
        except ValueError:
            print("Error: wrong input")

number = get_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", number)