# ============================================================
# PYTHON FUNDAMENTALS FOR DATA ENGINEERING
# ============================================================
#
# Topics covered:
# 1. Python Syntax
# 2. Python Data Types
# 3. Loops & Iterators
# 4. Generators
# 5. File Handling & Context Managers
# 6. Pandas Basics
#
# Run:
#     python python_fundamentals.py
#
# ============================================================


# ============================================================
# 1. PYTHON SYNTAX
# ============================================================

print("\n" + "=" * 60)
print("1. PYTHON SYNTAX")
print("=" * 60)


# ------------------------------------------------------------
# 1.1 Variables
# ------------------------------------------------------------

# Python does not require you to explicitly specify a type.
# The type is inferred from the value.

name = "Bilal"
age = 34
salary = 150000.50
is_data_engineer = True

print("\nVariables:")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Is Data Engineer:", is_data_engineer)


# ------------------------------------------------------------
# 1.2 Basic Operations
# ------------------------------------------------------------

a = 10
b = 3

print("\nArithmetic Operations:")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# // = integer/floor division
print("Floor Division:", a // b)

# % = remainder
print("Modulus:", a % b)

# ** = power
print("Power:", a ** b)


# ------------------------------------------------------------
# 1.3 String Operations
# ------------------------------------------------------------

first_name = "Bilal"
last_name = "Tahir"

full_name = first_name + " " + last_name

print("\nString Operations:")
print("Full Name:", full_name)

# f-string is commonly used in Python
message = f"My name is {full_name} and I am {age} years old."

print(message)

# String methods
email = "  BILAL@EXAMPLE.COM  "

print("Original:", email)
print("Lower:", email.lower())
print("Upper:", email.upper())
print("Trimmed:", email.strip())


# ------------------------------------------------------------
# 1.4 Conditions
# ------------------------------------------------------------

records_processed = 100

if records_processed > 0:
    print("\nRecords were processed.")
else:
    print("\nNo records were processed.")


# Multiple conditions

status = "SUCCESS"

if status == "SUCCESS":
    print("ETL pipeline completed successfully.")
elif status == "FAILED":
    print("ETL pipeline failed.")
else:
    print("ETL pipeline has an unknown status.")


# ------------------------------------------------------------
# 1.5 Logical Operators
# ------------------------------------------------------------

age = 34
experience = 8

if age > 30 and experience >= 5:
    print("\nExperienced professional.")

if age < 40 or experience > 10:
    print("Condition matched using OR.")


# ------------------------------------------------------------
# 1.6 Functions
# ------------------------------------------------------------

def add_numbers(x, y):
    """
    Function that adds two numbers.
    """
    return x + y


result = add_numbers(10, 20)

print("\nFunction Result:", result)


# Function with a default parameter

def greet(name="User"):
    return f"Hello, {name}!"


print(greet())
print(greet("Bilal"))


# ------------------------------------------------------------
# 1.7 Function for Data Engineering
# ------------------------------------------------------------

def calculate_total_sales(price, quantity):
    """
    Calculate total sales amount.
    """
    return price * quantity


price = 100
quantity = 5

total = calculate_total_sales(price, quantity)

print("\nTotal Sales:", total)


# ============================================================
# 2. PYTHON DATA TYPES
# ============================================================

print("\n" + "=" * 60)
print("2. PYTHON DATA TYPES")
print("=" * 60)


# ------------------------------------------------------------
# 2.1 Integer
# ------------------------------------------------------------

record_count = 100

print("\nInteger:")
print(record_count)
print(type(record_count))


# ------------------------------------------------------------
# 2.2 Float
# ------------------------------------------------------------

price = 99.99

print("\nFloat:")
print(price)
print(type(price))


# ------------------------------------------------------------
# 2.3 Boolean
# ------------------------------------------------------------

is_valid = True

print("\nBoolean:")
print(is_valid)
print(type(is_valid))


# ------------------------------------------------------------
# 2.4 String
# ------------------------------------------------------------

customer_name = "Bilal"

print("\nString:")
print(customer_name)
print(type(customer_name))


# ------------------------------------------------------------
# 2.5 List
# ------------------------------------------------------------

# List is ordered and mutable.
# Mutable means we can change it after creation.

customers = ["Bilal", "Ali", "Ahmed"]

print("\nList:")
print(customers)

customers.append("Usman")

print("After append:", customers)

customers[0] = "Bilal Tahir"

print("After modification:", customers)


# ------------------------------------------------------------
# 2.6 Tuple
# ------------------------------------------------------------

# Tuple is ordered but immutable.
# Once created, its values cannot be changed.

coordinates = (10, 20)

print("\nTuple:")
print(coordinates)

# This would cause an error:
#
# coordinates[0] = 100


# ------------------------------------------------------------
# 2.7 Set
# ------------------------------------------------------------

# Set stores unique values.
# Duplicate values are automatically removed.

departments = {"IT", "HR", "Finance", "IT"}

print("\nSet:")
print(departments)


# ------------------------------------------------------------
# 2.8 Dictionary
# ------------------------------------------------------------

# Dictionary stores key-value pairs.
# Very commonly used when working with JSON/API data.

customer = {
    "id": 1,
    "name": "Bilal",
    "age": 34,
    "city": "Lahore"
}

print("\nDictionary:")
print(customer)

print("Customer Name:", customer["name"])
print("Customer City:", customer["city"])


# Adding a new key

customer["country"] = "Pakistan"

print("After adding country:", customer)


# ------------------------------------------------------------
# 2.9 Dictionary is extremely important for Data Engineering
# ------------------------------------------------------------

record = {
    "customer_id": 101,
    "name": "Ahmed",
    "amount": 2500.50,
    "is_active": True
}

print("\nData Engineering Record:")

for key, value in record.items():
    print(key, "=", value)


# ------------------------------------------------------------
# 2.10 Mutable vs Immutable
# ------------------------------------------------------------

print("\nMutable vs Immutable:")

# Mutable:
# list
# dictionary
# set

# Immutable:
# int
# float
# bool
# string
# tuple

my_list = [1, 2, 3]

print("Before:", my_list)

my_list.append(4)

print("After:", my_list)


my_string = "hello"

# Strings cannot be changed directly.
# This creates a NEW string.

my_string = my_string.upper()

print("String:", my_string)


# ============================================================
# 3. LOOPS & ITERATORS
# ============================================================

print("\n" + "=" * 60)
print("3. LOOPS & ITERATORS")
print("=" * 60)


# ------------------------------------------------------------
# 3.1 For Loop
# ------------------------------------------------------------

print("\nFor Loop:")

customers = ["Bilal", "Ali", "Ahmed"]

for customer in customers:
    print(customer)


# ------------------------------------------------------------
# 3.2 For Loop with range()
# ------------------------------------------------------------

print("\nRange Loop:")

for i in range(5):
    print("Processing record:", i)


# range(1, 6) means 1 to 5

for i in range(1, 6):
    print(i)


# ------------------------------------------------------------
# 3.3 While Loop
# ------------------------------------------------------------

print("\nWhile Loop:")

counter = 1

while counter <= 5:
    print("Counter:", counter)
    counter += 1


# ------------------------------------------------------------
# 3.4 Loop through Dictionary
# ------------------------------------------------------------

print("\nDictionary Loop:")

customer = {
    "id": 101,
    "name": "Bilal",
    "city": "Lahore"
}

for key, value in customer.items():
    print(key, ":", value)


# ------------------------------------------------------------
# 3.5 Iterable vs Iterator
# ------------------------------------------------------------

# An ITERABLE is an object that we can loop over.
#
# Examples:
# list
# tuple
# string
# dictionary
# set
#
# An ITERATOR is an object that produces values one at a time.
#
# iter() converts an iterable into an iterator.


numbers = [10, 20, 30, 40]

print("\nIterable:")
print(numbers)


# Convert list into iterator

number_iterator = iter(numbers)

print("\nIterator:")
print(number_iterator)


# next() gets the next value

print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))


# Calling next() again would raise StopIteration.
#
# print(next(number_iterator))


# ------------------------------------------------------------
# 3.6 Iterator with while loop
# ------------------------------------------------------------

numbers = [100, 200, 300]

iterator = iter(numbers)

print("\nReading Iterator Manually:")

while True:

    try:
        value = next(iterator)
        print(value)

    except StopIteration:
        print("Iterator finished.")
        break


# ============================================================
# 4. GENERATORS
# ============================================================

print("\n" + "=" * 60)
print("4. GENERATORS")
print("=" * 60)


# ------------------------------------------------------------
# 4.1 Normal Function
# ------------------------------------------------------------

def create_numbers():
    """
    Creates a complete list in memory.
    """

    numbers = []

    for i in range(5):
        numbers.append(i)

    return numbers


normal_result = create_numbers()

print("\nNormal Function:")
print(normal_result)


# ------------------------------------------------------------
# 4.2 Generator Function
# ------------------------------------------------------------

def generate_numbers():
    """
    Generator produces one value at a time.
    """

    for i in range(5):

        # yield pauses the function.
        # The function continues from here
        # when next() is called again.

        yield i


generator = generate_numbers()

print("\nGenerator:")
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))


# ------------------------------------------------------------
# 4.3 Using Generator in a For Loop
# ------------------------------------------------------------

print("\nGenerator with For Loop:")

for number in generate_numbers():
    print(number)


# ------------------------------------------------------------
# 4.4 Generator for ETL
# ------------------------------------------------------------

def read_records():
    """
    Simulates reading records from a large data source.

    Instead of loading all records into memory,
    we process one record at a time.
    """

    records = [
        {"id": 1, "name": "Bilal"},
        {"id": 2, "name": "Ali"},
        {"id": 3, "name": "Ahmed"},
        {"id": 4, "name": "Usman"},
        {"id": 5, "name": "Hamza"}
    ]

    for record in records:

        # Yield one record at a time.
        yield record


print("\nProcessing Records Using Generator:")

for record in read_records():

    print("Processing:", record)


# ------------------------------------------------------------
# 4.5 Generator for Data Transformation
# ------------------------------------------------------------

def transform_records(records):
    """
    Simulates an ETL transformation.

    Input:
        records

    Output:
        transformed records one at a time
    """

    for record in records:

        transformed_record = {
            "id": record["id"],
            "name": record["name"].upper()
        }

        yield transformed_record


records = [
    {"id": 1, "name": "bilal"},
    {"id": 2, "name": "ali"},
    {"id": 3, "name": "ahmed"}
]


print("\nETL Transformation:")

for record in transform_records(records):

    print(record)


# ------------------------------------------------------------
# 4.6 Generator vs List - Memory
# ------------------------------------------------------------

import sys

# List creates all values immediately.

list_data = [i for i in range(10000)]

# Generator produces values when needed.

generator_data = (i for i in range(10000))


print("\nMemory Comparison:")

print(
    "List memory:",
    sys.getsizeof(list_data),
    "bytes"
)

print(
    "Generator memory:",
    sys.getsizeof(generator_data),
    "bytes"
)


# IMPORTANT:
#
# A list stores all values in memory.
#
# A generator stores the logic required to produce
# the next value.
#
# This is extremely useful for:
#
# - Large CSV files
# - Large database queries
# - ETL pipelines
# - Streaming data
# - Log processing
# - API pagination
#
# Example:
#
# 10 million records
#
# List:
#     Load 10 million records into memory.
#
# Generator:
#     Process one record at a time.


# ============================================================
# 5. FILE HANDLING & CONTEXT MANAGERS
# ============================================================

print("\n" + "=" * 60)
print("5. FILE HANDLING & CONTEXT MANAGERS")
print("=" * 60)


# ------------------------------------------------------------
# 5.1 Writing to a File
# ------------------------------------------------------------

file_name = "customers.txt"

# "w" means write mode.
#
# If the file doesn't exist:
#     Python creates it.
#
# If it exists:
#     Python overwrites it.

with open(file_name, "w") as file:

    file.write("Bilal\n")
    file.write("Ali\n")
    file.write("Ahmed\n")


print("\nFile created:", file_name)


# ------------------------------------------------------------
# 5.2 Reading a File
# ------------------------------------------------------------

print("\nReading File:")

with open(file_name, "r") as file:

    content = file.read()

    print(content)


# ------------------------------------------------------------
# 5.3 Reading Line by Line
# ------------------------------------------------------------

print("\nReading File Line by Line:")

with open(file_name, "r") as file:

    for line in file:

        print(line.strip())


# ------------------------------------------------------------
# 5.4 Append to File
# ------------------------------------------------------------

# "a" means append.

with open(file_name, "a") as file:

    file.write("Usman\n")


print("\nNew record appended.")


# ------------------------------------------------------------
# 5.5 Context Manager
# ------------------------------------------------------------

# The "with" statement is a context manager.
#
# It automatically closes the file when the block
# finishes, even if an exception occurs.
#
# This prevents resource leaks.


with open(file_name, "r") as file:

    print("\nFile is open:", not file.closed)

print("File is open after with:", not file.closed)


# ------------------------------------------------------------
# 5.6 CSV-style File Processing
# ------------------------------------------------------------

csv_file = "customers.csv"

with open(csv_file, "w") as file:

    file.write("id,name,city\n")
    file.write("1,Bilal,Lahore\n")
    file.write("2,Ali,Islamabad\n")
    file.write("3,Ahmed,Karachi\n")


print("\nCSV file created.")


# Reading CSV using Python's built-in csv module

import csv

print("\nReading CSV:")

with open(csv_file, "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)


# ============================================================
# 6. PANDAS BASICS
# ============================================================

print("\n" + "=" * 60)
print("6. PANDAS BASICS")
print("=" * 60)


# Pandas is one of the most important Python libraries
# for data analysis and data engineering.
#
# Install if necessary:
#
# pip install pandas


import pandas as pd


# ------------------------------------------------------------
# 6.1 Create a DataFrame
# ------------------------------------------------------------

data = {
    "id": [1, 2, 3, 4, 5],
    "name": [
        "Bilal",
        "Ali",
        "Ahmed",
        "Usman",
        "Hamza"
    ],
    "department": [
        "IT",
        "IT",
        "HR",
        "Finance",
        "IT"
    ],
    "salary": [
        150000,
        120000,
        100000,
        110000,
        130000
    ],
    "age": [
        34,
        30,
        28,
        32,
        29
    ]
}


df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# ------------------------------------------------------------
# 6.2 head()
# ------------------------------------------------------------

# Shows first 5 rows by default.

print("\nFirst 5 rows:")

print(df.head())


# You can specify the number of rows.

print("\nFirst 2 rows:")

print(df.head(2))


# ------------------------------------------------------------
# 6.3 tail()
# ------------------------------------------------------------

print("\nLast 2 rows:")

print(df.tail(2))


# ------------------------------------------------------------
# 6.4 info()
# ------------------------------------------------------------

# Provides information about:
#
# - Number of rows
# - Columns
# - Data types
# - Null values
# - Memory usage

print("\nDataFrame Information:")

df.info()


# ------------------------------------------------------------
# 6.5 describe()
# ------------------------------------------------------------

# Provides statistical information about numerical columns.

print("\nStatistical Description:")

print(df.describe())


# ------------------------------------------------------------
# 6.6 Selecting a Column
# ------------------------------------------------------------

print("\nNames:")

print(df["name"])


# Multiple columns

print("\nNames and Salaries:")

print(df[["name", "salary"]])


# ------------------------------------------------------------
# 6.7 Filtering Data
# ------------------------------------------------------------

print("\nEmployees with salary > 120000:")

high_salary = df[df["salary"] > 120000]

print(high_salary)


# Multiple conditions

print("\nIT employees with salary > 120000:")

filtered_data = df[
    (df["department"] == "IT")
    & (df["salary"] > 120000)
]

print(filtered_data)


# ------------------------------------------------------------
# 6.8 Sorting
# ------------------------------------------------------------

print("\nEmployees sorted by salary:")

sorted_df = df.sort_values("salary")

print(sorted_df)


# Descending order

print("\nEmployees sorted by salary descending:")

sorted_df = df.sort_values(
    "salary",
    ascending=False
)

print(sorted_df)


# ------------------------------------------------------------
# 6.9 GroupBy
# ------------------------------------------------------------

print("\nAverage Salary by Department:")

department_salary = df.groupby(
    "department"
)["salary"].mean()

print(department_salary)


# Count employees per department

print("\nEmployees per Department:")

department_count = df.groupby(
    "department"
)["id"].count()

print(department_count)


# ------------------------------------------------------------
# 6.10 Transform Data
# ------------------------------------------------------------

# Add a new column.

df["annual_salary"] = df["salary"] * 12

print("\nAnnual Salary:")

print(df)


# ------------------------------------------------------------
# 6.11 Apply Function
# ------------------------------------------------------------

# Apply a function to every value in a column.

df["name_upper"] = df["name"].apply(
    lambda name: name.upper()
)

print("\nUppercase Names:")

print(df)


# ------------------------------------------------------------
# 6.12 Handle Missing Values
# ------------------------------------------------------------

data_with_nulls = {
    "name": [
        "Bilal",
        "Ali",
        None,
        "Usman",
        "Ahmed"
    ],
    "salary": [
        150000,
        None,
        100000,
        120000,
        None
    ]
}

df_nulls = pd.DataFrame(data_with_nulls)

print("\nData with Missing Values:")

print(df_nulls)


# Check missing values

print("\nMissing Values:")

print(df_nulls.isnull())


# Count missing values

print("\nMissing Value Count:")

print(df_nulls.isnull().sum())


# ------------------------------------------------------------
# 6.13 Fill Missing Values
# ------------------------------------------------------------

# Fill missing salary with 0.

df_nulls["salary"] = df_nulls["salary"].fillna(0)

# Fill missing name with "Unknown".

df_nulls["name"] = df_nulls["name"].fillna("Unknown")


print("\nAfter Filling Missing Values:")

print(df_nulls)


# ------------------------------------------------------------
# 6.14 Drop Missing Values
# ------------------------------------------------------------

data_with_nulls = {
    "name": [
        "Bilal",
        "Ali",
        None,
        "Usman"
    ],
    "salary": [
        150000,
        None,
        100000,
        120000
    ]
}

df_nulls = pd.DataFrame(data_with_nulls)

print("\nBefore dropna:")

print(df_nulls)

df_clean = df_nulls.dropna()

print("\nAfter dropna:")

print(df_clean)


# ------------------------------------------------------------
# 6.15 Duplicate Values
# ------------------------------------------------------------

duplicate_data = {
    "id": [1, 2, 3, 3, 4],
    "name": [
        "Bilal",
        "Ali",
        "Ahmed",
        "Ahmed",
        "Usman"
    ]
}

df_duplicates = pd.DataFrame(duplicate_data)

print("\nData with Duplicates:")

print(df_duplicates)


# Find duplicates

print("\nDuplicate Rows:")

print(df_duplicates.duplicated())


# Remove duplicates

df_unique = df_duplicates.drop_duplicates()

print("\nAfter Removing Duplicates:")

print(df_unique)


# ------------------------------------------------------------
# 6.16 Read CSV Using Pandas
# ------------------------------------------------------------

# We already created customers.csv earlier.

print("\nReading CSV using Pandas:")

df_csv = pd.read_csv(csv_file)

print(df_csv)


# ------------------------------------------------------------
# 6.17 Write DataFrame to CSV
# ------------------------------------------------------------

output_file = "employees_output.csv"

df.to_csv(
    output_file,
    index=False
)

print("\nDataFrame exported to:", output_file)


# ============================================================
# 7. SMALL DATA ENGINEERING EXERCISE
# ============================================================

print("\n" + "=" * 60)
print("7. MINI DATA ENGINEERING EXERCISE")
print("=" * 60)


# Imagine this is raw data received from a source system.

raw_data = [
    {
        "id": 1,
        "name": "bilal",
        "department": "IT",
        "salary": 150000
    },
    {
        "id": 2,
        "name": "ali",
        "department": "IT",
        "salary": 120000
    },
    {
        "id": 3,
        "name": "ahmed",
        "department": "HR",
        "salary": 100000
    }
]


# ------------------------------------------------------------
# EXTRACT
# ------------------------------------------------------------

def extract_data():
    """
    Extract data from a source.
    """

    for record in raw_data:

        yield record


# ------------------------------------------------------------
# TRANSFORM
# ------------------------------------------------------------

def transform_data(records):
    """
    Transform records.
    """

    for record in records:

        transformed = {
            "employee_id": record["id"],
            "employee_name": record["name"].upper(),
            "department": record["department"],
            "monthly_salary": record["salary"],
            "annual_salary": record["salary"] * 12
        }

        yield transformed


# ------------------------------------------------------------
# LOAD
# ------------------------------------------------------------

def load_data(records):
    """
    Load transformed records.
    In a real Data Engineering project,
    this could insert data into:
    
    - SQL Server
    - PostgreSQL
    - Azure SQL
    - Data Lake
    - Snowflake
    - Databricks
    """

    for record in records:

        print("Loading:", record)


# ------------------------------------------------------------
# Execute ETL Pipeline
# ------------------------------------------------------------

print("\nRunning ETL Pipeline:")

extracted_records = extract_data()

transformed_records = transform_data(
    extracted_records
)

load_data(transformed_records)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PYTHON FUNDAMENTALS COMPLETED")
print("=" * 60)

print("""
You have practiced:

1. Variables
2. Conditions
3. Functions
4. Basic operations

5. int
6. float
7. bool
8. string
9. list
10. tuple
11. set
12. dictionary

13. for loop
14. while loop
15. iterable
16. iterator
17. iter()
18. next()

19. Generators
20. yield
21. Generator vs List
22. Memory-efficient processing

23. File reading
24. File writing
25. CSV files
26. Context managers
27. with statement

28. Pandas DataFrame
29. read_csv()
30. head()
31. info()
32. describe()
33. Filtering
34. Sorting
35. GroupBy
36. Transformations
37. Missing values
38. Duplicate values

39. Mini ETL Pipeline
40. Extract -> Transform -> Load
""")

print("\nPython Data Engineering fundamentals completed successfully!")