##############################################################################
## This script sets up the organizing module for my digital assistant, Pepo ##
##                   Mateus Vieira, 21/12/2021                              ##
##############################################################################

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import datetime
from pytz import timezone
import pytz
import json
import shutil
import logger
###Reading configurations in config###

with open('config.json', 'r') as jsonfile:
    data = json.load(jsonfile)

file_to_watch = data['file_to_watch']

new_dir = data['new_directory']



time_zone = pytz.timezone(data['time_zone'])

###

###Defining necessary functions###

class Organizing_functions:
    def filetype_classifier(self,file):
        file_split = os.path.splitext(file)
        file_extension = file_split[1]
        return file_extension

    def name_dir(self,ext):
        ext = ext.replace('.', '')
        return ext.upper() + 's'

###

### Main portion of code

functions = Organizing_functions()
class Mover_handler(FileSystemEventHandler): #Gets an event object from Observer() and does something to it. https://python-watchdog.readthedocs.io/en/stable/index.html for more
    def __init__(self):
        self.logs = []
    def on_modified(self, event):
        time.sleep(1)
        event_file = os.path.basename(event.src_path)
        extension = functions.filetype_classifier(event_file)
        if extension == '.tmp':
            print('Downloading file...')
        else:
            dir_name = functions.name_dir(extension)
            new_path = new_dir + dir_name #If the event is a pdf, you get new_dir + 'PDFs'
            try:
                os.mkdir(new_path)
                self.logs.append(str(datetime.datetime.now(tz = time_zone)) + ': ' + 'New directory created: ' + new_path)
                shutil.move(event.src_path, new_path)
                self.logs.append(str(datetime.datetime.now(tz = time_zone)) + ': ' + 'File ' + event_file + ' moved to ' + new_path)
                time.sleep(1)
            except FileExistsError:
                try:
                    shutil.move(event.src_path, new_path)
                    self.logs.append(str(datetime.datetime.now(tz = time_zone)) + ': ' + 'File ' + event_file + ' moved to ' + new_path)
                except shutil.Error:
                    print('File with same name already in directory. Please rename the file and try again.')
            logging_it = logger.Logger(self.logs)

###