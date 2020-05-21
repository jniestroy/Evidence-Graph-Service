FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip install pandas
RUN pip install flask
RUN pip install pystardog 
RUN pip install uwsgi

COPY . .

ENTRYPOINT [ "uwsgi", "--ini", "http.ini"]
