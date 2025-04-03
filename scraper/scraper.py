import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from bs4 import BeautifulSoup
from database.database import insert_product, insert_price

# Config
URL = 'https://www.ishopping.pk/electronics/mobile-phones-tablet-pc/mobile-phones-prices-in-pakistan.html'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}
MAX_ITEMS = 3  # Change when scaling

def scrape_and_store():
    response = requests.get(URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ Failed to fetch page: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    product_blocks = soup.find_all('div', class_='product-item-info')  # container for each product

    if not product_blocks:
        print("❌ No products found on the page.")
        return

    for block in product_blocks[:MAX_ITEMS]:
        try:
            # Product Name + URL
            name_tag = block.find('a', class_='product-item-link')
            name = name_tag.text.strip()
            url = name_tag['href']

            # Price (e.g. from span.price or span[data-price-type="finalPrice"])
            price_tag = block.find('span', class_='price')
            price_text = price_tag.text.strip().replace(',', '').replace('PKR', '').replace('Rs.', '')
            price = float(''.join(filter(lambda c: c.isdigit() or c == '.', price_text)))

            # Save to DB
            product_id = insert_product(name, url)
            insert_price(product_id, price)

            print(f"✅ {name} — Rs. {price} → stored.")

        except Exception as e:
            print("❌ Error parsing/storing a product:", e)

# Run the scraper
if __name__ == "__main__":
    scrape_and_store()
