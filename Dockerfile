FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

CMD [ "python", "main.py" ]