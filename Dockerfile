FROM python:3

ADD app.py /

RUN pip3 install python-telegram-bot request

CMD ["python", "./app.py"]