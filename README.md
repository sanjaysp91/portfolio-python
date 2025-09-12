# portfolio-python
These are my portfolio projects using Python Programming Language intended for interested clients. 

## 0. Begin Here
### Working with Python Environment
#### 1. Each project gets its own python environment. 
    Default directory for env is: .venv
#### 2. "venv" is used for virtual python environments.
#### 3. Using python env: 
##### 3a. Check python version, use latest:
```bash
sap@Sanjays-MacBook-Air use_jupyter % python3 --version
Python 3.13.3
```

##### 3b. Create python env: 
```bash
sap@Sanjays-MacBook-Air use_jupyter % python3 -m venv .venv
```
##### 3c. Check newly created .venv directory: 
```bash
sap@Sanjays-MacBook-Air use_jupyter % ls -la
drwxr-xr-x  5 sap  staff    160 Sep  2 22:42 .
drwxr-xr-x  4 sap  staff    128 Sep  2 22:32 ..
-rw-r--r--@ 1 sap  staff   6148 Sep  2 22:32 .DS_Store
drwxr-xr-x@ 7 sap  staff    224 Sep  2 22:42 .venv
-rw-r--r--@ 1 sap  staff  18343 Sep  2 22:33 how-to-python.ipynb
```
##### 3d. Activate environment: 
```bash
sap@Sanjays-MacBook-Air use_jupyter % source .venv/bin/activate
```
##### 3e. Install requirements using requirements.txt 
```bash
(.venv) sap@Sanjays-MacBook-Air use_jupyter % pip install -r requirements.txt
Collecting jupyterlab... 
```
##### 3f. If new libraries are used, update requirements file: 
###### Manual: 
Maually add exact library that is installed using 'python3 -m pip install <lib_name>' command.

E.g. To install Jupyter Lab: 
```bash
(.venv) sap@Sanjays-MacBook-Air use_jupyter % python3 -m pip install jupyterlab
```
Manually append: jupyterlab==4.4.6 to requirements.txt file 
###### Update full list: 
```bash
(.venv) sap@Sanjays-MacBook-Air use_jupyter % pip freeze > requirements_full.txt 
```
#### 4. Start jupyterlab: 
```bash
(.venv) sap@Sanjays-MacBook-Air use_jupyter % jupyter lab
```
#### 5. deactivate the environment:
```bash
(.venv) sap@Sanjays-MacBook-Air use_jupyter % deactivate 
```
### working with Jupyter Notebook

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

## 2. Prompt Automation 
This demonstrates:
1. Handling LLM/GPT API services including model selection.
2. Function definition for setting response, messages and temperature. 
3. Basic Architecture for prompt and response. 

#### Code
```python
# Function 
def llm_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
	messages=[{'role':'user', 'content':prompt}],
	temperature=0
    )
    return response.choices[0].message['content']
```

#### Usage
```bash
(terminal)~% sudo python3 openai_1.py
```

#### Output
```txt 
Hello, World
Positive
```
