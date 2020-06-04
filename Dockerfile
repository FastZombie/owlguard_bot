FROM python:3

RUN pip3 install python-telegram-bot requests

ADD app.py config.json /code/
WORKDIR /code
CMD ["python", "./app.py"]
