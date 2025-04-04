# Use official Python image
FROM python:3.11

# Set working directory inside the container
WORKDIR /app

# Pre-copy requirements to install early (Docker cache optimization)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app into container
COPY . .

# Install the app in editable/development mode
RUN pip install -e .

# Run the Flask API
CMD ["python", "api/app.py"]
