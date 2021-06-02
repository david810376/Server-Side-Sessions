import requests
import sys


url = sys.argv[-1]

#to get the url and store to json
r = requests.get(url)

# check url status 200 mean ok
if r.status_code == 200:
    for key in r.json()['keys']:
        getkey = requests.get(url +"/"+key)
        print(getkey.text)
