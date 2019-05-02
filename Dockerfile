FROM python:3

ADD app.py config.json /

RUN pip3 install python-telegram-bot requests

CMD ["python", "./app.py"]