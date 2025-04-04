import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime, timedelta

# ✅ Force load .env from the exact absolute path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ENV_PATH = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")
print("🔗 Using DATABASE_URL:", DATABASE_URL)


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


def get_all_products():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT product_id, name, url
                FROM products
                ORDER BY name;
            """)
            return cur.fetchall()


# 🧪 Test block: ONLY runs if you run this file directly
if __name__ == "__main__":
    create_tables()

    pid = insert_product(
        "Oppo Reno 13F 4g-Graphite Grey-256GB - 8GB RAM",
        "https://example.com/oppo13f"
    )

    if pid:
        now = datetime.now()
        for i, price in enumerate([79999, 74999, 69999, 64999]):
            fake_date = now - timedelta(days=i)
            with get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        INSERT INTO price_history (product_id, price, date_checked)
                        VALUES (%s, %s, %s);
                    """, (pid, price, fake_date))

        print(f"✅ Inserted 4 prices for product_id {pid}")
        history = get_price_history(pid)
        print("📈 Price History:", history)
