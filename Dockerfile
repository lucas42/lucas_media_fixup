FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y pipenv libtag1-dev

COPY Pipfile* ./
RUN pipenv install
COPY *.py .

CMD [ "pipenv", "run", "python", "all-tracks.py"]