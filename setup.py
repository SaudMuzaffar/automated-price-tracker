from setuptools import setup, find_packages

setup(
    name="automated_price_tracker",
    version="1.0.0",
    packages=find_packages(exclude=["venv", "tests"]),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-restx",
        "APScheduler",
        "selenium",
        "python-dotenv",
        "requests",
        "psycopg2-binary",
        "beautifulsoup4",
        "streamlit",
        "plotly",
        "pandas"
    ],
    entry_points={
        "console_scripts": [
            "price-tracker-api=api.app:create_app"
        ]
    },
    author="Mohammad Saud",
    description="Automated Price Tracker with Flask API, Streamlit dashboard, and Selenium scraper.",
    keywords="flask streamlit scraper selenium price-tracker",
    python_requires='>=3.8'
)
