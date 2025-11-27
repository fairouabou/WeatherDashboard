# Use lightweight Python image
FROM python:3.13-slim

# Set working directory in the container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5001

# Environment variables (optional but recommended)
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Start the application
CMD ["python", "app.py"]
