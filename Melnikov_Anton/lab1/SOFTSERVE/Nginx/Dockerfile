
ARG NG_VERSION=latest
FROM nginx:latest
MAINTAINER oxlamons@gmail.com
ARG NG_VERSION
ARG ARG_FILE=test
#VOLUME ./hosts/:/etc/nginx/sites-avalible/default
#VOLUME ./hosts/:/etc/nginx/sites-enable/default
#COPY /Nginx/example.com.conf ./etc/nginx/conf.d/
#VOLUME ./logs/nginx-error.log:var/log/nginx/error.log
#VOLUME ./logs/nginx-access.log:var/log/nginx/access.log
ENV NG_VERSION ${NG_VERSION}
RUN mkdir -p /opt/$ARG_FILE
