"""
Change either the www.py4e.com/code3/geojson.py or www.py4e.com/code3/geoxml.py
to print out the two-character country code from the retrieved data.
Add error checking so your program does not traceback if the country code
is not there.
Once you have it working, search for "Atlantic Ocean" and
make sure it can handle locations that are not in any country.
"""


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#brak when press Enter
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

#create a Python dictionary with the info from the json file
    try:
        js = json.loads(data)
    except:
        js = None

#check for retrieving errors
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

#when present, print the country code
    try:
        country_code = js['results'][0]['address_components'][2]['short_name']
        print ('Country code: ',country_code)
    except:
        print ("No country code found")
