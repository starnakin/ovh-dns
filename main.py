import ovh
import socket
from time import sleep
import requests
import os

print("ovh-dns start")

client = ovh.Client(
    endpoint=os.environ["ENDPOINT"],
    application_key=os.environ["APP_KEY"],
    application_secret=os.environ["APP_SECRET"],
    consumer_key=os.environ["CONSUMER_KEY"]
)

subdomain=os.environ["SUBDOMAIN"]
zone=os.environ["DOMAIN"]

while True:
    ip_in = requests.get('https://checkip.amazonaws.com').text.strip()
    
    ids = client.get('/domain/zone/{}/record'.format(zone), 
        subDomain=subdomain,
        fieldType=os.environ["RECORD_TYPE"]
    )
    ip_ext = client.get('/domain/zone/{}/record/{}'.format(zone, ids[0]))["target"]
    if(ip_in != ip_ext):
        result = client.put('/domain/zone/{}/record/{}'.format(zone, ids[0]), 
            target=ip_in
        )
        print("update:", ip_ext, "->", ip_in)
        sleep(100)
    sleep(1)

