FROM python:3.9
WORKDIR /app
ADD . /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT