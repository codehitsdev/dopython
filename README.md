# FastAPI + Supabase (Postgres) + JWT + CI/CD to DigitalOcean

## Features
- JWT auth endpoints: `/auth/register`, `/auth/login`, `/me`
- Protected items: `/items` (create/list)
- SQLAlchemy + Alembic (with initial migration)
- Works with Supabase Postgres (use pooled port 6543 + sslmode=require)
- GitHub Actions: Ruff + PyTest + deploy via `doctl` and `.do/app.yaml`

## Local (Docker Compose)
```bash
docker-compose up -d --build
alembic upgrade head
open http://localhost:8000/docs
```

## Local (no Docker)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/postgres"
export JWT_SECRET="dev-secret"
alembic upgrade head
uvicorn app:app --reload
```

## Supabase
- In Supabase project settings → Database, copy the connection string.
- Convert to SQLAlchemy URL (psycopg): `postgresql+psycopg://postgres:<password>@<host>:6543/postgres?sslmode=require`
- Set as `DATABASE_URL` in environment variables.

## DigitalOcean App Platform
- Connect repo, deploy via Dockerfile.
- Set env vars: `DATABASE_URL`, `JWT_SECRET`, `JWT_EXPIRE_MINUTES`.
- Health check path `/health`.

## GitHub Actions Secrets
- `DIGITALOCEAN_ACCESS_TOKEN` – DigitalOcean PAT
- `DIGITALOCEAN_APP_ID` – (optional) App ID to update; omit for first-time create
- `DATABASE_URL` – Supabase connection
- `JWT_SECRET` – your strong secret
- `JWT_EXPIRE_MINUTES` – e.g. `60`
