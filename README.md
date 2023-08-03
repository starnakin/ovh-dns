# ovh-dns
## <ins>First Step:</ins>
Create an API Key in OVH with at least **"Get"** and **"Put"** permissions. In the text box on the right, enter **"/*"**.
https://www.ovh.com/auth/api/createToken
	
## <ins>Second Step:</ins>
In main.py, insert your key information:
```
client = ovh.Client(
	endpoint='ovh-eu',
	application_key=[Your key],
	application_secret=[Your key],
	consumer_key=[Your key]
)
```

And fill in this information:

subdomain="[Your SubDomain]"
zone="[Your Domain]"
	
## <ins>Third Step:</ins>
Place **"ddns.service"** in your service file, for example, "/etc/systemd/system/".

Edit **"ddns.service"** and specify the file location where the program is located:
```
ExecStart=/usr/bin/python3 /your_location/ovh-dns/main.py
```

Enable and start the program:
"systemctl enable ddns.service" and "systemctl start ddns.service"
	
### <ins>Tips:</ins>
Don't forget to install Python 3 and the OVH API
"pip install ovh"
https://github.com/ovh/python-ovh

<br></br>
#### <ins>*Contributor:*</ins>
*Python by Starnakin, Readme by Xamora*
