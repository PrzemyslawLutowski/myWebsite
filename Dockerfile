# Plik tekstowy, który zawiera polecenia Dockera do utworzenia obrazu Docker
###########
# BUILDER #
###########

# pull official base image
FROM python:3.12.3


# set environment variables
# blokada zapisywania przez Pythona plików .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# włączanie bezpośredniego wysyłania strumieni stdout i stderr do terminala, bez ich uprzedniego buforowania
ENV PYTHONUNBUFFERED 1

# make work directory
# utworzenie katalogu roboczego obrazu
RUN mkdir /myWebsite


# set work directory
# zdefiniowanie katalogu roboczego obrazu
WORKDIR /myWebsite

# install dependencies
# aktualizacja i instalowanie pakietów
RUN pip install --upgrade pip
COPY requirements.txt /myWebsite/
RUN pip install -r requirements.txt

# kopiowanie kodu źrudłowego projektu, z katalogu lokalnego do katalogu roboczego
COPY . /myWebsite/
