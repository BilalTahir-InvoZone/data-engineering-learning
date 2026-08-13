# ============================================================
# TASK 1 - GENERATE LARGE TEST DATA
# ============================================================
#
# Local ETL Pipeline - Pandas vs PySpark
#
# Objective:
# Generate a large CSV dataset using a Python generator.
#
# We are using the sample CSV files supplied with the task:
#
#   input/
#       companies.csv
#       contacts.csv
#       deals.csv
#       line_items_sample.csv
#
# These files contain realistic CRM / sales data.
#
# We use them as reference/source data to generate a much
# larger synthetic dataset.
#
# Requirements:
#
#   - At least 100 columns
#   - At least 100,000 rows
#   - Integer values
#   - Float values
#   - String values
#   - Boolean values
#   - Date values
#   - Missing values
#   - Duplicate records
#   - Inconsistent string values
#
# IMPORTANT:
#
# We use a Python GENERATOR.
#
# We do NOT create a list containing 100,000 records.
#
# Instead:
#
#       Generator
#           |
#           +--> Record 1 --> CSV
#           |
#           +--> Record 2 --> CSV
#           |
#           +--> Record 3 --> CSV
#           |
#           +--> ...
#
# This keeps memory usage low.
#
# ============================================================


import csv
import os
import random
from datetime import datetime, timedelta


# ============================================================
# CONFIGURATION
# ============================================================

# Number of records to generate.
TOTAL_ROWS = 100_000

# Number of additional columns.
#
# The business columns + these columns will give us
# more than 100 columns.
ADDITIONAL_COLUMNS = 100

from pathlib import Path

# Project directories

SCRIPT_DIR = Path(__file__).resolve().parent
ETL_DIR = SCRIPT_DIR.parent

INPUT_DIR = ETL_DIR / "input"
OUTPUT_DIR = SCRIPT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "large_dataset.csv"

# ============================================================
# RANDOM SEED
# ============================================================

# Using a fixed seed makes our generated dataset
# reproducible.
#
# If we run the script again, we get the same
# random data pattern.

random.seed(42)


# ============================================================
# HELPER - READ CSV
# ============================================================

def read_csv_file(file_path):
    """
    Read a CSV file and return its rows.

    We only have a few source rows in the supplied
    sample files, so loading these small files into
    memory is completely fine.

    The LARGE generated dataset is handled using
    a generator.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        return list(reader)


# ============================================================
# LOAD SUPPLIED SOURCE DATA
# ============================================================

def load_source_data():
    """
    Load the four CSV files supplied with the task.
    """

    companies_file = os.path.join(
        INPUT_DIR,
        "companies.csv"
    )

    contacts_file = os.path.join(
        INPUT_DIR,
        "contacts.csv"
    )

    deals_file = os.path.join(
        INPUT_DIR,
        "deals.csv"
    )

    line_items_file = os.path.join(
        INPUT_DIR,
        "line_items_sample.csv"
    )


    print("Loading supplied source files...")


    companies = read_csv_file(
        companies_file
    )

    contacts = read_csv_file(
        contacts_file
    )

    deals = read_csv_file(
        deals_file
    )

    line_items = read_csv_file(
        line_items_file
    )


    print(
        f"Companies loaded: {len(companies)}"
    )

    print(
        f"Contacts loaded: {len(contacts)}"
    )

    print(
        f"Deals loaded: {len(deals)}"
    )

    print(
        f"Line items loaded: {len(line_items)}"
    )

    print()


    return (
        companies,
        contacts,
        deals,
        line_items
    )


# ============================================================
# DATA CLEANING HELPERS
# ============================================================

def random_name():
    """
    Generate a customer/contact name.
    """

    first_names = [
        "Bilal",
        "Ali",
        "Ahmed",
        "Usman",
        "Hamza",
        "Hassan",
        "Omar",
        "Ayesha",
        "Natasha",
        "Bruce",
        "Kate"
    ]

    last_names = [
        "Tahir",
        "Khan",
        "Malik",
        "Ahmed",
        "Shah",
        "Wayne",
        "Lang",
        "Potts",
        "Smith",
        "Johnson"
    ]

    return (
        random.choice(first_names)
        + " "
        + random.choice(last_names)
    )


# ------------------------------------------------------------


def random_email(name):
    """
    Generate an email address from a name.
    """

    email_name = (
        name.lower()
        .replace(" ", ".")
    )

    domains = [
        "example.com",
        "company.com",
        "business.com",
        "enterprise.com"
    ]

    return (
        email_name
        + "@"
        + random.choice(domains)
    )


# ------------------------------------------------------------


def make_inconsistent_string(value):
    """
    Intentionally create inconsistent string values.

    Examples:

        Lahore
        lahore
        LAHORE
         Lahore
        Lahore

    These inconsistencies will be cleaned during
    the Pandas ETL task.
    """

    if value is None:
        return None


    variation = random.randint(
        1,
        5
    )


    if variation == 1:

        return value.lower()


    elif variation == 2:

        return value.upper()


    elif variation == 3:

        return " " + value


    elif variation == 4:

        return value + " "


    else:

        return value


# ------------------------------------------------------------


def random_date():
    """
    Generate a random date between 2021 and 2025.
    """

    start_date = datetime(
        2021,
        1,
        1
    )


    random_days = random.randint(
        0,
        1825
    )


    result = (
        start_date
        + timedelta(days=random_days)
    )


    return result.strftime(
        "%Y-%m-%d"
    )


# ------------------------------------------------------------


def random_float():
    """
    Generate a floating-point value.
    """

    return round(
        random.uniform(
            10,
            100_000
        ),
        2
    )


# ------------------------------------------------------------


def random_boolean():
    """
    Generate a Boolean value.
    """

    return random.choice(
        [True, False]
    )


# ============================================================
# GENERATOR
# ============================================================

def generate_records(
    companies,
    contacts,
    deals,
    line_items,
    total_rows
):
    """
    Generate records ONE AT A TIME.

    This function is a GENERATOR because it uses yield.

    The important concept is:

        yield record

    instead of:

        return records

    We never create a list containing all 100,000
    generated records.
    """


    for row_number in range(
        1,
        total_rows + 1
    ):

        # ====================================================
        # SELECT SOURCE RECORDS
        # ====================================================

        company = random.choice(
            companies
        )

        contact = random.choice(
            contacts
        )

        deal = random.choice(
            deals
        )

        line_item = random.choice(
            line_items
        )


        # ====================================================
        # CREATE BUSINESS RECORD
        # ====================================================

        customer_name = random_name()


        record = {

            # ------------------------------------------------
            # Company information
            # ------------------------------------------------

            "company_id": company.get(
                "company_id"
            ),

            "company_name": company.get(
                "company_name"
            ),

            "company_domain": company.get(
                "domain"
            ),

            "industry": company.get(
                "industry"
            ),

            "number_of_employees": company.get(
                "number_of_employees"
            ),


            # ------------------------------------------------
            # Contact information
            # ------------------------------------------------

            "contact_id": contact.get(
                "contact_id"
            ),

            "first_name": contact.get(
                "first_name"
            ),

            "last_name": contact.get(
                "last_name"
            ),

            "email": contact.get(
                "email"
            ),


            # ------------------------------------------------
            # Deal information
            # ------------------------------------------------

            "deal_id": deal.get(
                "deal_id"
            ),

            "deal_name": deal.get(
                "deal_name"
            ),

            "amount": deal.get(
                "amount"
            ),

            "status": deal.get(
                "status"
            ),

            "close_date": deal.get(
                "close_date"
            ),


            # ------------------------------------------------
            # Line item information
            # ------------------------------------------------

            "product_name": line_item.get(
                "product_name"
            ),

            "quantity": line_item.get(
                "quantity"
            ),

            "unit_price": line_item.get(
                "unit_price"
            ),


            # ------------------------------------------------
            # Generated fields
            # ------------------------------------------------

            "customer_name": customer_name,

            "generated_email": random_email(
                customer_name
            ),

            "city": random.choice(
                [
                    "Lahore",
                    "Karachi",
                    "Islamabad",
                    "Rawalpindi",
                    "Peshawar",
                    "Multan"
                ]
            ),

            "country": random.choice(
                [
                    "Pakistan",
                    "Pakistan",
                    "Pakistan",
                    "UAE",
                    "Saudi Arabia"
                ]
            ),

            "order_amount": random_float(),

            "discount": round(
                random.uniform(
                    0,
                    30
                ),
                2
            ),

            "is_active": random_boolean(),

            "order_date": random_date(),

            "created_date": random_date(),

            "updated_date": random_date()
        }


        # ====================================================
        # INTRODUCE INCONSISTENT STRING VALUES
        # ====================================================

        record["city"] = make_inconsistent_string(
            record["city"]
        )


        record["country"] = make_inconsistent_string(
            record["country"]
        )


        record["industry"] = make_inconsistent_string(
            record["industry"]
        )


        record["status"] = make_inconsistent_string(
            record["status"]
        )


        record["product_name"] = make_inconsistent_string(
            record["product_name"]
        )


        # ====================================================
        # INTRODUCE MISSING VALUES
        # ====================================================

        # Around 5% of records will contain missing values.

        if random.random() < 0.05:

            record["company_name"] = ""


        if random.random() < 0.05:

            record["email"] = ""


        if random.random() < 0.05:

            record["city"] = ""


        if random.random() < 0.05:

            record["order_amount"] = ""


        if random.random() < 0.05:

            record["discount"] = ""


        # ====================================================
        # INTRODUCE INVALID DATA
        # ====================================================

        # Invalid quantity

        if random.random() < 0.01:

            record["quantity"] = -1


        # Invalid amount

        if random.random() < 0.01:

            record["order_amount"] = -500


        # Invalid employee count

        if random.random() < 0.01:

            record["number_of_employees"] = -10


        # ====================================================
        # ADD 100+ ADDITIONAL COLUMNS
        # ====================================================

        for column_number in range(
            1,
            ADDITIONAL_COLUMNS + 1
        ):

            data_type = (
                column_number % 5
            )


            # ----------------------------------------------
            # Integer
            # ----------------------------------------------

            if data_type == 0:

                value = random.randint(
                    1,
                    100_000
                )


            # ----------------------------------------------
            # Float
            # ----------------------------------------------

            elif data_type == 1:

                value = round(
                    random.uniform(
                        0,
                        100_000
                    ),
                    2
                )


            # ----------------------------------------------
            # String
            # ----------------------------------------------

            elif data_type == 2:

                value = (
                    "Value_"
                    + str(
                        random.randint(
                            1,
                            1000
                        )
                    )
                )


            # ----------------------------------------------
            # Boolean
            # ----------------------------------------------

            elif data_type == 3:

                value = random_boolean()


            # ----------------------------------------------
            # Date
            # ----------------------------------------------

            else:

                value = random_date()


            record[
                f"extra_column_{column_number}"
            ] = value


        # ====================================================
        # YIELD ONE RECORD
        # ====================================================

        yield record


# ============================================================
# COLUMN DEFINITIONS
# ============================================================

def get_columns():

    columns = [

        "company_id",
        "company_name",
        "company_domain",
        "industry",
        "number_of_employees",

        "contact_id",
        "first_name",
        "last_name",
        "email",

        "deal_id",
        "deal_name",
        "amount",
        "status",
        "close_date",

        "product_name",
        "quantity",
        "unit_price",

        "customer_name",
        "generated_email",

        "city",
        "country",

        "order_amount",
        "discount",
        "is_active",

        "order_date",
        "created_date",
        "updated_date"
    ]


    # Add additional columns.

    for column_number in range(
        1,
        ADDITIONAL_COLUMNS + 1
    ):

        columns.append(
            f"extra_column_{column_number}"
        )


    return columns


# ============================================================
# GENERATE CSV
# ============================================================

def generate_csv():

    # --------------------------------------------------------
    # Create output directory
    # --------------------------------------------------------

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )


    # --------------------------------------------------------
    # Load supplied data
    # --------------------------------------------------------

    (
        companies,
        contacts,
        deals,
        line_items
    ) = load_source_data()


    # --------------------------------------------------------
    # Get columns
    # --------------------------------------------------------

    columns = get_columns()


    print(
        "=" * 70
    )

    print(
        "TASK 1 - LARGE DATASET GENERATION"
    )

    print(
        "=" * 70
    )

    print(
        f"Target rows   : {TOTAL_ROWS:,}"
    )

    print(
        f"Total columns : {len(columns)}"
    )

    print(
        f"Output file   : {OUTPUT_FILE}"
    )

    print()


    # --------------------------------------------------------
    # Create generator
    # --------------------------------------------------------

    records = generate_records(
        companies,
        contacts,
        deals,
        line_items,
        TOTAL_ROWS
    )


    # --------------------------------------------------------
    # Write CSV
    # --------------------------------------------------------

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=columns
        )


        # Write header.

        writer.writeheader()


        previous_record = None


        # ----------------------------------------------------
        # Consume generator
        # ----------------------------------------------------

        for row_number, record in enumerate(
            records,
            start=1
        ):

            # ----------------------------------------------
            # Introduce duplicate records
            # ----------------------------------------------
            #
            # Every 10,000th record we write the previous
            # record instead of the new record.
            #
            # This gives us duplicate records that we will
            # later remove during ETL.
            #

            if (
                row_number % 10_000 == 0
                and previous_record is not None
            ):

                writer.writerow(
                    previous_record
                )

                print(
                    f"Added duplicate around row "
                    f"{row_number:,}"
                )


            else:

                writer.writerow(
                    record
                )


            previous_record = record


            # ----------------------------------------------
            # Progress
            # ----------------------------------------------

            if row_number % 10_000 == 0:

                print(
                    f"Generated "
                    f"{row_number:,} records..."
                )


    # --------------------------------------------------------
    # Final information
    # --------------------------------------------------------

    print()

    print(
        "=" * 70
    )

    print(
        "DATA GENERATION COMPLETED"
    )

    print(
        "=" * 70
    )

    print(
        f"Rows generated : {TOTAL_ROWS:,}"
    )

    print(
        f"Columns        : {len(columns)}"
    )

    print(
        "Duplicates      : Added intentionally"
    )

    print(
        "Missing values  : Added intentionally"
    )

    print(
        "Invalid values  : Added intentionally"
    )

    print(
        "Dirty strings   : Added intentionally"
    )

    print()

    print(
        "Generated file:"
    )

    print(
        os.path.abspath(
            OUTPUT_FILE
        )
    )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    generate_csv()