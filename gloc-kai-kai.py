#!/usr/bin/python3
#Version2: For Linux Machine
#Version2.1: Read wifilist --> Confirm "Live Wifi Router"
#https://www.google.co.jp/maps/@43.0613654,141.3496807,17.58z
import requests
import json
import sys
import os
import re
import folium

wifilist = []
datalist = {}

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
		#print("({})\t{}\t{}\t{}".format(count, SSID.ljust(16, " "), MAC, RSSI))
		wifilist.append(a[1:4])
		count += 1
	#print("-------------------------------------")

	#Choose Wifi -> Get MAC -> Get Location
	#while True:
	print("Can use list:")
	for n1 in range(0, count-1, 1):
		#print(n1)
		for n2 in range(count-1, n1, -1):
			#print("\t" + str(n2))
			#print("Select Wifi1, 2: ", end='')
			#n1, n2 = input().split(",")
			#n1 = int(n1)
			#n2 = int(n2)

			mac1 = str(wifilist[n1][1])
			rssi1 = str(wifilist[n1][2])
			mac2 = str(wifilist[n2][1])
			rssi2 = str(wifilist[n2][2])

			location = getlocation(mac1, rssi1, mac2, rssi2)
			#print("=================Your location:==============")
			#print(type(location))
			try: 
				coordinate = location['location']
				lat = coordinate['lat']
				lng = coordinate['lng']
				print("{}, {}\t{}, {}".format(n1, n2, lat, lng))
				#label = str(n1) + "," + str(n2)
				#data = str(lat) + "," + str(lng)
				#if label not in datalist:
				#	datalist[label] = data
			except: 
				continue
			#print("---------------------------------------------")
	
	#for k in datalist.keys():
	#	print("{}\t{}".format(label.ljust(8, " "), data))

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
		#print(type(location))
		return location

def mapping(lat, lng):
    latitude = lat
    longtude = lng
    name = "Point"
    map = folium.Map(location=[latitude, longtude], zoom_start=18) 
    folium.Marker(location=[latitude, longtude], popup=name).add_to(map) 
    map.save(str(lat) + "_" + str(lng) + ".html")
    #map.show()

if __name__ == "__main__":
		main()
