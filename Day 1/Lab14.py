word = input("Enter a word: ")

word = word.upper()

for letter in word:

    if letter in 'AEIOU':
        continue

    print(letter)