# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and MySQL Connector in a single RUN command to optimize image layers
RUN pip install --no-cache-dir flask mysql-connector-python

# Expose the port that the app runs on
EXPOSE 5001

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Run the command to start the Flask app
CMD ["python", "app.py"]
