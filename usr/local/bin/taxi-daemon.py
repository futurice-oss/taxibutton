#!/usr/bin/env python
"""
License:
    This file is part of Futurice Taxi Button package. 

    Futurice Taxi Button is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 3 as published by
    the Free Software Foundation.

    Futurice Taxi Button is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Futurice Taxi Button.  If not, see <http://www.gnu.org/licenses/>.


Readme:
    This file is part of Futurice Taxi Button package. Whole package is quick hack
    made just before our annual party. This is not production quality software,
    and it might require quite much of tinkering before it works reliably.
"""


import sys, datetime, serial, urllib2, os, time, stat
from daemon import Daemon

class TaxiDaemon(Daemon):
	def run(self):
		folder = '/var/run/taxi/'
		log = open('/var/log/taxi_log.txt','a')
		# TODO: change your address and company name to here. Also, change the password to match with one in kannel.conf
		url = 'http://localhost:13013/cgi-bin/sendsms?username=kanneluser&password=asdfasdf&to=13170&text=Helsinki+Osoite+numero+yrityksen+nimi'

		#Make sure that necessary folder(s) exists
		if not os.path.exists(folder+'old_messages'):
			log.write('Creating necessary folders\n')
			os.makedirs(folder+'old_messages')
			os.chmod(folder,stat.S_IRWXO)
			os.chmod(folder+'old_messages',stat.S_IRWXO)
			log.write('Folders created successfully\n')
		else:
			log.write('Folders ok\n')

		log.write('Starting daemon, opening serial port\n')
		ser = serial.Serial('/dev/ttyUSB3',9600,timeout=2) #TODO: change your Arduino serial port here
		log.write('Serial port open, starting daemon run\n')
		log.flush()
		prevClick = 0.0

		while True:
			# Read line from serial port (sends ".\r\n")
			l = ser.readline()

			if(len(l) != 0 and (not os.path.exists(folder+'lock') or (int(time.time()) - os.path.getmtime(folder+'lock')) > 120)): #2min lockdown
				open(folder+'lock','w')
				m = open(folder+'messages','a')
				log.write(str(datetime.datetime.now())+' Nappulaa painettu onnistuneesti\n')
				log.flush()
				m.write(str(int(time.time()))+":CLICK 0\n")
				m.close()
				urllib2.urlopen(url)
				prevClick = time.time()

			elif(len(l) != 0 and time.time() - prevClick > 0.5):
				log.write(str(datetime.datetime.now())+' Nappulaa painettu kesken lukituksen\n')
				log.flush()
				prevClick = time.time()

if __name__ == "__main__":
	daemon = TaxiDaemon('/tmp/taxi-daemon.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
