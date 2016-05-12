FROM tiangolo/uwsgi-nginx:latest

MAINTAINER Jiawei Zhou <4679kun@outlook.com>

RUN pip install flask
RUN pip install requests

# Add app configuration to Nginx
COPY nginx.conf /etc/nginx/conf.d/

# Copy sample app
COPY ./app /app
