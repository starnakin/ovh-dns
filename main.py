import ovh
import socket
from time import sleep
import requests

client = ovh.Client(
    endpoint='',
    application_key='',
    application_secret='',
    consumer_key=''
)

subdomain=""
zone="chauvet.pro"

while True:
    ip_in = requests.get('https://checkip.amazonaws.com').text.strip()
    ids = client.get('/domain/zone/{}/record'.format(zone), 
        subDomain=subdomain,
        fieldType="A"
    )
    print(ip_in)
    ip_ext = client.get('/domain/zone/{}/record/{}'.format(zone, ids[0]))["target"]
    if(ip_in != ip_ext):
        result = client.put('/domain/zone/{}/record/{}'.format(zone, ids[0]), 
            target=ip_in
        )
        print("update:", ip_ext, "->", ip_in)
        sleep(100)
    sleep(1)

