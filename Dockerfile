FROM python:3.13.7-slim

ENV PYTHONUNBUFFERED=1 \
    RUN_IN_APPDEAMON=false \
    TEMP_FILE=/data/temp_getjudo.pkl

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY python/ .

VOLUME /data

CMD ["python", "getjudo.py"]
