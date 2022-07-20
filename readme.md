####2022年  7月 17日 日曜日 15:54:30 JST
####Get location from 2 Wifi'MAC Address (+Mapping)
####Pisonnda 
####Version 2.0


#I. Prepare for Running
	1. 	Get Google API
	2.	Open getloc.py with editor (example: vim getloc.py)
	3. 	Set Google API to {your_google_API_key}


#II. Run getloc.py (Get location with Wifi's MAC Address):
		Get location:		./getloc.py MAC1 MAC2

#III. Run getloc-nama.py (Get wifilist -> choose Wifi -> Get location):
		Get location:		./getloc-nama.py --nama
		Mapping and output: ./getloc-nama.py --nama -o <outfile.html>
		Mapping and show: 	./getloc-nama.py --nama --show

#IV. Run getloc-from-list.py (Get wifilist -> choose wifi list file -> Get location):
		Get location: 		./getloc-from-list.py --wifilist <wifi list file>
		Mapping and output:	./getloc-from-list.py --wifilist <wifi list file> -o <outfile.html>
		Mapping and show:	./getloc-from-list.py --wifilist <wifi list file> --show
