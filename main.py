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
def calculate_remaining_dollars(items):
	remaining_dollars = float(get_remaining_dollars())
	for item in items:
		remaining_dollars = remaining_dollars - float(get_item_price(item))
		print (float(get_item_price(item)))

	update_remaining_dollars(remaining_dollars)
	return remaining_dollars


def get_item_price(name):
	with open('menu_json.json') as json_data:
		d = json.load(json_data)
		result = 0.0
		for i in range(len(d)):
			if d[i]["Item"] == name:
				result = float((d[i]["Price"]))
    	return result

def update_remaining_dollars(value):
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	config.set("OPTION","rmeal",value)
	config.write(open('config.ini',"w"))
def get_remaining_dollars():
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	return config.get("OPTION","rmeal")
def get_path(id):
	path = "img/"
	gif = ".gif"

	return (os.path.abspath(path + id + gif))


def get_item_name(id):
	with open('menu_json.json') as json_data:
		d = json.load(json_data)
    	return (d[id]["Item"])

if __name__ == '__main__':
	# init_ini()
	# update_time()
	print(get_item_name(1))
	# print (get_path("1"))
	update_remaining_dollars(5)
	print (get_remaining_dollars())
	