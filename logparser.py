#!/usr/bin/env python

import re
import fileinput
import glob

username = input ('Username: ')
password = input ('Password: ')

with open('routers.txt') as f:
    for row in f:
        ip = row.split()[0]
        from ftplib import FTP
        ftp = FTP(ip)
        ftp.login(username, password)
        ftp.set_pasv(False)
        ftp.cwd('/var/log/')
        ftp.retrbinary('RETR messages', open('messages'+ ip, 'wb').write)
        ftp.quit()
    f.close()
	
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