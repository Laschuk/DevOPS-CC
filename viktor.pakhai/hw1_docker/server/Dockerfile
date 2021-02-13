FROM python:latest
MAINTAINER Viktor Pakhai <sdgadmin@gmail.com>
WORKDIR /usr/src/app
RUN pip install flask
RUN pip install livereload
ADD ./project/ ./
CMD [ "python", "main.py" ]
#EXPOSE 5000
