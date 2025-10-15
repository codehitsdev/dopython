FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends build-essential         && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=8000         PYTHONUNBUFFERED=1         JWT_SECRET=change-me-in-env
EXPOSE 8000
CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
