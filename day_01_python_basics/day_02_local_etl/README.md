# Local ETL Pipeline — Pandas vs PySpark

## Overview

This project demonstrates a complete local and cloud-based ETL pipeline using Python, Pandas, PySpark, Azure Data Lake Storage Gen2, and Databricks.

The purpose of this project is to understand how Data Engineering pipelines work in practice and, more importantly, understand **why and when to use Pandas versus PySpark**.

The project covers:

* Python generators
* Large dataset generation
* CSV processing
* Pandas ETL
* Data cleaning
* Data normalization
* PySpark ETL
* Azure Data Lake Storage Gen2
* Azure Databricks
* Parquet
* Pandas vs PySpark performance
* Distributed data processing
* Spark lazy evaluation
* Spark transformations and actions

---

# Project Objective

Build a complete ETL pipeline that demonstrates:

```text
Python Generator
       ↓
Generate Large Dataset
       ↓
100,000 Rows × 127 Columns
       ↓
      CSV
       ↓
 ┌───────────────┐
 │               │
 ▼               ▼
Pandas         PySpark
 │               │
 ▼               ▼
Clean          Clean
 │               │
 ▼               ▼
Transform      Transform
 │               │
 ▼               ▼
Normalize      Normalize
 │               │
 ▼               ▼
Parquet        Parquet
 │               │
 └───────┬───────┘
         ▼
Pandas vs PySpark
Performance Comparison
```

---

# Technologies Used

* Python 3.14
* Pandas
* NumPy
* PyArrow
* PySpark
* Apache Spark
* Azure Databricks
* Azure Data Lake Storage Gen2
* CSV
* Parquet
* Git / GitHub

---

# Project Structure

```text
data-engineering-learning/
│
├── day_01_python_basics/
│   │
│   ├── day_01_python_basics/
│   │   └── ...
│   │
│   └── day_02_local_etl/
│       │
│       ├── data_generation/
│       │   ├── generate_data.py
│       │   └── output/
│       │       └── large_dataset.csv
│       │
│       ├── pandas_etl/
│       │   ├── pandas_etl.py
│       │   └── output/
│       │       ├── processed_dataset.csv
│       │       └── processed_dataset.parquet
│       │
│       ├── normalization/
│       │   ├── normalize_data.py
│       │   └── output/
│       │       ├── companies.csv
│       │       ├── contacts.csv
│       │       ├── deals.csv
│       │       ├── products.csv
│       │       ├── cities.csv
│       │       ├── customers.csv
│       │       └── orders.csv
│       │
│       ├── pyspark_etl/
│       │   └── Databricks notebook
│       │
│       └── output/
│           └── processed_dataset.csv
│
└── README.md
```

---

# Task 1 — Generate Test Data

## Objective

Generate a large CSV dataset using a **Python generator** rather than creating the complete dataset in a Python list.

## Requirements

The generated dataset contains:

* 100,000 rows
* 127 columns
* Integer values
* Float values
* String values
* Boolean values
* Date values
* Missing values
* Duplicate records
* Invalid values
* Inconsistent string values

## Result

```text
Rows generated : 100,000
Columns        : 127

Duplicates      : Added intentionally
Missing values  : Added intentionally
Invalid values  : Added intentionally
Dirty strings   : Added intentionally
```

Generated file:

```text
day_02_local_etl/data_generation/output/large_dataset.csv
```

## Why use a generator?

A normal approach could create all records in memory:

```python
records = []

for i in range(100000):
    records.append(create_record())
```

This means the entire dataset is stored in memory before it is written.

A generator instead produces one record at a time:

```python
def generate_records():
    for i in range(100000):
        yield create_record()
```

The generator does not need to keep all 100,000 records in memory.

Conceptually:

```text
Generator
   ↓
Record 1
   ↓
Record 2
   ↓
Record 3
   ↓
...
   ↓
Record 100,000
```

This is particularly useful in Data Engineering when processing large streams of records.

---

# Task 2 — Pandas ETL

## Objective

Process the generated CSV using Pandas.

The ETL process consists of:

```text
Extract
   ↓
Transform
   ↓
Load
```

---

## Extract

The CSV was loaded using Pandas:

```python
df = pd.read_csv(INPUT_FILE)
```

Dataset:

```text
Rows    : 100,000
Columns : 127
```

Measured loading time:

```text
Approximately 1.69 seconds
```

---

## Dataset Inspection

The following operations were performed:

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.dtypes
df.isnull().sum()
df.duplicated().sum()
```

### Dataset information

```text
Rows    : 100,000
Columns : 127
Memory  : approximately 82.9 MB
```

### Data types

The dataset contained:

* Integer columns
* Float columns
* Boolean columns
* String columns

---

# Transform

## 1. Remove Duplicate Records

The original dataset contained:

```text
Duplicate rows: 10
```

After removing duplicates:

```text
Rows before : 100,000
Rows after  : 99,990
Rows removed: 10
```

Code concept:

```python
df = df.drop_duplicates()
```

---

## 2. Handle Missing Values

The generated dataset intentionally contained missing values.

Before cleaning:

```text
Total missing values: 25,210+
```

Missing values were handled according to the business/data-quality rules.

Some missing values were intentionally retained for demonstration.

For example:

```text
order_amount
```

was intentionally left unchanged to demonstrate how an ETL pipeline can preserve fields when a business rule requires it.

---

## 3. Standardize Column Names

Column names were standardized to a consistent format.

Example:

```text
Company ID
company-id
Company_ID
```

can be standardized to:

```text
company_id
```

The final dataset contained:

```text
127 standardized columns
```

---

## 4. Clean String Values

String columns were cleaned by:

* Removing unnecessary whitespace
* Standardizing capitalization
* Standardizing industry values
* Standardizing country values
* Cleaning text fields

For example:

```text
Energy
energy
ENERGY
```

were standardized to:

```text
energy
```

The resulting industry values were:

```text
agriculture
food & beverage
energy
finance
pharmaceuticals
```

---

## 5. Convert Data Types

Incorrect or inconsistent data types were converted.

Important fields were converted to:

```text
company_id              Int64
number_of_employees     Int64
contact_id              Int64
deal_id                 Int64
quantity                Int64

amount                  float64
unit_price              float64
order_amount            float64
discount                float64

is_active               boolean

close_date              datetime
order_date              datetime
created_date            datetime
updated_date            datetime
```

---

## 6. Validate Invalid Records

The generated dataset intentionally contained invalid values.

Examples included:

* Negative employee counts
* Negative quantities
* Invalid order amounts

Validation identified:

```text
Invalid employee counts : 957
Invalid quantities      : 1,036
Invalid unit prices     : 0
Invalid amounts         : 0
Invalid order amounts   : 1,039
Invalid discounts       : 0

Total invalid records   : 2,999
```

This demonstrated how an ETL pipeline can identify bad records.

---

# Load

The cleaned Pandas DataFrame was saved into two formats.

## CSV

```text
processed_dataset.csv
```

## Parquet

```text
processed_dataset.parquet
```

Parquet is especially useful in Data Engineering because it is a columnar storage format and is generally much more efficient than CSV for analytical workloads.

---

# Task 3 — Data Normalization

## Objective

Separate the large denormalized dataset into logical entities.

The original dataset contained information belonging to multiple entities.

For example:

```text
company_id
company_name
contact_id
first_name
last_name
deal_id
deal_name
product_name
customer_name
city
country
order_amount
```

Instead of keeping everything in one large table, the data was separated into logical datasets.

---

# Normalized Entities

The following datasets were created.

## Companies

```text
Companies: 5 rows
```

File:

```text
companies.csv
```

---

## Contacts

```text
Contacts: 5 rows
```

File:

```text
contacts.csv
```

---

## Deals

```text
Deals: 5 rows
```

File:

```text
deals.csv
```

---

## Products

```text
Products: 9 rows
```

File:

```text
products.csv
```

---

## Cities

```text
Cities: 21 rows
```

File:

```text
cities.csv
```

---

## Customers

```text
Customers: 440 rows
```

File:

```text
customers.csv
```

---

## Orders

```text
Orders: 99,990 rows
```

File:

```text
orders.csv
```

---

# Why Normalize Data?

Normalization reduces:

* Duplicate information
* Storage requirements
* Data inconsistency
* Update problems

For example, instead of storing:

```text
Pakistan
Pakistan
Pakistan
Pakistan
Pakistan
```

inside every order record, we can have:

```text
cities
```

and reference the city/country using an ID.

Conceptually:

```text
Customers
    |
    | customer_id
    ↓
Orders
    |
    | product_id
    ↓
Products
```

This creates cleaner relationships between datasets.

---

# Task 4 — PySpark ETL

## Objective

Perform the same ETL process using PySpark and Azure Databricks.

The PySpark pipeline was executed using:

* Azure Databricks
* Azure Data Lake Storage Gen2
* PySpark
* Spark DataFrames

---

# Azure Architecture

The simplified architecture is:

```text
                    Azure
                      |
          +-----------+-----------+
          |                       |
          ▼                       ▼
      ADLS Gen2              Databricks
          |                       |
          |                       ▼
          |                    PySpark
          |                       |
          +----------->-----------+
                      |
                      ▼
                  ETL Process
                      |
                      ▼
                    Parquet
```

---

# ADLS Gen2

The storage account used for the project:

```text
storageaccountdatael
```

The data lake container:

```text
data
```

The project used the following logical layers:

```text
bronze
   ↓
silver
   ↓
gold
```

Conceptually:

```text
Bronze
Raw data
   ↓
Silver
Cleaned/transformed data
   ↓
Gold
Final business-ready data
```

---

# PySpark ETL Steps

## 1. Read CSV

The raw CSV was loaded into a Spark DataFrame.

```text
ADLS Gen2
    ↓
CSV
    ↓
Spark DataFrame
```

Dataset:

```text
100,000 rows
127 columns
```

---

## 2. Inspect Schema

The Spark schema was inspected using:

```python
df.printSchema()
```

This allowed us to verify:

* Integer fields
* Floating-point fields
* Boolean fields
* String fields
* Date fields

---

## 3. Handle Null Values

Null values were identified and handled using Spark functions such as:

```python
fillna()
```

and:

```python
isNull()
isNotNull()
```

---

## 4. Remove Duplicates

Duplicate records were removed using:

```python
dropDuplicates()
```

---

## 5. Transform Columns

String fields were cleaned using functions such as:

```python
trim()
lower()
initcap()
```

Date fields were converted using:

```python
to_date()
```

Numeric columns were transformed and validated where required.

---

## 6. Filter Records

Invalid records were filtered using Spark expressions.

For example:

```python
df.filter(
    (F.col("quantity") >= 0) &
    (F.col("amount") >= 0)
)
```

---

## 7. Normalize Data

The PySpark pipeline created logical entities:

```text
Companies
Contacts
Deals
Products
Cities
Customers
Orders
```

The result of the PySpark normalization was:

```text
Companies : 5
Contacts  : 5
Deals     : 5
Products  : 9
Cities    : 57
Customers : 21,740
Orders    : 87,321
```

The differences in row counts compared with the Pandas normalization are due to the different filtering/cleaning rules applied during the PySpark pipeline.

---

## 8. Join Related Datasets

The normalized datasets were joined using keys.

Conceptually:

```text
Companies
     |
     | company_id
     ↓
Contacts
     |
     | customer_id
     ↓
Orders
     |
     | product_id
     ↓
Products
```

This demonstrates how Spark can combine related datasets.

---

## 9. Write Final Data as Parquet

The final PySpark dataset was written to ADLS Gen2 in Parquet format.

Conceptually:

```text
PySpark DataFrame
       ↓
Parquet
       ↓
ADLS Gen2
       ↓
gold/final_orders
```

Task 4 was completed successfully.

---

# Task 5 — Pandas vs PySpark Comparison

## Objective

Run comparable workloads using Pandas and PySpark and compare their performance.

The dataset used was:

```text
100,000 rows
127 columns
```

---

## Comparison

| Metric               |            Pandas |                             PySpark |
| -------------------- | ----------------: | ----------------------------------: |
| Dataset size         |     100,000 × 127 |                       100,000 × 127 |
| Loading time         |         ~1.69 sec |              Measured in Databricks |
| Transformation time  |  Measured locally |              Measured in Databricks |
| Total execution time |  Measured locally |              Measured in Databricks |
| Memory usage         |          ~82.9 MB | Distributed Spark/Databricks memory |
| Ease of development  |            Easier |                        More complex |
| Processing model     |    Single machine |                         Distributed |
| Best use case        | Small/medium data |                    Large-scale data |

> **Important:** PySpark performance should be recorded from the actual Databricks benchmark rather than using theoretical numbers.

---

# Pandas Performance Observation

The Pandas run showed:

```text
Rows    : 100,000
Columns : 127
Memory  : approximately 82.9 MB
Loading : approximately 1.69 seconds
```

For this dataset size, Pandas is very practical because the dataset comfortably fits into memory.

---

# PySpark Performance Observation

PySpark was executed in Azure Databricks.

The important difference is that Spark is designed for distributed processing.

For a dataset of only 100,000 rows, Spark may not necessarily be faster than Pandas because Spark has additional overhead:

```text
Spark startup
     ↓
Task scheduling
     ↓
Partition management
     ↓
Execution
```

Therefore, **PySpark is not automatically faster for every dataset**.

Its major advantage is scalability.

---

# Task 6 — Understanding

## 1. What is Pandas?

Pandas is an open-source Python library for manipulating and analyzing structured/tabular data.

Its primary data structure is the DataFrame.

Example:

```python
import pandas as pd

df = pd.read_csv("orders.csv")

print(df.head())
```

Pandas is commonly used for:

* Data cleaning
* Data analysis
* CSV processing
* Data transformation
* Exploratory Data Analysis
* Small and medium ETL workloads

Pandas normally processes data on a single machine.

---

# 2. What is PySpark?

PySpark is the Python API for Apache Spark.

Apache Spark is a distributed data processing engine designed for processing large datasets.

PySpark allows Python developers to use Spark's distributed processing capabilities.

Typical architecture:

```text
Driver
   |
   +---- Executor
   |
   +---- Executor
   |
   +---- Executor
```

Executors process data partitions in parallel.

---

# 3. Difference Between Pandas DataFrame and Spark DataFrame

| Feature     | Pandas DataFrame   | Spark DataFrame   |
| ----------- | ------------------ | ----------------- |
| Processing  | Single machine     | Distributed       |
| Execution   | Mostly eager       | Lazy              |
| Memory      | Local machine      | Cluster resources |
| Scale       | Small/medium       | Large             |
| Parallelism | Local              | Distributed       |
| API         | Python             | PySpark           |
| Development | Easier             | More complex      |
| Best use    | Analysis/local ETL | Big Data ETL      |

A simple analogy:

```text
Pandas:
One person processes 100 boxes.

PySpark:
Many people process the boxes simultaneously.
```

For a small number of boxes, one person may be simpler.

For millions of boxes, many people working together are more practical.

---

# 4. Why is Pandas suitable for smaller datasets?

Pandas is suitable when the dataset can comfortably fit into the memory of a single machine.

Advantages include:

* Simple API
* Fast development
* Easy debugging
* Excellent data exploration
* Large ecosystem
* Easy integration with Python libraries

For example:

```python
df.head()
df.describe()
df.groupby()
df.sort_values()
df.fillna()
```

are very easy to use.

---

# 5. Why is PySpark suitable for large datasets?

PySpark can distribute data and computation across multiple machines.

For example:

```text
1 TB dataset

        ↓

Partitioned into smaller pieces

        ↓

Worker 1 → Partition 1
Worker 2 → Partition 2
Worker 3 → Partition 3
Worker 4 → Partition 4
...
```

Multiple workers can process different partitions concurrently.

This allows Spark to process datasets that would be difficult or impossible to process using a single machine.

---

# 6. How does PySpark distribute processing?

Spark divides data into **partitions**.

A Spark application generally has:

### Driver

The Driver:

* Coordinates the application
* Creates the Spark session
* Builds the execution plan
* Coordinates tasks

### Executors

Executors:

* Execute tasks
* Process partitions
* Store intermediate data
* Return results to the driver when required

Conceptually:

```text
                    Driver
                      |
               Execution Plan
                      |
        +-------------+-------------+
        |             |             |
        ▼             ▼             ▼
    Executor 1   Executor 2   Executor 3
        |             |             |
        ▼             ▼             ▼
   Partition 1   Partition 2   Partition 3
```

This is the foundation of Spark's distributed processing model.

---

# 7. What happens when data does not fit into memory?

With Pandas, if the DataFrame becomes larger than available memory, the process can fail with a `MemoryError` or experience severe performance degradation due to operating-system swapping.

Spark has a different architecture.

Spark distributes data and processing across the cluster.

Spark can also spill intermediate data to disk when memory is insufficient.

Conceptually:

```text
Data
 ↓
Memory
 ↓
Memory pressure
 ↓
Spill intermediate data to disk
 ↓
Continue processing
```

However, disk is much slower than memory.

Therefore, Spark still requires adequate cluster resources.

The important point is:

> Spark does not eliminate memory limitations. It distributes resources across multiple machines and can handle much larger workloads than a single-machine process.

---

# 8. What is Lazy Evaluation in PySpark?

Lazy evaluation means Spark does not immediately execute transformations.

For example:

```python
df2 = df.filter(df.amount > 100)
```

Spark doesn't necessarily execute the filtering immediately.

Instead, Spark builds an execution plan.

For example:

```text
Read
 ↓
Filter
 ↓
Select
 ↓
Write
```

Execution occurs when an **action** is called.

Examples:

```python
df.count()
df.show()
df.collect()
df.write.parquet(...)
```

Therefore:

```text
Transformation
      ↓
Execution Plan
      ↓
Action
      ↓
Actual Execution
```

Lazy evaluation allows Spark to optimize the execution plan before processing the data.

---

# 9. Difference Between Spark Transformations and Actions

## Transformations

Transformations define how the data should be changed.

Examples:

```python
filter()
select()
withColumn()
drop()
join()
distinct()
groupBy()
```

Example:

```python
filtered_df = df.filter(df.amount > 100)
```

This creates a new DataFrame and contributes to Spark's execution plan.

---

## Actions

Actions trigger execution and produce a result or output.

Examples:

```python
count()
show()
collect()
first()
write.parquet()
write.csv()
```

Example:

```python
filtered_df.count()
```

The action causes Spark to execute the required transformations.

### Easy way to remember

```text
Transformation = What should Spark do?

Action = Execute the work.
```

---

# 10. When Would You Choose Pandas Over PySpark?

I would choose Pandas when:

### Dataset fits comfortably into memory

For example:

```text
500 MB dataset
32 GB RAM
```

assuming the actual DataFrame memory requirements are comfortably within available resources.

### Quick development is important

Pandas has a very simple API:

```python
df.drop_duplicates()
df.fillna()
df.groupby()
df.sort_values()
```

### Exploratory Data Analysis is required

Pandas is excellent for:

```python
df.head()
df.info()
df.describe()
```

### Local ETL is sufficient

If a business receives a relatively small daily CSV file, introducing a Spark cluster may add unnecessary complexity and cost.

### Machine Learning preprocessing

Pandas is frequently useful for preparing datasets for machine learning when the data fits comfortably into memory.

---

# Pandas vs PySpark — Real-World Decision

The choice should not simply be:

```text
Pandas = Small
PySpark = Large
```

The actual decision depends on:

* Dataset size
* Available memory
* Number of records
* Processing complexity
* Processing frequency
* Number of machines
* Infrastructure
* Cost
* Development complexity
* Performance requirements

A simple decision process:

```text
                 Dataset / Workload
                         |
              +----------+----------+
              |                     |
          Fits easily           Very large
          on one machine        / distributed
              |                     |
              ▼                     ▼
           Pandas                PySpark
```

---

# Key Learnings

## 1. Generators

Generators allow records to be produced one at a time rather than storing the entire dataset in memory.

```python
yield record
```

This is useful when generating or processing large streams of data.

---

## 2. Pandas

Pandas is simple and powerful for local data processing.

Best suited for:

```text
Small → Medium datasets
Single machine
Quick analysis
Local ETL
Exploration
```

---

## 3. PySpark

PySpark provides distributed data processing.

Best suited for:

```text
Large datasets
Data Lakes
Distributed ETL
Cloud data processing
Large-scale transformations
```

---

## 4. Parquet

Parquet is a columnar storage format commonly used in modern Data Engineering pipelines.

Compared with CSV, Parquet provides advantages such as:

* Columnar storage
* Compression
* Efficient analytical queries
* Schema information
* Better integration with Spark and data lakes

---

## 5. Azure Data Lake Storage

ADLS Gen2 provides scalable cloud storage for Data Engineering workloads.

Our pipeline used:

```text
ADLS Gen2
    ↓
Bronze
    ↓
Silver
    ↓
Gold
```

---

## 6. Databricks

Azure Databricks provides a managed environment for running Apache Spark workloads.

It was used in this project to execute PySpark ETL against data stored in ADLS Gen2.

---

# Final ETL Architecture

The completed project can be represented as:

```text
                     PYTHON
                       │
                       ▼
                Python Generator
                       │
                       ▼
              100,000 × 127 Dataset
                       │
                       ▼
                     CSV
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
       PANDAS                  ADLS GEN2
          │                         │
          ▼                         ▼
      Extract                  Databricks
          │                         │
          ▼                         ▼
      Transform                  PySpark
          │                         │
          ▼                         ▼
      Normalize                 Transform
          │                         │
          ▼                         ▼
       Parquet                  Normalize
          │                         │
          │                         ▼
          │                       Join
          │                         │
          │                         ▼
          │                      Parquet
          │                         │
          └────────────┬────────────┘
                       ▼
                PERFORMANCE
                 COMPARISON
                       │
                       ▼
              PANDAS vs PYSPARK
```

---

# Final Results

## Data Generation

```text
Rows generated : 100,000
Columns        : 127
```

## Pandas

```text
Rows loaded    : 100,000
Columns loaded : 127
Memory usage   : approximately 82.9 MB
Loading time   : approximately 1.69 seconds
Rows after cleaning: 99,990
```

## Pandas Normalization

```text
Companies : 5
Contacts  : 5
Deals     : 5
Products  : 9
Cities    : 21
Customers : 440
Orders    : 99,990
```

## PySpark Normalization

```text
Companies : 5
Contacts  : 5
Deals     : 5
Products  : 9
Cities    : 57
Customers : 21,740
Orders    : 87,321
```

The different PySpark normalized row counts demonstrate that the transformation/filtering logic applied during the PySpark pipeline can affect the resulting entities and records. In a production pipeline, these differences would need to be investigated and reconciled with clearly defined business rules.

---

# What This Project Demonstrates

By completing this project, we demonstrated the following Data Engineering concepts:

```text
Python
  ↓
Generators
  ↓
Large Dataset Generation
  ↓
CSV
  ↓
Pandas ETL
  ↓
Data Cleaning
  ↓
Data Validation
  ↓
Normalization
  ↓
Parquet
  ↓
Azure Data Lake Storage
  ↓
Azure Databricks
  ↓
PySpark ETL
  ↓
Distributed Processing
  ↓
Joins
  ↓
Parquet
  ↓
Performance Comparison
```

The main lesson is not simply that one technology is faster than another.

The key lesson is:

> **Use the simplest technology that can reliably handle the workload.**

For data that comfortably fits on one machine, Pandas can provide excellent performance and developer productivity.

For very large datasets requiring distributed processing, cloud-scale ETL, or cluster-based computation, PySpark becomes a much more appropriate choice.

---

# Interview Summary

If asked:

### "Why did you use Pandas?"

> I used Pandas for local ETL because the dataset was small enough to fit comfortably into memory. Pandas provided a simple API for cleaning, transforming, validating, and normalizing the data.

### "Why did you use PySpark?"

> I used PySpark to demonstrate distributed ETL and understand how the same workload can be processed using Spark. PySpark is more appropriate when datasets become too large for a single machine or when distributed processing is required.

### "Was PySpark faster for your 100,000-row dataset?"

> Not necessarily. For a relatively small dataset, Spark has cluster and execution overhead. The real advantage of Spark appears when the workload becomes large enough to benefit from distributed processing.

### "What did you learn?"

> I learned the complete ETL flow from generating large datasets with Python generators through Pandas and PySpark transformations, normalization, Azure Data Lake Storage, Databricks, Parquet, and performance comparison. More importantly, I learned how to decide between single-machine processing with Pandas and distributed processing with PySpark based on workload requirements.

---

# Conclusion

This project provided hands-on experience with a complete Data Engineering ETL workflow.

The project demonstrated:

* Python generators for memory-efficient data generation
* Pandas for local ETL
* Data cleaning and validation
* Data normalization
* PySpark for distributed ETL
* Azure Data Lake Storage Gen2
* Azure Databricks
* Spark transformations and actions
* Lazy evaluation
* Parquet-based data storage
* Pandas vs PySpark comparison

The key architectural decision is based on **data volume, memory requirements, scalability, infrastructure, cost, and development complexity**, rather than simply choosing one technology over another.
