import requests
import json

def time_zone():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    return j['time_zone']

if __name__ == '__main__':
    print time_zone()
