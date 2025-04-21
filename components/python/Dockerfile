# ========== Base Stage ==========
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG UID=10001
ENV UID=${UID}

# Optional: Nicht-root User
RUN adduser --disabled-password --gecos "" --uid ${UID} appuser

# ========== Build Stage ==========
FROM base as builder

WORKDIR /app

# Systempakete für native builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-venv \
 && rm -rf /var/lib/apt/lists/*

# Venv erstellen
RUN python3 -m venv /venv

# Aktiviere venv + installiere Abhängigkeiten
COPY ./components/backend/requirements.txt ./
RUN . /venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
RUN . /venv/bin/activate &&  pip install gunicorn

COPY ./components/backend .

# ========== Dev Stage ==========
FROM base as dev

WORKDIR /app

COPY --from=builder /venv /venv
COPY --from=builder /app /app

ENV PATH="/venv/bin:$PATH"
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]

# ========== Prod Stage ==========
FROM base as prod

WORKDIR /app

COPY --from=builder /venv /venv
COPY --from=builder /app /app

ENV PATH="/venv/bin:$PATH"
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PORT=8000

EXPOSE ${PORT}

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT wsgi:app"]
