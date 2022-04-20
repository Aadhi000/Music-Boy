FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /kaal/
WORKDIR /kaal/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
WORKDIR /app
COPY config.json /app/config.json
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN snap install -y ffmpeg

CMD ["python", "./main.py"]
