FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --clear --noinput
COPY . /app/
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000