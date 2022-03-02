FROM python:3.10.2

EXPOSE 8000

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "main.py"]