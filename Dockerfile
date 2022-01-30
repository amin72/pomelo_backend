# base image
FROM public.ecr.aws/bitnami/python:3.10.2-debian-10-r9

#maintainer
LABEL Author="Pomelo"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED 1

#directory to store app source code
#RUN mkdir ~/code

#switch to /app directory so that everything runs from here
WORKDIR /code

COPY requirements.txt /code/

#copy the app code to image working directory

#let pip install required packages
RUN pip install -r requirements.txt

COPY . /code