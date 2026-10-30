FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m playwright install --with-deps chromium firefox

COPY src/ ./src/
COPY tests/ ./tests/
COPY pages/ ./pages/
COPY test_data/ ./test_data/
COPY pytest.ini .

RUN mkdir -p reports


CMD ["python", "-m", "pytest", "-v", "--junitxml=reports/junit.xml", "--html=reports/day41-test-report.html", "--self-contained-html"]