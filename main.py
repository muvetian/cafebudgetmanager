from openpyxl import Workbook
import time, ConfigParser
import csv
import json
import os
def init_ini():
	config = ConfigParser.ConfigParser()
	config.add_section("TIME")
	config.add_section("OPTION")
	#There are two sessions TIME and OPTION
	config.set("TIME","year","0000")
	config.set("TIME","mon","00")
	config.set("TIME","mday","00")
	config.set("TIME","wday","0")
	config.set("OPTION","moption","16")
	config.set("OPTION","dblance",0)
	config.set("OPTION","rmeal",0)

	config.write(open('config.ini',"w"))

def update_time():
	# This function updates the config.ini with the current time stamp
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	cur = time.localtime()
	config.set("TIME","year",cur.tm_year)
	config.set("TIME","mon",cur.tm_mon)
	config.set("TIME","mday",cur.tm_mday)
	config.set("TIME","wday",cur.tm_wday)
	config.write(open('config.ini',"r+"))

def get_path(id):
	path = "img/"
	gif = ".gif"

	return (os.path.abspath(path + id + gif))


def read_json():
	with open('menu_json.json') as json_data:
		d = json.load(json_data)
    	print(d[0]["Price"])

if __name__ == '__main__':
	init_ini()
	update_time()
	read_json()
	print (get_path("1"))
