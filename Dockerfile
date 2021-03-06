FROM python:latest

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD gunicorn yatube_api.wsgi:application --bind 0.0.0.0:8000 --timeout 90