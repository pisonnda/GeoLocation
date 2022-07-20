#!/usr/bin/python3
#Version2: For Linux Machine
#Version2.1: Read wifilist --> Confirm "Live Wifi Router"
#https://www.google.co.jp/maps/@43.0613654,141.3496807,17.58z
import requests
import json
import sys
import os
import re

#############################################################
#       Sample Wifi List                                                                                #
#                                                        SSID BSSID                                             #
#                                       Wifi_bigGlobe 08:10:86:d6:2e:aa                 #         
#                                  Galaxy A215879 62:3a:af:92:58:79                     #
#                                                VietViet 08:10:86:d5:da:f7                     #
#       DIRECT-B4-HP ENVY 4520 series dc:4a:3e:31:71:b5                 #
#                                 SPWH_H32_2BC67E 0c:2c:54:2b:c6:7e                     #
#                          SPWH_H32_2BC681_5G 0c:2c:54:2b:c6:81                 #
#               Linux
#1      Address: 3C:7C:3F:85:67:D0                                                              #
#       ESSID:"asus-rog-rapture"                                                                #
#2      Address: C6:CD:36:6D:D9:B4                                                              #
#       ESSID:"adhoc"                                                                                   #
#3      Address: 00:22:CF:E6:AE:AB                                                              #
#       ESSID:"Planex_24-E6AEAB"                                                                #
#       Address: 84:AF:EC:4A:56:01                                                              #
#       ESSID:"Buffalo-G-5600"                                                                  #
#       Address: 34:76:C5:1E:B4:40                                                              #
#       ESSID:"device01-2G"                                                                             #
#############################################################
wifilist = []

#Main Function
def main():
    count = 0
    filename = sys.argv[1]
    with open(filename, "r") as fp:
            buf = fp.readlines()
    result = buf[1:]

    #Get list of wifi and print to screen
    print("List of wifi")
    for row in result:
        a = re.sub('^ +', '', row)
        a = re.sub(' +', ',', row)
        a = a.split(",")
        SSID = a[1]
        MAC  = a[2]
        RSSI = a[3]
        print("({})\t{}\t{}\t{}".format(count, SSID.ljust(16, " "), MAC, RSSI))
        wifilist.append(a[1:4])
        count += 1
    print("-------------------------------------")

    #Choose Wifi -> Get MAC -> Get Location
    while True:
        print("Select Wifi1, 2: ", end='')
        n1, n2 = input().split(",")
        n1 = int(n1)
        n2 = int(n2)

        mac1 = str(wifilist[n1][1])
        print(mac1)
        rssi1 = str(wifilist[n1][2])
        mac2 = str(wifilist[n2][1])
        print(mac2)
        rssi2 = str(wifilist[n2][2])

        location = getlocation(mac1, rssi1, mac2, rssi2)
        print("=================Your location:==============")
        print(type(location))
        print(location)
        print("---------------------------------------------")

#Get location Function
def getlocation(mac1, rssi1, mac2, rssi2):
        #POST URL
        url = "https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCeoRn12KZ3-WXXcVRhSnLVy2jdPF1H1Yw"
        #JSON
        json_data = {
        "considerIp": "false",
        "wifiAccessPoints": [
        {
        "macAddress": mac1,
        "signalStrength": rssi1,
        "signalToNoiseRatio": 0
        },
        {
        "macAddress": mac2,
        "signalStrength": rssi2,
        "signalToNoiseRatio": 0
        }
        ]
        }
        #POST 送信
        #print(json_data)
        response = requests.post(
                url, 
                data = json.dumps(json_data)
                )
        location = response.json()
        return location

if __name__ == "__main__":
        main()
