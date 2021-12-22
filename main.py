############################################################################
## This is the main, startup script for my digital assistant, Pepo        ##  
##                   Mateus Vieira, 21/12/2021                            ##
############################################################################

###Reading configurations in config###
import json
import pytz

with open('config.json', 'r') as jsonfile:
	data = json.load(jsonfile)

file_to_watch = data['file_to_watch']

new_dir = data['new_directory']

log_path = data['log_path']


time_zone = pytz.timezone(data['time_zone'])

###

import organizer
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import datetime

import pandas as pd

###



if __name__ == "__main__":
	event_handler = organizer.Mover_handler()
	observer = Observer()
	observer.schedule(event_handler, path= file_to_watch, recursive=False)
	observer.start()

	i = 0
	try:
		while True:
			time.sleep(1)
			if i == 0:
				print('Pepo initialized successfully!')
			i += 1
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
