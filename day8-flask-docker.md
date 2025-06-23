# Day 8 – Dockerized Flask App

## ✅ What I Did
- Created a Flask app (`app.py`)
- Created `requirements.txt`
- Dockerized it using a Dockerfile
- Built image and tested on port 5000

## ✅ Commands Used

```bash
docker build -t flask-docker-app .
docker run -p 5000:5000 flask-docker-app
