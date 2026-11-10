FROM python:3.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-5001} src.app:app"]