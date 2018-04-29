# -*- coding: utf-8 -*-
# 
import configparser
import codecs
import re

import shutil

cf = configparser.ConfigParser()
cf.read('./patchTool.ini')

secs = cf.sections()

print('secs',secs)

src_main_java_dir = cf.get('maven','src_main_java')

src_main_resources = cf.get('maven','src_main_resources')

web_root = cf.get('maven','web_root')

web_app = cf.get('maven','web_app')

patch_dir = cf.get('maven','patch_dir')


with open('./patchTest2.txt','r') as inputFile:
	readFile = inputFile.readlines()
	for line in readFile:
		print(line)
		line = re.sub(r'^src/main/webapp/','123',line)
		print(line)

		

