#!/usr/bin/env python

import re
import fileinput
import glob

file_list = glob.glob("*.tx")
with open('logmessages.txt', 'w') as file:
	input_lines = fileinput.input(file_list)
	file.writelines(input_lines)

with open('logmessages.txt') as f:
	for row in f:
		strings = ['alarm', 'Alarm']
		for string in strings:
			match = re.search(string, row)
			if match:
				print('Found "{}" in "{}"'.format(string, row))
	f.close()