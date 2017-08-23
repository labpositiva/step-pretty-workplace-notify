FROM python:3.6.1
MAINTAINER Luis Mayta <@slovacus>

# set working directory to /app/
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

# install python dependencies
RUN pip install -r /app/requirements.txt

COPY . /app

CMD ["make run"]
