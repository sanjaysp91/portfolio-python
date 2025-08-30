# portfolio-python
These are my portfolio projects using Python Programming Language intended for interested clients. 

## 1. Large Number Processing
This demonstrates:
1. Handling extremely large integers (math.factorial).
2. High-precision decimal arithmetic (decimal.Decimal).
3. Efficient processing of large datasets with big numbers.

#### Code
```python
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
```

#### Usage
```bash
(terminal)~% sudo python3 large-number-demo.py
```

#### Output
```txt 
Digits in 5000!: 16326
1/7 with high precision: 0.14285714285714285714285714285714285714285714285714
Approximation of pi: 3.1415929203539823008849557522123893805309734513274
Sum of dataset of huge numbers: 500000000000000000000000000000000000000000000000010
```

## 2. 