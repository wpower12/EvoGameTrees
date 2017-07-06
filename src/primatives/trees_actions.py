import random as r

SUCCESS, FAILURE, RUNNING = 0, 1, 2

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

