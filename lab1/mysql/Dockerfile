FROM python:3.8.3-slim-buster

RUN mkdir -p /mysql/
WORKDIR /mysql/
COPY . /mysql/

ENV SECRET_KEY my_secret_string

RUN pip install --upgrade pip && pip install -r requirements.txt && pip freeze > requirements.txt
RUN pip install python-dotenv && pip install psycopg2-binary
