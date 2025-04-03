# automated-price-tracker
# 🏷️ Automated Price Tracker

A full-stack Python application that automatically tracks product prices from e-commerce sites, stores historical data, and lays the foundation for future dashboards, APIs, and alerts.

---

## 🚀 Features (Planned)

- ✅ Scrapes product prices using Python
- ✅ Stores product and price history in PostgreSQL
- ✅ Dockerized with complete `docker-compose` setup
- ⏳ Visual dashboard with Streamlit (coming soon)
- ⏳ REST API with Flask (coming soon)
- ⏳ Scheduled automation using cron (coming soon)
- ⏳ Email alerts when price drops (optional bonus)

---

## 🧱 Tech Stack

- **Backend:** Python 3.11
- **Database:** PostgreSQL 14
- **Scraping Tools:** `BeautifulSoup` or `Selenium` (TBD)
- **DevOps:** Docker & Docker Compose
- **Environment Config:** `python-dotenv`

---

## 🗂️ Project Structure

```
automated-price-tracker/
│
├── database/
│   └── database.py         # DB functions: create, insert, fetch
├── .env                    # Secure DB URL
├── Dockerfile              # Docker config for app
├── docker-compose.yml      # App + DB containers
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/pricetracker
```

---

## 🐳 Run the App with Docker

1. **Build the containers:**
```bash
docker compose build
```

2. **Run the application:**
```bash
docker compose up
```

Your app will:
- Spin up a Postgres DB
- Create tables automatically
- Insert a sample product and price
- Print price history in logs

---

## 📈 Example Output

```
✅ Tables created!
✅ Inserted product + price
📊 Price History: [{'price': Decimal('999.99'), 'date_checked': datetime.datetime(…)}]
```

---

## ✨ What's Next?

- [ ] Build `scraper.py` to fetch real product prices
- [ ] Hook it into the database module
- [ ] Develop the Streamlit dashboard
- [ ] Add Flask API endpoints
- [ ] Set up cron jobs for daily runs

---

## 🤝 Contributing

This project is still in its early stages. Contributions, suggestions, and pull requests are welcome!

---

## 📜 License

Free License © 2025 Mohammad Saud Muzaffar


