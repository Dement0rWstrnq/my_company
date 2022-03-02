ARG PYTHON_VERSION=3.10.2

FROM python:$PYTHON_VERSION as builder

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

WORKDIR /app

FROM python:$PYTHON_VERSION as final

ADD requirements.migrations.txt ./

RUN pip install -r requirements.migrations.txt

ADD migrations /migrations
ADD alembic.ini ./

ENTRYPOINT ["alembic"]
CMD ["upgrade", "head"]
