# 📈 Automated Price Tracker

A full-stack Python app that tracks product prices from [iShopping.pk](https://www.ishopping.pk/), stores historical prices in PostgreSQL, and visualizes trends with Streamlit + Plotly.

---

assets/1.png
assets/2.png
assets/3.png
assets/4.png


## 🧙‍♂️ Features

- ✅ Scrapes product data using Selenium
- ✅ Stores price history in PostgreSQL
- ✅ REST API with Swagger UI (Flask + Flask-RESTX)
- ✅ Interactive dashboard built with Streamlit
- ✅ Scheduler runs scraper automatically every 6 hours (APScheduler)
- ✅ Fully Dockerized for easy setup
- ✅ Packaged as a Python project (`pip install -e .` ready)

---

## 🛠 Tech Stack

- Python 3.11
- Selenium + BeautifulSoup
- Flask + Flask-RESTX
- PostgreSQL
- APScheduler
- Streamlit + Plotly
- Docker & Docker Compose

---

## 🚀 How to Run (Dockerized)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/automated-price-tracker.git
cd automated-price-tracker
```

### 2. Add environment config

Create a `.env` file in the root:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/pricetracker
```

Or just duplicate `.env.example` and fill in credentials.

### 3. Build and run the app

```bash
docker-compose up --build
```

Once running:

- 📊 Dashboard → [http://localhost:8501](http://localhost:8501)
- 🧪 Swagger API → [http://localhost:5050/swagger](http://localhost:5050/swagger)
- 🟔 PostgreSQL DB → `localhost:5432`

---

## ⚙️ Project Modules

| Module       | Purpose                                          |
|--------------|--------------------------------------------------|
| `scraper/`   | Scrapes product prices from iShopping.pk         |
| `database/`  | Handles PostgreSQL operations                     |
| `api/`       | Flask REST API + Swagger docs                     |
| `dashboard/` | Streamlit UI showing price trends (Plotly)        |
| `scheduler/` | APScheduler task that runs scraper every 6 hours |
| `Docker`     | Dockerized setup with app, DB, dashboard          |

---

## 🥪 Sample Product Scrape (Manual)

```bash
docker-compose run app python scraper/scraper.py
```

(Useful for testing before the scheduler runs it automatically)

---


> 💡 In **VS Code**, you can drag & drop images directly into the `assets/` folder, then copy the path.

---

## 🥪 API Documentation

Interactive Swagger docs available at:

> [http://localhost:5050/swagger](http://localhost:5050/swagger)

### Example API Endpoints

- `GET /api/products` → list all products
- `GET /api/products/<product_id>` → get price history
- `POST /api/products` → add new product (JSON body)

---

## 📆 Packaging (for Devs)

Install in editable mode:

```bash
pip install -e .
```

This allows you to run the app or scheduler directly via import.

---

## 🔮 Coming Soon

- Email alerts on price drops
- Google Sheets + Airtable export
- Multi-store scraping (Daraz, Amazon, etc.)
- Advanced analytics (price prediction)

---

## 📄 License

License — free to use, modify, and share.

---

Made with ❤️ by [Mohammad Saud](mailto:saudmuzaffar@gmail.com)

