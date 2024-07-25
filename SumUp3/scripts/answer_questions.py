import pandas as pd
from sqlalchemy import create_engine

def answer_questions():
    engine = create_engine('sqlite:////app/data/database.db')

    # Top 10 stores per transacted amount
    top_10_stores = pd.read_sql_query('''
        SELECT s.name as store_name, SUM(t.amount) as total_amount
        FROM transactions t
        JOIN devices d ON t.device_id = d.id
        JOIN stores s ON d.store_id = s.id
        WHERE t.status = 'accepted'
        GROUP BY s.name
        ORDER BY total_amount DESC
        LIMIT 10
    ''', con=engine)
    print("Top 10 Stores by Transacted Amount:\n", top_10_stores)

    # Top 10 products sold
    top_10_products = pd.read_sql_query('''
        SELECT product_name, COUNT(*) as total_sold
        FROM transactions
        WHERE status = 'accepted'
        GROUP BY product_name
        ORDER BY total_sold DESC
        LIMIT 10
    ''', con=engine)
    print("Top 10 Products Sold:\n", top_10_products)

    # Average transacted amount per store typology and country
    avg_amount_typology_country = pd.read_sql_query('''
        SELECT s.typology, s.country, AVG(t.amount) as avg_amount
        FROM transactions t
        JOIN devices d ON t.device_id = d.id
        JOIN stores s ON d.store_id = s.id
        WHERE t.status = 'accepted'
        GROUP BY s.typology, s.country
    ''', con=engine)
    print("Average Transacted Amount per Store Typology and Country:\n", avg_amount_typology_country)

    # Percentage of transactions per device type
    pct_transactions_device_type = pd.read_sql_query('''
        SELECT d.type, COUNT(t.id) * 100.0 / (SELECT COUNT(*) FROM transactions WHERE status = 'accepted') as percentage
        FROM transactions t
        JOIN devices d ON t.device_id = d.id
        WHERE t.status = 'accepted'
        GROUP BY d.type
    ''', con=engine)
    print("Percentage of Transactions per Device Type:\n", pct_transactions_device_type)

    # Average time for a store to perform its 5 first transactions
    avg_time_first_5_transactions = pd.read_sql_query('''
        WITH ranked_transactions AS (
            SELECT t.*, 
                d.store_id, 
                ROW_NUMBER() OVER (PARTITION BY d.store_id ORDER BY t.happened_at) as rn
            FROM transactions t
            JOIN devices d ON t.device_id = d.id
            WHERE t.status = 'accepted'
        ),
        first_fifth_transactions AS (
            SELECT store_id, 
                MIN(CASE WHEN rn = 1 THEN happened_at END) as first_transaction,
                MAX(CASE WHEN rn = 5 THEN happened_at END) as fifth_transaction,
                COUNT(*) as trans_count
            FROM ranked_transactions
            GROUP BY store_id
        )
        SELECT store_id, AVG(julianday(fifth_transaction) - julianday(first_transaction)) as avg_time_days
        FROM first_fifth_transactions
        WHERE trans_count >= 5
    ''', con=engine)

    print("Average Time for First 5 Transactions per Store in Days:\n", avg_time_first_5_transactions)

