FROM FROM python:3.7.4-slim-stretch
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
