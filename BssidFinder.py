import requests
import xmltodict

mac = input("Enter BSSID here: ").replace(':', '')

try:
    response = requests.get('http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks='+mac+':-65&app=ymetro')
except Exception:
    print('Can\'t connect to internet.')
    exit()

response.encoding = 'utf-8'

dicto = dict(xmltodict.parse(response.text))

try:
    dcordos = dict(dict(dicto['location'])['coordinates'])
except KeyError:
    print("bssid not finded.")
    exit()

print("""
Latitude: {0}
Longitude: {1}

Nlatitude: {2}
Nlongitude: {3}
""".format(dcordos['@latitude'], dcordos['@longitude'], dcordos['@nlatitude'], dcordos['@nlongitude']))