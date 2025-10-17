# Use an appropriate Python slim base image
FROM python:3-alpine
# Prevent Python from writing pyc files and force stdout/stderr flush (good practices)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project code
COPY . /app

EXPOSE 8000

# Collect static files (Whitenoise will serve these files)
RUN python manage.py collectstatic --no-input

# Set the container startup command:
# 1) Apply Django migrations
# 2) Start Gunicorn to serve the application
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
