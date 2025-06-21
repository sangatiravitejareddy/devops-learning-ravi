
# Use an offical Python base image

FROM python:3.9-slim


# Set the Working directory in the container

WORKDIR /app

# Copy local file into container

COPY app.py .


# Run the Python Script

CMD ["python", "app.py"]


