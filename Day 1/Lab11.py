
secret_number = 777

while True:

    user_guess = int(input(""""Welcome to my game, muggle! 
Enter an integer number, 
and guess what number I've picked for you.
So, what is the secret number?"""""))
    if user_guess == secret_number:
        print("Well done, muggle! You are free now.")
        break
