# Use an official lightweight Python image.
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install dependencies
# Adding build dependencies and cleaning up to keep the container clean and minimal
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --no-cache-dir psycopg2 configparser \
    && apt-get purge -y --auto-remove gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Expose port 5000 for the application
EXPOSE 5000

# Run the migration script to set up the database
CMD ["python", "database/migrate_db.py"]
