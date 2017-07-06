""" TODO
 - New Population
 - Ramped 50/50 for both types of trees
 - Typed GP for both (see notebook)- Need types for
 	+ BTres
 	+ Action Trees
"""
import ConfigParser
import random as r
from primatives.trees_behavior import *
from primatives.trees_actions import *

class Init:
	"""Helper class to read configuration file and hold parameters"""
	def __init__(self, config_fn):
		config = ConfigParser.RawConfigParser()
		config.read(config_fn)
		# All the parameters.
		self.environment                = config.get('DEFAULT', 'environment')
		self.epochs                     = config.getint('DEFAULT', 'epochs')
		self.btree_max_depth            = config.getint('DEFAULT', 'btree_max_depth')
		self.btree_max_branch           = config.getint('DEFAULT', 'btree_max_branch')
		self.btree_population_size      = config.getint('DEFAULT', 'btree_pop')
		self.btree_sims_per_epoch       = config.getint('DEFAULT', 'btree_sims_per_epoch')
		self.actiontree_max_depth       = config.getint('DEFAULT', 'actiontree_max_depth')
		self.actiontree_population_size = config.getint('DEFAULT', 'actiontree_pop')
		self.actiontree_sims_per_epoch  = config.getint('DEFAULT', 'actiontree_sims_per_epoch')

	def new_pop(self):
		pop = []
		for p in range(self.btree_population_size):
			pop.append( {'ind': self.new_btree(), 'fit': 0} )
		return pop

	def new_btree(self):
		return self.rec_b_tree( self.btree_max_depth )

	def rec_b_tree(self, depth):
		node = get_random_internalnode()
		children = []	
		for i in range(r.randint(2, self.btree_max_branch)):
			if( depth == 0 ):
				children.append(get_random_leafnode())
			else:
				children.append(self.rec_b_tree(depth-1))
		node.children = children
		return node



