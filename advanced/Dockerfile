FROM python:2.7.14-jessie
# FROM python:2.7
MAINTAINER Tilak T "tilaknayarmelpal@gmail.com"
COPY . /app
WORKDIR /app/show_pages
RUN pip install -U pip setuptools && pip install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]
# ENTRYPOINT ["python"]
# CMD ["app.py"]
