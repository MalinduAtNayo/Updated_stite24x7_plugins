from cryptography import x509
import socket
import ssl
import sys
from datetime import datetime
from datetime import timezone 
import json

# if any changes are done to the metrics or units, increment the plugin version number here
PLUGIN_VERSION = "1"
HEARTBEAT = "true"

#Enter the name of the host/site being monitored for SSL expiration

hostname = "fpapp01.bfusa.com"
sni = "ifs.bfusa.com"
hostport = 443
#sjeapp02.local
#ifsdev.sjeifs.com

# create default context
context = ssl.create_default_context()

data = {'plugin_version': PLUGIN_VERSION, 'heartbeat_required': HEARTBEAT}

# override context so that it can get expired cert
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

try:
    with socket.create_connection((hostname, hostport)) as sock:
        with context.wrap_socket(sock, server_hostname=sni) as ssock:
            

            # get cert in DER format
            ssldata = ssock.getpeercert(True)
            
            # convert cert to PEM format
            pem_data = ssl.DER_cert_to_PEM_cert(ssldata)
            

            # pem_data in string. convert to bytes using str.encode()
            # extract cert info from PEM format
            cert_data = x509.load_pem_x509_certificate(str.encode(pem_data))

            # show cert expiry date
            #print("Expiry date:", cert_data.not_valid_after)
            data['expiry_date'] = str(cert_data.not_valid_after_utc)
            

            #print("Days left until expiry: ",(cert_data.not_valid_after-datetime.today()).days)
            data['days_until_expiry'] = (cert_data.not_valid_after_utc-datetime.today().replace(tzinfo=timezone.utc)).days

except Exception as e:
    data['status'] = 0
    data['msg'] = str(e)

print(json.dumps(data, indent=4, sort_keys=True))