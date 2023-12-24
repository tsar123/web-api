# pull official base image
FROM python:3.11

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# set work directory
RUN mkdir app
WORKDIR /app
ADD ./ /app/

