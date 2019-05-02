FROM python:3

ADD app.py /

RUN pip3 install python-telegram-bot requests

CMD ["python", "./app.py"]