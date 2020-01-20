#!/usr/bin/env python3

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
        ftp.retrbinary('RETR messages', open('messages'+ ip + '.tx', 'wb').write)
        ftp.quit()
    f.close()
	
file_list = glob.glob("*.tx")
with open('logmessages.txt', 'w') as file:
	input_lines = fileinput.input(file_list)
	file.writelines(input_lines)
	file.close()

with open('logmessages.txt') as f:
	for row in f:
		strings = ['alarm', 'Alarm']
		for string in strings:
			match = re.search(string, row)
			if match:
				with open('output.txt', 'a') as f:
					print('Found {}'.format(row), end = '', file=f)
					f.close()
		f.close()