# Introduction
# Day 1 - 30DaysOfPython Challenge

# Excercise level: 2
# 1.Operations
print(3 + 4)   # addition(+)
print(3 - 4)   # subtraction(-)
print(3 * 4)   # multiplication(*)
print(3 / 4)   # division(/)
print(3 ** 4)  # exponential(**)
print(3 % 4)   # modulus(%)
print(3 // 4)  # Floor division operator(//)

# 2.Strings on Python
print('Yulissa')
print('Martínez')
print('Mexico')
print('Im enjoying 30 days of python')

# 3.Checking data types

print(type(10))                  # Int
print(type(9.8))                  
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


# Excercise: level 3
import math

int_p = 4
int_q = 2.5
int_distance = math.sqrt((int_p - int_q)**2)

print(int_distance)