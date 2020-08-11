import requests
import xmltodict

mac = input("Enter BSSID here: ")

def FindFromBssid(bssid):

    bssid = bssid.replace(':', '')

    response = requests.get('http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks='+bssid+':-65&app=ymetro')

    response.encoding = 'utf-8'

    dicto = dict(xmltodict.parse(response.text))
    dcordos = dict(dict(dicto['location'])['coordinates'])

    return {'latitude': float(dcordos['@latitude']), 'longitude': float(dcordos['@longitude'])}

try:
    result = FindFromBssid(mac)
except KeyError:
    print("Bssid location not found.")
    exit()
except Exception:
    print('Unable to connect to the internet.')
    exit()

print('Latitude: {0}\nLongitude: {1}'.format(result['latitude'], result['longitude']))