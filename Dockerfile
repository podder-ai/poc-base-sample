FROM ubuntu:18.04

RUN apt-get update \
&& apt-get install -y python3.6 \
&& apt-get install -y python3-pip \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# work directory
COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install -r requirements.txt

CMD python main.py
