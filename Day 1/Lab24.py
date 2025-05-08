# Set Creation
A = {1, 2, 3, 4, 5}
print("Initial Set A:", A)

# Set Length
print("Number of elements in set A:", len(A))

# Adding Elements
A.add(6)
A.add(7)
print("Set A after adding 6 and 7:", A)

# Removing Elements
A.remove(3)
print("Set A after removing 3:", A)

# Create Set B
B = {4, 5, 6, 7, 8}
print("Set B:", B)

# Set Operations
print("Union of A and B:", A.union(B))
print("Intersection of A and B:", A.intersection(B))
print("Difference of A and B (A - B):", A.difference(B))
print("Symmetric Difference of A and B:", A.symmetric_difference(B))

# Subset Check
print("Is A a subset of B?", A.issubset(B))

# Bonus Task: Clear the set
A.clear()
print("Set A after clearing:", A)