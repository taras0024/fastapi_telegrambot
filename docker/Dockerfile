FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install netcat nano -y

RUN apt install -y vim wget
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ bullseye"-pgdg main | tee  /etc/apt/sources.list.d/pgdg.list

RUN apt-get update
RUN apt-get -y install postgresql-client-14

RUN mkdir magistr

COPY requirements.txt /magistr

RUN pip install --upgrade pip
RUN pip install -r ./magistr/requirements.txt --ignore-installed --force-reinstall --upgrade --no-cache-dir

COPY . /magistr
WORKDIR /magistr

RUN chmod o+x ./docker/wait.sh

EXPOSE 8000
