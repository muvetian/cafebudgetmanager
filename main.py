from openpyxl import Workbook
import time, ConfigParser
import csv

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

def read_csv():
	with open('menu.csv','rb') as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		for row in csvreader:
			print row

def save_set():
	
if __name__ == '__main__':
    init_ini()
    update_time()
    read_csv()