FROM alpine

RUN apk update && apk upgrade -y

RUN apk install -y python3 python3-pip git

RUN pip3 install --break-system-packages ovh

RUN git clone https://github.com/starnakin/ovh-dns /app

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]