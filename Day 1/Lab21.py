def is_prime(n):
    # Check if input is a valid integer greater than 1
    if not isinstance(n, int) or n <= 1:
        return False
    # 2 and 3 are prime
    if n <= 3:
        return True
    # Eliminate even numbers and multiples of 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Check for factors up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example test cases
print(is_prime(2))    # True
print(is_prime(17))   # True
print(is_prime(18))   # False
print(is_prime(1))    # False
print(is_prime(97))   # True
print(is_prime(-7))   # False