""" TODO
 - New Population
 - Ramped 50/50 for both types of trees
 - Typed GP for both (see notebook)- Need types for
 	+ BTres
 	+ Action Trees
"""

import configparser

class Init:
	"""Helper class to read configuration file and hold parameters"""
	def __init__(self, config_fn):
		self.fn = config_fn
		config = configparser.ConfigParser()
		config.read(config_fn)
		self.parameters = config['DEFAULT']

	def new_pop(self):
		return { "a", "b", "c" }