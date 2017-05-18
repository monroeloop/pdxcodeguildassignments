# Chase wrote this for Week 2 Day 3 class

import math

def centuryFromYear(year):
    return math.floor((year - 1) / 100) + 1
    # century = math.floor((year -1) / 100)+1
    # if century in range(1, 1000):
    #     return century
    # elif century in range(1001, 1900):
    #     return century
    # elif century in range(1901, 2000):
    #     return math.floor(year / 100)+ 1

print(centuryFromYear(1999))
