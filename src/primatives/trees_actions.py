import random as r

SUCCESS, FAILURE, RUNNING = 0, 1, 2

## General types of action trees?  Follow the B-tree paper:
## Make some species 'checkers', some 'doers'

class ActionTreeNode():
	def __init__(self, id):
		self.id = id
		self.children = []

	def eval(self):
		if r.random() > 0.5:
			print( "Succesful exectuion of node: "+str(self.id))
			return SUCCESS
		else:
			return FAILURE

"""
CHECKERS:
	COMPARE-RAM
	COMPARE-STACK
	IF-THEN-ELSE

DOERS:
	Randomly Sampled from the action set?
	COMPARE-STACK
	IF-THEN-ELSE
"""


