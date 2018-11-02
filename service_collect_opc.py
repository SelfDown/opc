#!/usr/bin/env python
# -*- coding: utf_8 -
from json_str_ws import strJSONWS
from position import getPosition
from parse_json import parseJSON
import OpenOPC
from config import globalData
items =[]
def readItems(name):
	global items
	file = open(name)
	content = file.read()
	items = content.split("\n");
	print "read file"
	return items
def getData(collection):
	import time
	global items
	print collection
	
	client = OpenOPC.open_client(collection['opc_server_ip'])
	client.connect(collection['opc_name'])
	items = collection['opc_items']
	arr = []
	for name, value, quality,create_time in client.read(items):
		collect_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		arr.append({"quality":quality,"project_id":collection['project_id'],"name":name,"value":value,"create_time":create_time,"collect_time":collect_time})
		#写日志
	client.close()
	return {"data":arr,"success":"true"}