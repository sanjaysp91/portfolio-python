import sys
from decimal import Decimal, getcontext
import math

# Increase Python's safety limit for converting big integers to string
sys.set_int_max_str_digits(1000000)

# 1. Arbitrary precision integers
large_factorial = math.factorial(5000)  
num_digits = len(str(large_factorial))  # number of digits in 5000!

# 2. High precision floating-point arithmetic
getcontext().prec = 50  # set precision to 50 decimal places
a = Decimal(1) / Decimal(7)             # precise fraction
b = Decimal(355) / Decimal(113)         # pi approximation

# 3. Processing a dataset of big integers
dataset = [10**50 + i for i in range(5)]  # simulate 5 huge integers
dataset_sum = sum(dataset)

print("Digits in 5000!:", num_digits)
print("1/7 with high precision:", a)
print("Approximation of pi:", b)
print("Sum of dataset of huge numbers:", dataset_sum)
