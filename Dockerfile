# pull official base image
FROM python:3.10.12-slim-bullseye


# set work directory. If the WORKDIR doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction
WORKDIR /usr/src/ppms


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        # Pamiętaj, aby dodać tutaj wszystkie niezbędne zależności build-time,
        # np. jeśli używasz bazy PostgreSQL i potrzebujesz psycopg2:
        # build-essential \
        # libpq-dev \
        nano \
    && rm -rf /var/lib/apt/lists/*
# update, upgrade and install nano
RUN apt-get update
#RUN apt-get upgrade -y
RUN apt-get install -y nano


# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy entrypoint.sh

COPY ./entrypoint.sh .

RUN #ls -l ./entrypoint.sh && file ./entrypoint.sh
#RUN chmod +x entrypoint.sh && \
#    sed -i 's/\r$//g' entrypoint.sh
#RUN chmod +x /usr/src/ppms/entrypoint.sh
#RUN sed -i 's/\r$//g' /usr/src/ppms/entrypoint.sh


# copy project
COPY . .

RUN sed -i 's/\r$//g' ./entrypoint.sh && chmod +x ./entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/usr/src/ppms/entrypoint.sh"]

