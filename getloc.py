#!/usr/bin/python3
#Version1: 2022.06.08 	Get location of device with 2 MAC Address of Wifi
#Version2: 2022.07.17 	Fixing

#####Import Module####
import requests
import json
import sys

#######Main Function
def main():
	argc = len(sys.argv[0:])
	if argc < 3:
		print("Syntax Error")
		print("getloc.py MAC1 MAC2")
		exit()

	mac1 = str(sys.argv[1])
	mac2 = str(sys.argv[2])

#POST URL
	url = "https://www.googleapis.com/geolocation/v1/geolocate?key={your_google_API_key}"

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

	print(response)

	res_data = response.json()
	print(res_data)


if __name__== '__main__':
	main()
