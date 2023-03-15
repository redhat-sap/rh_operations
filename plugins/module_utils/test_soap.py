from suds.client import Client
from suds.transport.http import HttpAuthenticated, HttpTransport
# import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context

url = "http://sapabap751.westeurope.cloudapp.azure.com:8000/sap/bc/soap/wsdl?sap-client=001&services=SLDAG_GET_COMPUTER_INFO"

https_url = "https://sapabap751.westeurope.cloudapp.azure.com:44300/sap/bc/soap/wsdl?sap-client=001&services=SLDAG_GET_COMPUTER_INFO"
client = Client(url, username='DDIC', password="eAi6WKzMJ69uel",)

a = client.service.SLDAG_GET_COMPUTER_INFO()
method = getattr(client.service, 'SLDAG_GET_COMPUTER_INFO'.replace('/', '_-'))
a = method()

# rfcname = rfcname.replace('/', '_-')
# TODO SSL is not working
# urllib.error.URLError: <urlopen error [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:997)>
# https://techcommunity.microsoft.com/t5/running-sap-applications-on-the/secure-communication-to-fetch-sap-netweaver-sap-control-and-sap/ba-p/3735151

print(dict(a))