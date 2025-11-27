FROM python:3.13-slim

WORKDIR /app

# Copy your app code
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Azure requires FLASK to bind to 0.0.0.0
ENV PORT=5001

EXPOSE 5001

CMD ["python", "app.py"]
