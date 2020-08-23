FROM python:3.6-alpine

RUN pip install pika

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY send.py ./

CMD ["python", "/app/send.py"]
