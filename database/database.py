import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)

def create_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    url TEXT NOT NULL UNIQUE
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS price_history (
                    id SERIAL PRIMARY KEY,
                    product_id INT REFERENCES products(product_id),
                    price NUMERIC NOT NULL,
                    date_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
        print("✅ Tables created!")
    
def insert_product(name, url):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO products (name, url)
                VALUES (%s, %s)
                ON CONFLICT (url) DO NOTHING
                RETURNING product_id;
            """, (name, url))
            result = cur.fetchone()
            return result['product_id'] if result else None

def insert_price(product_id, price):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO price_history (product_id, price)
                VALUES (%s, %s);
            """, (product_id, price))

def get_price_history(product_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT price, date_checked
                FROM price_history
                WHERE product_id = %s
                ORDER BY date_checked;
            """, (product_id,))
            return cur.fetchall()



# OPTIONAL: Run this if you call python database/database.py directly
if __name__ == "__main__":
    create_tables()
    
    # Test insert
    pid = insert_product("iPhone 15 Pro", "https://example.com/iphone15pro")
    if pid:
        insert_price(pid, 999.99)
        print("✅ Inserted product + price")

    # Fetch and print history
    history = get_price_history(pid)
    print("📈 Price History:", history)

