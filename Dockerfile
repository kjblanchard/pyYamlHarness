FROM python:3.8-alpine
RUN apk --update add bash nano 
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
EXPOSE 5000
WORKDIR /home/flaskapp
COPY . /home/flaskapp
CMD ["gunicorn","--bind","0.0.0.0:5000","frontend:app"]