FROM alpine

RUN apk update && apk upgrade

RUN apk add python3 py3-pip git

RUN pip3 install --break-system-packages ovh

RUN git clone https://github.com/starnakin/ovh-dns /app

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]