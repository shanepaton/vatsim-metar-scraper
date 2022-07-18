from time import sleep
import requests
airport=input("Enter airport ICAO code: ")

while True:
    url = 'http://metar.vatsim.net/metar.php?id=' + airport
    r = requests.get(url, allow_redirects=True)
    open('metar.txt', 'wb').write(r.content)
    sleep(900)
