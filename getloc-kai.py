#!/opt/homebrew/bin/python3
import requests
import json
import sys
import os
import re

#############################################################
#   Sample Wifi List                                        #
#                            SSID BSSID                     #
#                   Wifi_bigGlobe 08:10:86:d6:2e:aa         #     
#                  Galaxy A215879 62:3a:af:92:58:79         #
#                        VietViet 08:10:86:d5:da:f7         #
#   DIRECT-B4-HP ENVY 4520 series dc:4a:3e:31:71:b5         #
#                 SPWH_H32_2BC67E 0c:2c:54:2b:c6:7e         #
#              SPWH_H32_2BC681_5G 0c:2c:54:2b:c6:81         #
#############################################################
info = []

#Main Function
def main():
    count = 1
    osc = findos()
    wifilist = []
    #MacOS
    if osc == 0:
        wifilist = list(os.popen('airport -s').read().split("\n"))
        wifilist = wifilist[1:len(wifilist)-1]
    #Linux
    if osc == 1:
        wifilist = list(os.popen("iwlist wlan0 scanning | grep -oe 'Address.*' -e 'ESSID.*'")).read()

    result = wifilist
    #Get list of wifi and print to screen
    print("List of wifi now")
    for row in result:
        a = re.sub('^ +', '', row)
        a = re.sub(' +', ',', row)
        a = a.split(",")
        print("({}) - {} - {}".format(count, a[1], a[2]))
        info.append(a[1:3])
        count += 1

    #Choose Wifi -> Get MAC -> Get Location
    print("Select Wifi1: ", end='')
    n1 = int(input())
    print("Select Wifi2: ", end='')
    n2 = int(input())
    mac1 = info[n1][1]
    mac2 = info[n2][1]
    location = getlocation(mac1, mac2)
    print(location)

#Find OS
def findos():
    uname = str(os.popen('uname').read())
    if uname == "Darwin":
        return 0
    if uname == "Linux":
        return 1

#Get location Function
def getlocation(mac1, mac2):
    #POST URL
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key={your_google_API}"
    #JSON
    json_data = {
    "considerIp": "false",
    "wifiAccessPoints": [
    {
    "macAddress": mac1,
    "signalStrength": -43,
    "signalToNoiseRatio": 0
    },
    {
    "macAddress": mac2,
    "signalStrength": -55,
    "signalToNoiseRatio": 0
    }
    ]
    }
    #POST 送信
    response = requests.post(
        url, 
        data = json.dumps(json_data)
        )
    location = response.json()
    return location

if __name__ == "__main__":
    main()
