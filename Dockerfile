FROM python:3.7-slim

WORKDIR /Heart-Failure-Preciction

ADD . /Heart-Failure-Prediction

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME OpentoAll

CMD ["python3","app.py"]
