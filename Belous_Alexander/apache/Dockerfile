FROM httpd:2-alpine
COPY index.html /usr/local/apache2/htdocs/
COPY httpd.conf /usr/local/apache2/conf/
CMD ["httpd", "-D", "FOREGROUND"]
