def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_gregorian(year):

    if year >= 1582:
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_gregorian(year):

    if is_leap_year(year):
        print(f"{year} is a Leap Year in the Gregorian calendar.")
    else:
        print(f"{year} is a Common Year in the Gregorian calendar.")
else:
    print(f"{year} is not in the Gregorian calendar.")
