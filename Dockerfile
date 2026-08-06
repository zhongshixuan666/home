# ===== 前端构建阶段 =====
FROM node:20-alpine AS frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ .
RUN npm run build

# ===== Django 运行阶段 =====
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=sport_website.settings_prod

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY --from=frontend /app/frontend/dist ./frontend/dist
COPY frontend/public/images/ ./media/images/
COPY frontend/public/videos/ ./media/videos/

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "sport_website.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "60"]
