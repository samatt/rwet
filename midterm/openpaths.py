import oauth2, time, urllib, urllib2, json

ACCESS = "UPOGHBXXQLZTBKNHO4E4VES6CA"
SECRET = "YOEZVNX51HMOA9Z7QXNW7KMXPOC7HF7UFR524YTR7WV042VMS9I6JORRMQKI8TM8"
URL = "https://openpaths.cc/api/1" 

def build_auth_header(url, method):
    params = {                                            
        'oauth_version': "1.0",
        'oauth_nonce': oauth2.generate_nonce(),
        'oauth_timestamp': int(time.time()),
    }
    consumer = oauth2.Consumer(key=ACCESS, secret=SECRET)
    params['oauth_consumer_key'] = consumer.key 
    request = oauth2.Request(method=method, url=url, parameters=params)    
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    request.sign_request(signature_method, consumer, None)
    return request.to_header()

# GET data (last 24 hours)
now = time.time()
params = {'start_time': now - 24*60*60, 'end_time': now}    # get the last 24 hours
query = "%s?%s" % (URL, urllib.urlencode(params))
print(query)
try:
    request = urllib2.Request(query)
    request.headers = build_auth_header(URL, 'GET')
    connection = urllib2.urlopen(request)
    data = json.loads(''.join(connection.readlines()))
    print(json.dumps(data, indent=4))
except urllib2.HTTPError as e:
    print(e.read())    