# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBUG=False \
    PORT=8000

ADD . /app
COPY . /app

# install dependencies
RUN pip install -r requirements.txt

# copy project

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]