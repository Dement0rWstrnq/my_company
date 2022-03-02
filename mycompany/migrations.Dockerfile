FROM python:3.10.2

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

COPY requirements.migrations.txt ./

RUN pip install -r requirements.migrations.txt

COPY migrations /migrations
COPY alembic.ini ./

ENTRYPOINT ["alembic"]
CMD ["upgrade", "head"]
