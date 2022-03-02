ARG PYTHON_VERSION=3.10.2

FROM python:$PYTHON_VERSION as builder

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

WORKDIR /app

FROM python:$PYTHON_VERSION as final

EXPOSE 8000

ADD . /app

RUN rm -rf /app/migrations
RUN rm -f /app/alembic.ini

ENTRYPOINT ["python", "run.py"]
CMD []