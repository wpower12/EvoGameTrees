""" TODO
 - New Population
 - Ramped 50/50 for both types of trees
 - Typed GP for both (see notebook)- Need types for
 	+ BTres
 	+ Action Trees
 - Maybe I don't need typed.  Only really care about the distinction b/w
   A and B Trees.
 - Have the new pop method return a struct that holds the B-trees and A-tree 
   species seperatly.
"""
import ConfigParser
import random as r
import primatives.trees_behavior as btrees
import primatives.trees_actions as atrees
from ramdiff.RamDiff import get_ranked_ram_locs

class Init:
	"""Helper class to read configuration file and hold parameters"""
	def __init__(self, config_fn):
		config = ConfigParser.RawConfigParser()
		config.read(config_fn)
		# All the parameters.
		self.environment           = config.get('DEFAULT', 'environment')
		self.epochs                = config.getint('DEFAULT', 'epochs')
		self.btree_max_depth       = config.getint('DEFAULT', 'btree_max_depth')
		self.btree_max_branch      = config.getint('DEFAULT', 'btree_max_branch')
		self.btree_population_size = config.getint('DEFAULT', 'btree_pop')
		self.btree_sims_per_epoch  = config.getint('DEFAULT', 'btree_sims_per_epoch')
		self.atree_max_depth       = config.getint('DEFAULT', 'actiontree_max_depth')
		self.atree_species         = config.getint('DEFAULT', 'actiontree_species')
		self.atree_species_pop	   = config.getint('DEFAULT', 'actiontree_species_pop')
		self.atree_sims_per_epoch  = config.getint('DEFAULT', 'actiontree_sims_per_epoch')
		self.sim_length 		   = config.getint('DEFAULT', 'simulation_length')
		# Used when creating new A-trees
		self.env_ram_suggestions = get_ranked_ram_locs( self.environment )

	def new_pop(self):
		return {'btrees': self.new_btree_pop(), 'atrees': self.new_atree_pop()}

	## Generating B-trees ###########################
	def new_btree_pop(self):
		btree_pop = []
		for p in range(self.btree_population_size):
			btree_pop.append( {'ind': self.new_btree(), 'fit': 0} )
		return btree_pop

	def new_btree(self):
		return self.rec_b_tree( self.btree_max_depth )

	def rec_b_tree(self, depth):
		node = btrees.get_random_internalnode()
		children = []	
		for i in range(r.randint(2, self.btree_max_branch)):
			if( depth == 0 ):
				children.append(btrees.get_random_leafnode(self.atree_species))
			else:
				children.append(self.rec_b_tree(depth-1))
		node.children = children
		return node
	
	## Generating A-Trees ###########################
	def new_atree_pop(self):
		pop = []
		for s in range(self.atree_species):
			species = []
			for i in range(self.atree_species_pop):
				species.append({'ind': self.new_atree(), 'fit': 0})
			pop.append({'species_id': s, 'species_pop': species})
		return pop

	def new_atree(self):
		a = 1
		""" BIG TODO - Creating the actual action trees
			- Get the ramdiffs - 'most used' ram locations
			- create the atomic sets of atree operations
			- write the recursive tree builder
			- modify btree generation to use species ID's in the
			  leaf nodes.
			- actually start evaluating shit correctly. 
		"""
		return a







