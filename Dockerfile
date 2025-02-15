FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
VOLUME db/store.sqlite

RUN mkdir /app/secrets && mv atmoscargo.json /app/secrets/
ENV GOOGLE_SHEETS_CREDENTIALS="/app/secrets/atmoscargo.json"

CMD ["python", "main.py"]

