FROM python:3.10
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
VOLUME db/store.sqlite

CMD ["python", "main.py"]