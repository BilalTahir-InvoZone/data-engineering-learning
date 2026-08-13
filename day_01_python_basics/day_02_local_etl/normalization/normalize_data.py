"""
Task 3 - Data Normalization

This script takes the cleaned dataset produced by the Pandas ETL
pipeline and separates it into logical entities.

Input:
    processed_dataset.csv

Output:
    companies.csv
    contacts.csv
    deals.csv
    products.csv
    cities.csv
    customers.csv
    orders.csv
"""

from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT DIRECTORIES
# ============================================================

# Directory containing this Python file
BASE_DIR = Path(__file__).resolve().parent

# day_02_local_etl
ETL_DIR = BASE_DIR.parent

# Input produced by Task 2
INPUT_FILE = (
    ETL_DIR
    / "output"
    / "processed_dataset.csv"
)

# Output directory for normalized datasets
OUTPUT_DIR = (
    BASE_DIR
    / "output"
)


# ============================================================
# EXTRACT
# ============================================================

def load_data():
    """
    Load the cleaned dataset produced by Task 2.
    """

    print("=" * 70)
    print("TASK 3 - DATA NORMALIZATION")
    print("=" * 70)

    print()
    print("Loading processed dataset...")
    print(f"Input file: {INPUT_FILE}")
    print()

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    df = pd.read_csv(
        INPUT_FILE
    )

    print("Dataset loaded successfully.")
    print(f"Rows    : {len(df):,}")
    print(f"Columns : {len(df.columns):,}")
    print()

    return df


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

def create_output_directory():
    """
    Create the normalization output directory if it doesn't exist.
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# NORMALIZE COMPANIES
# ============================================================

def create_companies(df):
    """
    Create the companies entity.

    A company should appear only once in the companies dataset.
    """

    print("=" * 70)
    print("NORMALIZING COMPANIES")
    print("=" * 70)

    company_columns = [
        "company_id",
        "company_name",
        "company_domain",
        "industry",
        "number_of_employees"
    ]

    companies = (
        df[company_columns]
        .drop_duplicates(
            subset=["company_id"]
        )
        .sort_values(
            "company_id"
        )
        .reset_index(
            drop=True
        )
    )

    print(f"Companies created: {len(companies):,}")
    print()

    return companies


# ============================================================
# NORMALIZE CONTACTS
# ============================================================

def create_contacts(df):
    """
    Create the contacts entity.

    Each contact is associated with a company using company_id.
    """

    print("=" * 70)
    print("NORMALIZING CONTACTS")
    print("=" * 70)

    contact_columns = [
        "contact_id",
        "company_id",
        "first_name",
        "last_name",
        "email"
    ]

    contacts = (
        df[contact_columns]
        .drop_duplicates(
            subset=["contact_id"]
        )
        .sort_values(
            "contact_id"
        )
        .reset_index(
            drop=True
        )
    )

    print(f"Contacts created: {len(contacts):,}")
    print()

    return contacts


# ============================================================
# NORMALIZE DEALS
# ============================================================

def create_deals(df):
    """
    Create the deals entity.

    Each deal belongs to a company and can be associated
    with a contact.
    """

    print("=" * 70)
    print("NORMALIZING DEALS")
    print("=" * 70)

    deal_columns = [
        "deal_id",
        "company_id",
        "contact_id",
        "deal_name",
        "amount",
        "status",
        "close_date"
    ]

    deals = (
        df[deal_columns]
        .drop_duplicates(
            subset=["deal_id"]
        )
        .sort_values(
            "deal_id"
        )
        .reset_index(
            drop=True
        )
    )

    print(f"Deals created: {len(deals):,}")
    print()

    return deals


# ============================================================
# NORMALIZE PRODUCTS
# ============================================================

def create_products(df):
    """
    Create the products entity.

    Our source data doesn't contain product_id.

    Therefore, we create a surrogate product_id based on
    the unique product names.
    """

    print("=" * 70)
    print("NORMALIZING PRODUCTS")
    print("=" * 70)

    products = (
        df[
            [
                "product_name",
                "unit_price"
            ]
        ]
        .drop_duplicates(
            subset=["product_name"]
        )
        .reset_index(
            drop=True
        )
    )

    # Generate surrogate product IDs.
    products.insert(
        0,
        "product_id",
        range(
            1,
            len(products) + 1
        )
    )

    print(f"Products created: {len(products):,}")
    print()

    return products


# ============================================================
# NORMALIZE CITIES
# ============================================================

def create_cities(df):
    """
    Create the cities/location entity.

    A city is logically associated with a country.
    """

    print("=" * 70)
    print("NORMALIZING CITIES")
    print("=" * 70)

    cities = (
        df[
            [
                "city",
                "country"
            ]
        ]
        .drop_duplicates()
        .reset_index(
            drop=True
        )
    )

    # Generate surrogate city IDs.
    cities.insert(
        0,
        "city_id",
        range(
            1,
            len(cities) + 1
        )
    )

    print(f"Cities created: {len(cities):,}")
    print()

    return cities


# ============================================================
# NORMALIZE CUSTOMERS
# ============================================================

def create_customers(df, cities):
    """
    Create the customers entity.

    Customers are linked to cities through city_id.
    """

    print("=" * 70)
    print("NORMALIZING CUSTOMERS")
    print("=" * 70)

    customers = (
        df[
            [
                "customer_name",
                "generated_email",
                "city",
                "country"
            ]
        ]
        .drop_duplicates(
            subset=[
                "customer_name",
                "generated_email"
            ]
        )
        .reset_index(
            drop=True
        )
    )

    # Join the city_id from the cities entity.
    customers = customers.merge(
        cities,
        on=[
            "city",
            "country"
        ],
        how="left"
    )

    # Remove city and country because city_id now
    # maintains the relationship.
    customers = customers[
        [
            "customer_name",
            "generated_email",
            "city_id"
        ]
    ]

    # Generate surrogate customer IDs.
    customers.insert(
        0,
        "customer_id",
        range(
            1,
            len(customers) + 1
        )
    )

    print(f"Customers created: {len(customers):,}")
    print()

    return customers


# ============================================================
# NORMALIZE ORDERS
# ============================================================

def create_orders(df, customers, products):
    """
    Create the orders/fact entity.

    Orders reference:

        customer_id
        product_id

    instead of storing the full customer and product
    information repeatedly.
    """

    print("=" * 70)
    print("NORMALIZING ORDERS")
    print("=" * 70)

    orders = df[
        [
            "customer_name",
            "generated_email",
            "product_name",
            "quantity",
            "order_amount",
            "discount",
            "order_date"
        ]
    ].copy()

    # --------------------------------------------------------
    # Add customer_id
    # --------------------------------------------------------

    orders = orders.merge(
        customers[
            [
                "customer_id",
                "customer_name",
                "generated_email"
            ]
        ],
        on=[
            "customer_name",
            "generated_email"
        ],
        how="left"
    )

    # --------------------------------------------------------
    # Add product_id
    # --------------------------------------------------------

    orders = orders.merge(
        products[
            [
                "product_id",
                "product_name"
            ]
        ],
        on="product_name",
        how="left"
    )

    # --------------------------------------------------------
    # Create order_id
    # --------------------------------------------------------

    orders.insert(
        0,
        "order_id",
        range(
            1,
            len(orders) + 1
        )
    )

    # --------------------------------------------------------
    # Keep only relationship IDs and order attributes
    # --------------------------------------------------------

    orders = orders[
        [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "order_amount",
            "discount",
            "order_date"
        ]
    ]

    print(f"Orders created: {len(orders):,}")
    print()

    return orders


# ============================================================
# SAVE DATASETS
# ============================================================

def save_dataset(df, filename):
    """
    Save a normalized dataset as CSV.
    """

    output_file = (
        OUTPUT_DIR
        / filename
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Saved: {output_file}"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # LOAD
    # --------------------------------------------------------

    df = load_data()

    # --------------------------------------------------------
    # CREATE OUTPUT DIRECTORY
    # --------------------------------------------------------

    create_output_directory()

    # --------------------------------------------------------
    # NORMALIZE ENTITIES
    # --------------------------------------------------------

    companies = create_companies(
        df
    )

    contacts = create_contacts(
        df
    )

    deals = create_deals(
        df
    )

    products = create_products(
        df
    )

    cities = create_cities(
        df
    )

    customers = create_customers(
        df,
        cities
    )

    orders = create_orders(
        df,
        customers,
        products
    )

    # --------------------------------------------------------
    # SAVE DATASETS
    # --------------------------------------------------------

    print("=" * 70)
    print("SAVING NORMALIZED DATASETS")
    print("=" * 70)

    save_dataset(
        companies,
        "companies.csv"
    )

    save_dataset(
        contacts,
        "contacts.csv"
    )

    save_dataset(
        deals,
        "deals.csv"
    )

    save_dataset(
        products,
        "products.csv"
    )

    save_dataset(
        cities,
        "cities.csv"
    )

    save_dataset(
        customers,
        "customers.csv"
    )

    save_dataset(
        orders,
        "orders.csv"
    )

    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    print()
    print("=" * 70)
    print("NORMALIZATION COMPLETED")
    print("=" * 70)

    print()
    print("Normalized datasets:")
    print()

    print(
        f"Companies : {len(companies):,} rows"
    )

    print(
        f"Contacts  : {len(contacts):,} rows"
    )

    print(
        f"Deals     : {len(deals):,} rows"
    )

    print(
        f"Products  : {len(products):,} rows"
    )

    print(
        f"Cities    : {len(cities):,} rows"
    )

    print(
        f"Customers : {len(customers):,} rows"
    )

    print(
        f"Orders    : {len(orders):,} rows"
    )

    print()
    print(f"Output directory: {OUTPUT_DIR}")
    print()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()