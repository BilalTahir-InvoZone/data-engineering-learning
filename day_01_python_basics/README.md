# Python Fundamentals for Data Engineering

A hands-on Python learning project focused on the fundamental concepts required for **Data Engineering**.

The project covers Python syntax, data types, loops, iterators, generators, file handling, context managers, and Pandas.

The goal is not only to learn Python syntax but also to understand how Python handles data in memory and why concepts such as generators are important when processing large datasets.

---

## 📚 Topics Covered

### 1. Python Syntax

Learn the basic building blocks of Python:

* Variables
* Conditions
* `if`, `elif`, `else`
* Arithmetic operations
* String operations
* Functions
* Function parameters
* Return values
* f-strings

Example:

```python
def calculate_total_sales(price, quantity):
    return price * quantity

total = calculate_total_sales(100, 5)

print(total)
```

---

### 2. Python Data Types

The project demonstrates the following Python data types:

* `int`
* `float`
* `bool`
* `str`
* `list`
* `tuple`
* `set`
* `dict`

It also demonstrates the difference between **mutable** and **immutable** objects.

#### Mutable

These objects can be modified after creation:

```text
list
dict
set
```

#### Immutable

These objects cannot be modified after creation:

```text
int
float
bool
str
tuple
```

---

### 3. Loops & Iterators

The project covers:

* `for` loops
* `while` loops
* `range()`
* Iterables
* Iterators
* `iter()`
* `next()`
* `StopIteration`

Example:

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

### Iterable vs Iterator

An **iterable** is an object that can be iterated over.

Examples:

```text
list
tuple
string
set
dictionary
```

An **iterator** is an object that produces values one at a time.

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

value = next(iterator)
```

This concept is important for understanding generators and memory-efficient data processing.

---

## 4. Generators

Generators are one of the most important Python concepts for Data Engineering.

The project demonstrates:

* `yield`
* Generator functions
* Lazy evaluation
* Generator vs List
* Memory-efficient processing
* Processing records one at a time

Example:

```python
def generate_numbers():
    for i in range(5):
        yield i
```

A generator does not create all values at once.

Instead:

```text
Request value
     ↓
Generate value
     ↓
Process value
     ↓
Request next value
     ↓
Generate next value
```

### Why Generators Matter in Data Engineering

Imagine processing:

```text
10 million records
```

Using a list could require loading a large amount of data into memory.

A generator allows us to process records one at a time:

```python
def read_records(records):

    for record in records:
        yield record
```

This makes generators useful for:

* Large CSV files
* ETL pipelines
* Log processing
* API responses
* Database records
* Streaming data
* Large datasets

---

## 5. File Handling & Context Managers

The project demonstrates reading and writing files using Python.

### Write a file

```python
with open("customers.txt", "w") as file:
    file.write("Bilal\n")
```

### Read a file

```python
with open("customers.txt", "r") as file:
    content = file.read()

print(content)
```

### Read line by line

```python
with open("customers.txt", "r") as file:

    for line in file:
        print(line.strip())
```

### Context Managers

The `with` statement is used as a context manager.

It automatically handles resource cleanup.

For example:

```python
with open("customers.txt", "r") as file:
    data = file.read()
```

After leaving the `with` block, Python automatically closes the file.

This is important because resources such as:

* Files
* Database connections
* Network connections

should be properly released after use.

---

# 6. Pandas Basics

The project introduces Pandas for working with structured datasets.

Topics include:

* Creating DataFrames
* Reading CSV files
* Writing CSV files
* `head()`
* `tail()`
* `info()`
* `describe()`
* Selecting columns
* Filtering
* Sorting
* `groupby()`
* Transformations
* `apply()`
* Missing values
* Duplicate values

---

## Creating a DataFrame

```python
import pandas as pd

data = {
    "name": ["Bilal", "Ali", "Ahmed"],
    "salary": [150000, 120000, 100000]
}

df = pd.DataFrame(data)

print(df)
```

---

## Reading CSV

```python
df = pd.read_csv("customers.csv")
```

---

## Exploring Data

### First rows

```python
df.head()
```

### Dataset information

```python
df.info()
```

### Statistical information

```python
df.describe()
```

---

## Filtering

Example:

```python
high_salary = df[df["salary"] > 120000]
```

Multiple conditions:

```python
filtered_data = df[
    (df["department"] == "IT")
    & (df["salary"] > 120000)
]
```

---

## Sorting

```python
df.sort_values(
    "salary",
    ascending=False
)
```

---

## Grouping

Calculate average salary by department:

```python
df.groupby("department")["salary"].mean()
```

---

## Handling Missing Values

Check for missing values:

```python
df.isnull().sum()
```

Fill missing values:

```python
df["salary"] = df["salary"].fillna(0)
```

Remove rows containing missing values:

```python
df = df.dropna()
```

---

## Handling Duplicates

Check for duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

---

# 7. Mini ETL Pipeline

The project also contains a simple Extract → Transform → Load pipeline.

```text
             SOURCE
                │
                ▼
             EXTRACT
                │
                ▼
           GENERATOR
                │
                ▼
            TRANSFORM
                │
                ▼
              LOAD
                │
                ▼
           DESTINATION
```

### Extract

Data is extracted from a simulated source:

```python
def extract_data():

    for record in raw_data:
        yield record
```

### Transform

Records are transformed:

```python
def transform_data(records):

    for record in records:

        transformed = {
            "employee_id": record["id"],
            "employee_name": record["name"].upper(),
            "annual_salary": record["salary"] * 12
        }

        yield transformed
```

### Load

The transformed records are loaded:

```python
def load_data(records):

    for record in records:
        print("Loading:", record)
```

This demonstrates the basic idea behind an ETL pipeline.

---

# 🚀 Getting Started

## Prerequisites

Make sure Python is installed:

```bash
python --version
```

Recommended:

```text
Python 3.10+
```

---

## Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd python-data-engineering-fundamentals
```

---

## Install Dependencies

Install Pandas:

```bash
pip install pandas
```

Or:

```bash
python -m pip install pandas
```

---

## Run the Project

```bash
python python_fundamentals.py
```

On Windows:

```bash
py python_fundamentals.py
```

---

# 📁 Project Structure

```text
python-data-engineering-fundamentals/
│
├── python_fundamentals.py
├── README.md
├── .gitignore
│
├── customers.txt
├── customers.csv
└── employees_output.csv
```

### Files

| File                     | Description                 |
| ------------------------ | --------------------------- |
| `python_fundamentals.py` | Main Python learning script |
| `README.md`              | Project documentation       |
| `.gitignore`             | Git ignored files           |
| `customers.txt`          | Generated text file         |
| `customers.csv`          | Generated CSV file          |
| `employees_output.csv`   | Generated Pandas output     |

---

# 🎯 Learning Objectives

After completing this project, I should be able to:

* Understand Python syntax
* Work with Python data types
* Understand mutable vs immutable objects
* Use loops effectively
* Understand iterables and iterators
* Use `iter()` and `next()`
* Create and use generators
* Understand lazy evaluation
* Understand why generators save memory
* Read and write files
* Use context managers
* Work with CSV files
* Create Pandas DataFrames
* Read and write CSV datasets
* Filter and sort datasets
* Group and aggregate data
* Handle missing data
* Remove duplicate records
* Build a basic ETL pipeline

---

# 🧠 Important Data Engineering Concepts

The most important concepts from this project are:

```text
Python
  │
  ├── Data Types
  │
  ├── Collections
  │
  ├── Iterables
  │
  ├── Iterators
  │
  ├── Generators
  │       │
  │       └── Memory-efficient processing
  │
  ├── File Handling
  │
  └── Pandas
          │
          ├── DataFrame
          ├── Filtering
          ├── Sorting
          ├── GroupBy
          ├── Missing Values
          └── Duplicate Handling
```

---

# 🔜 Next Steps

After completing these fundamentals, the next topics to study are:

1. Python Virtual Environments
2. Python Modules & Packages
3. Exception Handling
4. Object-Oriented Programming
5. Python Type Hints
6. Logging
7. Working with JSON
8. Working with APIs
9. SQL + Python
10. Database connectivity
11. ETL pipelines
12. PySpark
13. Azure Data Engineering
14. Azure Data Factory
15. Azure Data Lake
16. Databricks

---

## Author

**Bilal Tahir**

Python & Data Engineering Learning Project
