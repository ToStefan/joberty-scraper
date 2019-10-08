import urllib.request
import json
import os

def write_file(file_name, data):
	with open(file_name, "w+", encoding="utf-8") as f:
		f.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

def get_json(url):
	with urllib.request.urlopen(url) as result:
		return json.loads(result.read().decode())

def clear():
	if(os.name =="nt"):
		os.system("cls")
	else:
		os.system("clear")