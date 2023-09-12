"""
	教學:
		https://www.youtube.com/watch?v=9-wuyhMkl9E
	json viewer: https://jsonviewer.stack.hu/
	postman: https://www.postman.com/
"""

import sys
import time
import requests
import json
import traceback
from pprint import pprint

def get_map_info(query,debug=True):
	output = {
		"status":0,
		"搜尋":"",
		"類別":[],
		"名稱":"",
		"地址":"",
		"電話":"",
		"LatLon":[],
		"營業時間":{}
	}
	res = requests.get(f'https://www.google.com.tw/search?tbm=map&q={query}')
	if res.status_code == 200:
		raw = res.text.lstrip(")]}'")
		d = json.loads(raw)
		try:
			
			output["搜尋"] = d[0][0]
			output["名稱"] = d[0][1][0][14][11]
			output["地址"]= d[0][1][0][14][2][0]
			output["類別"] = d[0][1][0][14][13]
			lat = d[0][1][0][14][9][2]
			lon = d[0][1][0][14][9][3]
			output["LatLon"] = [lat,lon]
			output["電話"] = d[0][1][0][14][178][0][0]
			#0-1-0-14-34-1
			open_hours = d[0][1][0][14][34][1]
			for tup in open_hours:
				weekday = tup[0]
				time_windows = tup[1]
				output["營業時間"][weekday] = time_windows
			output["status"] = 1
		except Exception as e:
			print(traceback.format_exc())
		time.sleep(1)
	if debug:
		pprint(output)
	return output

if __name__ == "__main__":
	try:
		if sys.argv[1] == "--query":
			inputStr = sys.argv[2]
			get_map_info(inputStr)
	except Exception as e:
		print(e)
		print("===============================")
		print("--query [query]")
		print("ex: --query 老虎城")



	
	