FROM python:3.8

WORKDIR /app

RUN apt-get update
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["python3", "manage.py", "runserver", "--noreload"]