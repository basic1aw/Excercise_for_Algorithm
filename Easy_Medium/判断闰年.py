"""
leap year: 4的倍数但不是100的倍数 或 400的倍数
"""

def leap_year():
    year = int(input('Enter a year to determine is_leapyear'))
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print('%d is leap year'%year)
    else:
        print('%d is not a leap year'%year)

leap_year()
