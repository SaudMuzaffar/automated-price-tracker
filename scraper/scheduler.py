# api/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from scraper import scrape_all_products  # or whatever function kicks off scraping
import logging

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_all_products, 'interval', hours=6)
    scheduler.start()
    logging.info("Scheduler started. Scraper will run every 6 hours.")
