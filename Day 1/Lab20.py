def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


test_years = [2020, 1900, 2000, 2023, 2400]
for year in test_years:
    result = is_leap_year(year)
    print(f"{year} is a leap year: {result}")