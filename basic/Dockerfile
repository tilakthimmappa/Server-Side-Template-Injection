FROM python:2.7.14-jessie

WORKDIR /apps/

COPY app/ /apps/

WORKDIR /apps/

RUN pip install -U pip setuptools && pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]