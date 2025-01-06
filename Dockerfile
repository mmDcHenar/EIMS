FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /src/

COPY requirements.txt .
RUN [ "pip", "install", "--upgrade", "--no-cache-dir", "-r", "requirements.txt" ]

COPY . .

CMD ["bash", "-c", "alembic upgrade head && python3 -m uvicorn main:app --host 0.0.0.0 --port 8000"]