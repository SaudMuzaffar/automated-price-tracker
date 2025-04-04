# Dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use Streamlit to run the dashboard
CMD ["streamlit", "run", "dashboard/streamlit_app.py"]
