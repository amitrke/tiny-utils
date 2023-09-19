FROM python:latest

RUN apt update
RUN apt install git -y
WORKDIR /app
COPY python/requirements.txt /app/python/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /app/python/requirements.txt

CMD tail -f /dev/null