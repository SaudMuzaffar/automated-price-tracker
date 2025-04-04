import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import plotly.graph_objects as go
from database.database import get_price_history, get_all_products





st.set_page_config(page_title="📊 Price Tracker", layout="centered")
st.title("📊 Product Price Tracker")

# 🧪 DEBUG: Show status while loading products
st.write("🔄 Loading products from database...")

try:
    products = get_all_products()  # Returns list of (id, name)
    
    
    if not products:
        st.warning("⚠️ No products found in the database.")
        st.stop()
    else:
        st.success(f"✅ Loaded {len(products)} products.")
except Exception as e:
    st.error(f"❌ Failed to load products: {e}")
    st.stop()

# Build product dropdown
product_map = {product["name"]: product["product_id"] for product in products}
selected_name = st.selectbox("Select a product to view its price history:", list(product_map.keys()))

if selected_name:
    product_id = product_map[selected_name]  # ✅ Get actual int ID
    
    # 🧪 Try loading price history
    try:
        st.write("📦 Selected Name:", selected_name)
        st.write("🆔 Product ID to fetch:", product_id)

        history = get_price_history(product_id)  # List of (price, date)
    except Exception as e:
        st.error(f"❌ Failed to load price history: {e}")
        st.stop()

    if not history:
        st.warning("⚠️ No price history found for this product.")
    else:
        prices = [row["price"] for row in history]
        dates = [row["date_checked"] for row in history]


        # 📈 Build Plotly chart
        fig = go.Figure(data=go.Scatter(x=dates, y=prices, mode='lines+markers'))
        fig.update_layout(
            title=f"📈 Price Trend for '{selected_name}'",
            xaxis_title="Date",
            yaxis_title="Price (PKR)",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
