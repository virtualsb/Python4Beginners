# Creating the tuple
fruits = ("apple", "banana", "orange", "kiwi", "grape")

# Accessing elements
print("Third element:", fruits[2])         # Indexing starts at 0, so index 2 is the third element
print("Last element:", fruits[-1])         # Negative index -1 gives the last element

# Tuple length
print("Length of tuple:", len(fruits))

# Slicing
selected_fruits = fruits[:3]               # First three elements (indices 0, 1, 2)
print("Selected fruits:", selected_fruits)

# Adding elements by concatenation
more_fruits = ("pineapple", "watermelon")
all_fruits = fruits + more_fruits          # Concatenate the two tuples
print("All fruits:", all_fruits)