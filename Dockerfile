FROM FROM python:3.6.8-slim-stretch
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
EXPOSE 5000
