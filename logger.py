############################################################################
## This script sets up the logging module for my digital assistant, Pepo  ##
##                   Mateus Vieira, 21/12/2021                            ##
############################################################################

import os
from time import sleep
import numpy as np

import json

###Reading configurations in config###

with open('config.json', 'r') as jsonfile:
    data = json.load(jsonfile)

log_path = data['log_path']

###

class Logger:
	def __init__(self, logs):
		print(logs[-1])
		try:
			with open(log_path, 'r') as file:
				log_file = file.read().split('\n')
		except (OSError,IOError):
			log_file = []
		log_file = log_file + logs
		log_file = list(dict.fromkeys(log_file))
		np.savetxt('Pepo_logs.txt', log_file, delimiter = '\n', fmt = '%s')