FROM debian

RUN apt update && apt upgrade -y

RUN apt install -y python3 python3-pip

RUN pip3 install --break-system-packages ovh

RUN git clone https://github.com/starnakin/ovh-dns /app

WORKDIR /app

ENTRYPOINT ["python3", "main.py"]