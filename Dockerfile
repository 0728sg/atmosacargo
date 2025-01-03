FROM python:3.10
WORKDIR /bot

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
VOLUME db/store.sqlite

CMD ["python", "main.py"]