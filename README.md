# 📈 Automated Price Tracker

A full-stack Python app that tracks product prices from [iShopping.pk](https://www.ishopping.pk/), stores history in PostgreSQL, and visualizes trends using Streamlit + Plotly.

---

## 🧩 Features

- ✅ Scrapes product data using Selenium
- ✅ Stores price history in PostgreSQL
- ✅ Interactive dashboard built with Streamlit
- ✅ Runs fully inside Docker
- ✅ Designed for future automation (via cron or n8n)

---

## 🛆 Tech Stack

- Python 3.11
- Selenium
- BeautifulSoup
- PostgreSQL
- Streamlit
- Plotly
- Docker & Docker Compose

---

## 🚀 How to Run (Dockerized)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/automated-price-tracker.git
cd automated-price-tracker
```

### 2. Add environment config

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/pricetracker
```

### 3. Build and run

```bash
docker compose up --build
```

- Dashboard will be live at: [http://localhost:8501](http://localhost:8501)
- Database runs inside Docker at `localhost:5432`

---

## 🛠️ Modules

| Module     | Purpose                               |
|------------|----------------------------------------|
| `scraper`  | Scrapes product prices from Daraz/iShopping |
| `database` | Handles PostgreSQL DB operations       |
| `dashboard`| Streamlit UI for price trends          |
| `Docker`   | Containers all services                |

---

## 🧪 Sample Product (iShopping)

```bash
docker compose run app python scraper/scraper.py
```

---

## 🔮 Coming Soon

- Email alerts on price drops
- Cron-based automation
- Airtable or Google Sheets export
- Multi-store price comparison

---

## 📄 License

 License — free to use, modify, share.

---

Made with ❤️ by [Saud Muzaffar](mailto:saudmuzaffar@gmail.com)

